---
title: 'Beyond Imitation: Filtering On-Policy Distillation by Reasoning Progress'
title_zh: 超越模仿：基于推理进展的在线蒸馏奖励过滤
authors:
- Chen Yang
- Haiyuan Wan
- Rengrong Xiong
- Yize Chen
- Danny H. K. Tsang
affiliations:
- The Hong Kong University of Science and Technology (Guangzhou)
- Tsinghua University
- Zhejiang University
- University of Alberta
arxiv_id: '2608.19408'
url: https://arxiv.org/abs/2608.19408
pdf_url: https://arxiv.org/pdf/2608.19408
published: '2026-08-18'
collected: '2026-08-26'
category: Training
direction: 推理蒸馏训练 · 过程奖励过滤
tags:
- On-Policy Distillation
- Process Reward
- Reasoning
- LLM
- Knowledge Distillation
- Reward Filtering
one_liner: 提出 R2-OPD，用独立过程奖励检测并过滤在线蒸馏中与推理进展冲突的教师信号
practical_value: '- 业务中若用小模型蒸馏大模型做 query 改写、推荐理由生成或搜索意图理解，不要只对齐教师 token 分布：可引入与业务目标一致的过程信号（如是否推进任务完成、是否命中正确商品），检测并
  mask 教师信号冲突的片段，避免学到“像老师但错误”的行为。

  - 训练多步 Agent 推理链路（如商品筛选、排序解释）时，用 rollout 估计中间状态 solve probability 并把相邻同向 progress
  合并后再评估，能显著降低 Monte Carlo 噪声，比逐 step 使用过程奖励更稳定。

  - 工程上 masking 比例和 segment 颗粒度很关键：论文中 q=30% 是甜点，q=50% 会损害性能；业务落地建议先做小比例过滤，并对不确定样本保守回退，避免误删有效教师信号。

  - 该方法只在离线蒸馏阶段引入额外 rollout 计算，不影响线上推理时延；成本较高，可只对高价值或难样本启用。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
On-policy distillation（OPD）在推理模型后训练中有效，但它默认教师 token 相似度等同于推理进展。实际中，学生可能偏离教师分布却更接近正确答案，而教师认可的 span 未必推进解题；统一施加教师监督可能抑制有效推理路径。此外，约三分之一 correct reasoning paths 因 overthinking 被截断，outcome-based 过滤无法利用这些轨迹。

**方法关键点**
- 提出 R2-OPD：用独立估计的过程奖励（process reward）作为教师无关的推理进展参考，只将其用于检测蒸馏信号冲突并选择性 mask，不替换 OPD 目标，也不把过程奖励作为额外优化项。
- 过程奖励估计：将响应按反思词分割为 reasoning segments；在每段边界，用当前学生模型做 N_eval=8 次 answer-eliciting rollouts，估计 solve probability；process reward 为相邻 solve probability 的增量。
- 噪声消减：先将相邻 sign-consistent 的 process reward 合并（telescoping 消除内部边界误差），再平均 segment 内 token-level KL loss 降低方差（O(1/L)）。
- 冲突检测：在每个 response 内按 process reward 排序 segment，若高 progress 段对应更高平均 KL loss 则累积 inconsistency score；按预算 q=30% mask 最不一致的 segment，loss 按剩余 token 重新归一化。
- 保守 fallback：若过程奖励不可用、segment 不足或无冲突则完全不 mask，保留原教师监督。

**关键结果**
在 DeepSeek-R1-Distill-Qwen-1.5B 学生 + JustRL-1.5B 教师、DAPO-Math-17K 训练、AIME 2024/2025 + OlympiadBench 评估的设置下，R2-OPD 达到 avg@4 35.06、pass@4 51.83，分别超标准 OPD 2.51/4.46 分，超最强基线 Uni-OPD 4.28/5.17 分，AIME 提升最明显。异构迁移 Qwen3-1.7B + e3-1.7B 上 pass@4 提高 2.49。消融显示 q=30% 最优，q=50% 大幅掉点；sign-consistent merging 将 PR–KL rank agreement 从约 0.20–0.27 提升到 0.55–0.73，移除后 AIME 24/25 掉 15.0/14.16 分。

**最值得记住的一句话**
教师相似度不等于推理进展；用独立过程奖励做“可靠性测试”，只 mask 与进展排序冲突的蒸馏信号，比直接替换或加权更稳健。
