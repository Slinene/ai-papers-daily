---
title: 'Trading Engagement for Sustainability: Carbon-Aware Re-ranking for E-commerce
  Recommendations'
title_zh: 碳感知重排序：电商推荐中参与度与可持续性的权衡
authors:
- Noah Lund Syrdal
- Anders Vestrum
- Jorgen Bergh
affiliations:
- University of California, Berkeley
arxiv_id: '2606.04550'
url: https://arxiv.org/abs/2606.04550
pdf_url: https://arxiv.org/pdf/2606.04550
published: '2026-06-03'
collected: '2026-06-04'
category: RecSys
direction: 电商推荐 · 碳感知重排序 · 多目标优化
tags:
- carbon-aware recommendation
- re-ranking
- product carbon footprint
- LLM for PCF estimation
- Pareto trade-off
one_liner: 在缺碳标签场景下，用检索增强LLM估计PCF并以线性λ重排序，发现大幅减排仅需微小参与度损失
practical_value: '- 借鉴检索增强+少样本LLM估计商品碳足迹的思路，仅需目录文本元数据即可为缺标签商品补全PCF，降低对LCA数据的依赖

  - 后置重排序的线性标量公式\(s_{ui}=(1-\lambda)\tilde{y}_{ui}-\lambda\tilde{PCF}_i\)实现透明、可插拔的碳感知控制，无需重训模型，适合快速上线与迭代

  - 将\(\lambda\)作为可审计的政策参数，允许业务侧按品类或季节动态调节参与度与碳之间的取舍，符合算法透明性要求

  - 品类间碳减排可及性的显著差异提示我们：在电商应用中应按品类（或细分类目）评估替代品丰富度，差异化设计碳感知策略，避免一刀切'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
电商推荐系统直接塑造消费可见性，但产品碳足迹(PCF)在目录规模上几乎不可用。法规压力与可持续消费趋势要求将碳信号纳入推荐，而真实场景下标签缺失使这一目标极具挑战。论文试图在大规模Amazon目录中，仅凭元数据推断PCF，并通过后置重排序探索参与度与碳足迹之间的可量化权衡。

**方法关键点**  
- **PCF估计**：构建检索增强 pipeline，以Carbon Catalogue（866个LCA标注产品）为监督源，比较最近邻平均、零样本LLM、少样本检索增强LLM三种策略。最终选用基于all-MiniLM-L6-v2语义检索5近邻+Qwen2.5-3B-Instruct chain-of-thought提示的少样本方法，在消费者级留出集上RMSE最低(1708.6)、MAE最低(695.1)。  
- **推荐流水线**：使用RecBole训练BPR、NeuMF、LightGCN三个基线模型，产生候选物品的相关性分数；重排序阶段对分数进行用户级min-max归一化，对PCF进行全局min-max归一化，通过线性标量\(s_{ui}=(1-\lambda)\tilde{y}_{ui}-\lambda\tilde{PCF}_i\) 组合，\(\lambda\in[0,1]\) 作为显式权衡参数。  
- **评估**：在Amazon Reviews的Home & Kitchen、Sports & Outdoors、Electronics三个品类上，以评论作为隐式反馈，用NDCG@10衡量参与度、AvgPCF@10衡量碳影响，通过\(\lambda\) 网格扫描绘制帕累托前沿。

**关键结果**  
- 在允许NDCG@10下降≤5%的条件下，BPR与LightGCN在多数品类可实现70–86%的碳减排，而NeuMF在Electronics仅获7.6%减排，模型与品类间差异显著。  
- Home & Kitchen品类最灵活，三模型均超80%减排；Electronics最受限。  
- PCF估计阶段，少样本LLM的Spearman秩相关系数达0.518，优于零样本LLM但略低于最近邻平均(0.728)，其绝对误差优势使其成为下游主信号。  

**最值得记住的一句话**  
碳感知重排序能以极小参与度代价实现大幅碳减排，但可行域高度依赖基模型与品类结构，透明参数\(\lambda\) 为此提供了一种可审计的业务杠杆。
