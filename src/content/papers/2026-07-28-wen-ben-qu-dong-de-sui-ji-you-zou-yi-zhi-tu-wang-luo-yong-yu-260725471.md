---
title: 'TRWH: A Text-Driven Random Walk Heterogeneous GNN for Semantic-Aware Sparse
  Recommendation'
title_zh: 文本驱动的随机游走异质图网络用于语义感知稀疏推荐
authors:
- He Ma
- Chen Liu
affiliations:
- The University of Sydney
- Nankai University
arxiv_id: '2607.25471'
url: https://arxiv.org/abs/2607.25471
pdf_url: https://arxiv.org/pdf/2607.25471
published: '2026-07-28'
collected: '2026-07-29'
category: RecSys
direction: LLM+异质GNN稀疏推荐 · 评分预测
tags:
- Heterogeneous GNN
- Random Walk
- LLM Profiling
- Sparse Recommendation
- Rating Prediction
- Semantic Integration
one_liner: 融合LLM用户/物品画像与异质GNN，通过随机游走增强稀疏图，发现LLM嵌入对图增强敏感
practical_value: '- **LLM画像生成流程可复用**：使用精心设计的系统提示和推理引导，让LLM（如Llama-3.2-3B）为每个用户和物品生成结构化文本描述，再通过指令微调的embedder（如instructor-xl）转为稠密向量，可增强召回或排序模型的语义特征，尤其适合电商中评论、标题等文本丰富的场景。

  - **异质图多边类型建模**：构建包含评分、评论、购买、同店铺、相似关系等九种边类型的异质图，可迁移至电商推荐中，用于捕获用户行为的多面性，提升冷启动或稀疏交互下的表示学习。

  - **谨慎使用图增强与LLM嵌入**：实验表明对Word2Vec等传统嵌入，随机游走新增二阶边能提升性能；但对LLM生成的语义向量，图聚合会稀释精细的个性化信号，导致RMSE/MAE变差。业务中若引入LLM特征，需评估图传播是否损害语义独特性，或采用自适应游走策略。

  - **按业务目标选择损失函数**：MSE训练更关注减少大误差（RMSE更低），适合需要控制极端错误率的场景（如高价值商品评分预测）；但MAE可能不如直接使用ChatGPT的基线。可根据业务侧重的指标调整损失，或采用联合优化。'
score: 10
source: arxiv-cs.MM
depth: full_pdf
---

**动机**  
推荐系统面临交互图稀疏与语义理解不足的双重挑战。GNN能建模结构关系，LLM擅长提取语义，但二者融合困难，尤其在稀疏场景下，图聚合可能破坏LLM捕捉的细致偏好。本文提出TRWH，旨在通过随机游走增强异质图，将LLM生成的高质量文本画像融入GNN，解决稀疏推荐中的精度与语义融合问题。

**方法关键点**  
- **Embedding Creation**：两种方式——传统Word2Vec基于标题和评论文本训练；LLM方式则用Llama-3.2-3B-Instruct为用户和物品生成结构化profile，提示中加入推理步骤减少幻觉，再用instructor-xl embedder编码为向量。  
- **异质图构建**：包含9种边（评分、评论、购买、同店铺、以及通过随机游走生成user-related-to-user和item-related-to-item等），显式建模多关系交互。  
- **随机游走增强**：基于user-rates-item边执行一步随机游走，添加二阶用户相似边和物品相似边，丰富稀疏图。实验发现对Word2Vec嵌入有正向作用，但会稀释LLM嵌入的细粒度语义。  
- **HeteroGNN训练**：单层图卷积，MSE损失，端到端预测评分。

**关键实验与结果**  
在Amazon 2023 Fashion（2M用户，825K物品）和Beauty（631K用户，112K物品）数据集上，对比P5、MF、ChatGPT等基线，TRWH的LLMHet变体在Fashion上RMSE 1.0604（相比最优基线降低80%），MAE 0.9107；Beauty上RMSE 0.8944，MAE 0.8421。消融表明：LLM嵌入+随机游走（LLMRHet）性能反而下降，说明语义敏感的LLM特征不适合过度图聚合。  

**核心启示**  
图增强并非总能提升效果，对LLM生成的语义表达，须设计自适应或语义保护的传播策略，避免邻域平均化损失个性化语义。
