---
title: Virtual Head Attention
title_zh: 虚拟头注意力：线性重参数化实现双重 KV 压缩与质量提升
authors:
- Xibo Ding
- Guoxia Wang
- Jinle Zeng
- Jiabin Yang
- Sirui Tao
- Chao Yang
- Dianhai Yu
affiliations:
- Baidu Inc.
- Peking University
arxiv_id: '2610.17959'
url: https://arxiv.org/abs/2610.17959
pdf_url: https://arxiv.org/pdf/2610.17959
published: '2026-10-12'
collected: '2026-10-17'
category: LLM
direction: 长上下文 LLM · 注意力重参数化
tags:
- Virtual Head Attention
- KV cache compression
- Grouped-Query Attention
- Reparameterization
- Long-context LLM
- MoE
one_liner: 通过 Q Premix 与 Linear Postmix 将训练后模型吸收为标准 GQA-2，实现 KV cache 4 倍压缩、训练 FLOPs
  下降且质量提升
practical_value: '- 线上长序列生成式推荐/Agent 工具调用受 KV cache 限制时，可参考 VHA：训练时加入线性头间混合，推理时重新参数化为标准
  GQA-2，无需改推理框架；已有 GQA-8 服务可尝试降到 2 个 KV heads 并配合 Premix/Postmix，保持质量同时降低 4 倍缓存。

  - (I+BA^T) 低秩 identity-residual 结构可迁移到多场景/多任务序列建模的输出融合，低秩约束提供隐式正则化，防止跨 head 混合过拟合；电商多业务场景可用其做
  soft routing 而非共享 attention。

  - Premix 的 per-group query transform 能实现 group-conditioned query specialization，在用户长期行为序列中根据不同
  KV group 学习不同查询方向，不增加缓存即提升注意力多样性。

  - 消融显示单纯 halve heads 会损失质量，必须同时在 query 侧做虚拟扩展、在输出侧做跨组融合；如果要在推荐模型中压缩 attention 头数，应同时设计两侧补偿，缺一不可。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
长上下文 LLM 中注意力机制同时决定 KV cache 大小、训练/prefill FLOPs 和模型质量，三者难以兼得。GQA-8 质量强但缓存大；把 KV heads 从 8 降到 2 可压缩缓存，但 1.7B 上平均精度掉 1.00%；MLA 缓存小但质量最低；MFA 质量接近 GQA-8 但训练/prefill FLOPs 增加 49.8%。VHA 目标是在 2 个 KV heads 下同时改善三个维度。

**方法关键点**  
- 将物理 query heads 减半，KV heads 固定为 2，得到 1.00 KB/layer/token 的 BF16 缓存，比 GQA-8 小 4 倍（dense），比 GQA-4 小 2 倍（MoE）。  
- Q Premix：在每个 KV group 内对物理 query heads 施加近恒等线性变换 W_premix^g，把 H'_q 个物理 heads 扩展为 H_v=H_kv×H'_q 个虚拟 heads，恢复注意力多样性。初始化 I+αε。  
- Linear Postmix：对 attention 输出沿 head 维做低秩 identity-residual 混合 Y+BA^T Y，rank r=H'_q/2，实现跨 group 信息融合；B 初始为 0。  
- 推理吸收：Premix 可折叠进 W_Q，Postmix 折叠进 W_O，模型退化为标准 GQA-2，直接复用 vLLM/SGLang 等推理优化，零额外开销。  
- 该设计类似 LoRA/RepVGG：前向等价于受限 GQA，但分离参数化带来不同梯度路径与隐式正则化。

**关键实验**  
在 0.6B/1.7B/4B dense 和 8B-A1B MoE 四个尺度、50B tokens 预训练中，VHA 平均准确率均超过 GQA baseline（+0.05% 到 +0.81%），同时缓存最小。1.7B 上，GQA 16-2-2 比 GQA 16-8-8 掉 1.00%，再减半物理 heads 的 GQA 8-2-2 共掉 1.71%；VHA 同样 (8,2,2) 形状恢复并超过 GQA-8 +0.41%。训练 FLOPs 比 GQA 基线降 7.9%，比同等缓存的 MFA 低很多。工业 30B-A3B MoE 500B tokens 任务上，VHA 平均 50.36，超过 MLA 49.66 和 GQA-4 47.76。10B-A1B MoE 长上下文 128K 上，RULER 平均 84.4 vs GQA 73.0。

**最值得记住的一句话**  
VHA 用纯线性训练时重参数化（Q Premix + Linear Postmix）在 2 个 KV heads 下同时压缩 KV cache、降低训练 FLOPs 并提升质量，推理时完全吸收为 GQA-2，零额外开销复用现有 serving 框架。
