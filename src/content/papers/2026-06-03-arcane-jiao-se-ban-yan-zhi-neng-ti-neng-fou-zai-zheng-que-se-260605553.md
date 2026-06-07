---
title: 'ArcANE: Do Role-Playing Language Agents Stay in Character at the Right Time?'
title_zh: ArcANE：角色扮演智能体能否在正确时间保持角色性格？
authors:
- Woojung Song
- Nalim Kim
- Sangjun Song
- Chaewon Heo
- Jongwon Lim
- Yohan Jo
affiliations:
- Graduate School of Data Science, Seoul National University
arxiv_id: '2606.05553'
url: https://arxiv.org/abs/2606.05553
pdf_url: https://arxiv.org/pdf/2606.05553
published: '2026-06-03'
collected: '2026-06-07'
category: Eval
direction: 角色扮演智能体评估 · 心理轨迹一致性
tags:
- role-playing
- evaluation
- character-arc
- language-agents
- narrative-understanding
one_liner: 提出 ArcANE 基准，用“角色弧”评估角色扮演智能体在心理轨迹上的动态一致性，发现弧上下文在未见场景中优势最大。
practical_value: '- **客服/虚拟人个性演化**：为长期用户交互的电商客服或直播虚拟人设计阶段性人设档案，借鉴“角色弧”按交互阶段调整回复倾向，避免机械一致。

  - **对抗性评估样本构造**：用“相同场景跨阶段提问”和“文本外推演情境”生成难度分层的测试用例，探测模型在未见情境下的性格漂移，用于业务人格 agent 的鲁棒性评估。

  - **上下文策略组合**：在构造角色 prompt 时，除摘要和检索片段外，加入按时间线标注的心理状态描述（弧），可显著提升角色一致性，尤其适合长会话或连载式互动。

  - **微调数据构造**：用小说角色弧数据微调基础模型，能明显改善对人物心理变化的捕捉，可用于训练具有动态人格的对话推荐或导购 agent。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有角色扮演基准只测量对原著的静态知识回忆，无法评估角色在不同故事阶段的价值观与行为变化是否合理，尤其当用户提出原著未覆盖的假设场景时。
**方法**：自动构建 ArcANE 基准，覆盖 17 部小说中的 80 个主要角色。将每部小说的叙事划分为若干心理阶段（角色弧），对每个角色设计跨阶段的相同情景提问，分为“文本内情境”（原著有依据）和“文本外情境”（完全假设）。评估 6 个模型在 6 种上下文模式下的表现，包括仅摘要、原著检索、角色弧等，并微调得到 ArcANE-8B/32B。
**关键结果**：在所有模型上，使用角色弧作为上下文均优于其他策略；在文本外情境中优势最大（检索方法几乎无帮助）。微调后的模型进一步拉开差距，表明明确的阶段化心理信息对维持动态角色真实性至关重要。
