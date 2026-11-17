---
title: 'Harness Leverage Across Model Size: A Ladder of Five Local Agent Harnesses
  from 0.75B to 4.7B'
title_zh: 跨模型规模的 Harness 杠杆：0.75B 到 4.7B 五级本地 Agent Harness 阶梯
authors:
- Hao Wang
- Ting Huang
affiliations:
- School of Mathematics and Physics, University of Science and Technology Beijing,
  Beijing, China
- Honor Device Co., Ltd., Beijing, China
arxiv_id: '2611.21407'
url: https://arxiv.org/abs/2611.21407
pdf_url: https://arxiv.org/pdf/2611.21407
published: '2026-11-16'
collected: '2026-11-17'
category: Agent
direction: Agent harness 评估与本地小模型部署
tags:
- agent harness
- small language models
- local inference
- task completion
- empirical evaluation
one_liner: 系统比较五个本地 Agent harness 在四个小模型上的任务完成率，Mingbird 在各规模均最优，harness 效应体现在是否产出工件
practical_value: '- 在资源受限场景（如端侧/边缘设备）部署 Agent 时，优先选择带完成控制门的 harness（如 Mingbird），它在
  0.75B-4.7B 模型上均稳定提升任务完成率，可作为本地推荐 Agent 或客服 Agent 的轻量级模板。

  - 防重复规则对小型模型至关重要：移除该规则在 0.75B 模型上导致 0.411 分下降并让 8/18 任务无产物。在电商场景中，加入重复阻断逻辑可避免模型反复生成同一推荐或话术。

  - 评分 Agent 任务时，不要只看退出状态或日志，必须检查实际产出的 artifact（文件、推荐列表等），因为许多失败案例正常退出但无产出。建议在评估流水线中加入产物文件存在性检查，避免误报成功。

  - 完成门中具体检查项（如六个 executable checks）贡献有限，可考虑简化 harness 以降低延迟和实现复杂度，把重点放在防重复和终止条件设计上。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：现有研究要么固定模型比较 harness，要么固定 harness 比较模型，缺乏同时变化两者的系统评估。本文旨在量化 harness 在不同模型规模下的杠杆效应，为本地小模型部署提供依据。

**方法**：构建五个已发布的 harness（包括完成控制型 Mingbird），在 18 个产出 artifact 的任务上，搭配四个本地可部署的开源模型（0.75B、1.9B、4.7B、35.5B，其中 35.5B 为锚点），共 360 个阶梯单元，使用一个确定性检查器统一评分。

**关键结果**：Mingbird 在所有模型规模上均值最高；四个预注册配对对比中两个通过 Holm 校正（0.75B 和 4.7B）；部署解读下 16 个配对区间中 13 个排除零。完成门不是关键：禁用所有六个可执行检查对均值影响很小（+0.080, +0.117, +0.003, -0.004），区间均含零，仅 1.9B 产生空运行。但移除一个防重复规则在 0.75B 成本达 0.411，并导致 18 个任务中 8 个无 artifact。harness 效应本质是 progress 效应：决定运行是否在磁盘上留下任何产物。357 个可用单元中 127 个未留下声明产物，其中 85 个正常退出，表明基于退出状态的评分会错误给予分数。harness 效应随规模变化方向不明确：地板臂上升、天花板臂下降、跨家族臂出现峰值。
