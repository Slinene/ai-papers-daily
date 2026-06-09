---
title: 'OneFeed: A Unified Generative Framework for Feed ContentEnhancement and Query
  Generation'
title_zh: OneFeed：统一生成式框架同时建模商品推荐与搜索Query生成
authors:
- Guo Xun
arxiv_id: '2606.07972'
url: https://arxiv.org/abs/2606.07972
pdf_url: https://arxiv.org/pdf/2606.07972
published: '2026-06-06'
collected: '2026-06-09'
category: GenRec
direction: 生成式推荐 · Semantic ID 联合 Query 生成
tags:
- Generative Recommendation
- Semantic ID
- Query Generation
- Contrastive Alignment
- Closed-Loop Self-Enhancement
- Unified Architecture
one_liner: 用一个共享编码器同时生成推荐用的语义ID和搜索用的自然语言Query，并通过对比对齐弥补语义鸿沟
practical_value: '- **统一 Feed 与搜索的生成范式**：共享行为编码器同时产生 Semantic ID 和自然语言 Query，可以借鉴到电商的「千人千面」Feed
  流中，让一个模型既做推荐又做搜索类目/query 推送，减少维护两套系统的成本。

  - **SID-Query 对齐的设计**：用对比学习让离散的语义 ID 和自然语言 Query 共享嵌入空间，这样生成的 Query 可以直接检索到与语义 ID
  对应的商品候选，推荐和搜索的候选池可以无缝融合。在业务里可尝试将商品聚类码与用户搜索词进行对齐，提升跨链路触达。

  - **闭环自增强范式**：利用生成内容获得的隐式反馈（点击/跳过/转化）同时监督两个生成头，无需人工标注。可以复用到 Agent/多智体场景中，Agent 生成的推荐物料或查询被用户反馈后，作为训练信号自举提升。

  - **弱监督 Query 构造**：在只有商品文本元数据的场景下，用标题、类目、高频词拼接伪 Query，为没有搜索日志的业务线提供了一种低成本冷启动搜索式推荐的思路。注意严格防泄露：训练时只用历史时间窗口前的元数据，测试集不参与聚类和共现校准。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
现代信息获取中，Feed 推荐（基于隐式反馈）和搜索（基于显式 Query）虽紧密耦合但被独立建模，导致用户意图理解割裂，冷启动与长尾场景下尤其严重。生成式推荐（如 Semantic ID）为统一建模提供了可能，但现有方法未显式利用推荐与搜索的互补性。论文提出 OneFeed，用一个生成式框架同时完成未来内容语义 ID 的生成和意图 Query 的生成，使推荐流可获得搜索式候选补充，搜索意图可从浏览行为中提升。

**方法关键点**  
- **共享行为编码器**：将用户异构行为（点击、搜索、时长等）映射为统一嵌入，供两个生成头共用。  
- **分层 Semantic ID 构造**：基于文本聚类和行为共现校准生成层级 ID token。  
- **Feed SID 生成器**：自回归生成下一物品的语义 ID，用于推荐候选检索。  
- **Intent Query 生成器**：条件于同一行为表示生成自然语言 Query，发往搜索引擎获取候选。  
- **SID-Query 对齐**：对比学习拉近匹配的语义 ID 和 Query 表示，跨任务知识迁移。  
- **候选增强一致性损失**：要求生成的 Query 检索到的候选能获得正向用户反馈。  
- **闭环自增强**：线上反馈信号同时优化两路生成，离线通过重放模拟迭代自训练。  
- **弱监督 Query 构造**：在无真实搜索日志的公开数据集上，用商品标题、类目、高频词构造伪标签，并严格防泄露（时间分割、元数据不回视、测试集零参与）。

**实验设计**  
在 KuaiRec、Amazon Reviews、MovieLens-1M 上定义了完整协议：时间切分、弱监督 Query 构造、层级 SID 构建。对比基线包括 GRU4Rec、SASRec、BERT4Rec、P5、OneRec 等推荐模型，以及关键词抽取、T5、BART、GPT2 等 Query 生成模型。评测指标涵盖推荐 Recall/NDCG、Query BLEU/ROUGE-L/BERTScore/Distinct-n 和检索可达率、候选覆盖度、长尾召回、搜索补充率等。论文目前给出基于已知基线的预期性能（标记 †），例如 OneFeed 在 Amazon Reviews 上预期 Recall@10 超过 0.119，Query 可达率超过 0.719，融合候选重放 NDCG 超过 0.088，消融实验显示去掉对齐或一致性损失后指标下降。同时提供了合成数据集上的最小原型验证管道可执行性。

**核心记忆点**  
“OneFeed 证明：让一个模型同时生成推荐品的语义 ID 和搜索 Query，并用对比学习对齐两者，就能让 Feed 和搜索的候选池互相补充，形成闭环自进化。”
