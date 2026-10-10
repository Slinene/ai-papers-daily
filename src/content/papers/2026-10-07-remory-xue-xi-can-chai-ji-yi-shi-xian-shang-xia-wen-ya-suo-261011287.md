---
title: 'REMORY: Learning Residual Memory for Context Compaction'
title_zh: REMORY：学习残差记忆实现上下文压缩
authors:
- Hanchen Xia
- Baoyou Chen
- Yutang Ge
- Naihao Deng
- Senqiao Yang
- Zilong Dong
- Weihao Yuan
- Siyu Zhu
affiliations:
- Shanghai Academy of AI for Science
- Fudan University
- Shanghai Jiao Tong University
- University of Michigan
- Alibaba Group
arxiv_id: '2610.11287'
url: https://arxiv.org/abs/2610.11287
pdf_url: https://arxiv.org/pdf/2610.11287
published: '2026-10-07'
collected: '2026-10-10'
category: Agent
direction: Agent 长程上下文压缩与记忆
tags:
- context compaction
- soft memory tokens
- long-horizon agents
- LLM memory
- residual connection
one_liner: REMORY 在摘要后追加可学习软记忆 token，通过冻结 LLM 的续写分布逼近训练，以少量位置预算显著提升长程 agent 表现
practical_value: '- 会话/上下文压缩：在电商导购、客服或搜索 Agent 的长对话中，用“文本摘要 + 可学习软 token 残差”替代纯摘要；摘要保持可读
  checkpoint，软 token 补偿后续决策所需的隐式信息，避免丢失关键细节。

  - 训练方式：不微调大模型，只训练轻量 memory encoder，通过冻结 LLM 的 teacher-student 分布匹配（reverse KL）接入；可在业务已有模型上低成本部署，在线只增加少量输入
  token，无需改动 actor 权重。

  - 两阶段课程：先重建阶段学习信息保持，再在固定摘要下学续写分布，直接优化“摘要遗漏但后续需要”的补偿；可迁移到生成式推荐中的用户历史压缩、query 会话 embedding
  等场景。

  - 工程配置：每 1024 positions 产生 64 soft tokens，层次压缩至最多 4096 slots，用约 5% 的位置预算接近全上下文效果；同时减少重复工具调用和工具错误，利于降低
  API 成本、提升任务完成率。'
score: 8
source: huggingface-daily
depth: full_pdf
---

动机：长程 agent 必须在有限上下文窗口内反复压缩历史；常见做法是生成文本摘要，但摘要只保留主线，未必支持后续每个决策。人类工作记忆容量很小却能长期执行复杂项目，依赖部分线索激活分布式长期记忆。REMORY 受此启发，学习有界软记忆 token 作为摘要的残差补充。

方法关键点：
- 在 compaction 边界，给定历史 Hi 和新摘要 Si，记忆网络生成软 token Mi = C_φ(Hi; Si)，|Mi| ≤ m，拼接到摘要后 [Si; Mi]，形成序列维度的残差连接。
- 软 token 位于冻结 actor 输入空间，仅更新记忆网络参数；每个 1024 source positions block 生成 64 soft tokens，层次压缩最多 4096 slots。
- 训练分两阶段：Stage I 重建，教师接收完整 source 并重复，学生以软记忆替换 source，用 reverse KL 逼近教师预测；Stage II 摘要条件续写，教师看完整历史，学生看摘要+记忆，共同预测同一后续 assistant 响应，优化摘要遗漏但后续需要的补偿能力。
- 记忆编码器使用冻结 actor 特征 + learned queries，gated cross-attention 到摘要；基于 DFlash / DFlash-2，参数分别为 1.94B 和 1.502B。

关键实验：
- SummHay 源归因：在 92 queries 上，Summary + REMORY 相比 Summary 在 citation F1 提高 4.04 分（56.98→61.03），joint score 提高 3.55 分（39.84→43.39），覆盖率几乎不变（67.55→67.95）；仅用 5.2% 输入位置（5,024 vs 96,872）接近全上下文 joint score（43.41）。
- 长程 agent：Qwen3.8-27B 在 AutomationBench +9.8 分（35.5→45.3），JobBench +7.6 分（33.4→41.0），Terminal-Bench +4.5 分（71.9→76.4），BrowseComp +3.0 分（74.0→77.0）；GLM-5.3-Flash 在 Terminal-Bench +3.3 分（84.3→87.6），BrowseComp +4.1 分（84.9→89.0）。重复工具输出减少 17.9–29.8%，工具错误减少 25.3–49.7%，生成成本多数下降。

最值得记住的一句话：文本摘要提供可读 checkpoint，而可学习软 token 补偿摘要无法覆盖的后续决策信息，并以冻结大模型分布匹配为目标，在不改 actor 参数的情况下提升长程 agent 稳定性与任务完成率。
