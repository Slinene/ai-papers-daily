---
title: 'TailorMind: Towards Preference-Aligned Multimodal Content Generation'
title_zh: TailorMind：面向偏好对齐的多模态内容生成
authors:
- Hengji Zhou
- Ye Liu
- Yufeng Liu
- Si Wu
- Lianghao Xia
- Liqiang Nie
affiliations:
- South China University of Technology
- Harbin Institute of Technology, Shenzhen
arxiv_id: '2606.23643'
url: https://arxiv.org/abs/2606.23643
pdf_url: https://arxiv.org/pdf/2606.23643
published: '2026-06-22'
collected: '2026-06-23'
category: GenRec
direction: 生成式推荐 · 多模态内容生成
tags:
- Personalized Generation
- Multimodal
- Collaborative Filtering
- RAG
- Preference Alignment
- Textual Gradient Descent
one_liner: 链接协同偏好建模与可控多模态生成，实现个性化多模态内容创建
practical_value: '- 用户行为→文本偏好：利用超图协同过滤从稀疏交互中提炼文本用户画像，可直接迁移到商品描述/广告文案的个性化生成，作为 prompt
  输入。

  - 文本梯度下降优化：用排序误差反馈迭代更新用户画像，类似思路可用于优化推荐解释或搜索 query 的文本生成，使输出更贴近真实偏好。

  - RAG 风格控制：检索真实 UGC 作为风格参考，能避免生成内容失真，适用于电商场景中保持品牌调性或社区风格统一。

  - 跨模态一致性反思：通过图文相似度比对减少语义漂移，启发构建多模态内容审核或一致性校验模块。

  - TailorBench 评估维度：连贯性/新颖性/美学/幻觉/画像匹配，可作为生成式推荐效果评估的参考框架。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：个性化内容系统高度依赖 UGC，但新颖或专业内容常因成本、技能等原因缺失或延迟。现有生成器难以将用户行为转化为可控的生成偏好，无法实现即时、个性化的多模态内容创建。  
**方法**：提出 TailorMind 框架，包含四个关键模块：  
1. **超图协同过滤**：基于用户历史行为构建超图，丰富稀疏兴趣表示，生成用户兴趣词分布。  
2. **文本画像优化**：用排序误差反馈和文本梯度下降，将兴趣词分布转化为与用户偏好对齐的文本画像，作为生成控制条件。  
3. **检索增强风格控制**：根据文本画像检索语义相近的真实 UGC 样本，提取风格噪声，指导扩散模型生成符合平台调性的图片。  
4. **跨模态一致性反思**：计算生成图像与文本的 CLIP 相似度，过滤低匹配度样本，确保图文语义一致。  
**结果**：在来自三大主流平台的 TailorBench 上，TailorMind 的连贯性得分与基线可比或更优，新颖性和美学质量显著超越 GPT-4V 等生成基线及真实 UGC，并在推荐重排序中 Recall 最高提升 29%。
