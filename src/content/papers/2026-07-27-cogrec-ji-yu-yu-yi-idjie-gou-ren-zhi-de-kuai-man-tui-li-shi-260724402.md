---
title: 'CogRec: Structure-Cognitive Fast-and-Slow Reasoning for Generative Recommendation'
title_zh: CogRec：基于语义ID结构认知的快慢推理生成式推荐
authors:
- Xiang Liu
- Jingsong Su
- Shuqi Zhao
- Pengbo Mo
- Yiming Qiu
- Huimu Wang
- Mingming Li
- Jiao Dai
- Jizhong Han
- Songlin Hu
affiliations:
- Institute of Information Engineering, Chinese Academy of Sciences
- School of Cyber Security, University of Chinese Academy of Sciences
- School of Artificial Intelligence, Beijing Normal University
- JD.com
arxiv_id: '2607.24402'
url: https://arxiv.org/abs/2607.24402
pdf_url: https://arxiv.org/pdf/2607.24402
published: '2026-07-27'
collected: '2026-07-28'
category: GenRec
direction: 生成式推荐 · Semantic ID · 结构推理
tags:
- Generative Recommendation
- Semantic IDs
- Fast-and-Slow Reasoning
- SID Routing
- Structure-grounded Reasoning
- Constrained Decoding
one_liner: 将推荐推理定义为SID空间内的Match/LateralJump/Explore操作，实现结构认知的快慢组合推理
practical_value: '- **构建语义ID拓扑增强推理**：在现有SID分层编码基础上，利用码本余弦相似度构建层内语义图（top-16邻居，相似度阈值0.15），并建立项级HNSW索引，为生成式推荐提供可导航的离散推理空间，可直接应用于电商商品的Semantic
  ID体系。

  - **操作化快慢推理**：将推理过程分解为Match（快速垂直匹配）、LateralJump（沿图边横向跳转）和Explore（无直接边时的探索），根据历史锚点与目标项的层间关系自动生成路由监督，无需额外模块，可通过控制非Match步数调节推理深度，适合线上自适应推理策略。

  - **多阶段训练管线设计**：先对齐新增SID token embedding（冻结基座），再训练直接SID生成，最后从同一checkpoint分叉出自然语言推理和结构路由分支，保证公平对比且工程可控。训练时对用户历史与助理回复全掩码计算loss，直接强化输入侧SID表征。

  - **推理格式的选择依据**：实验表明当用户历史与目标前缀匹配不足但存在可学习的层内语义关系时（中等难度），结构路由推理优于语言推理和直接生成；否则直接生成更高效。这可为业务中是否启用推理模块提供决策参考。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
基于语义ID（SID）的生成式推荐将物品表示为分层离散token序列，并将下一物品预测转化为受约束的序列生成。现有方法仅将SID作为输出目标记忆，其层次结构、层内关系和物品近邻未被作为显式推理空间。虽已有方法在生成前先产生自然语言理由，但该理由与最终的离散SID解码空间耦合较弱，导致推理-预测空间割裂。CogRec旨在将推理过程嵌入SID拓扑之中，实现结构认知的快慢推理。

**方法关键点**
- **结构认知SID拓扑**：在标准分层SID基础上，对每一层构建码本质心的语义图（余弦相似度top-16邻居，过滤阈值0.15），并基于HNSW建立物品级近邻索引，将SID空间从纯层次树转变为可导航的推理空间。
- **SID路由操作**：为每对历史锚点与目标物品逐层判定操作类型：若代码相同则Match（快速定位）；若存在图边则LateralJump；否则Explore（无直接边，需从序列模式学习）。将Match/LateralJump/Explore的成本设为0/1/2，用于诊断路由复杂度，但不参与训练损失。
- **多阶段训练**：Stage 0初始化拓扑与扩展词表；Stage 1冻结基座，仅训练新增SID token嵌入与物品语义对齐；Stage 2训练直接SID生成；Stage 3a和3b分别从同一Stage 2 checkpoint出发，训练自然语言推理和SID路由推理分支，共享SID映射、候选空间与trie约束解码。所有训练采用用户历史-助理回复的联合语言模型损失，以强化输入侧SID表征。

**关键结果**
- 在Beauty、Sports、Toys三个Amazon数据集上，SID路由相较于直接生成在Sports上Hit@10/NDCG@10分别提升至0.0473/0.0274（直接为0.0427/0.0256），在Beauty上Hit@10到达0.0854，但在Toys上略逊于直接生成，表明推理收益与数据集结构相关。
- 难度分层显示：中等难度（历史与目标前缀不共享深度但语义图可达）样本上，路由推理显著优于纯语言推理和直接生成；简单样本直接生成已够，困难样本所有方法均难，说明结构路由在可学习转移但无直接匹配时有条件优势。
- 路由步骤分布表明70%以上测试样本需要3-4个非Match操作，推理过程带来更长的生成token序列，增加解码成本，存在误差累积风险。

**核心启示**
在SID空间内定义可操作的结构化推理路径，比自然语言理由更紧密地对齐生成目标，但推理的适用性取决于历史与目标的语义拓扑关系。
