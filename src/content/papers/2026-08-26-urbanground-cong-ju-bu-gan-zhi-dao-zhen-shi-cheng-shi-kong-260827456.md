---
title: 'UrbanGround: From Local Perception to Spatial Agency in a Real-Scale City'
title_zh: UrbanGround：从局部感知到真实城市空间行动能力
authors:
- Tianjie Ju
- Zheng Wu
- Yueqing Sun
- Yuhan Cui
- Bobo Li
- Shengqiong Wu
- Pengzhou Cheng
- Haodong Zhao
- Zongru Wu
- Xinbei Ma
affiliations:
- Shanghai Jiao Tong University
- National University of Singapore
- Meituan
- The Chinese University of Hong Kong
- Shanghai University
arxiv_id: '2608.27456'
url: https://arxiv.org/abs/2608.27456
pdf_url: https://arxiv.org/pdf/2608.27456
published: '2026-08-26'
collected: '2026-08-29'
category: Eval
direction: MLLM智能体城市空间导航评估
tags:
- MLLM
- Agent
- Spatial Reasoning
- Embodied AI
- Benchmark
- Navigation
one_liner: 提出香港真实3D城市沙盒UrbanGround，系统性评估MLLM智能体从局部视觉感知到持续导航行动的可靠性
practical_value: '- **渐进式评估设计可迁移**：论文通过三个递进问题（局部场景grounding → 远距离导航 → 路线与行人扰动）暴露智能体能力断裂点，电商Agent评估同样应区分单步能力与多步组合能力，避免局部指标掩盖全局失败。

  - **长程任务错误累积的警示**：MLLM在短距离空间推理尚可，但持续探索中错误无法纠正，这提醒在构建推荐或搜索Agent时，需加入全局状态追踪与纠错机制，而非单纯堆叠单步模型能力。

  - **高保真仿真环境的价值**：基于真实地理数据构建可闭环交互的沙盒，能为Agent提供物理约束下的测试场。电商场景可借鉴构建虚拟购物环境，测试Agent在商品导航、路径规划中的鲁棒性。

  - **论文核心是具身智能与空间导航，与电商推荐业务直接关联较弱，可借鉴点主要集中在Agent评估方法论与仿真环境设计。**'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有MLLM能理解街景，但城市行动力（urban agency）要求局部感知在智能体移动后仍能支撑可靠决策。论文旨在探究当前MLLM智能体能否将局部城市感知转化为真实城市中的可靠行动。

**方法**：提出UrbanGround，首个基于香港全境3D地理数据构建的真实尺度城市沙盒，支持第一人称视角闭环交互与程序化控制。通过三个研究问题递进分析：1）主动观察后能否回答局部空间问题；2）局部grounding能否支撑到远近不同目的地的导航；3）行为在路线变化与行人运动扰动下是否稳定。

**关键结果**：当代MLLM智能体在视觉识别和短距离空间推理上表现可用，但方向判断与行人感知运动不可靠；核心缺陷在长时间探索中暴露——局部能力无法组合为持续目标导向行为，错误累积且缺乏纠错。UrbanGround为系统评估MLLM智能体在复杂开放城市环境中的探索可靠性提供基础。
