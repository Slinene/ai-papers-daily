---
title: 'From Item-Only to Query-Item: Query-Conditioned Generative Search with QGS
  in Quark'
title_zh: 从物品到查询-物品：Quark搜索中的查询条件生成式搜索QGS
authors:
- Yanglong Song
- Zihao Yang
- Shuo Meng
- Rujun Guo
- Jin Zhang
- Bin Wang
- Shaoyu Liu
- Xiaozhao Wang
- Guanjun Jiang
affiliations:
- Alibaba Group
- University of Science and Technology of China
arxiv_id: '2605.25514'
url: https://arxiv.org/abs/2605.25514
pdf_url: https://arxiv.org/pdf/2605.25514
published: '2026-05-25'
collected: '2026-05-26'
category: GenRec
direction: 查询条件生成式搜索 · 线性注意力
tags:
- Generative Search
- Query-Conditioned
- Linear HSTU
- HFG-Attention
- InfoNCE
- Search Ranking
one_liner: 以查询条件下一物品预测取代物品自回归，消除搜索序列中查询跳变造成的噪声监督，并引入线性HSTU和异构特征分组注意力实现工业落地。
practical_value: '- **查询条件预测目标**：在搜索、对话或Agent行为序列中，当存在明显的上下文切换（如新查询、新任务），可将下一查询/意图作为条件引入下一个动作预测，将噪声边际分布转为干净条件分布，有效降低训练损失波动。

  - **线性HSTU编码器**：将HSTU的U-gating与RWKV式因果线性递归结合，复杂度从O(L²)降至O(L)，在长度1000时保持排序质量并加速37%，适合电商推荐/搜索的长序列在线建模。

  - **HFG-Attention异构特征融合**：将稀疏跨特征按语义分组，投影到统一维度后用HSTU注意力交互，保留FFN增强非线性，可用于推荐系统中稠密序列表示与稀疏交叉特征的融合，避免直接拼接信息损失。

  - **InfoNCE对比训练技巧**：在batch内负采样时使用padding mask和collision mask（剔除重复目标），提升训练稳定性，可复用至生成式推荐模型的序列预测训练中。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
搜索行为由查询驱动，每次查询切换导致用户交互历史中的物品出现主题剧变。现有生成式搜索方法将查询和物品展平为单一句子序列，不区分查询边界，模型被迫从历史物品直接预测下一物品，监督信号充满噪声（图3）。本文指出，**每个物品都有对应的查询作为因果解释**，因此必须显式建模查询与物品的条件依赖，将预测目标从 P(item | history) 变为 P(item | history, next_query)，以消除序列级语义不连续。

### 方法关键点
- **查询-物品对令牌构建**：每个交互表示为 (query, item) 对，融合BERT文本语义和151维数值/类别交叉特征，确保每个序列位置携带完整的查询-物品交互信息。
- **查询条件下一物品预测**：训练时，每一步输入历史编码输出和下一步的查询语义嵌入，预测下一步的物品，使用InfoNCE对比损失，负样本来自同一batch，并采用 padding/collision mask 避免无效负样本。
- **Linear HSTU Encoder**：将HSTU的点积聚合注意力改造为线性递归：Q,K,V,U 均由SiLU投影得到，通过 K⊙V 累积并做因果逐元素求和，输出由 Q 和 U 双重门控调制，保留HSTU的 softmax-free 和 U-gating，复杂度降为 O(L)。在长度1000时推理加速37%，排序质量持平。
- **HFG-Attention**：由于候选物品不能作为序列输入，其交叉特征需另行引入。将异构稀疏特征按语义分组（如查询-文档匹配、位置统计等），每组投影到统一维度，再经过保留FFN的HSTU注意力融合，与序列表示拼接后进入多任务塔，弥合了稀疏特征与稠密序列表示之间的语义鸿沟。

### 关键结果
在夸克搜索的生产数据上（488M曝光记录）离线评估：QGS 的GAUC达到0.7573，较生产基线提升+6.06%，较HSTU和HLLM等生成式基线提升显著（+1.61~1.37 GAUC）。消融指出查询条件预测损失功能最大（移除后GAUC下降1.91点），HFG-Attention次之（下降1.63点）。在线A/B测试：CTR +0.62%，点击搜索比 +0.38%，页面浏览时长 +3.55%，所有提升统计显著。

> **一句话**：搜索序列中的每一次物品点击都对应一个解释性查询，生成式搜索模型必须用“查询条件下一物品”取代“物品自回归”，才能把噪声监督转成干净信号。
