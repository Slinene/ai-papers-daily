---
title: Towards Generalizable and Efficient Large-Scale Generative Recommenders
title_zh: 迈向通用且高效的大规模生成式推荐系统
authors:
- Qiuling Xu
- Ko-Jen Hsiao
- Moumita Bhattacharya
affiliations:
- Netflix Research
arxiv_id: '2605.23312'
url: https://arxiv.org/abs/2605.23312
pdf_url: https://arxiv.org/pdf/2605.23312
published: '2026-05-22'
collected: '2026-05-25'
category: RecSys
direction: 生成式推荐 · 大规模生产优化
tags:
- scaling laws
- multi-token prediction
- cold-start
- sampled softmax
- semantic towers
- generative recommenders
one_liner: 在10亿参数生成式推荐模型中，用任务相关缩放法则、多token预测和语义塔解决了规模化后的效果迁移与工程效率难题。
practical_value: '- **任务相关的缩放法则作为资源分配指南**：不同推荐任务的预测难度与天花板差异极大，直接用 MRR 拟合偏移幂律可量化剩余
  headroom，指导模型容量投入——若任务已接近天花板，应转向优化目标函数或对象表示，而非盲目扩大 backbone。

  - **多 token 预测对齐缓存服务延迟**：电商推荐中常因在线排序延迟而使用缓存，导致 next-token 目标在服务时已失效。MTP 用带时间衰减的多目标加权标签训练，在
  48 小时延迟下 MRR 提升 20%+，可直接用于离线与近线推理的标签构造，且不增加线上推理成本。

  - **语义塔与协同嵌入掩码协同处理冷启动**：新物品缺乏 ID 嵌入时，通过共享的多模态语义塔（知识图谱、LLM 文本嵌入、人工标签）构建物品向量，并在训练时按比例随机掩码协同嵌入为
  OOV 嵌入，使解码器学会平衡 ID 与语义信号。电商新品上架可直接复用该范式。

  - **轻量级解码效率方案**：用 1% 均匀采样负样本的 sampled softmax 加 d/8 投影头，在不改 backbone 前提下可大幅降低训练
  FLOPs（如 10^6 输出空间下降 35 倍），支持万亿级行为 token 的频繁重训练，工程实现简单且与 SID 等方法正交。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
生成式推荐将用户行为视为序列，用一个 backbone 支撑检索、排序、用户表征等多任务，但规模化后预训练增益难以自动迁移到下游——不同任务的 headroom 差异大、频繁重训练的成本高、缓存服务导致 next-token 目标失效、冷启动物品缺少可靠 ID 嵌入。本文在 Netflix 推荐场景下，将模型 backbone 从 2M 扩展到 1B 参数，系统研究这些生产约束下的解决方案。  

**方法关键点**  
- **任务相关缩放法则**：按可预测性将任务分为三类（长期偏好/短期参与/时间驱动），用偏移幂律 \(P(N)=P_0 - (N/N_0)^{-a}\) 拟合 MRR，\(P_0\) 指示天花板，用于判断哪些任务值得继续扩规模。  
- **解码效率**：预训练时用 1% 均匀采样负样本做 sampled softmax，并将 decoder 投影到 d/8 维度，大幅降低 FLOPs，使 1B 模型可频繁重训。  
- **多 token 预测 (MTP)**：针对缓存延迟下 next-token 目标失效，用指数衰减权重（半衰期 1 小时）对一组未来高价值目标做多标签训练，线上仍用单次解码打分，对延迟敏感任务提升显著。  
- **语义塔与嵌入掩码**：为冷启动物品构建共享多模态塔（图嵌入、LLM2Vec 语言嵌入、人工标注特征），在训练时按在线冷启动率随机掩码物品的协同嵌入为 learnable OOV 向量，迫使 decoder 综合 ID 与语义信息。  

**关键实验**  
在包含万亿级行为 token 的数据集上，对比 2M 和 1B backbone 的模型：  
- 缩放法则：Task A 的 \(P_0=0.311\) 接近天花板，Task C 的 \(P_0=1.075\) 接近 MRR 上限，偏移幂律拟合误差低于 log-linear。  
- MTP：48 小时缓存延迟下，5 token MTP 相对 MRR 提升 +22.1% (Task A) / +27.8% (Task B) / +27.9% (Task C)。  
- 一周百万用户生产影子评估：1B 模型在所有任务上优于基线，Task A +22.5%，冷启动 +28.1%，验证了综合方案的有效性。  

**核心论断**  
“模型规模应作为生产迁移问题的一个组件，与任务天花板、解码成本、服务延迟对齐、物品泛化能力协同考量，而非孤立追求参数量。”
