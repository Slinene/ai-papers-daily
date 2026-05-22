---
title: LLM Retrieval for Stable and Predictable Ad Recommendations
title_zh: 稳定可预测广告推荐的LLM检索框架
authors:
- Vinodh Kumar Sunkara
- Satheeshkumar Karuppusamy
- Hangjun Xu
- Sai Deepika Regani
- Kshitij Gupta
- Gaby Nahum
- Sneha Iyer
- Jean-Baptiste Fiot
- Yinglong Guo
- Xiaowen Guo
affiliations:
- Meta Platforms, Inc.
arxiv_id: '2605.21969'
url: https://arxiv.org/abs/2605.21969
pdf_url: https://arxiv.org/pdf/2605.21969
published: '2026-05-21'
collected: '2026-05-22'
category: RecSys
direction: LLM语义表征增强广告可预测性
tags:
- LLM
- Ads
- Semantic Retrieval
- Predictability
- Graph Traversal
- Candidate Generation
one_liner: 提出基于LLM语义属性与图扩展的广告候选生成，线上可预测性指标A/A'差异降低8.62%，收入提升0.45%。
practical_value: '- 可预测性指标(A/A''差异)可作为系统稳定性新指标：在电商推荐中，可用来评估模型对商品描述微调、ID切换等输入扰动的鲁棒性，提前发现因特征工程缺陷导致的冷启动或收入波动问题。

  - 利用LLM离线提取商品/广告的层次化语义属性（品类、品牌、上下文描述等），构建语义图，通过Jaccard相似度的图遍历实现语义相似召回；该通道可与现有双塔、图召回共存，作为补充候选源，提升召回多样性和长尾覆盖。

  - 工程上采用离线LLM批量生成元数据+在线查图服务的模式，避免实时LLM推理的高延迟；对于电商推荐，可将商品描述输入LLaMA等模型，生成结构化属性，再通过近似匹配进行相似商品扩展，成本可控。

  - 实验表明LLM候选生成器能有效提升最终召回（+1.2%）和线上收入（+0.45%），且对A/A''波动抑制明显（MAD改善45%），推荐业务可将其作为稳定性优化组件，尤其适合需要高频更新商品库的场景。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
传统广告推荐系统仅关注点击/转化预估的准确率（如NDCG、Recall），缺乏对系统输出**可预测性**的量化。在广告库存随生成式AI激增的背景下，广告主对素材的微小改动（如文案微调）可能导致推荐结果剧烈波动，引发冷启动和重复性问题。该工作首次定义系统级可预测性指标，并基于LLM构建语义感知的候选生成框架，从根本上提升系统鲁棒性。

**方法关键点**  
- 提出**可预测性度量**：构造「主广告」与「影子广告」（通过复制并微调某特征模拟小扰动），计算两者转化差异的统计显著性（StatSigDiff）和每日曝光差的中位绝对偏差（MAD），作为系统稳定性评估依据。  
- **LLM语义提取**：用微调的Llama3-8B Instruct模型从广告素材（标题、描述等文本）推断层次化语义属性（品类、品牌、上下文描述）。  
- **语义图构建与遍历**：基于LLM输出的属性集合，计算广告间Jaccard相似度，构建语义图；检索时通过图遍历扩展出语义等价类中的相似广告，实现ad-to-ad候选生成。  
- **两阶段引擎**：第一阶段LLM批量离线生成广告的类别、属性与上下文标签；第二阶段利用这些标签进行快速候选检索与相关性打分，在线服务仅需查图，避免实时LLM调用。  

**关键实验**  
在Meta大规模广告推荐系统上进行在线A/B实验。基线为双塔、嵌入及图模型集成的候选生成器；测试组引入LLM候选生成通道。数据集规模达数千万条文本描述。  
- 线上top-line收入指标提升**+0.45%**，最终召回提升**+1.2%**。  
- **可预测性**：A/A' StatSigDiff相对降低**8.62%**，日曝光差MAD改善**45%**，显著减少因微小输入变化带来的交付波动。  

**值得记住的一句话**  
“用LLM提取广告的层次语义属性并构建语义图进行候选扩展，可在不牺牲线上效果的同时，大幅提升广告系统的可预测性和稳定性。”
