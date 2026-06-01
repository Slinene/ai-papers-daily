---
title: 'The Flip Side of RLHF: On-Policy Feedback for Reward Model Self-Supervised
  Improvement'
title_zh: RLHF的另一面：在线反馈驱动奖励模型自监督改进
authors:
- Xiaobo Wang
- Tong Wu
- Min Tang
- Jiaqi Li
- Qi Liu
- Zilong Zheng
affiliations:
- State Key Laboratory of Cognitive Intelligence, University of Science and Technology
  of China
- University of Science and Technology of China
- Institute of Artificial Intelligence, Hefei Comprehensive National Science Center
- State Key Laboratory of General Artificial Intelligence, BIGAI
arxiv_id: '2605.30888'
url: https://arxiv.org/abs/2605.30888
pdf_url: https://arxiv.org/pdf/2605.30888
published: '2026-05-28'
collected: '2026-06-01'
category: Training
direction: LLM 对齐中的奖励模型自监督训练
tags:
- RLHF
- Reward Model
- Self-supervised
- On-policy
- Value Function
- Alignment
one_liner: 提出SAVE框架，利用在线反馈和价值锚定对奖励模型进行自监督改进，缓解策略分布偏移
practical_value: '- 在推荐 RL 策略优化中，利用实时生成的 on-policy 数据与价值函数估计的期望回报计算优势值，作为自监督信号更新奖励模型，无需额外标注，同时缓解静态
  RM 与策略不匹配问题。

  - 借鉴 prompt-specific value head 设计，为每个用户或上下文动态构建价值头，自适应确定反馈阈值，过滤低质量样本，提升训练信号信噪比。

  - 采用对比目标区分正负样本时，可直接利用策略采样结果的排序（如按 RM 打分划分）构造正负对，减少对绝对偏好标注的依赖。

  - 方法轻量易集成，计算优势 → 过滤 → 对比更新，可嵌入现有推荐系统 RL 框架，适用于生成式推荐、对话式推荐等策略频繁漂移的场景。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：构建强奖励模型（RM）是 LLM 对齐的核心瓶颈，高质量偏好数据获取昂贵且静态 RM 难以适应策略进化，导致越训练越失真的问题。  
**方法**：提出 SAVE（Self-supervised reward model improvement via Value-Anchored On-policy feedback），利用策略实时生成的响应作为在线反馈，通过 prompt-specific 的价值头作为自适应锚点，计算 RM 优势值并过滤模糊样本，最终以对比目标更新 RM，实现无额外标注的自监督改进。  
**关键结果**：在 6 个多样性基准测试中，SAVE 全面超越基线，且在 GRPO、RLOO、GSPO 三种主流 RL 算法及不同策略模型上均取得一致的性能提升，验证了其有效性与泛化性。
