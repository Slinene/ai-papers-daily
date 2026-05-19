---
title: Dual-Diffusional Generative Fashion Recommendation
title_zh: 双扩散生成式时尚推荐架构
authors:
- Mingzhe Yu
- Lei Wu
- Qianru Sun
- Yunshan Ma
affiliations:
- Singapore Management University
- Shandong University
arxiv_id: '2605.17357'
url: https://arxiv.org/abs/2605.17357
pdf_url: https://arxiv.org/pdf/2605.17357
published: '2026-05-17'
collected: '2026-05-19'
category: GenRec
direction: 生成式推荐 · 双扩散多模态架构
tags:
- Dual-Diffusion
- Generative Recommendation
- Fashion
- Multimodal
- Text-Image Generation
- Personalization
- Interpretability
one_liner: 提出双扩散Transformer，联合图像与文本生成，实现个性化且可解释的时尚推荐。
practical_value: '- **用户偏好建模**：利用属性级结构化caption + 偏好加权采样，从交互历史提取高维语义意图，避免视觉冗余，可直接用于电商多模态推荐中的用户画像构建。

  - **双模态联合生成与互增强**：图像与文本分支跨注意力、联合损失训练，生成结果自带解释文本，可用于电商导购场景生成推荐理由，提升可解释性。

  - **高效文本增强微调**：仅用LLM生成的多样化匹配文本微调文本分支，比图像级DPO微调快7倍，且提升多样性与兼容性，可借鉴用于推荐模型的高效领域适配。

  - **多条件可控推理**：通过Classifier-Free Guidance独立控制任务定义、匹配条件、用户偏好，可灵活调节推荐生成的质量、个性化与多样性权衡。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
现有生成式时尚推荐主要依赖图像模态，存在两个根本缺陷：(1) 用户行为建模不足——历史交互图像包含大量偏好无关视觉细节，难以提取精准偏好；(2) 缺乏可解释性——仅输出图像，无法解释为何推荐该物品。这些问题源于图像中心架构的限制，亟需迁移到多模态联合生成范式。

## 方法关键点
- **双扩散Transformer**：图像分支采用连续流匹配扩散，文本分支采用离散掩码扩散，跨注意力传递多模态条件。
- **偏好建模**：用VLM将交互物品转为结构化属性caption，再按频率加权采样生成用户文本偏好，平衡探索与利用。
- **三阶段训练**：
  - Warm-up：在时尚图文对上进行图文对齐与结构化文本重建；
  - 匹配感知个性化训练：引入不完整outfit的匹配条件（VAE编码+可学习角色嵌入），联合优化图像流匹配损失与文本掩码损失；
  - 文本增强微调：用LLM生成多样化匹配文本，仅用文本损失微调，高效提升多样性和适配性。
- **多条件可控推理**：使用分类器无关引导独立控制任务定义、匹配条件和个人偏好三种信号。

## 关键实验
在两个时尚数据集iFashion和Polyvore-U上，评估PFITB（填空）与GOR（整身生成）任务。对比SD系列、ControlNet、DiFashion、FashionDPO等基线，DualFashion在个性化得分上大幅领先（iFashion PFITB Per. 65.17 vs 60.39），同时保持较高的图像质量与兼容性，多样性也得到改善。训练效率比FashionDPO快约7倍。消融实验证实Warm-up、可学习角色嵌入、联合损失和文本增强微调均不可或缺。

## 核心启示
多模态双扩散架构通过解耦用户偏好与匹配信息，实现了图像生成与文本可解释性的协同增强，为生成式推荐提供了更高效且可控的方案。
