---
title: 'Transfiver: Human-AI Co-Inference through a Shared Editable State'
title_zh: Transfiver：通过共享可编辑状态实现人机协同推理
authors:
- Minji Park
- Seunghyun Yoon
- Hyuk Lim
affiliations:
- Korea Institute of Energy Technology (KENTECH)
arxiv_id: '2609.03797'
url: https://arxiv.org/abs/2609.03797
pdf_url: https://arxiv.org/pdf/2609.03797
published: '2026-09-03'
collected: '2026-09-06'
category: Agent
direction: 人机协同推理 · 共享可编辑状态
tags:
- human-AI interaction
- editable state
- state management
- memory
- transparency
one_liner: 提出 Transfiver 架构，让人类与 AI 共享同一可编辑持久状态，实现可验证的协同推理
practical_value: '- 在电商推荐用户建模中，可将用户长期偏好维护为一个显式可编辑状态，让用户直接修改（例如对某类商品不感兴趣）并立即影响后续推荐，而不是依赖隐式行为推断或追加历史记录。

  - 模型隐式更新状态时采用“修订已有项”或“创建新项”两种操作，有助于保持偏好状态的一致性，避免过期信息（如旧地址、旧兴趣）干扰推荐或搜索排序。

  - 参数与状态分离的设计允许在部署期间动态更新状态而不重新训练模型，适合线上个性化记忆的实时更新，降低维护成本。

  - 论文为架构性设想，缺乏具体实现与实验验证，落地前需要自行设计状态表示、更新规则和冲突消解机制。'
score: 6
source: arxiv-cs.HC
depth: abstract
---

**动机**：长期人机交互中，模型隐式更新引导推理的信息，用户无法直接查看或控制，导致过期信息持续影响回答。论文提出 Transfiver 架构，让交互特定信息保存在单一持久状态 S_t 中，模型和人类均可更新。

**方法关键点**：
- 共享可编辑状态：所有交互相关信息存于 S_t，模型计算直接读取该状态，人类修改即改变后续推理依据。
- 两种状态演化模式：隐式流更新由模型解释持续交互，判断新信息是修订已有状态项还是创建新项；显式定向编辑由人类检查并修改指定状态项。两者作用于同一底层状态，避免多副本不一致。
- 参数与状态分离：共享参数 θ 在部署前学习，持久状态 S_t 在部署期间演化，无需重新训练参数。

**结果**：论文未报告量化实验结果，属于架构性工作；作者指出扩展到丰富自然语言、关系型和大规模共享状态仍是开放问题。
