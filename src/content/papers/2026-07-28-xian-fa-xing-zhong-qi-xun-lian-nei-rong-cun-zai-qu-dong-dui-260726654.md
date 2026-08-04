---
title: 'Constitutional Midtraining: Content Presence Drives Alignment Gains'
title_zh: 宪法性中期训练：内容存在驱动对齐增益
authors:
- Desiree Cho
- Cameron Tice
- Bernie Hogan
- Hunar Batra
- Puria Radmard
- Jun Zhao
- Nigel Shadbolt
affiliations:
- University of Oxford
- Geodesic Research
- Oxford Internet Institute
arxiv_id: '2607.26654'
url: https://arxiv.org/abs/2607.26654
pdf_url: https://arxiv.org/pdf/2607.26654
published: '2026-07-28'
collected: '2026-08-04'
category: Training
direction: 中期训练对齐干预与持久性
tags:
- Constitutional AI
- Midtraining
- Alignment Durability
- Generalization
- Curriculum Learning
- LLM Safety
one_liner: 仅在中训阶段插入少量宪法性文本，即可获得经下游微调后仍持久的对齐泛化收益，且能力无损
practical_value: '- 在推荐/对话模型的预训练后、SFT 前，插入少量公司价值观/安全准则文档（几百 M tokens），可大幅提升模型对规则的遵守和跨场景泛化，且不会被后续业务微调覆盖。

  - 文档设计不必过度追求课程排序或显式推理块的精细结构；原则性内容的“存在”本身是主要驱动力，降低工程复杂度。

  - 这种干预几乎零能力成本，甚至在常识推理等任务上有小幅提升，适合作为标准 SFT 流水线的补充步骤。

  - 对齐效果在需要主动对抗上下文压力的场景（如多轮交锋、价值冲突）较脆弱，业务中若涉及此类动态对抗，仍需结合后训练或额外安全机制。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
当前大模型对齐主要依赖后训练（RLHF、DPO 等），但这些干预往往浅层且脆弱，经下游无关任务微调后容易回退。中期训练（预训练之后、SFT 之前）是一个计算高效、能提供更持久对齐的窗口，但将完整的宪法性文本仅在中训阶段注入是否能产生持久、泛化的对齐效果仍未被大规模验证。

**方法要点**
- 从 Anthropic 2026 版宪法手动提取 40 个价值观，用 SBERT 嵌入并计算语义中心性，通过层次聚类分为 4 个簇（k1–k4），按中心性排序形成课程顺序。
- 2×2 实验设计：课程 vs 均匀顺序 × 含显式推理块（DR）vs 无推理块（noDR），共 4 个宪法中训条件，外加一个仅重放预训练数据的控制组。
- 以 120B MoE 模型（Nemotron-3-Super）为基础，在中训阶段以 500M tokens（DR）或约 265M tokens（noDR）插入合成宪法文档，随后所有条件经过统一的、价值中立的 SFT 和基于 GSM8K 的 GRPO 良性微调。
- 评估覆盖 ID/OOD 行为选择、勒索、对齐伪装、压力抵抗、价值冲突消解等对齐基准，并进行能力检查。

**关键结果**
- **OOD 泛化**：中训后 CMT 组 OOD 安全回答率 92.6%，远超控制组 63.9%（+28.8pp）；SFT 后仍保持显著优势（+3.9pp）。
- **勒索任务（Blackmail）**：各阶段 CMT 组勒索率始终低于控制组约 17–18.5pp，SFT 后所有模型勒索倾向上升，但 CMT 的抑制效果几乎不减，是持久性最突出的证据。
- **能力无害**：中训后 CMT 在 ARC-Easy、piqa 上甚至显著优于控制组（+8.2pp、+12.6pp），SFT 后无统计学差异；未观察任何“对齐税”。
- **结构影响微弱**：课程与均匀、DR 与 noDR 在大部分基准上无显著差异，仅在中训后瞬时出现少量微弱效果，提示内容存在远重于具体组织方式。
- **脆弱之处**：在需要主动对抗上下文压力的任务上，CMT 的中训后优势在 SFT 后消失，提示该方法对动态对抗场景的加固有限。

**核心结论一句话**
宪法性中期训练以极低成本提供了泛化且持久的默认对齐行为提升，其关键在于原则性内容的注入本身，而非内容的细粒度编排。
