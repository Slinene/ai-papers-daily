---
title: 'HarnessMM: Recursive Self-Improvement for Harness Token Efficiency'
title_zh: HarnessMM：通过守卫决策复用与递归自改进提升 Agent 工具链 Token 效率
authors:
- Yuhua Jiang
- Chang Xu
- Feifei Gao
- Li Zhao
affiliations:
- Tsinghua University
- Microsoft Research Asia
arxiv_id: '2610.32813'
url: https://arxiv.org/abs/2610.32813
pdf_url: https://arxiv.org/pdf/2610.32813
published: '2026-10-23'
collected: '2026-10-26'
category: Agent
direction: Agent 工具链推理复用与配置自改进
tags:
- Agent Harness
- Token Efficiency
- Decision Reuse
- Recursive Self-Improvement
- Tool Use
one_liner: 用守卫决策复用替换工具反馈后的重复推理回调，不改模型权重即可降低Agent harness token成本
practical_value: '- 在电商/导购类 Agent 中，工具返回收据后若满足预设 guard（如价格、库存未变），直接用缓存的动作参数继续执行，避免重复调用
  LLM；把“已解析的工具调用”做成可执行决策图，存字面参数与依赖，工程上可大幅省 token。

  - 引入 Certified Callback Substitution：在模型-工具边界注册回调替换时，保留原生接口并记录删除慢回调，新语义或证据不足就回退原模型，实践中保障效果不下降。

  - 借鉴 RSI：固定模型权重，用训练/评估反馈迭代优化 harness 配置（守卫阈值、缓存策略），验证集选优，能以低成本对线上 agent 配置做自动调参。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：Agent harness 在工具反馈后反复触发推理，即使之前的调用已经确定了下一步动作，造成大量 token 浪费；现有压缩/历史管理方法治标不治本。

**方法**：HarnessMM 在模型-工具边界引入 controller，通过 Executable Decision Graphs 存储已解析的确切动作、字面参数、因果依赖和公共守卫。Guarded Decision Reuse 根据观察到的 receipt 激活持久化决策；Certified Callback Substitution 通过原生接口执行并移除已注册慢回调。当出现新语义决策、不支持的证据或 selector 弃权时，回退到原 actor 推理。递归自改进（RSI）从训练反馈迭代优化 harness 配置，验证集选择部署配置，模型权重保持不变。

**结果**：HumanEval 上 Codex 成功率保持 90.82%，Tokens/task 从 66.72k 降至 47.02k，节省 29.54%；DeepSeek Harness 成功率从 71.43% 升至 85.71%，Tokens/task 从 96.28k 降至 11.62k，节省 87.93%；MBPP 消融比单次图低 26.91%，比保留回调低 19.52%。
