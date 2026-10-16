---
title: Information-Gain Calibrated On-Policy Distillation for Deep Search Agents
title_zh: 基于信息增益校准的在线策略蒸馏用于深度搜索智能体
authors:
- Chenxi Li
- Xueyang Feng
- Songyang Liu
- Chenxu Wang
- Xiaoying Tang
- Chaozhuo Li
- Litian Zhang
affiliations:
- The Chinese University of Hong Kong, Shenzhen
- Renmin University of China
- Beijing University of Posts and Telecommunications
- Beijing Academy of Artificial Intelligence (BAAI)
arxiv_id: '2610.20664'
url: https://arxiv.org/abs/2610.20664
pdf_url: https://arxiv.org/pdf/2610.20664
published: '2026-10-14'
collected: '2026-10-16'
category: Training
direction: On-policy distillation · 信息增益校准
tags:
- On-policy Distillation
- Information Gain
- Search Agent
- Evidence-blind Supervision
- Multi-turn Agent
- LLM Distillation
one_liner: 提出 IG-OPD，用检索后信息增益校准 OPD 的预算与方向先验，修正证据盲监督
practical_value: '- 多轮检索/会话 agent 蒸馏时，teacher 对 query 的似然偏好不等于检索证据的实际效用；可引入 post-retrieval
  information gain（如文档是否包含答案、证据是否改变后续置信）作为校准信号，对 query/tool-call tokens 做奖励修正，避免好
  query 被误罚。

  - 按 turn 而不是按 token 长度分配监督权重：搜索/召回 turn 通常短但信息增益高，合成/回答 turn 长但增益低；ITC 的预算重分配可通过
  token loss 乘 ratio 实现，无需改 trainer，工程成本低。

  - 在电商搜索/推荐中，用户 query 改写、检索式推荐、多跳推理 agent 训练可借鉴 IQC 只修正 action-critical tokens（query
  字符串、工具参数）而保持 reasoning tokens 不变；对第一跳正反馈、后续跳负反馈更可靠，可据此设计课程和 cosine ramp 避免早期对搜索行为的过度惩罚。

  - 训练后模型推理无额外开销，但蒸馏时需额外做一次 teacher 对 gold answer 的评分，增加约 10% 训练时间/显存，适合离线训练阶段接受。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
Deep search agents 需要多轮检索外部证据，用 RL 训练昂贵且难以收敛。On-policy distillation (OPD) 提供稠密监督，但标准 OPD 在监督每个 student query 时只用 pre-retrieval 上下文，产生 evidence-blind supervision (EBS)：teacher 偏好不一定等于检索证据的实际效用。诊断发现两个隐式先验：budget prior 按 token 长度分配监督，导致首个搜索 turn 贡献 51.1% 信息增益却只获 18.0% 监督；direction prior 使 43.7% 的 query 监督与 post-retrieval IG 符号不一致。

**方法关键点**
- 定义 post-retrieval information gain g_t 为 teacher 对 gold answer 的 length-normalized log-likelihood 变化。
- ITC 用 |g_t| 校准 turn 预算 q_t = (1+λtanh(|g_t|/σ_g)) / sum，替代 token 长度权重，防止单 turn 垄断，保留 response 基线。
- IQC 用 signed g_t 对 action-critical tokens（工具名/参数/query 字符串）添加 α_k g_t / m_t 校正，只修正搜索决策，不修改 reasoning tokens。
- cosine ramp 逐步增加 α，作为从 imitation 到 evidence-calibrated distillation 的课程。
- 整体为 policy-gradient surrogate，用 stop-gradient 的 calibrated advantage。

**关键结果**
在 6 个多模态搜索基准（MMSearch, MMSearch+, BrowseComp-VL, LiveVQA, SimpleVQA, FVQA）上，IG-OPD 比 OPD 平均提升 3.4pp（2B 学生）和 1.7pp（4B 学生）；4B 学生在 MMSearch 和 BrowseComp-VL 上超过 8B teacher。消融显示 ITC 把搜索 turn 预算从 52.4% 提升到 80.9%，训练中 first-search gold-evidence hit rate 从 12.9% 升至 16.9%。训练开销 +11.6% 时间、+10.6% 显存，推理无额外成本。

**最值得记住的一句话**：用检索后信息增益校准 OPD 的预算与方向，让蒸馏监督真正反映证据效用而非 teacher 措辞偏好。
