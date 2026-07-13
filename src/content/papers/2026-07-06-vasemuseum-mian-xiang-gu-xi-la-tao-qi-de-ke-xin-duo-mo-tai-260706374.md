---
title: 'VaseMuseum: Digital Intelligent Museum for Ancient Greek Pottery'
title_zh: VaseMuseum：面向古希腊陶器的可信多模态数字博物馆 Agent
authors:
- Jiazi Wang
- Nonghai Zhang
- Qiushi Xie
- Zeyu Zhang
- Yufeng Chen
- Yang Zhao
- Ling Shao
- Hao Tang
arxiv_id: '2607.06374'
url: https://arxiv.org/abs/2607.06374
pdf_url: https://arxiv.org/pdf/2607.06374
published: '2026-07-06'
collected: '2026-07-13'
category: Agent
direction: Agent 多模态推理与可靠性控制
tags:
- Multimodal Agent
- Retrieval Augmented Generation
- Hallucination Mitigation
- Reliability Control
- GRPO
- Digital Museum
one_liner: 通过证据级与响应级双重可靠性控制及无训练 GRPO 选择，缓解 VLM 在专业检索中的幻觉与过度自信
practical_value: '- **检索增强生成的双重可靠性控制**：在电商商品问答或推荐解释生成中，可先检索权威来源，通过源级控制过滤多样且可验证的证据，生成后由响应级控制检查声明是否被证据支持；若支持度低，强制输出中性回答，有效抑制幻觉。

  - **无训练推理时选择机制（GRPO-style）**：不更新 VLM 骨干，从多个候选回答中选择引用有效性和置信度校准更好的结果，适合成本敏感或无法微调的场景，可直接嵌入推荐
  Agent 的答案生成模块。

  - **3D 多模态感知与推理**：支持 2D 图像和 3D 点云输入，可为商品 3D 展示、AR 试穿等场景提供知识增强交互的参考架构。

  - **模块化 Agent 设计**：感知、检索、推理、控制解耦，便于在现有推荐或客服 Agent 中按需插入可靠性控制组件，快速提升可信度。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：数字博物馆中 VLM 辅助面临两大挑战：细粒度视觉证据需结合权威策展知识，但检索过程易引入弱源和不可验证引用；证据不足或模糊时 VLM 倾向自信作答而非校准不确定性。

**方法**：提出轻量模块化多模态 Agent 框架 VaseMuseum，核心为 VaseAgent，具备 2D/3D 感知、外部知识检索、推理时可靠性控制。控制分两层：①源级控制，从权威网络和博物馆来源选择多样且可验证的证据；②响应级控制，生成后检查声明与证据池一致性，若缺乏支持则引导输出中性、证据受限的回答。此外，引入训练无关的 GRPO 风格选择机制，在多个候选响应中偏好有效引用和置信度校准更好的答案，无需更新 VLM 骨干。

**结果**：在真实数字博物馆模拟实验中，相比带检索的 VLM 基线，VaseMuseum 显著提高引用有效性，减少知识密集型查询的幻觉，并在模糊情境下产生更多中性、可信的回答。
