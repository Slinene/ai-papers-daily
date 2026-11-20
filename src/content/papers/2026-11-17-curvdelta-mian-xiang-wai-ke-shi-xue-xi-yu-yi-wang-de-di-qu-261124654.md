---
title: 'CurvDelta: Low-Curvature Delta Modeling For Surgical Learning and Unlearning'
title_zh: CurvDelta：面向外科式学习与遗忘的低曲率增量建模
authors:
- Zeguan Xiao
- Zhuocheng Liang
- Yun Chen
- Yong Wang
- Guanhua Chen
- Pinyan Lu
affiliations:
- Shanghai University of Finance and Economics
- Alibaba Group
- Southern University of Science and Technology
arxiv_id: '2611.24654'
url: https://arxiv.org/abs/2611.24654
pdf_url: https://arxiv.org/pdf/2611.24654
published: '2026-11-17'
collected: '2026-11-20'
category: Training
direction: LLM 适配与选择性遗忘的能力保持
tags:
- LLM
- Fine-tuning
- Selective Unlearning
- K-FAC
- Parameter-Efficient
- Capability Preservation
one_liner: 通过低曲率参数化，在 LLM 适配与选择性遗忘中保持通用能力，CurvLoRA 提供高效低秩变体
practical_value: '- 在电商/广告 LLM 微调（类目识别、query 改写、商品文案生成）时，若担心丢通用能力，可按 CurvDelta 思路用保留集计算
  K-FAC/低曲率投影，把更新限制在不伤旧能力的子空间；资源受限时用 CurvLoRA 这类低秩投影，工程成本更低。

  - 对用户数据删除、过时商品知识下线等选择性遗忘场景，CurvDelta 适合只忘目标事实、保留相邻知识，缓解直接梯度上升带来的能力崩坏；TOFU/MUSE 结果表明保留性能接近重训参考。

  - 把保留约束显式嵌入参数化而非仅加正则项，可迁移到多任务持续微调：先构造 preservation loss，再用二阶信息找低曲率方向，比单点梯度约束更稳。

  - K-FAC 有额外计算/存储开销，适合离线训练或周期性更新；线上推理无额外成本，delta 合并后可直接部署。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：LLM 适配新任务或选择性遗忘时，常见副作用是通用能力下降；学习与遗忘都要求更新是选择性的。

方法：CurvDelta 把保留约束嵌入参数更新：在预适配模型附近分析保留损失的局部几何，构造低曲率空间，使参数更新对保留损失近似不变。为扩展到 LLM，采用 Kronecker-factored approximate curvature (K-FAC) 和分解投影；进一步提出低秩变体 CurvLoRA，在相同保留几何下做参数高效适配。

结果：在数学推理和代码生成上，CurvDelta/CurvLoRA 取得有竞争力的下游性能，同时更好地保留通用能力，获得比基线更优的 acquisition-retention trade-off。在 TOFU 和 MUSE 的知识遗忘任务中，目标遗忘与保留的平衡优于基线，保留性能接近从头重训的参考水平。
