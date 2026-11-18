---
title: 'More Than a Score: Reinforcement Learning with Verbalized Feedback for Generative
  Recommendation'
title_zh: 超越分数：言语化反馈强化生成式推荐
authors:
- Zipeng Chen
- Xinyu Lin
- Yuliang Sun
- Sheng Zhang
- Zeyu Wang
- Xiaowen Shi
- Junwei Pan
- Chengguo Yin
affiliations:
- Tencent Inc.
- National University of Singapore
- The Chinese University of Hong Kong
arxiv_id: '2611.22410'
url: https://arxiv.org/abs/2611.22410
pdf_url: https://arxiv.org/pdf/2611.22410
published: '2026-11-17'
collected: '2026-11-18'
category: GenRec
direction: 生成式推荐 · Verbalized Feedback RL
tags:
- Generative Recommendation
- Reinforcement Learning
- Verbalized Feedback
- GRPO
- User Simulator
- Semantic ID
one_liner: 将用户模拟器生成的个性化言语反馈融入GRPO，引导候选修正并联合优化原始与修正候选，提升生成式推荐准确率
practical_value: '- 用户模拟器只在训练时生成个性化言语反馈，推理时移除，不增加线上延迟；可迁移到电商/广告场景：用LLM先总结用户历史交互的正负偏好（aspect），再对候选item做同样总结，离线生成评分+评论文本，作为RL训练信号。

  - 联合优化原始候选与反馈修正候选：把两者放进同一个group做GRPO，原始候选走标准CLIP，修正候选用Policy Shaping f(x)=x/(x+γ)避免低概率更新不稳；奖励用binary命中
  + rank-aware负样本惩罚，适合生成式推荐中的全库排序训练。

  - 反馈质量决定收益：随机/错配的用户反馈比不用反馈更差（Shuf/MGF结果低于w/o VF）；开工前先用MAE/RMSE/BLEURT评测模拟器质量，保证反馈与用户偏好对齐后再接入RL。

  - 言语反馈能提升探索多样性：训练过程中类别多样性、SID token多样性、unique item覆盖都更高，奖励收敛所需步数约少1.9倍；在Agent RL里也可以尝试用自然语言critique来引导探索，而不是只靠reward
  shaping。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
生成式推荐（GR）常用SFT+RL，但RL只依赖标量奖励，低奖励无法说明是偏好不匹配还是重复推荐，策略只能盲目试错。VerRec希望用个性化言语反馈（verbalized feedback, VF）提供显式探索信号，指出“哪里错了、怎么改”。

**方法关键点**  
- 用户模拟器（LLM）将用户历史交互总结为正负方面（aspect），对候选item也做同样总结，生成评分+评论作为VF。  
- 对每个原始候选，policy基于历史+原始候选+VF生成修正候选；原始与修正共2G个候选，统一GRPO优化。  
- 奖励设计：二元命中（是否为目标item）+ rank-aware惩罚高分负样本。  
- 原始候选用标准CLIP，修正候选用Policy Shaping f(x)=x/(x+γ)，避免低概率token更新不稳定。  
- 用户模拟器只在训练时使用，推理时移除。

**关键实验**  
在三个Amazon数据集（Cell Phones, Baby, Book）上，以MiniOneRec-SFT和LETTER为backbone，与SASRec、BIGRec、MiniOneRec、R2ec等比较。VerRec大多数指标最优：例如Cell Phones MiniOneRec-SFT backbone上H@5 0.0357 vs MiniOneRec 0.0346，N@5 0.0246 vs 0.0240。反馈模拟质量优于MGFRec/Agent4Rec；错配或随机反馈会伤害性能。训练奖励提升更快（达到相同奖励步数约少1.9倍），类别多样性、SID token多样性、unique item覆盖更高。

**最值得记住的一句话**：个性化言语反馈将“哪里错了、怎么改”显式注入RL，比标量奖励更能引导生成式推荐探索；但反馈质量决定成败。
