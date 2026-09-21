---
title: 'A Lie Detector Test for Language Models: Reading Knowledge a Model Won''t
  Reveal'
title_zh: 语言模型测谎：读取模型不愿透露的知识
authors:
- Hiskias Dingeto
affiliations:
- StackOne Technologies
arxiv_id: '2609.21996'
url: https://arxiv.org/abs/2609.21996
pdf_url: https://arxiv.org/pdf/2609.21996
published: '2026-09-18'
collected: '2026-09-21'
category: LLM
direction: LLM 内部知识探测与隐藏知识审计
tags:
- LLM auditing
- internal probing
- sandbagging
- unlearning verification
- concealed information test
one_liner: 用内部状态探测识别 LLM 隐藏但已知的答案，区分“不愿答”与“不会答”
practical_value: '- 在电商/广告 Agent 上线前，用 PIR 式内部探测评估模型是否真正掌握商品知识或策略却因 prompt 冲突、安全过滤误伤而故意不输出，避免仅靠行为日志误判能力。

  - 对经过 RLHF 或 unlearning 的模型，用内部识别信号验证敏感知识是否真正遗忘而非仅在输出层被压制，可用于合规删除用户数据或品牌敏感信息的审计。

  - 该方法无需标注真值，可对长尾商品/query 做无标签知识覆盖度审计，帮助识别模型“知道但不说”的候选，减少标注成本。

  - 可将候选答案的内部识别分数作为生成结果可信度辅助特征或 Agent 决策路由依据，在关键推荐/搜索环节检测模型是否隐藏高置信答案。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

**动机**：LLM 可能隐藏已知知识（如 sandbagging、欺骗性回答），或因 unlearning 丢失知识，但仅靠行为输出无法区分“不愿答”和“不会答”，这影响能力评估、安全审计与遗忘验证。

**方法关键点**：借鉴法医学 Concealed Information Test，提出 Probe of Internal Recognition (PIR)。将问题与候选答案一起输入模型，从其内部状态读取模型对哪个候选识别为正确，无需诚实参考模型或标注真值。PIR 可应用于多选题和自由形式生成，信号具有因果性，能提供超出黑盒行为线索的额外信息。

**关键结果**：在 5 个模型家族 8 个模型上，PIR 以 0.70–0.87 的平衡准确率恢复被识别答案，显著高于未知项基线 0.28–0.40 和随机水平 0.25。在 prompted deception、trained sandbagging、password-locked 和 circuit-broken checkpoints 等各种隐藏形式下，识别率保持在 0.85–0.93。当 unlearning 移除知识后，识别率降至模型从未学过的水平。因此 PIR 能有效分离模型“不愿回答”与“无法回答”，支持 sandbagging 审计与 unlearning 验证。
