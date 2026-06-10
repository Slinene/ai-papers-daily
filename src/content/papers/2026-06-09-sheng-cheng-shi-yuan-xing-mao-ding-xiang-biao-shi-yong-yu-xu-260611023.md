---
title: Generative Archetype-Grounded Item Representations for Sequential Recommendation
title_zh: 生成式原型锚定项表示用于序列推荐
authors:
- Yifan Li
- Jiahong Liu
- Xinni Zhang
- Hao Chen
- Yankai Chen
- Wenhao Yu
- Jianting Chen
- Irwin King
affiliations:
- The Chinese University of Hong Kong
- McGill University
- Tongji University
arxiv_id: '2606.11023'
url: https://arxiv.org/abs/2606.11023
pdf_url: https://arxiv.org/pdf/2606.11023
published: '2026-06-09'
collected: '2026-06-10'
category: RecSys
direction: LLM 增强物品表示 · 生成式用户原型
tags:
- LLM
- item representation
- sequential recommendation
- archetype
- behavioral calibration
- embedding
one_liner: 用大模型生成物品理想受众描述（原型），并通过行为校准将其与真实交互模式对齐，提升序列推荐效果
practical_value: '- **物品原型生成可迁移至电商冷启动**：利用 LLM 基于商品标题、品牌、描述等元数据生成“理想目标用户画像”，作为额外的语义特征补充
  ID 嵌入，显著改善长尾或新品缺少行为信号时的表示质量。

  - **行为校准损失可直接复用**：提出的基于物品共现统计的自适应排斥力调节方法（association‑weighted repulsion），本质是对均匀性损失的行为先验注入，可以轻量地加到已有
  CTR／召回模型的表示学习模块，迫使嵌入布局贴合真实交互结构，而无需额外架构。

  - **模型无关且推理零开销**：GenAIR 的嵌入生成过程离线完成，与 GRU4Rec、SASRec、Bert4Rec 等常用序列模型无缝衔接，推理时仅需缓存向量，适合对延迟敏感的生产环境。

  - **可扩展至生成式 Query 推荐**：原型生成逻辑可自然映射到搜索/推荐场景：为用户搜索意图生成原型描述、为推送消息生成受众画像，进而提升 QueryRec
  或内容理解中的语义匹配质量。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
现有序列推荐严重依赖 ID 嵌入，数据稀疏时长尾物品表示质量差，且基于大模型的语义增强方法仅静态编码物品属性，忽略了“物品身份也由其目标受众定义”这一关键视角。语义空间与真实行为模式之间存在鸿沟，导致表示难以捕捉用户偏好。  
**方法关键点**  
- **原型生成**：针对每个物品，将名称、品牌、类别等元数据填入提示模板，调用 LLM（如 Llama 2‑7B‑Chat）生成一段描述该物品理想目标用户的文本（Archetype）。利用 LLM 生成过程中的预填充隐藏状态（物品属性）和解码隐藏状态（用户原型），经平均池化、PCA 降维保留 95% 方差后拼接，再通过可训练 MLP 投影到推荐模型空间。  
- **行为校准**：引入基于物品共现频次的关联分数 $S(i,j)$，构造衰减函数 $w(i,j)=e^{-\gamma S(i,j)}$，将其乘入均匀性损失的高斯核中，形成校准损失 $\mathcal{L}_{\rm cal}$。该损失通过加权排斥力使得行为上相关物品的夹角更小，无关物品保持分离，从而将语义空间向实际交互结构对齐。联合训练时与排序损失 $\mathcal{L}_{\rm rank}$ 相加，由 $\alpha$ 控制权重。  
- **训练与推理**：嵌入生成一次完成，训练时仅微调投影 MLP 和主干模型；推理时直接使用缓存嵌入，无额外 LLM 调用。  
**关键实验**  
在 Yelp、Amazon Beauty、Fashion 三个数据集上，基于 GRU4Rec、Bert4Rec、SASRec 评估。GenAIR 一致超越 CITIES、MELT 等传统方法及 LLMInit、LLM‑ESR、LLMEmb、Alphafuse 等语言增强基线。例如 Fashion 数据集上 SASRec 的 HR@10 达到 0.6133（+4.44%），NDCG@10 0.5207（+4.71%）。消融表明预填充嵌入、解码嵌入与校准损失均对性能有正向贡献。效率上训练参数仅 5.95M，推理 FLOPs 与基础模型持平（0.22G）。  
**值得记住的一句话**  
*“物品的表示不应只是自身属性的编码，更应是对其理想受众的画像与真实被接受群体的行为投射。”*
