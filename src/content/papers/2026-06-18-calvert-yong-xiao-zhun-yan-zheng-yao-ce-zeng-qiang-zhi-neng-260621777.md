---
title: 'CalVerT: Augmenting Agents with Calibrated Verifier Telemetry Improves Action
  and Learning in Knowledge-Intensive Tasks'
title_zh: CalVerT：用校准验证遥测增强智能体，改进知识密集型任务行动与学习
authors:
- Ashwin Vinod
- Ying Ding
- Elias Stengel-Eskin
affiliations:
- The University of Texas at Austin
arxiv_id: '2606.21777'
url: https://arxiv.org/abs/2606.21777
pdf_url: https://arxiv.org/pdf/2606.21777
published: '2026-06-18'
collected: '2026-06-23'
category: Agent
direction: Agent校准遥测改进检索决策
tags:
- Agent
- Calibration
- Retrieval-Augmented QA
- Self-Confidence
- Grounding Verifier
- Reinforcement Learning
one_liner: 给智能体状态加入校准自置信和接地验证分数，纠正过度信任参数知识与冗余检索
practical_value: '- 在购物助手、搜索Agent等场景，可引入类似双信号状态：用模型对候选答案的校准置信度（如 p(true)）和检索片段对答案的支持度（grounding
  verifier）作为决策依据，减少幻觉和无用检索。

  - 无需重新训练即可将遥测信号接入现有Agent框架（如 ReAct、RaR），只需在 Prompt 或状态中附加这两个分数，即可立竿见影提升回答准确率并节省检索成本。

  - 当业务场景面临“模型太自信却答错”或“反复查询知识库却已有充分信息”时，可借鉴该工作设计决策规则：当置信度低且接地分低时触发检索，当两者都高时直接回答。

  - 若后续采用强化学习微调Agent策略，将遥测信号作为状态特征加入，能进一步优化决策，此思路可直接复用于电商对话Agent的检索策略训练。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：LLM 智能体在知识密集型问答中存在两种典型失败模式——过度信任参数知识导致回答错误，以及已有充分证据仍反复检索浪费计算。

方法：提出 CalVerT，为智能体状态引入两类校准遥测：1）校准后的自置信分数（如 p(true)），反映模型对当前答案正确性的估计；2）接地验证分数，衡量检索段落对答案的事实支持程度。这两个信号作为额外上下文集成到智能体的观察中，无需训练即可接入现有框架；也可在强化学习训练中作为状态特征，引导策略优化。

结果：在四个 QA 基准上，CalVerT 无需训练就使 F1 提升，具体表现为更少错过检索时机（减少参数过度信任），同时降低冗余检索次数。在训练场景中，使用相同 RL 算法，带有遥测状态的智能体显著优于无遥测的基线，证明了状态增强对策略学习的额外收益。
