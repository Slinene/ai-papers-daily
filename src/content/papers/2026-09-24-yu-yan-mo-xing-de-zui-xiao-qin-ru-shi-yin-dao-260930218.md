---
title: Minimally Invasive Steering of Language Models
title_zh: 语言模型的最小侵入式引导
authors:
- Taha Entesari
- Jingyu Zhang
- Daniel Khashabi
- Mahyar Fazlyab
affiliations:
- Johns Hopkins University
arxiv_id: '2609.30218'
url: https://arxiv.org/abs/2609.30218
pdf_url: https://arxiv.org/pdf/2609.30218
published: '2026-09-24'
collected: '2026-09-25'
category: LLM
direction: LLM测试时对齐 · 预logit引导
tags:
- pre-logit steering
- KL regularization
- Fisher information
- test-time alignment
- activation steering
one_liner: MISVO用Fisher信息惩罚预logit干预的局部KL，冻结LLM测试时奖励引导，7项任务6项最佳
practical_value: '- 对冻结 LLM 的最后隐藏状态加位置特定干预向量，用 Fisher 二次型惩罚诱导分布与参考分布的局部 KL，适合电商文案、广告标题生成时按点击率、GMV
  等黑盒奖励在线调整，无需微调模型。

  - 工程上只需用冻结 language-model head 做矩阵-向量积解析计算梯度，轻量可部署到推理链路中，可在 Agent 调优或文案生成后叠加测试时奖励优化，避免重训成本。

  - 局部 KL 正则相比裸奖励优化，能防止输出分布过度偏离原始模型，保持语义连贯性与多样性，适合需要生成质量与业务目标平衡的场景，如搜索广告文案、商品卖点生成。

  - 对于变化快、延迟反馈的奖励信号（用户反馈、转化数据），可借鉴该无参数测试时优化思路，与 Best-of-N 采样结合，提升平均奖励且维持样本多样性。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：测试时奖励随用户、上下文或黑盒评估器变化，预 logit 引导能对冻结 LLM 做轻量干预，但无正则的奖励优化会显著改变输出分布，破坏生成质量。

**方法关键点**：提出 MISVO，在预 logit 引导中引入诱导 token 分布的局部 KL 几何惩罚；Fisher 二次型度量分布敏感性，解析梯度通过冻结语言模型头的矩阵-向量积高效计算。论文推导了序列级 KL 梯度的精确分解：解析 Fisher 项 + 后缀 score-function 项；在固定生成 horizon 下，后缀项是引导幅度的二阶量，三种 Fisher 替代与完整 KL 梯度一阶一致。MISVO 使用冻结参考替代，优化位置特定干预向量，不更新模型参数。

**关键结果**：在约 1B–14B 参数的偏好与代码生成任务上，7 个模型-任务设置中 6 个取得最高平均奖励；多样性、连贯性指标接近 Best-of-N，同时在奖励上优于无正则引导。
