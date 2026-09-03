---
title: 'Influence-Directed Distillation: Solving the Diversity Bottleneck in Sampled-Token
  On-Policy Distillation'
title_zh: 影响力导向蒸馏：解决采样令牌在线蒸馏中的多样性瓶颈
authors:
- Run Yang
- Runpeng Dai
- Jie Sun
- Jielei Zhang
- Fan Zhou
- Hongtu Zhu
- Peiyi Li
- Longwen Gao
affiliations:
- BiliBili.Inc
- University of North Carolina at Chapel Hill
- University of Science and Technology of China
- Shanghai University of Finance and Economics
arxiv_id: '2608.29846'
url: https://arxiv.org/abs/2608.29846
pdf_url: https://arxiv.org/pdf/2608.29846
published: '2026-08-29'
collected: '2026-09-03'
category: Training
direction: On-policy 蒸馏多样性保持
tags:
- on-policy distillation
- diversity
- pass@k
- entropy
- sampled-token
- LLM
one_liner: 提出 IDA-OPD，用一阶局部熵影响力识别并替换熵收缩更新，仅靠采样令牌教师概率提升 pass@k 并保持 pass@1
practical_value: '- 在蒸馏小模型做生成任务时（如 query 推荐、商品描述、广告文案），不要只盯 pass@1；引入 pass@k 监控多样性继承，避免蒸馏后输出同质化。

  - 可以低成本复用 IDA-OPD 思想：用教师仅对采样 token 的 log-prob 做更新，通过一阶局部熵影响力判断更新是否压缩熵，对熵收缩更新做自适应优势收缩，无需全词表教师
  logits，适合线上资源受限的生成推荐场景。

  - 若已有 on-policy 蒸馏流程，先用该影响力代理做离线诊断，定位哪些训练 step 导致多样性下降，再有针对性调整更新或数据混合，比盲目增加正则更高效。

  - 在生成式推荐中，若要继承教师模型生成多样性（如多样商品标题、搜索联想词），可借鉴本文用符号一阶代理解耦教师-学生差距与学生局部概率结构的方法，快速识别负影响力位置。'
score: 7
source: huggingface-daily
depth: abstract
---

## 动机
Sampled-token on-policy distillation (OPD) 仅用教师对学生生成 token 的 log-prob 做蒸馏，避免全词表计算，但常出现 pass@1 提升而 pass@k 停滞的多样性蒸馏失败。现有修复手段多依赖昂贵的全词表 Forward-KL，不利于大规模部署。

## 方法
提出 First-Order Local Entropy Influence：一个带符号的一阶代理，将每次更新的熵效应解耦为教师-学生 log-prob 差距与学生的局部概率结构，并实证发现熵收缩集中在负影响力位置。基于此设计 IDA-OPD：不保留所有更新，而是保留熵增更新，将熵收缩更新替换为 divergence-adaptive advantage shrinkage，仅使用教师对采样 token 的 log-probability，不需要全词表信息。

## 结果
在 reasoning-oriented distillation 实验中，IDA-OPD 一致提升 pass@k，成功继承教师多样性，与最强的 teacher-informed 方法效果持平但成本严格更低，同时基本维持 vanilla OPD 的 pass@1。该方法证明无需全词表教师信息也能解决采样 token 蒸馏的多样性瓶颈。
