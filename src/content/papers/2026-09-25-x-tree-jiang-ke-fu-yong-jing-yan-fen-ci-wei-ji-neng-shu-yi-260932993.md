---
title: 'X-Tree: Tokenizing Reusable Experience for Efficient Agent Generalization'
title_zh: X-Tree：将可复用经验分词为技能树以高效泛化智能体
authors:
- Sitao Cheng
- Xunjian Yin
- Zhiyuan Sun
- Yuxuan Li
- Ruiwen Zhou
- Xiangru Jian
- Victor Zhong
affiliations:
- University of Waterloo
- Duke University
- National University of Singapore
arxiv_id: '2609.32993'
url: https://arxiv.org/abs/2609.32993
pdf_url: https://arxiv.org/pdf/2609.32993
published: '2026-09-25'
collected: '2026-10-03'
category: Agent
direction: Agent 技能层级挖掘与 RL 训练
tags:
- X-Tree
- hierarchical RL
- RLVR
- OPSD
- web agents
- experience tokenization
one_liner: 把智能体轨迹中可复用动作片段按频次/长度/成功率挖成层级 X-Tree，并以数据、奖励、上下文三种方式训入权重
practical_value: '- 动作/行为序列先做 canonicalization：把点击、填表、搜索等映射为 verb⟨role⟩ token，去掉具体商品/页面
  id，再做频次挖掘；比直接使用原始 action 文本更容易发现跨商品、跨 query 的复用流程，适合从电商 session 日志抽取“浏览→筛选→加车→下单”等宏动作。

  - 离线无仿真环境时，不要只对整段 trajectory 做 SFT/RL；把高频且成功的子序列节点当作 RL 实例，用 gold prefix 做 partial
  rollout，奖励设为 step-matching + depth-scaled completion bonus。WebArena 上同样数据比整轨迹 SFT
  高 +4.5 SR，说明细粒度子过程很值钱。

  - 在线 RLVR 面临稀疏 verifier reward 时，可以加一个 adaptive skill bonus：按 group win rate 线性衰减，只在
  verifier 不能区分 rollout 好坏时生效；这样既提供早期稠密梯度，又不会在后期污染奖励。推荐/搜索 agent 的在线探索奖励可借鉴。

  - 用 OPSD/self-distillation 训练策略时，教师上下文中的 LLM 写 skill bank 可替换为从日志挖掘的 X-Tree 渲染文本，效果相当且零
  LLM 成本；对无法频繁调用大模型做抽象的工程场景很有用。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
多步 Agent 常把轨迹视为扁平动作流，SFT/RLVR 对每个 token 等权，忽略跨任务复用的子过程；而经验数据很稀缺。现有 LLM 生成 skill 只放 context，不进权重，检索之外难泛化。X-Tree 借鉴文本 tokenizer 的频次合并思想，从轨迹池直接挖出层级技能树。

**方法关键点**
- 先 canonicalization：原始 action → typed token verb⟨role⟩，剥离 id/物体名，保留可恢复信息；让结构相同动作共享符号。
- 用 X-Score = f·(len)^p·(succ+ε)^ps 选择合并对，再加压缩约束 f−1 > η(len)；递归合并成深度为 d 的 X-Tree，节点表示复用技能。
- 三种训练接入：离线 RL 中每个节点作为一个 GRPO 实例，从 gold prefix 出发，奖励 = step-match + depth-scaled completion bonus；在线 RLVR 中给 rollout 命中的节点加 adaptive bonus，其权重随 group win rate 从 λ0 衰减到 0；OPSD 中把 X-Tree 作为自教师 privileged context，做 per-token distillation。

**关键实验**
- WebArena 离线：Qwen2.5-7B，X-Tree+offline RL 22.9 SR，比 Go-Browse SFT 18.4 高 4.5；随机树 17.9，证明结构有效。
- ScienceWorld 3 个 scale：X-Tree bonus 比 outcome-only GRPO 高至 +4.9 SR（G0）、+3.9（G2）。
- WebShop 3 个 scale：success 高至 +3.6，graded 高至 +4.6。
- OPSD 中 X-Tree 与 LLM 写 skill bank 相当，零 LLM 调用。

最值得记住的一句：把经验 tokenize 成技能树，并作为数据、奖励、上下文三种方式注入训练，比只用扁平轨迹更省数据，也更可审计。
