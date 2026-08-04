---
title: 'SAF-OPD: Stable Advantage Fusion for On-Policy Distillation'
title_zh: 稳定优势融合：在线策略蒸馏的熵崩溃应对方法
authors:
- Yifan Ding
- Xincheng Wei
- Yoshua Y. Li
- Ziheng Li
- Yuquan Lu
- Siyu Zhang
- Dongsheng Ma
- Rongxiang Weng
- Xunliang Cai
- Yun Chen
affiliations:
- Shanghai University of Finance and Economics
- Meituan
- The Chinese University of Hong Kong, Shenzhen
- Peking University
arxiv_id: '2607.29209'
url: https://arxiv.org/abs/2607.29209
pdf_url: https://arxiv.org/pdf/2607.29209
published: '2026-07-30'
collected: '2026-08-04'
category: Training
direction: RLVR与在线蒸馏的稳定融合训练策略
tags:
- RLVR
- OPD
- GRPO
- knowledge distillation
- entropy collapse
- advantage fusion
one_liner: 通过稀疏压缩控制量级、预热退火调度时间，稳定GRPO与OPD优势融合，避免熵崩溃并提升生成质量
practical_value: '- 在强化推荐系统中，业务指标（如点击）提供稀疏奖励，教师模型（如大模型打分）提供密集信号，借鉴SAF的量级控制（top-k稀疏化+tanh压缩）可抑制教师信号中少数极端
  token 对梯度更新的主导，避免训练崩溃。

  - 采用KL散度触发的预热和线性退火策略，自适应调节教师信号强度，防止早期过度模仿限制探索，后期保留教师指引的同时释放业务奖励的探索压力，可迁移到Agent训练或生成式推荐策略优化。

  - SAF仅修改优势融合部分，不增加额外模型或损失，实现轻量、即插即用，适合在已有强化学习训练流程中快速验证教师信号融合效果。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：强化学习验证奖励（RLVR）如GRPO仅提供序列级稀疏奖励，在线策略蒸馏（OPD）提供token级密集信号但会限制探索上限。两者融合时，由于GRPO优势有界（组归一化），而OPD优势无界且存在长尾分布，固定系数融合会导致两个失配：1）量级失配（少量token的OPD值远大于GRPO，主导更新）；2）时间失配（全强度OPD持续牵引学生，令其过早丧失探索，性能天花板低于教师）。因此固定融合会引发策略熵崩溃，最终性能反而不及单独使用。

**方法**：提出SAF（稳定优势融合）框架，仅对OPD优势施加四阶段控制：量级控制通过序列内top-k%稀疏化（保留|A_OPD|超过分位数的token）和带阈值c的tanh压缩（将优势限制在(-c,c)）；时间控制则先进行KL散度触发的线性预热（监测学生-教师KL下降比例，达到δ时提前结束预热），再线性退火至残差系数c_min。最终融合信号为 A_GRPO + opd_coef(s)·scale(s)·A_OPD_tanh，四阶段可独立开关，退火跨度由预热实际结束点决定，引入开销极小。

**实验**：在数学推理（AIME24/25、HMMT25）和代码生成（HumanEval+、MBPP+、LiveCodeBench）共7个基准上，以Qwen3-8B/4B/1.7B为学生、Qwen3-30B-A3B为教师，对比Base、GRPO-only、OPD-only和固定融合GRPO+OPD。结果：SAF在所有6组模型-任务域上均优于固定融合，平均提升0.51%-2.70%（数学最高+1.85%，代码最高+2.70%），且避免熵崩溃，保持较高策略熵和较长生成长度，验证准确性后期持续上升。消融表明量级控制单独使用不足，预热+退火时间控制是关键，KL触发阈值δ=0.2最优。
