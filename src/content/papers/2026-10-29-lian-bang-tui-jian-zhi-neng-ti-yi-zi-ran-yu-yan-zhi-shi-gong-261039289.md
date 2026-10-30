---
title: Federated Recommender Agents
title_zh: 联邦推荐智能体：以自然语言知识共享实现隐私保护的 LLM 推荐协作
authors:
- Jaehyung Lim
- Woojoo Kim
- Junyoung Kim
- Dongha Kim
- Wonbin Kweon
- Hwanjo Yu
affiliations:
- Pohang University of Science and Technology
- Sungkyunkwan University
arxiv_id: '2610.39289'
url: https://arxiv.org/abs/2610.39289
pdf_url: https://arxiv.org/pdf/2610.39289
published: '2026-10-29'
collected: '2026-10-30'
category: RecSys
direction: 联邦推荐 · LLM Agent 知识共享
tags:
- Federated Recommendation
- LLM Agents
- Knowledge Sharing
- Recommender Agents
- Privacy-Preserving
- Reasoning Integration
one_liner: 在不更新 LLM 参数的前提下，用 C–T–R 知识单元和双隐私记忆实现推荐 Agent 的联邦协作
practical_value: '- 在隐私约束或跨租户/跨店铺协作场景，可把用户行为抽象为 Condition–Transition–Reasoning 自然语言知识单元，去标识化后上传服务端做聚类整合，替代模型参数聚合，避免频繁微调
  LLM。

  - 用户画像拆成 semantic memory（偏好）和 decision memory（决策倾向）双记忆，推荐时分别用于检索和分支选择；实验显示分离维护比统一记忆保留率更高，可复用到个性化
  rerank。

  - 服务端对共享 reasoning 的整合需要跨分支 discrimination：相似行为下用户可能继续、回归或探索，必须保留不同 transition 分支，否则通用化会损失推荐精度。

  - 固定客户端与服务端 LLM 参数，仅更新自然语言知识库（memory bank），适合端侧资源受限的推荐 Agent 部署，便于业务侧冷启动与隐私合规。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
LLM 推荐智能体通过推理与记忆实现个性化，但集中访问用户信息带来隐私风险，而完全本地化又无法利用其他用户的行为模式。现有联邦推荐依赖模型参数或协同信号的数值聚合，往往需要更新 LLM 参数，计算和内存开销大。论文提出 Federated Recommender Agents 场景：本地 Agent 保留交互历史与私有记忆，仅通过自然语言知识协作，且不更新 LLM 参数。

**方法关键点**
- 共享知识单元采用 C–T–R 结构：Condition 描述行为上下文，Transition 描述下一步选择方向，Reasoning 解释该决策原因；生成时明确去除具体 item 和用户偏好细节。
- 每个客户端维护双隐私记忆：semantic memory 捕获用户偏好，decision memory 捕获不同上下文下的选择倾向；两者分离更新，推荐时共同参与 retrieval、branch selection 与 ranking。
- 服务端按 condition–transition 层次组织共享知识：先按 condition 聚类，再在 condition 内按 transition 分支，分支内做蒸馏（distillation）与时间合并（merge），最后对同 condition 下不同 transition 分支做 discrimination，强化 reasoning 的可区分性。
- 训练时客户端用共享 reasoning 作为起点做本地 revision，上传更新后的知识；推理时基于私有记忆检索最相关分支，再由 LLM 对候选 item 重排。

**关键结果**
在 Amazon CDs、Music、Office 三个领域 dense/sparse 六个数据集上，FedRecAgent 的最优变体在 N@10 和 MRR 上全部超过最强 baseline：N@10 相对提升 1.54%–9.19%，MRR 提升 3.01%–16.29%。在 FedSASRec hard-negative 评测下，六个数据集中的五个也取得最高。消融显示，去掉共享知识、去掉 discrimination 或合并双记忆都会显著掉点，证明结构化推理整合与双记忆互补的有效性。
