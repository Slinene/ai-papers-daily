---
title: AI Outperforms Humans in Personalized Image Aesthetics Assessment via LLM-Based
  Interviews and Semantic Feature Extraction
title_zh: 基于LLM访谈与语义特征提取的个性化图像美学评估超越人类
authors:
- Yoshia Abe
- Tatsuya Daikoku
- Yasuo Kuniyoshi
affiliations:
- The University of Tokyo
arxiv_id: '2605.14761'
url: https://arxiv.org/abs/2605.14761
pdf_url: https://arxiv.org/pdf/2605.14761
published: '2026-05-14'
collected: '2026-05-17'
category: Multimodal
direction: 个性化美学评估 · LLM交互式偏好获取
tags:
- Personalized AI
- Image Aesthetics
- LLM Interviews
- Semantic Features
- Human-AI Comparison
one_liner: LLM半结构化访谈提取个人语义偏好，结合图像低层特征，预测个人美学评分误差小于人类及自身重评
practical_value: '- **用LLM做用户偏好访谈**：在电商/推荐场景，可仿照半结构化LLM访谈主动捕获用户对商品风格、语义属性的偏好，代替纯被动行为数据，生成更细粒度的个性化标签。

  - **混合高低层特征建模**：将商品图像的低层视觉特征（CNN）与LLM提取的高层语义特征（如“简约”“复古”）融合，提升个性化推荐和排序的准确率，尤其对高偏好物品的命中率。

  - **AI预测稳定性优于人类自评**：可利用该系统作为用户当前审美偏好的“稳定代理”，避免人工标注的波动性，用于个性化搜索、穿搭推荐等场景的长期偏好建模。

  - **交互式偏好挖掘框架**：借鉴其半结构化访谈流程，在Agent或多轮对话中逐步深化对用户意图的理解，解决冷启动或稀疏反馈问题。'
score: 6
source: arxiv-cs.HC
depth: abstract
---

**动机**：个性化图像美学评估需同时捕捉客观视觉特征与主观个人偏好，传统DL模型仅基于低层特征，难以顾及个体差异；人类评价者又受自身审美干扰，预测他人偏好误差大。

**方法**：提出DL-LLM集成系统，通过LLM与用户进行半结构化访谈，主动引导用户表述对图像语义、风格、情感等高层特征的偏好，并将访谈提取的语义特征与CNN提取的低层视觉特征融合，训练回归模型预测个人美学评分。

**关键结果**：
- 在个性化评分预测上，该系统显著优于仅用图像特征的基线、人类预测者，甚至优于用户本人在一段时间后的重新评分。
- 预测误差低于个体内部的重评波动（within-person variability），表明AI可更稳定地捕获用户当前审美状态。
- 对高评分图像的预测优势尤为突出，而人类预测者易受自身审美偏差影响，误差最大。

**结论**：AI通过结合语义访谈与视觉特征，有望成为个体审美偏好的深层解释者，甚至比他人或未来的自己更准确。
