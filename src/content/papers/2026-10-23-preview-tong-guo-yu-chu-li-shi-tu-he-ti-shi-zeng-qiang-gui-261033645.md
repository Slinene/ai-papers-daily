---
title: 'PreView: Enhancing GUI Grounding with Preprocessed Views and Cues'
title_zh: PreView：通过预处理视图和提示增强 GUI 定位
authors:
- Wenjun Hou
- Kaishuai Xu
affiliations:
- Independent Researcher
arxiv_id: '2610.33645'
url: https://arxiv.org/abs/2610.33645
pdf_url: https://arxiv.org/pdf/2610.33645
published: '2026-10-23'
collected: '2026-10-31'
category: Multimodal
direction: GUI 视觉定位 · 输入预处理增强冻结模型
tags:
- GUI Grounding
- Multimodal Agent
- Input Preprocessing
- Visual Cues
- Localization
- Frozen Model
one_liner: 提出轻量辅助预处理器 PreView，为冻结 GUI 定位模型生成局部放大视图与候选特定视觉/文本提示，无需微调提升定位准确率。
practical_value: '- 在电商/广告领域的 Agent 自动化（如 RPA、后台操作、广告审核）中，面对高分辨率复杂界面，可借鉴 PreView 的轻量辅助模型预测候选中心、裁剪放大局部视图，显著降低
  VLM 输入分辨率和 token 成本，同时提升小控件点击准确率。

  - 候选特定 cue 设计可直接复用：用红圈标记 + 位置提示（如“在左上角附近”）作为视觉 cue，结合候选身份/功能的简短文本描述（如“这是一个‘立即购买’按钮”），消除多控件密集布局下的歧义，这对商品详情页、广告落地页元素定位与合规检测尤其有用。

  - 冻结主干模型、仅训练轻量预处理模块的范式适合业务快速迭代：无需重训或微调现有 VLM/grounding 模型，可快速适配不同界面风格和业务场景；中心细化机制可借鉴为
  coarse-to-fine 定位策略。

  - 注意视觉输入预算管理：论文分析了视觉输入 budgets，启示在部署时可根据目标控件数量动态调整裁剪视图数量与分辨率，平衡准确率与推理成本。'
score: 6
source: huggingface-daily
depth: abstract
---

动机：GUI grounding 需要在高分辨率、密集布局的截图中精准定位小控件，单纯裁剪放大可能仍有歧义。现有 grounding 模型在专业界面面临挑战，问题在于如何更好地呈现输入。

方法：提出 PreView，一个辅助预处理器，不改动冻结 grounding 模型。训练轻量辅助模型预测并细化中心坐标，据此裁剪并放大局部视图，生成 zoomed-in 视觉输入。同时准备两类 cues：视觉 cue（红圈标记 + 位置提示）和文本 cue（候选控件的身份或功能描述）。冻结的 grounding 模型消费这些预处理输入，输出最终点击坐标。

结果：在五个 benchmark 上，PreView 平均提升了 Qwen3-VL-2B、OS-Atlas-4B、Qwen3-VL-4B 的 grounding 准确率，且无需进一步训练这些模型。消融分析考察了 views 与 cues 的贡献、中心细化和视觉输入预算的影响。
