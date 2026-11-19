---
title: 'DNeo: Your Parallel Draft Model Needs Better Target Feature Encoding'
title_zh: DNeo：并行草案模型需要更好的目标特征编码
authors:
- Jameson Sandler
- Shane Bergsma
- Mostafa Elhoushi
- Bin Claire Zhang
- Gavia Gray
- Joel Hestness
- Nolan Dey
- Ferdinando Fioretto
affiliations:
- University of Virginia
- Cerebras Systems
arxiv_id: '2611.21925'
url: https://arxiv.org/abs/2611.21925
pdf_url: https://arxiv.org/pdf/2611.21925
published: '2026-11-15'
collected: '2026-11-19'
category: LLM
direction: LLM 推测解码 · 并行草案模型
tags:
- Speculative Decoding
- Parallel Drafting
- LLM Inference
- Feature Encoding
- MoFA
- Rejection Memory
one_liner: 提出 DNeo 并行草案架构，通过 MoFA 特征编码、拒绝记忆与融合因果头，在相同质量下实现比 DFlash-2 快 1.3 倍生成。
practical_value: '- 在电商/Agent 在线服务部署 LLM 时，可自研或改造并行 drafter 加速；已有 drafter 可优先用 MoFA
  替换 dense 特征编码：对 target 多层 hidden states 做 softmax 加权求和，保持维度不变，参数量极小，能稳定提升 TPF；避免在编码时混入
  cross-dimension 投影。

  - 多轮生成/对话式推荐中，历史被拒 draft token 是几乎零成本的上下文，可借鉴 rejection memory 设计：用 cross-attention
  读取上轮 rejected tokens 的 target hidden states，而不是把它们直接拼进输入或做 MLP fusion；实验证明 fusion
  会引入瓶颈，attention 能按需检索。

  - 对线上高并发吞吐敏感，可参考 prefix-only attention + 2-tap causal conv：删掉 masked block 内部 self-attention
  能降低 drafter 延迟，且不损失质量；结合因果头即可保持草稿左到右一致性。

  - 训练并行 drafter 必须使用 on-policy rollout/online distillation，确保与推理时 rejection memory
  的序列依赖一致，否则 train-test mismatch 会抵消收益；对在线学习 drafter 的迭代部署有直接参考价值。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：LLM 自回归解码是主要延迟瓶颈，speculative decoding 能无损加速，但并行 drafter 的 TPF 受制于特征编码质量。现有 DFlash/DSpark 的特征编码有三个问题：dense 投影混合 target 残差维度（residual mixing），破坏特征结构；drafter 无记忆，忽略上轮被拒 token 中有用信息；均匀选层把低信息量的早期层也纳入编码。

**方法关键点**：
- MoFA：用可学习 softmax 门控对 target 多隐藏层加权求和，不做跨维度混合，参数量仅 dense 编码约 0.05%，且权重可解释为层重要性。
- 拒绝记忆：复用 target 在验证阶段已算出的被拒位置 hidden states，通过 cross-attention 让 masked positions 检索上轮 rejection features，而不是 MLP/input fusion。
- DNeo 因果头：在低秩 latent space 中融合 DSpark 低秩头与 DFlash-2 bilinear score head，对全词表做上下文感知修正。
- Prefix-only attention + 2-tap causal conv：屏蔽掉 masked block 内部 self-attention，依赖局部卷积和因果头建模左到右依赖，降低 drafter 延迟。
- 层选择协议：根据 MoFA 权重发现后半层更重要，只保留 first layer + 后半层作为编码层。

**关键结果**：在 Qwen3-4B、H100、SGLang，b=16 的六个 benchmark 上：
- DNeo 比 DFlash-2 快最多 20.7% / 1.3× 生成速度，吞吐在 B=32 下高 58%（Transformers serving）。
- 消融：MoFA +0.651 τ、2-tap conv +0.331、rejection memory +0.182、DNeo head +0.217。
- 关键发现：受限 dense 编码（保留对角线结构）与 MoFA 几乎同等，说明 residual mixing 是 dense 编码劣势的决定因素；拒绝特征用 attention 比 input fusion 好，MLP fusion 只 +0.030，attention +0.189。

**最值得记住的一句话**：Dense 特征编码的劣势主要来自残差维度混合；对 target features 做结构保持的加权融合即可低参数量提升 draft quality，无需复杂投影。
