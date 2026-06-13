---
title: MiniMax Sparse Attention
title_zh: MiniMax稀疏注意力（MSA）
authors:
- Xunhao Lai
- Weiqi Xu
- Yufeng Yang
- Qiaorui Chen
- Yang Xu
- Lunbin Zeng
- Xiaolong Li
- Haohai Sun
- Haichao Zhu
- Vito Zhang
affiliations:
- MiniMax
- Peking University
- NVIDIA
- Zhejiang University
- Huazhong University of Science and Technology
arxiv_id: '2606.13392'
url: https://arxiv.org/abs/2606.13392
pdf_url: https://arxiv.org/pdf/2606.13392
published: '2026-06-10'
collected: '2026-06-13'
category: LLM
direction: 超长上下文LLM推理 · 分块稀疏注意力
tags:
- Sparse Attention
- Long Context
- Grouped Query Attention
- Kernel Optimization
- Top-k Selection
one_liner: 提出MiniMax稀疏注意力，通过分组索引分支动态选择关键块，将1M上下文计算量降低28.4倍并实现14.2倍预填充加速
practical_value: '- **长上下文LLM服务降本**：对于需要处理超长对话历史或文档的多轮Agent、客服系统，MSA的分组稀疏选择机制可直接集成到GQA模型中，用轻量索引分支动态裁剪KV块，大幅降低每token注意力成本，适合高并发在线服务。

  - **分组独立Top-k选择**：每个GQA group独立选择重要块，比统一选择更灵活，在推荐系统中的用户行为序列建模（如长序列Transformer）可借鉴，按不同head关注点实现差异化稀疏检索。

  - **推理kernel协同设计**：论文的exp-free Top-k和KV-outer稀疏注意力kernel利用块级访存模式提升张量核心利用率，可直接用于自研推理引擎，尤其在批量解码时实现高吞吐。

  - **训练稳定性的KL蒸馏**：索引分支通过KL loss对齐主分支注意力分布且梯度解耦，这种学习稀疏选择的方法可迁移到其他需端到端学习稀疏检索的场景（如召回中的粗筛网络）。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：大模型在Agent工作流、代码库级推理等场景需要处理百万Token的超长上下文，但传统softmax注意力的二次计算量使部署成本过高，亟需实用稀疏方案。  
**方法**：提出MiniMax Sparse Attention（MSA），基于分组查询注意力（GQA）构建分块稀疏机制。轻量索引分支为每个GQA组独立评分KV块并选出Top-k，主分支仅对选中块执行精确块稀疏注意力；索引分支梯度脱离主分支，通过KL散度损失对齐两者的块级注意力分布。同时协同设计了GPU推理kernel：利用免指数Top-k选择减少计算，以及KV-outer稀疏注意力提升块粒度访存下张量核心的利用率。  
**结果**：在原生多模态训练的109B参数模型上，1M上下文时每Token注意力计算量减少28.4倍，性能与GQA持平；配合定制kernel，在H800上预填充阶段提速14.2倍，解码阶段提速7.6倍，模型已开源。
