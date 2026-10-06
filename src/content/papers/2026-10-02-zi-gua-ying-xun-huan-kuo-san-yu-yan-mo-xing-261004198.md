---
title: 'ALoDLM: Adaptively Looped Diffusion Language Models'
title_zh: 自适应循环扩散语言模型
authors:
- Liancheng Fang
- Zhuowei Li
- Youngeun Kim
- Tianchen Zhao
- Rajat Koner
- Jiaye Wu
- Linghan Xu
- Xuanbai Chen
- Xiang Xu
- Zheng Zhang
affiliations:
- University of Illinois Chicago
- Amazon AGI
- Korea University
arxiv_id: '2610.04198'
url: https://arxiv.org/abs/2610.04198
pdf_url: https://arxiv.org/pdf/2610.04198
published: '2026-10-02'
collected: '2026-10-06'
category: Training
direction: 扩散语言模型 · 自适应计算
tags:
- Diffusion LM
- Adaptive Computation
- Latent Recurrence
- Parallel Decoding
- LLM Training
one_liner: 按 token 难度分配计算，扩散语言模型在多个基准上超越同规模 AR 模型并保持并行解码
practical_value: '- **难度自适应计算可迁移到生成式推荐/query生成**：在并行生成 Semantic ID、搜索词或推送文案时，不同 token
  的预测难度差异大，可借鉴 ALoDLM 按 token 置信度动态分配迭代次数，避免对简单位置做无谓计算。

  - **离散提交 + 隐状态继续精修**：对电商场景中的流式生成或交互式 Agent，可将已确定的 token 提前作为条件输入，只对高不确定性 token 保留隐状态继续推理，类似级联早退机制，能显著降低平均延迟。

  - **计算调度作为隐变量联合训练**：如果把 token 的“停止迭代”决策也作为可学习变量，并用 NELBO 与最终生成质量一起优化，可以在线上对推理预算和业务指标做端到端权衡，比人工固定迭代次数更优。

  - **并行解码吞吐优势明显**：在需要大批量生成商品标题、广告文案或搜索 suggestion 的场景，扩散式并行解码能提供比 AR 更高的吞吐，适合高 QPS
  线上服务。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：扩散语言模型通过并行预测多个 token 加速生成，但与同规模 AR 模型相比质量仍有差距。作者认为原因是计算难度不匹配：部分未知 token 容易预测，其余需要更多计算，但现有 DLM 在每个去噪步对所有未知位置施加统一计算深度。

**方法关键点**：提出 ALoDLM，将统一计算替换为 token 自适应的隐状态循环。每个去噪步内，模型迭代精修表示，并根据 token 难度分配计算：准备提交的 token 作为离散上下文反馈，未解决的 token 保留隐状态继续经过额外循环。将 token 级计算调度建模为隐变量，推导条件负证据下界（NELBO）联合学习 token 预测与计算分配。训练 1.7B 和 8B 两个规模。

**关键结果数字**：在 11 个基准上，ALoDLM 在两个规模的平均基准分数上均超越所有评估的 DLM 和对应 AR 基线；同时保持快速并行解码，在优化推理引擎下实现强质量-效率权衡。
