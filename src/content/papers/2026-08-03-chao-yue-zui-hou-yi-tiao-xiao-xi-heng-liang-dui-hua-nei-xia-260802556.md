---
title: 'Beyond the Final Prompt: Measuring the Effect of Within-Conversation Context
  on AI Answers'
title_zh: 超越最后一条消息：衡量对话内上下文对AI回答的影响
authors:
- Benjamin Tannenbaum
affiliations:
- Aiso, Tel Aviv, Israel
arxiv_id: '2608.02556'
url: https://arxiv.org/abs/2608.02556
pdf_url: https://arxiv.org/pdf/2608.02556
published: '2026-08-03'
collected: '2026-08-05'
category: Eval
direction: 对话式AI评估中查询单元的重新定义
tags:
- conversational AI
- evaluation
- context importance
- material difference
- prefix compression
one_liner: 实验证明忽略对话前置上下文会导致44.7%的回答发生实质性变化，压缩前缀仅部分弥补
practical_value: '- 评估对话式推荐/客服Agent时，必须携带完整对话历史，否则近半数回答会实质性变化，导致离线指标不可靠

  - 生产环境A/B测试或日志复盘，应将整个session作为query单元，而非单条最终消息，以准确反映模型是否满足用户需求

  - 出于成本考虑，可压缩对话前缀至160词，将实质性差异率从44.7%降至30.8%，但仍有约1/3的回答受影响，需权衡性价比

  - 构建对话评价数据集时，标注需基于完整上下文，仅看最后消息可能错误估计模型能力'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：AI系统评估通常将对话最后一条用户消息视为独立查询，但真实对话中，用户的请求往往分散在多轮交互中，忽略之前的上下文可能导致评估结果与实际能力不符。  
**方法**：从受控商业语料和公共PRISM数据集抽取180个多轮英文对话，固定最终用户消息和回答生成模型，分别用三种上下文生成答案：① 完整角色标注对话；② 仅最后一条消息；③ 最后消息+压缩前缀（≤160词）。由另一个评判模型在随机化标签下判断回答间是否存在“实质性差异”（足以改变用户行为）。主要分析使用逆概率加权校正选择偏差。  
**结果**：全量对话与仅最后消息的回答在44.7%的案例中出现实质性差异（95% CI 33.8%–56.1%），全量对话的请求满足度评分（0–4）平均高出0.49分（0.32–0.67）。加入压缩前缀后，实质性差异率降至30.8%，满足度差距缩至0.01分（−0.12–0.13），但仍有近1/3的回答存在实质性差异，无法完全替代完整历史。商业语料中的差异率（68.5%）远高于PRISM（35.4%）。一致性检验中，互换顺序重复判决的同意率达91.7%，κ=0.83。  
**结论**：对话上下文对AI回答有重大影响，评估时应将整个对话视为查询单元，而非仅最后一条消息；压缩前缀可部分缓解性能损失，但无法完全取代完整历史。
