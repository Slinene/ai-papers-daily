---
title: 'WhisperRec: Latent Reasoning for Efficient Foundation Recommendation Models'
title_zh: WhisperRec：用潜在推理压缩思维链，实现高效基础推荐模型
authors:
- Hao Jiang
- Peiru Du
- Pengfei Yao
- Mengting Li
- Siyuan Lou
- Kuo Cai
- Sheng Yu
- Qiang Luo
- Jian Liang
- Ruiming Tang
affiliations:
- Kuaishou Technology
arxiv_id: '2607.26621'
url: https://arxiv.org/abs/2607.26621
pdf_url: https://arxiv.org/pdf/2607.26621
published: '2026-07-29'
collected: '2026-07-30'
category: GenRec
direction: 生成式推荐 · 潜在推理 Semantic ID
tags:
- latent reasoning
- generative recommendation
- semantic ID
- chain-of-thought
- foundation model
- multi-view reasoning
one_liner: 将显式思维链压缩为可学习的潜在 token，在保持推理语义的同时提升 10 倍以上吞吐量
practical_value: '- **用潜在 token 代替长文本 CoT**：在需要 LLM 推理的推荐系统中，避免生成繁杂的自然语言解释，直接插入少量可学习
  latent token，推理延迟接近无 CoT 模型，吞吐量提升 >10 倍，适合在线低延迟场景。

  - **多视角自适应 CoT 构造高质量监督**：从探索（开放意图发现）、评估（候选打分）和归因（转化证据）三个视角构造互补推理轨迹，并结合行为信号强度自适应调整推理深度，避免简单样本过度推理和困难样本分析不足。在电商广告推荐中可借鉴此思路，用业务规则定义不同视角的推理模板。

  - **三阶段潜在推理对齐**：先单视图对齐，再多视图对齐，最后推荐导向上下文对齐，逐步将大教师模型的 CoT 知识内化到 latent token 中。该方法可用于将复杂推理能力从大模型蒸馏到线上部署的小模型，工程上可结合
  KV cache 复用进一步降低开销。

  - **基于课程的多阶段后训练**：从高活跃用户到低活跃用户的课程式微调，缓解稀疏行为下的推荐效果退化。在用户冷启动或行为稀疏的业务中，可迁移此策略提升模型鲁棒性。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
显式思维链（CoT）用于基础推荐模型（FRM）时存在两大问题：
1. **过度推理与低 ROI**：即使意图明确的简单请求也会生成冗长推理，增加延迟和资源消耗；
2. **兴趣漂移与脆弱推理**：固定的单路径 CoT 容易过度强调历史兴趣，忽略短期上下文依赖，一步错导致最终推荐错误。

这些问题严重限制了 CoT 在工业级推荐系统中的落地效率。

### 方法关键点
- **核心思想**：将多视角教师 CoT 压缩为**可学习的潜在 token**，推理时只输入这些 token 即可直接生成目标物品的 Semantic ID，无需生成显式文本。
- **MV-ACoT 教师监督**：构建**探索（Exploration）、评估（Evaluation）、归因（Attribution）** 三个互补视角的推理轨迹，并根据样本难度（行为信号强弱）自适应调整推理复杂度，避免固定模板。
- **三阶段潜在推理对齐**：
  1. **单视图对齐**：用高置信度、无目标的推理热身潜在 token；
  2. **多视图对齐**：用所有 MV-ACoT 推理目标平均损失，使 token 能处理多种推理任务；
  3. **推荐导向上下文对齐**：将潜在 token 与下一物品预测目标联合优化，建立桥梁。
- **多阶段课程式后训练**：从高活跃用户到低活跃用户逐步微调，同时混合标准推荐样本和潜在推理样本（1:1），保持推理与无推理模式的性能。
- **推理高效性**：在线时仅输入 `[用户上下文；潜在 token]`，解码三级 SID，推理开销由固定数量 token 决定，与 CoT 长度无关。

### 关键结果
- 在快手公开 LLM-Rec 基准和工业本地生活数据集上，WhisperRec 一致优于 OneReason 的显式 Think/No-Think 变体。
- 与显式 CoT Think 相比，SID@64 提升 **17.44%**；与 No-Think 相比提升 **9.33%**。
- 推理吞吐量是显式 CoT 方法的 **10 倍以上**，延迟接近无 CoT 模型。
- 消融证实：MV-ACoT 的多视角和自适应复杂度均带来显著增益；潜在 token 数量为 3 时达到最佳平衡。
- LLM-as-Judge 评分和语义相似度分析表明，潜在 token 保留了约 0.8 的核心推理语义。

**一句话**：不要坚持让模型说人话去推理，把推理知识“熔炼”进几个隐空间 token，推荐准了，推理也快了一个数量级。
