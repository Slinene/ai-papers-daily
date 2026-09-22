---
title: 'onPanda: Efficient Annotation of On-Policy Alignment Data for LLMs and Agents
  via Token-Level Correction'
title_zh: onPanda：基于 Token 级纠错的 LLM 与 Agent 对齐数据高效标注
authors:
- Lei Yang
- Mengyin Liu
- Jia Wang
- Hangyu Guo
- Liang Zhao
- Zheng Ge
- Kang An
- Binxing Jiao
- Qi Han
- Daxin Jiang
affiliations:
- StepFun
- Xiamen University
arxiv_id: '2609.24983'
url: https://arxiv.org/abs/2609.24983
pdf_url: https://arxiv.org/pdf/2609.24983
published: '2026-09-20'
collected: '2026-09-22'
category: Training
direction: LLM 对齐数据标注 · token-level correction
tags:
- LLM alignment
- token-level correction
- data annotation
- on-policy
- agent trajectories
- SFT
one_liner: 用 token 级定位-纠错-续写循环高效生成 on-policy 对齐数据，标注时间中位数降低 52%
practical_value: '- 生成式推荐/对话式 Agent 的 SFT 数据可由模型续写产生：先让模型生成候选回复，标注员只做 token 级首错纠正，后续自动截断重新生成，大幅减少人工整段改写，同时保持数据接近模型自身分布。

  - token 级纠错记录提供「前缀 - 错 token - 正确 token」的孪生样本，可直接构造细粒度偏好对或 token 级 loss，比整句 preference
  更有定位能力，适合电商导购话术、搜索词改写等短文本生成的调优。

  - 对 Agent 轨迹标注可借鉴其交互思路：在 trajectory 回放中定位第一个错误 step/token，修正后继续 roll-out，能获得低成本
  on-policy 轨迹数据并保留后续状态分布，适合工具调用、多轮商品推荐对话的数据采集。

  - 工程上可参考其候选 token 展示与编辑结合的方式：先给出模型 top-k token 供快速点选，无法匹配时再自由输入，兼顾标注效率与灵活性；概率颜色编码帮助标注员快速定位低置信
  token。'
score: 6
source: huggingface-daily
depth: abstract
---

动机：LLM 对齐与 Agent 数据标注存在成本高、off-policy 偏差大、监督粒度粗的瓶颈。传统人工撰写或 post-editing 得到的响应偏离模型自身采样分布，不利于 on-policy SFT 与偏好建模。

方法关键点：onPanda 核心是 token-level correction 交互。标注员阅读模型响应，定位第一个不合适 token，从模型候选 token 中选择替代或直接编辑文本；系统截断该位置之后的所有 token，从修正后的前缀继续生成，重复「定位-纠错-续写」循环直到满意。最终响应中绝大部分 token 由模型自身生成，保留采样分布。纠错操作同时记录精确位置和正负样本对。系统可连接外部工具与 harness，支持真实环境中的 Agent trajectory 标注。另发布 Panda-CVL 数据集与 token-level correction benchmark。

关键结果：小规模对照研究中，onPanda 的 median 标注时间比 manual post-editing 降低 52%；生成数据适合构建 on-policy SFT 与 preference 数据，并附带 token 级细粒度监督。
