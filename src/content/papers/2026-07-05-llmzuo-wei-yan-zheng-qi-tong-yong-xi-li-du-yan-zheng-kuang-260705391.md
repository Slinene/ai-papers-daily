---
title: 'LLM-as-a-Verifier: A General-Purpose Verification Framework'
title_zh: LLM作为验证器：通用细粒度验证框架
authors:
- Jacky Kwok
- Shulu Li
- Pranav Atreya
- Yuejiang Liu
- Yixing Jiang
- Chelsea Finn
- Marco Pavone
- Ion Stoica
- Azalia Mirhoseini
affiliations:
- Stanford University
- UC Berkeley
- NVIDIA Research
arxiv_id: '2607.05391'
url: https://arxiv.org/abs/2607.05391
pdf_url: https://arxiv.org/pdf/2607.05391
published: '2026-07-05'
collected: '2026-07-07'
category: Agent
direction: Agent验证与测试时扩展
tags:
- LLM-as-a-Verifier
- Verification Scaling
- Trajectory Reward
- Fine-grained Feedback
- Test-Time Scaling
- RL Reward Shaping
one_liner: 用token logits期望代替离散评分，实现连续验证并支持评分粒度、重复、分解三维扩展，跨域SOTA
practical_value: '- **连续评分替代离散打分**：提取评分token完整logits分布求期望，消除离散评委的高平局率（27%→0%），可迁移到任何需LLM打分排序的场景（广告/商品质量评估），显著提升区分度。

  - **三维验证扩展**：通过评分粒度（1→20 tokens）、重复评估（1→16次）、标准分解（单标准→多标准Ensemble），验证准确率从73%提升至78%，工程中可按成本预算灵活拼接，平衡精度与延迟。

  - **成本高效候选选择**：概率枢轴锦标赛（PPT）算法，仅需𝒪(Nk²)次比较（k≪N），利用环形消除位置偏置并集中预算于前k候选，适用于大规模召回后的精排或生成式推荐item
  pool筛选。

  - **验证分数作为稠密RL奖励**：将连续验证信号作为中间过程奖励，显著提升off-policy SAC（约1.8×样本效率）和on-policy GRPO（1.1×效率）的训练速度与最终成功率，可直接用于推荐策略或聊天Agent的强化学习优化，无需手工设计奖励函数。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：当前LLM作为判断器（judge）输出离散分数，导致高频平局（27%），无法区分复杂候选方案，限制了测试时扩展（test-time scaling）的上限。作者将验证看作一个独立的扩展维度，提出利用评分token的完整logits分布进行细粒度连续评估，并系统研究其扩展性。

**方法要点**：
- **连续奖励估计**：不取argmax，而是计算所有评分token概率的期望值作为轨迹奖励，消除平局并反映模型的不确定性。
- **三维扩展**：① 评分粒度（从1～20 tokens），增大信噪比；② 重复评估（1～16次）降低方差；③ 标准分解（如规范、输出、错误三个子标准）减少单一标准偏差。三者互补，验证准确率从73%升至78%。
- **成本高效排序**：提出概率枢轴锦标赛（PPT），先通过随机环形消偏，再挑选前k个枢纽进行两两比较，将复杂度从𝒪(N²)降为𝒪(Nk²)，且保留高选择质量。
- **通用轨迹奖励模型**：框架无需训练，可直接作为任何Agent轨迹的奖励模型，输出连续偏好概率。

**关键结果**：
- 跨编码、机器人、医疗等多域SOTA：Terminal-Bench V2 86.5%（Pass@1 83.1%），SWE-Bench Verified 78.2%（76.1%），RoboRewardBench 87.4%，MedAgentBench 73.3%。
- 验证信号与任务进度高度相关（VOC 0.848），可用于实时监控。
- 作为稠密奖励，在LIBERO机器人任务上用DSRL-SAC提升样本效率约1.8倍，最终成功率0.76 vs. 0.69；在MATH数学推理上用GRPO提升约1.1倍。

**最值得记住**：将评分token的完整概率分布作为连续奖励，是零成本提升LLM验证能力的通用原则。
