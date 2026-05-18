---
title: 'Look Before You Leap: Autonomous Exploration for LLM Agents'
title_zh: 先看再跳：LLM Agent 的自主环境探索能力训练
authors:
- Ziang Ye
- Wentao Shi
- Yuxin Liu
- Yu Wang
- Zhengzhou Cai
- Yaorui Shi
- Qi Gu
- Xunliang Cai
- Fuli Feng
affiliations:
- University of Science and Technology of China
- Meituan
arxiv_id: '2605.16143'
url: https://arxiv.org/abs/2605.16143
pdf_url: https://arxiv.org/pdf/2605.16143
published: '2026-05-14'
collected: '2026-05-18'
category: Agent
direction: LLM Agent 自主探索能力训练与评估
tags:
- LLM Agent
- Exploration
- GRPO
- ECC
- Environment Understanding
- Explore-then-Act
one_liner: 通过 ECC 指标和交错 GRPO 训练，显式培养 LLM Agent 在陌生环境中的主动探索能力，显著改善下游任务表现。
practical_value: '- **探索-利用分离范式可迁移至电商场景**：agent 在接单前先自主探索商品状态、接口参数或用户偏好，获取结构化知识后执行推荐/购物任务，提升动态环境的适配性。

  - **用 ECC 量化领域探索度**：为电商或工具 Agent 定义关键产品、属性、API 返回等“探索检查点”，像本文计算覆盖率，可客观评价 agent 对业务环境的理解程度，避免依赖模糊的成功率。

  - **交错训练平衡探索与任务优化**：采用 GRPO 交替优化探索奖励（覆盖度）与任务奖励（转化/收益），可训练出既会收集信息又能完成目标的 agent，比纯任务
  RL 更鲁棒。

  - **鲁棒性增强可用于生成式推荐**：环境扰动（如物品库存变化）时，让 agent 先探索再决策，类似事前信息采集，可减少因过拟合静态知识导致的错误推荐，提升在线适应力。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
当前 LLM agent 在新环境中常因“过早利用”（premature exploitation）而失败——依赖训练时的先验知识，而不是主动探索环境状态、对象和可用操作。任务导向的强化学习（RLVR）仅奖励任务完成，不仅不鼓励探索，甚至会压缩探索行为。因此，将自主探索作为独立可训能力来显式培养变得迫切。

**方法与关键设计**
- **探索检查点覆盖率（ECC）**：为每个环境实例预定义一组“检查点”（关键位置、对象、 affordance），以 agent 在无任务指令的自由探索中覆盖这些检查点的比例作为探索质量的可验证指标。
- **交错 GRPO 训练**：同时采样任务完成 rollout（奖励任务成功）和探索 rollout（奖励 ECC），在同一个 GRPO 优化中交替更新，避免单一目标偏向，使 agent 既具备探索技能又保持任务求解能力。
- **Explore-then-Act 推理范式**：agent 先在无具体目标的条件下进行固定步数的探索，将交互历史总结为知识摘要 K，再在 K 的指导下执行下游任务。

**关键实验与结论**
- 在 ALFWorld、ScienceWorld、TextCraft 三个交互环境中评估 Qwen2.5-7B、Qwen3-4B 等多款模型。直接测试发现，开源模型平均 ECC 仅 22-31%，闭源 Claude 可达 89.5%，且任务导向 GRPO 反而使 ECC 降低（如 Qwen3-4B 从 28.5% 降至 18.8%）。
- 使用交错 GRPO 训练后，探索能力和下游任务成功率同步提升：例如在 ALFWorld 上用 Qwen2.5-7B，E-t-A 成功率从 Task-Only 的 93.2% 提升到 98.5%（+5.3%）；在扰动环境变体下，探索训练 agent 的鲁棒性显著优于纯任务 agent。
- 行为分析显示，探索训练使 agent 的重复动作率从 63.4% 降至 24.9%，信息寻求和错误恢复动作比例大幅增加，说明探索能力也是一种元能力，能改善决策质量。

**核心洞察**：显式优化探索覆盖率能让 agent 在陌生环境中更高效地将交互预算转化为有用知识，是通往可泛化 agent 的实用路径。
