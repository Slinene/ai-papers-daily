---
title: Verifiable Social Reasoning for LLM Assistants
title_zh: 面向 LLM 助理的可验证社会推理评估框架
authors:
- Amir Taubenfeld
- Zorik Gekhman
- Avigail Grinstein-Dabush
- Itay Laish
- Ariel Goldstein
- Marian Croak
- Avinatan Hassidim
- Yossi Matias
- Amir Feder
affiliations:
- Google Research
- Hebrew University
- University of Cambridge
arxiv_id: '2609.17496'
url: https://arxiv.org/abs/2609.17496
pdf_url: https://arxiv.org/pdf/2609.17496
published: '2026-09-14'
collected: '2026-09-19'
category: Eval
direction: 评估框架 · 多智能体模拟 · 社会推理
tags:
- LLM
- Social Reasoning
- Multi-Agent Simulation
- Evaluation
- User-Mediated
- Bias
one_liner: 构建多智能体模拟框架 Fuse，用隐藏动机与用户中介生成可验证社会推理评估，揭示 LLM 对偏见框架的系统性敏感
practical_value: '- 在对话式推荐或 Agent 客服场景中，可借鉴 Fuse 的多智能体模拟思路：让一个“用户代理”带着有偏/不完整信息咨询 LLM，同时隐藏真实意图作为
  ground truth，低成本构建可验证的对话推理评估集，避免依赖昂贵人工标注。

  - 论文发现 LLM 对用户偏置框架敏感，提示在电商导购/客服机器人中需警惕用户主观描述（如“我觉得这是假货”“这个商品很差”）引入的偏差，可在 prompt
  中显式要求模型分离事实与用户评价，或引入多轮确认机制而非直接采信。

  - “更长对话并不总是提高性能”的结论可迁移到对话策略：不要默认多轮追问一定好，应结合用户耐心和任务难度设置最大追问轮数，或训练模型只在关键信息缺失时提问。

  - 评估中区分模型所需细节与人类所需细节的思路，可用于生成式推荐的评测：设计“信息效率”指标，衡量模型在最少用户输入下能否正确推理偏好，而不仅是最终准确率。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：LLM 助手被广泛用于日常社交建议，但评估其在咨询场景中的社会推理困难：助手从主观用户叙述了解情况，且社会属性（如他人意图）缺乏可验证 ground truth。

**方法关键点**：提出 Fuse，一个多智能体模拟框架。目标代理持有隐藏动机，与其他代理（包括用户代理）交互；用户随后咨询被评估助手推断目标动机，从而在构造上提供可验证 ground truth。通过 24k 人工标注验证仿真保真度。应用于 12 个 LLM，系统隔离关键因素。

**关键结果**：用户中介加剧社会推理固有难度；LLM 对偏置用户框架表现系统性敏感；模型达到正确预测所需细节可多于人类；更长对话不一定提升性能，尽管提供澄清提问机会。开源 Fuse 及 21k 样本数据集。
