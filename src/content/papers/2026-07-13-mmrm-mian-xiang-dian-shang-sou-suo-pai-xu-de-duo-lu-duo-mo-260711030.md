---
title: 'MMRM: A Multiplex Multimodal Representation Model for Product Ranking in E-commerce
  Search'
title_zh: MMRM：面向电商搜索排序的多路多模态商品表示模型
authors:
- Zhen-Lin Chen
- Maosen Sheng
- Peng Lin
- Jianmin Chen
- Zhuojian Xiao
- Dongyue Wang
- Xiwei Zhao
affiliations:
- JD.COM
arxiv_id: '2607.11030'
url: https://arxiv.org/abs/2607.11030
pdf_url: https://arxiv.org/pdf/2607.11030
published: '2026-07-13'
collected: '2026-07-15'
category: RecSys
direction: 多路多模态表示 · 多任务对比学习
tags:
- Multimodal Representation
- Contrastive Learning
- Multitask Learning
- E-commerce Search
- LLM Fine-tuning
- User Behavior Modeling
one_liner: 用共享MLLM加任务特定token，一次推理生成四种解耦商品向量，并设计多路用户表示提升多目标排序
practical_value: '- 多任务协同信号联合训练：将搜索点击、行为序列中的点击/加购/下单四种信号分别构建三元组数据集，用对比学习对齐多模态LLM，生成更全面的商品表示。可迁移到电商多行为序列建模，捕捉不同意图（流行、搭配、复购）的品间关系。

  - 一次推理产出多套解耦向量：在输入中插入[SEARCH]/[CLICK]/[CART]/[ORDER]等任务特定token，经过共享主干后由独立MLP投影，单次前向获得四个解耦嵌入，避免为每个任务单独微调或推理，适合工程落地。

  - 排序侧的多路用户表示：利用多套商品向量分别进行Soft Search提取任务相关行为序列，再通过Multi-Head Target Attention生成任务特定用户表示，最后经MMoE融合。这种设计能让CTR/加购/转化塔各取所需，缓解多任务场景的表示纠缠问题。

  - 数据构建技巧：基于行为图采样时，用Word2Vec风格的子采样概率和难负例采样（同子类目负例）提升对比学习质量；使用GradCache突破显存瓶颈，在4B参数MLLM上用4096
  batch size训练，可直接参考其工程参数。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
电商搜索排序需要捕捉用户在不同目标（CTR、加购、转化）下的细粒度偏好。现有方法通常只利用单一协同信号（如点击）微调多模态大模型（MLLM），忽略了电商场景中搜索点击、同品类点击、加购、下单等行为的语义差异，导致学习到的商品表示难以适配多任务排序；同时，排序模型常把多模态表示当作扁平特征使用，未充分挖掘其对用户行为建模的潜在价值。

**方法**
- **数据集构建**：从京东日志中构造四种三元组数据集——`q2i_click`（搜索-物品点击）、`i2i_click/cart/order`（基于10分钟/30分钟/7天行为图），并用子采样和难负例采样增强对比学习。
- **多路多模态表示模型（MMRM）**：以Qwen3-VL-4B为骨干，在输入序列末尾添加[SEARCH]、[CLICK]、[CART]、[ORDER]四类特殊token，每个token的最后一层隐藏状态通过独立MLP投影得到任务的商品表示。训练时四个任务混合均匀，仅对当前任务的正例计算对比损失，其他任务的item作为in-batch负例，总损失通过可调权重加和。使用GradCache将batch size提到4096，以提升对比学习效果。
- **多路用户表示排序模型**：对每个任务用对应的商品嵌入表做Soft Search提取top-K相关行为序列，经Multi-Head Target Attention生成任务特定用户表示；所有用户表示与其他特征一起输入MMoE，再与任务特定用户表示拼接后送入各自的Tower预测CTR/ACR/CVR。

**关键结果**
在京东商品检索/排序测试集上，MMRM的F1@5/NDCG@5全面优于单任务模型和普通多任务（共享[EMB] token）模型，消融实验证实大批量能稳定提升效果。排序模型离线GAUC：相比线上基线（单端到端嵌入的SIM），MMRM多路版本CTR +2.5%，ACR +1.3%，CVR +1.4%。线上A/B测试：UCTR +0.42%，UACR +0.37%，UCVR +0.35%，已在京东全量上线。
