---
title: 'Beyond Retrieval: Learning Compact User Representations for Scalable LLM Personalization'
title_zh: TAP-PER：用紧凑前缀替代冗长提示，实现可扩展的大模型个性化
authors:
- Heng Cao
- Fan Zhang
- Jian Yao
- Yujie Zheng
- Changlin Zhao
- Lu Hao
- Yuxuan Wei
- Wangze Ni
- Huaiyu Fu
- Yuqian Sun
affiliations:
- Microsoft
- Shanghai International Studies University
- Zhejiang University
- The Hong Kong Polytechnic University
arxiv_id: '2606.04547'
url: https://arxiv.org/abs/2606.04547
pdf_url: https://arxiv.org/pdf/2606.04547
published: '2026-06-03'
collected: '2026-06-04'
category: LLM
direction: LLM 个性化 · 用户嵌入 · 前缀微调
tags:
- LLM Personalization
- Prefix Tuning
- User Embedding
- LoRA
- Temporal Attention
one_liner: 用可学习的紧凑用户前缀替换显式提示和每用户适配器，实现可扩展、时序感知的 LLM 个性化。
practical_value: '- **用户状态前缀可作为长期兴趣嵌入**：在电商推荐或对话系统中，可以为每个用户维护一个轻量级嵌入（仅32K参数），离线训练后在线快速适应，大幅降低存储与部署成本。

  - **查询感知的时序记录前缀替代显式检索**：借鉴DIN式注意力和可学习的时间衰减，直接对用户全量交互历史进行加权，省去BM25等检索器，避免检索质量对个性化效果的波动，适合行为序列丰富的场景。

  - **共享桥接LoRA降低参数冗余**：冻结任务适配后的骨干LLM，仅训练一个共享的LoRA模块来深度融合前缀信号，避免为每个用户单独维护一个大尺寸适配器，千级用户时总参数量仅为传统方法的约一半。

  - **支持在线增量更新不停服**：新反馈到来时，只需对用户前缀做几次梯度更新即可吸收偏好变化，共享模块不动，便于在电商流式场景中实现持续个性化，无需全量重训。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：现有LLM个性化方法主要有两类：一是通过检索增强（RAG）或用户画像（PAG）将用户历史注入提示，灵活但高度依赖检索质量和提示设计；二是为每个用户训练专属参数高效模块（如OPPU、PER-PCS），虽然效果更好，但存储与维护成本随用户规模线性增长，且大多忽略用户兴趣的时间演变。该工作试图回答：能否在不使用显式提示和不维护大量每用户参数的情况下，实现可扩展、时序感知的LLM个性化？

**方法关键点**：
- 提出**TAP-PER**（Temporal Attentive Prefix for PERsonalization），采用两阶段训练：第一阶段在聚合用户数据上做LoRA微调，获得任务适配的骨干模型；第二阶段冻结骨干，引入个性化前缀。
- **用户状态前缀**：为每个用户学习一个可训练的嵌入（大小 L×d，L=8，d=4096），表征其长期稳定的偏好，存储开销仅32K/用户。
- **查询感知的记录前缀**：利用DIN式注意力机制，计算当前查询与用户历史每条记录的交互权重，并加入**可学习的时间间隔衰减和顺序间隔衰减**，突出近期且相关的记录，输出一个动态前缀。该过程无需外部检索器，直接对全量历史进行软加权。
- 两个前缀逐元素求和后挂载到模型输入，同时训练一个**共享的桥接LoRA**，作用于所有transformer层的投影矩阵，使前缀信号深度融合进骨干网络，而桥接LoRA的参数被所有用户共享，保持低参数膨胀。

**实验与结果**：
- 在LaMP个性化基准的6个任务（分类、评分、生成）上，TAP-PER全面超越RAG、PAG、OPPU、PER-PCS等基线。例如LaMP-2M（电影标签分类）准确率提升7.2个点，LaMP-5（学术标题生成）ROUGE-1提升2.8个点。
- 参数效率显著：每用户仅32K参数，相比OPPU的4.2M减少130倍；1000用户下总参数仅为PER-PCS的约53%。
- 消融实验验证了用户状态前缀、记录前缀、桥接LoRA均不可或缺；时间衰减移除后性能明显下降，案例显示时间注意力帮助模型抓取近期相关记录。
- 在流式反馈模拟中，仅更新用户前缀（Online‑Emb）即可稳定提升性能，接近全量重训，证明框架适合在线持续学习。

**一句话**：紧凑的用户表征可以替代繁琐的提示工程和笨重的每用户适配器，成为可扩展、时序感知的LLM个性化新范式。
