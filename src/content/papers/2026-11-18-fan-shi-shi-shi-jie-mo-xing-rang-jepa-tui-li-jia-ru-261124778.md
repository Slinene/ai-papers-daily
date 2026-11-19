---
title: 'Counterfactual World Models: JEPAs That Reason About "What If"'
title_zh: 反事实世界模型：让 JEPA 推理“假如…”
authors:
- Randall Balestriero
- Yann LeCun
- Kerda Varaku
affiliations:
- Brown University
- AMI Labs
- New York University
- Independent Researcher
arxiv_id: '2611.24778'
url: https://arxiv.org/abs/2611.24778
pdf_url: https://arxiv.org/pdf/2611.24778
published: '2026-11-18'
collected: '2026-11-19'
category: Reasoning
direction: 因果反事实推理 · 世界模型
tags:
- Counterfactual Reasoning
- World Models
- JEPA
- Causal Inference
- Hindsight Planning
one_liner: 提出无需反事实数据、额外参数或重训练的反事实世界模型，通过一阶近似将观察结果与预测差值结合
practical_value: '- 离线策略评估/反事实评估：在推荐或广告策略迭代中，无法知道未采用动作的结果；可借鉴“观察结果 + 模型预测差值”的一阶修正法，仅需已有世界模型（如用户行为模拟器）即可近似反事实，无需构造配对数据或额外训练。

  - Agent 规划与事后归因：对智能体（如对话策略、投放策略），可用来回答“如果当时采取另一个动作会怎样”，分离坏决策和坏运气；方法实现简单，只需复用现有 world
  model 的前向预测差值。

  - 隐藏上下文建模：当用户意图/市场状态等隐变量与动作共同影响结果且作用可加时，假设交互为二阶小量，可在一阶近似下解耦隐变量和动作，减少对隐变量推断的依赖。

  - 注意适用边界：不适用于动作与扰动有强交互（如存在缩放指令、不连续、折叠）的场景，迁移前需评估动力学平滑性。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：世界模型在无法完全观测的环境中运行，当隐藏扰动（如水流推船）改变动作结果时，需要回答反事实问题。论文证明仅训练于事实转移的世界模型无法独立回答反事实问题，无论数据或容量多大。

**方法关键点**：利用物理系统中的“自然不跳跃”性质：当动作与扰动作为独立力作用时，其交互在时间上是二阶量，因此反事实结果可一阶近似为观察结果加上世界模型在替代动作与事实动作下预测的差值。基于此，可在不引入反事实数据、不添加额外参数、不重新训练的情况下，将任意世界模型改造为反事实世界模型。对时长 $h$，证明了相对扰动方差的 $O(h^2)$ 误差界，并建立了匹配的 minimax 下界；同时刻画了不连续性、坐标折叠和缩放指令等失效情况。

**关键结果**：在四个渲染模拟器上，同一世界模型的反事实 $R^2$ 从 38--46% 提升到 86--96%；在水下航行器任务上，用 16 倍事实数据达到 90--94%；四个额外冻结编码器（DINOv3、SigLIP 2、CLIP、EVA-02）在相同模拟器上达到 81--95%。事后规划中，该方法找到本应可达目标的动作比例达 35--69%，显著优于知道模拟器但不知结果的 oracle 规划器（14--23%）。
