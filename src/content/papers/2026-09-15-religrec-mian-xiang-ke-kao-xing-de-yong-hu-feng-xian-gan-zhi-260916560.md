---
title: 'ReliGRec: Reliability-Oriented LLM-Based Generative Recommendation via User-Risk-Aware
  Prompt Routing'
title_zh: ReliGRec：面向可靠性的用户风险感知生成式推荐提示路由
authors:
- Haoran Yang
- Fei Chen
- Yutian Xiao
- Jiahao Liang
affiliations:
- Central South University
- Beihang University
- South China University of Technology
arxiv_id: '2609.16560'
url: https://arxiv.org/abs/2609.16560
pdf_url: https://arxiv.org/pdf/2609.16560
published: '2026-09-15'
collected: '2026-09-16'
category: GenRec
direction: 生成式推荐 · Semantic ID + 风险路由
tags:
- LLM4Rec
- Semantic ID
- Prompt Routing
- Weak Risk
- Graph Token
- LoRA
one_liner: 用弱监督用户风险信号在解码前路由 Simple/Cautious Prompt，并注入时序 Graph Token 做 Semantic ID
  生成
practical_value: '- 用户级弱风险信号可以从评价反馈里低成本构建：Beauty 用 helpful/total，Yelp 用 useful/(useful+funny+cool)，高/低阈值取
  0.85/0.40，再按多数投票聚合到用户。电商/内容场景有差评、举报、刷单投诉等弱标签，可用来标用户行为波动，不必确认恶意身份，降低人工审核成本。

  - 把风险估计做成生成前控制，而不是训练侧重加权或生成后 rerank：推理时按分数路由不同 prompt。Cautious Prompt 显式要求忽略短时/孤立/重复证据、优先稳定且协同支撑的
  pattern，并用 Graph Token 补充上下文。迁移到推送文案、搜索 query 推荐时，可对高波动用户切换更保守的生成指令。

  - Graph Token 注入是更稳定的增益点：按时间窗口建图得到用户/物品状态，聚合窗口物品向量后过 temporal Transformer，再投影替换
  LLM 输入占位。Beauty 上相比纯历史序列，Hit@5 +2.78%、NDCG@5 +4.65%；工程上可离线缓存窗口 Graph Token，控制在线开销。

  - 弱风险路由本身要谨慎：文中 weak-risk-guided 路由并未超过 All-Simple prompt，耗时也介于 All-Simple 和 All-Cautious
  之间。业务上如果目标是稳定性/风控，可结合在线 A/B；不要把弱风险分数当校准概率，也不要单独把它作为推荐质量提升手段。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
LLM 生成式推荐通常对所有用户使用同一 prompt，但真实交互历史里存在兴趣突变、bursty 行为、过度重复和协同不一致，这些可能来自正常偏好演化，也可能来自 shilling 攻击。统一 prompt 容易让模型过度依赖不稳定历史证据。已有 robust 方法多在训练侧重加权或图聚合，输出侧用 uncertainty 重排；缺少在生成前按用户弱风险选择策略的机制。

**方法关键点**
- 弱监督 proxy label：从 review 投票比构造用户级弱风险标签，Beauty 用 helpful/total，Yelp 用 useful/(useful+funny+cool)，阈值 0.85/0.40，多数投票聚合；仅部分用户有标签。
- 双路用户表示：Behavior Token 由 Transformer 编码最近 50 条交互得到；时序 Graph Token 按滑动时间窗口建用户-物品二部图，GAT 得到节点状态，再聚合窗口物品向量，经 temporal Transformer 得到动态协同表示。
- Dual-View Weak-Risk Estimator：拼接两个表示后过 MLP 输出弱风险分数，用正类加权 BCE 训练。
- 生成与路由：离线 RQ-VAE 学四层 Semantic ID；Qwen2.5-1.5B-Instruct + LoRA 做生成器；Graph Token 投影后替换输入占位。训练按 proxy label 分配 Cautious/Simple prompt，推理用固定阈值 0.5 路由。Cautious Prompt 要求优先稳定、协同支撑证据，减少孤立/短期/重复信号的影响。

**关键实验**
- 数据集：Amazon Beauty、Yelp，leave-one-out 评估。
- 推荐指标：Beauty 上相比最强 baseline LETTER-TIGER，H@1 提升 54.67%（0.01771 vs 0.01145），N@5 提升 27.28%；Yelp 上 H@1 持平 0.00540，其余指标第二。
- 弱风险估计：AUPRC Beauty 0.2633（GraphRfi 0.2187），Yelp 0.2990（PGT4Rec 0.1990）；Graph+Behavior 融合优于单视图。
- 路由分析：weak-risk-guided 路由未超过 All-Simple prompt；耗时 0.479s，介于 All-Simple 0.460s 和 All-Cautious 0.548s 之间。
- 消融：注入静态或时序 Graph Token 均优于 history-only；时序图对弱风险预测 AUPRC 提升更明显。

**最值得记住的一句话**
弱风险信号可以作为生成前的控制信号，但当前证据只支持“路由行为”成立，不证明它比统一强 prompt 更好；Graph Token 注入才是更稳定可复用的推荐增益。
