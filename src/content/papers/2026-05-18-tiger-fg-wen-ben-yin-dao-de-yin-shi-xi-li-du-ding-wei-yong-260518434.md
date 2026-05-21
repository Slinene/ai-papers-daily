---
title: 'TIGER-FG: Text-Guided Implicit Fine-Grained Grounding for E-commerce Retrieval'
title_zh: 'TIGER-FG: 文本引导的隐式细粒度定位用于电商图像到多模态检索'
authors:
- Xinyu Sun
- Huangyu Dai
- Lingtao Mao
- Zexin Zheng
- Zihan Liang
- Ben Chen
- Chenyi Lei
- Wenwu Ou
affiliations:
- Kuaishou Technology
arxiv_id: '2605.18434'
url: https://arxiv.org/abs/2605.18434
pdf_url: https://arxiv.org/pdf/2605.18434
published: '2026-05-18'
collected: '2026-05-21'
category: RecSys
direction: 电商图像检索 · 文本引导隐式细粒度对齐
tags:
- IMMR
- Text-guided Grounding
- Distillation
- E-commerce Retrieval
- Mosaic Augmentation
- Fine-grained Representation
one_liner: 提出文本引导的隐式定位框架，无需物体检测即可从全图中提取目标聚焦的多模态嵌入，显著提升混叠场景下的检索精度。
practical_value: '- **文本作为定位引导**：利用商品标题、类别等结构化文本作为语义先验，通过交叉注意力模块自动关注图像中的目标区域，省去显式检测模块，降低工程部署成本与误差传播风险。

  - **双蒸馏目标稳定表征**：空间关系蒸馏（LSRD）保持patch级空间一致性，相似度分布蒸馏（LSDD）继承教师模型的全局视觉相似结构，两者联合可提升嵌入的判别力与训练稳定性，均可迁移至其他需要细粒度对齐的召回模型。

  - **Mosaic 增强与批次内竞争**：将目标商品与跨类干扰物粘贴到随机背景上构成 Mosaic 样本，并将同一 Mosaic 中的多个商品放入同一 batch，迫使模型依赖文本来区分视觉相似但语义不同的候选项，适用于存在背景杂乱或多物共现的搜索场景。

  - **高效轻量的工程适配**：仅 85.7M 用户侧参数、256 维嵌入，可直接接入现有向量检索库；训练时仅需物品检测框作为辅助监督，索引与检索时完全无需任何框信息，适合大规模电商检索系统。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
电商图像搜索通常将用户截取的目标区域作为查询，从商品整图与结构化文本构成的候选项库中检索对应商品。该场景存在两个不对称：① 模态差异——纯视觉查询需匹配图文多模态候选项；② 粒度差异——局部裁剪区域需对应包含背景、多物体干扰的整图。现有检测类方法依赖显式定位，成本高、易传播误差；CLIP 等双塔模型用全局表征，对背景与干扰敏感。因此需要一种无需检测、直接从整图中产生目标聚焦嵌入的方法。

**方法关键点**  
- **文本引导的隐式定位**：用可学习的查询 token 先与文本 token 交叉注意，再与视觉 token 交叉注意，生成文本条件的视觉槽位，经 MLP 加权得到语义聚焦特征 `f_m`；同时引入互补视觉分支，融合 `f_m` 与视觉 cls token 引导 patch 池化，得到外观特征 `f_a`，最终残差合并为项目嵌入 `f_i`。  
- **项目侧正则化**：施加区域-文本对齐 (`Lv2t`)、目标锚定融合-区域对齐 (`Li2v`，并引入跨类目文本硬负样本防止误匹配)、空间关系蒸馏 (`LSRD`，用冻结的 DINOv3 教师保持目标 patch 间的空间结构)。  
- **双塔训练与蒸馏**：查询-项目对比学习 (`Lq2i`) 中加入图像-文本不匹配硬负样本；相似度分布蒸馏 (`LSDD`) 对齐师生模型在 batch 内的查询-候选项相似度分布，稳定检索判别。  
- **数据集与增强**：构建 10M 训练对和 Normal / Mosaic 评估集；Mosaic 评估将目标与跨类干扰物随机粘贴到背景上，训练时混合原始与 Mosaic 样本，并将同 Mosaic 内的多个商品放入同一 batch 形成强竞争。

**关键结果**  
在自建基准 ECom-RF-IMMR 上，TIGER-FG 在 Normal 集 Recall@1 达 80.1，比最强基线 Qwen3-VL-Emb 高 6.1 个百分点；在 Mosaic 杂乱场景下 Recall@1 达 75.2，比最强基线高 34.4 个百分点，且去除 Mosaic 训练后该指标跌至 47.8，验证了杂乱感知训练的必要性。公共基准 LookBench 上，HitRate@1 提升 6.7 个百分点。模型仅用 85.7M 查询侧参数和 256 维嵌入，兼顾了高效与高性能。
