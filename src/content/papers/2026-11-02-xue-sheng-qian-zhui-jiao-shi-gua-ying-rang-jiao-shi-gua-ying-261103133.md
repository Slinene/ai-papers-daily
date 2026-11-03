---
title: 'Meet Students Where They Are: Student-Prefix Teacher Adaptation for On-Policy
  Distillation'
title_zh: 学生前缀教师适应：让教师适应学生生成前缀以提升在线策略蒸馏
authors:
- Xue Zhang
- Songming Zhang
- Yunlong Liang
- Fandong Meng
- Yufeng Chen
- Jinan Xu
affiliations:
- Beijing Jiaotong University
- Weixin AI, Tencent
arxiv_id: '2611.03133'
url: https://arxiv.org/abs/2611.03133
pdf_url: https://arxiv.org/pdf/2611.03133
published: '2026-11-02'
collected: '2026-11-03'
category: Training
direction: On-policy 蒸馏·教师前缀适配
tags:
- On-Policy Distillation
- Teacher Adaptation
- RLVR
- Knowledge Distillation
- Prefix Conditioning
one_liner: 在蒸馏前用学生前缀 RLVR 微调教师，提升其对学生在策略轨迹的监督可靠性，无需改变蒸馏目标
practical_value: '- 在模型轻量化部署（如大模型蒸馏到线上小模型）时，除标准蒸馏外，先收集学生 rollout 截断为前缀，用可验证奖励（如最终答案/转化标签正确性）微调教师，使教师能“从学生所在状态继续”，可显著改善
  token 级监督质量。实现时只对 continuation 部分做 RL，前缀作为 context，不模仿学生错误。

  - 评估教师蒸馏能力应增加前缀条件恢复率（prefix-conditioned recovery accuracy），即给定学生常见前缀下教师正确完成的概率。该指标比独立准确率更能预测蒸馏增益；若教师在前缀上优势几乎消失，标准
  OPD 可能停滞。

  - 随机截断学生 rollout 作为前缀训练集，无需标注错误位置，是低成本构建教师故障恢复数据的方法。在电商文案/搜索 query 改写等任务中，可用类似方案让教师适应小模型的实际输出，并周期性从最新学生采集前缀以追踪分布漂移。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**
On-policy distillation (OPD) 用学生自生成轨迹训练，缓解曝光偏差，但教师模型对学生的错误推理和不熟悉表达存在分布不匹配，token 级监督可靠性随前缀增长而衰减。实验显示，教师解决干净问题准确率 60.99%，但接到 50% 学生前缀后降至 28.91%。现有方法多在学生侧截断、加权，未直接适配教师。

**方法关键点**
- 两阶段：先收集学生 rollout，随机截断 1-90% 作为前缀，用 RLVR 在教师上继续生成，奖励为最终答案正确性（verifiable reward），只对 continuation tokens 计算 action log-probs，前缀作为 context，不模仿学生错误。
- 冻结适配后的教师，用于标准 OPD，蒸馏目标完全不变。
- 迭代扩展：下一轮从最新蒸馏学生重新采集前缀，教师学生均 warm-start，跟踪学生分布漂移。

**关键实验**
在五个数学基准（AIME24/25、AMC23、HMMT24/25）上，三个师生配对。单轮 SPTA 相比标准 OPD 平均提升：Qwen3-4B→Qwen3-4B-Base +3.78（31.52→35.30）；DeepSeek-R1-Distill-Qwen-7B→1.5B +3.03（30.20→33.23）；JustRL-DeepSeek-1.5B→同学生 +0.82（41.97→42.79）。与 task-level RLVR 教师对照，SPTA 分别高 3.33 和 0.87 点，表明增益来自前缀条件而非额外教师训练。教师恢复指标：Qwen3-4B 在 50% 前缀时由 28.91→49.88，90% 前缀时由 22.36→47.68；尽管教师干净准确率下降 6.60 点，学生仍更优。第二迭代再 +1.27（35.30→36.57）。

**最值得记住的一句话**
教师的独立解题能力不等于其在学生生成前缀上提供可靠监督的能力；蒸馏前应让教师适应学生实际访问的状态。
