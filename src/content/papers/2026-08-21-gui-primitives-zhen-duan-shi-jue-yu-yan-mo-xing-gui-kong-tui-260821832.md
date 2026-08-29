---
title: 'GUI-Primitives: Diagnosing Spatial Reasoning Failures in Vision-Language GUI
  Grounding'
title_zh: GUI-Primitives：诊断视觉语言模型 GUI 空间推理失败的基准
authors:
- Md Abrar Jahin
- Md Rizwan Parvez
affiliations:
- University of Southern California
- USC Information Sciences Institute
- Qatar Computing Research Institute (QCRI)
arxiv_id: '2608.21832'
url: https://arxiv.org/abs/2608.21832
pdf_url: https://arxiv.org/pdf/2608.21832
published: '2026-08-21'
collected: '2026-08-29'
category: Eval
direction: GUI Agent 空间推理评估基准
tags:
- GUI grounding
- spatial reasoning
- benchmark
- vision-language models
- computer-use agents
one_liner: 构建对比指令对基准，解耦候选定位与关系理解，揭示 VLM 在 GUI 元素定位的主要瓶颈是候选定位而非空间关系推理
practical_value: '- 在电商导购/客服 Agent 落地 GUI 自动化时，可借鉴对比指令对方法：固定截图和锚点，只改变关系表达式，构造最小差异样本，低成本排查模型是“找错元素”还是“看不懂关系”。

  - 该基准显示模型输出坐标大量落在候选框外（60–92%），工程实现中应避免让 VLM 直接回归任意坐标，可先接一个候选区域检测器（如 OCR/图标检测），再用
  VLM 做区域内选择或关系判断，或对输出坐标做约束/后处理。

  - 论文的 oracle 诊断：把两个候选框标记在图上，选择准确率提升 35–57 个百分点，说明“给定候选集后模型关系理解尚可”。业务上可用于两阶段 pipeline：召回候选元素（如商品卡片、按钮）后，再让
  VLM 根据指令选择目标，降低定位错误。

  - 评估 Agent 时，建议同时报告 strict point-in-box 与 conditional accuracy，区分候选定位失败与关系理解失败；这比单一
  Overall Acc 更能指导模型迭代方向。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：Computer-use agents 需根据自然语言指令在截图中定位界面元素，但现有基准未隔离模型是否将关系语言绑定到正确元素。

**方法关键点**：GUI-Primitives 包含 994 项对比指令对，覆盖 7 种空间关系（左右、上下、包含、对齐、邻近、列表序、遮挡）。每个指令对固定截图和 anchor，仅改变关系表达式，使正确目标在两个候选区域间切换。五人标注验证 196 项子集，well-formedness κ=0.94，target selection κ=0.79。

**关键结果**：19 个 VLM 最高 strict point-in-box 准确率仅 32%。预测坐标落在两个候选框外的比例高达 60–92%。条件准确率（预测落在候选框内时）在水平位置、垂直位置、邻近、列表序上达 0.82–0.90，但在包含和遮挡上不显著高于 0.50（随机水平），说明多数失败源于候选定位而非关系理解。10 个模型上，基准准确率与 ScreenSpot-Pro 准确率 Spearman ρ=+0.74（探索性相关）。标记两个候选框的 oracle 设置使选择准确率提升 35–57 个百分点。
