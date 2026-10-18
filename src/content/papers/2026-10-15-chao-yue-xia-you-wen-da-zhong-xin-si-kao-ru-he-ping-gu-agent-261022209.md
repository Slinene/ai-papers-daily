---
title: 'Beyond Downstream QA: Rethinking How We Evaluate Agent Memory'
title_zh: 超越下游问答：重新思考如何评估 Agent 记忆
authors:
- Sebastian-Antonio Toma
- Jean de Kernier
- Mike Ply
- Oliviu Matei
affiliations:
- Amazon Web Services
- Technical University of Cluj-Napoca
arxiv_id: '2610.22209'
url: https://arxiv.org/abs/2610.22209
pdf_url: https://arxiv.org/pdf/2610.22209
published: '2026-10-15'
collected: '2026-10-18'
category: Eval
direction: Agent 记忆评估 · 内在指标
tags:
- Agent Memory
- Intrinsic Evaluation
- Benchmark
- Fact Evolution
- LLM Agents
one_liner: 提出 FEB-30 事实演化基准与内在评估方法，证明仅靠 QA 评估会掩盖记忆存储层故障
practical_value: '- 在构建 Agent 长期记忆或用户/商品画像记忆时，不要只用端到端任务指标（如下游推荐/回答准确率）评估记忆模块；应定期对比存储的
  profile、事件状态与 ground truth，计算 claim coverage、更新检测召回、误更新率，定位是抽取、合成还是检索瓶颈。

  - 可借鉴 paradigm inversion：用多模型轮换和 judge 校验生成带 ground truth 的时序事实轨迹（如用户兴趣演变、商品属性变更、库存/价格状态变化），低成本构建
  memory 回归测试集。

  - 注意记忆写路径的操作分类质量：论文代表性系统 revise 操作仅 20% 分类正确、false update 22%；建议对 create/update/reinforce/supersede
  决策单独评估，并引入 temporal guard，但需避免把应 update 的旧信息错误降级为 reinforce。

  - 检索瓶颈与 LLM 补偿问题在电商推荐中同样存在：画像正确但 embedding 召回不匹配会导致失败，强 LLM 可能用部分结果生成看似正确答案；建议同时监控检索命中率和生成结果，区分故障层。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**
现有 Agent memory 基准几乎都通过下游 QA 得分评估记忆质量，一个综合分数混叠了记忆正确性、检索质量和生成质量。这会产生两类系统性问题：强生成模型在记忆错误时仍能推理出正确答案（false positives），以及记忆正确但检索失败导致问答错误（false negatives）。这类似 NLP 中词嵌入早期只看下游任务、后来引入内在评估（类比任务、相似度相关性）以加速进展的历史。

**方法关键点**
- FEB-30：30 条事实演化轨迹，6 个诊断类别——C1 LLM 补偿、C2 检索瓶颈、C3 操作分类准确性、C4 合成质量、C5 时序正确性、C6 多作者归因；难度分 L1/L2/L3。
- paradigm inversion：从已知 ground truth 事实轨迹生成多文档，而非在真实文档上标注；用 6 个模型跨 5 家提供商轮换、3 个独立 judge 验证，共 147 篇文档。
- 评分框架同时计算内在指标（claim coverage、update detection recall、false update rate、confidence MAE）和外在 QA 得分，用 mean absolute divergence (MAD) 与 DivRate 衡量两者分歧。

**关键实验与数字**
在代表性 extract-embed-classify-synthesize 记忆系统上，内在与外在评估平均分歧 0.168 ± 0.025，44% 的轨迹超过 0.15 阈值；操作分类准确率仅 20.1%，false update 率 22.2%。C1 分歧最高（MAD 0.295，内在 82.2% vs 外在 54.5%），C6 内在最低（41.5%）。分类准确率随难度从 33.8% 降至 10.1%，claim miss rate 从 L1 54% 升至 L3 86%，fact count 从 9.6 膨胀到 22.4，表明系统倾向于碎片化而非合成。内在与外在 Pearson r=0.423，仅 18% 方差共享。

**最值得记住的一句话**
仅靠下游 QA 评估 Agent memory 会掩盖存储层故障，直接检查 memory store 的内在评估应作为标准补充。
