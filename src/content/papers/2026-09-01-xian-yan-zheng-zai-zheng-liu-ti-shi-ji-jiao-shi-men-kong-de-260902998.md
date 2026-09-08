---
title: 'Verify Before You Distill: Prompt-Level Teacher Gating for On-Policy Distillation'
title_zh: 先验证再蒸馏：提示级教师门控的在线策略蒸馏
authors:
- Zhiwei Zhang
- Zechen Sun
- Fei Zhao
- Kang Peng
- Bin Liang
- Huayu Deng
- Yao Hu
- Kam-Fai Wong
- Mu Chuan
affiliations:
- AllSpark Team
arxiv_id: '2609.02998'
url: https://arxiv.org/abs/2609.02998
pdf_url: https://arxiv.org/pdf/2609.02998
published: '2026-09-01'
collected: '2026-09-08'
category: Training
direction: On-policy distillation 教师门控
tags:
- On-policy distillation
- Teacher gating
- RLVR
- GRPO
- LLM post-training
- GPU utilization
one_liner: 通过 verifier 探针按 prompt 门控教师信号，可靠才用稠密 OPD，否则退回 verifier-grounded GRPO
practical_value: '- 蒸馏 / 生成式推荐中不要无条件信任 teacher：可对 teacher 生成的候选或软标签加一道低成本验证。用与最终 reward
  一致的验证器（业务规则、点击 / 转化标签、代码单测等）采 KT=3 个样本，按 prompt 级通过率决定是否采用 teacher 信号；不过门就退回基于 outcome
  的 GRPO 或直接 mask。

  - 利用异步 pipeline 里空闲的 teacher 节点做 reliability probes：推荐系统离线训练中教师打分节点常因等学生 rollout
  而闲置，把探针生成放在该窗口可把 GPU 利用率从不足 10% 拉到 70% 以上，end-to-end 时间开销仅约 6%。

  - 硬路由优于信号插值：TGOPD 不使用加权混合 OPD 与 GRPO，避免不同密度、不同来源信号互相干扰。工程落地简单，且消融显示大部分收益来自屏蔽坏信号而非
  fallback。

  - 阈值设置从简：三探针两票通过（KT=3, τ=2/3）或多数投票即可，无需精细排序。对缺少精确 verifier 的开放域任务，可先用可自动判定的弱标签（如规则、分类器）验证，扩展受限时优先关注自信错误的高风险
  prompt。'
score: 8
source: huggingface-daily
depth: full_pdf
---

动机：
On-policy distillation（OPD）以冻结教师对学生 rollout 提供逐 token 的 reverse-KL 稠密信号，样本效率远高于轨迹级 RLVR。但 Vanilla OPD 对每个 prompt 无条件信任教师；reverse KL 的 mode-seeking 特性会集中学生到教师高概率行为，一旦教师在该 prompt 上自信但错误，稠密梯度会放大错误。诊断显示教师自我置信度并不能可靠区分可靠性：代码域 AUROC 0.51，数学 0.73；低可靠性区域内教师最高置信度回答在代码和数学上分别错误 84% 和 61%。同时异步 OPD 教师节点只做前向评分，利用率仅 9.8%。因此需要在 prompt 级验证教师可靠性，并复用空闲算力。

方法关键点：
- 定义教师可靠性 RT(x)=E_{y~πT}[r(x,y)]，用 KT 个 teacher probes 的 verifier 通过率 qT(x) 估计。
- 门控规则：qT(x)≥τ 时纯 OPD，否则纯 verifier-grounded GRPO；两者硬路由、不混合。
- 默认 KT=3、τ=2/3（至少两个探针通过），探针与学生 rollout 并发执行，利用教师节点空闲窗口。
- 学生 rollout 仍照常由验证器评分，两种候选优势提前形成，但 gate 只选择一个。

关键实验：
- 在 4B/35B 两个规模、数学/代码/指令遵循三个域上评估，baseline 包括 Vanilla OPD、TrOPD、RG-OPD、RLSD-style。
- 单域六个设置全部优于 Vanilla OPD，代码域增益最大（4B +3.0、35B +2.9）。
- 35B 代码域 LiveCodeBench 上所有其他蒸馏方法均负迁移，TGOPD 是唯一正迁移并超越教师的方法（相对 base +3.0，相对 teacher +1.3）。
- 多域训练七基准平均提高 1.14（4B）和 0.95（35B）。
- 消融显示约 90% 收益来自屏蔽不可靠教师信号；阈值在多数投票附近有宽最优。
- 教师节点 GPU 利用率从 9.8% 升至 78.9%，35B 码域步时仅增加 5.9%。

最值得记住：
先验证教师、再决定是否用其稠密信号，并用空闲算力做验证，是简单而有效的 OPD 改进。
