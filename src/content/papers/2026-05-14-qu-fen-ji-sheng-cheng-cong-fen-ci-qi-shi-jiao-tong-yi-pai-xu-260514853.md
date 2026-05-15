---
title: 'Discrimination Is Generation: Unifying Ranking and Retrieval from a Tokenizer
  Perspective'
title_zh: 区分即生成：从分词器视角统一排序与检索
authors:
- Shuli Wang
- Junwei Yin
- Changhao Li
- Senjie Kou
- Chi Wang
- Yinqiu Huang
- Yinhua Zhu
- Haitao Wang
- Xingxing Wang
affiliations:
- Meituan
arxiv_id: '2605.14853'
url: https://arxiv.org/abs/2605.14853
pdf_url: https://arxiv.org/pdf/2605.14853
published: '2026-05-14'
collected: '2026-05-15'
category: RecSys
tags:
- RecSys
- Semantic ID
- Discriminative Training
- Unified Retrieval-Ranking
- Tokenizer
- Generative Recommendation
one_liner: 将分词器嵌入判别式排序模型端到端联合训练，使排序器原生具备生成式检索能力
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机** 生成式推荐将物品量化为语义ID（SID）并通过束搜索实现全库检索，突破了传统漏斗的计算瓶颈。然而，现有SID构建过程与个性化信号完全解耦：分词器仅编码物品静态属性，用户-物品交叉特征（u2i）从未参与码本训练，导致同一个SID对不同用户无区分度，生成式检索持续落后于判别式排序。根本原因在于架构层面——分词器独立训练，判别式梯度无法回传至码本，个性化信号天然缺失。本文重新审视SID的本质：排序在物品空间求argmax，检索在token空间求argmax，二者是同一优化问题在不同粒度上的求解；生成式检索能力早已蕴含在判别式排序模型之中，分词器的角色是将其释放。

**方法关键点**  
- **特征分类体系**：将特征分为三类——物品静态特征（Type-I）编码入SID；请求级特征（Type-II）作为排序和检索的条件；用户-物品交叉特征（Type-III）在训练时隐式拉近码本边界至推荐决策边界，推理时通过MLP u2t在token粒度近似。  
- **统一分词器**：SID解耦为地址码本（VQ+RQ，EMA更新）与语义嵌入（端到端训练），解决了寻址与语义共享的矛盾；离线平衡K-Means树保证零碰撞初始化。  
- **统一训练**：五部分联合损失——排序BCE、逐层检索BCE、码本承诺损失、语义重构损失及MLP u2t蒸馏损失。每个训练步，同一token桶内物品的u2i特征聚合为u2t，驱动码本分区向用户偏好边界靠拢；MLP u2t学习从用户表示和SID前缀预测个性化u2t，弥补桶内平均的信息损失。  
- **统一推理**：排序模型直接执行束搜索检索，仅将物品嵌入替换为SID前缀嵌入，并将u2i特征替换为MLP u2t在线输出，检索路径与排序路径共享同一Mixer，从根本上消除传统双系统语义鸿沟。

**关键结果**  
在5个数据集上（淘宝广告、KuaiRec-S/B、美团大规模及小规模业务），DIG在检索Recall@10上全面超越TIGER、LETTER、DAS、DOS、ETEGRec等基线，同时排序AUC一致提升。稀疏且u2i特征丰富的工业场景增益尤为显著：淘宝Recall@10从0.0007提升至0.0019（+171%），美团小规模从0.0035提升至0.0112（+220%）。排序AUC在淘宝+0.0177，美团小规模+0.0205。消融实验证实，端到端判别式梯度、训练侧u2i信号、推理侧MLP u2t三者缺一不可，且协同效果超过各自独立贡献之和。

最值得记住的一句话：**排序和检索是同一优化在不同粒度上的求解，判别式排序模型早已内蕴生成式检索能力，分词器只是将其释放。**
