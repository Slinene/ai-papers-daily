---
title: 'Mid-Harness: Scaling Actions Between Model and Harness for Terminal Agents'
title_zh: 终端智能体动作级采样与验证方法
authors:
- Minki Kang
- Ryo Hachiuma
- Shaokun Zhang
- Subhashree Radhakrishnan
- Yonggan Fu
- Jindong Jiang
- Mingjie Liu
- Ehsan Hosseini-Asl
- Yi Dong
- Yu-Chiang Frank Wang
affiliations:
- NVIDIA
- KAIST
arxiv_id: '2609.39982'
url: https://arxiv.org/abs/2609.39982
pdf_url: https://arxiv.org/pdf/2609.39982
published: '2026-09-29'
collected: '2026-10-01'
category: Agent
direction: 终端 Agent 动作级验证与测试时扩展
tags:
- Terminal Agents
- Test-Time Scaling
- Action Verification
- Pairwise Verification
- Distillation
- LLM Agents
one_liner: 在动作执行前采样并验证多个候选，以 pairwise 比较和蒸馏提升终端 Agent 轨迹成功率，成本效率优于纯轨迹扩展
practical_value: '- 对会改变环境状态的关键动作（选品、改库存、出价、下架、发消息）在执行前采样多个候选并用 pairwise verifier
  筛选；pairwise 比 listwise/pointwise 更稳定，尤其生成器与验证器同模型时。

  - 有更强模型但推理成本高时，离线收集 teacher 的 pairwise 偏好，用 LoRA 蒸馏出轻量 verifier，生成器不动；决策-only 只输出
  A/B，可再降 20-24% token 成本，9B 模型上 Pass@1 不降反升。

  - 动作级验证可与轨迹级 Best-of-N/Sequential Refine 叠加：同等环境执行次数下 Pass@1 可显著提升；测试时算力优先加动作验证，比单纯多跑完整
  trajectory 更划算。

  - 离线诊断 disagreement 发现失败集中在「命令语义 / 执行可行性」，建议业务中重点标注此类样本，优化 verifier。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
终端 Agent 通过随机采样动作工作，但能否生成有用动作不等于能可靠执行。一个坏命令（装错包、改错文件）会改变环境，使后续步骤变差，即使模型本可以生成更好候选。已有 test-time compute 多在轨迹级，动作级采样与验证何时有效、哪种验证机制好，仍不明确。

**方法关键点**  
- Mid-Harness 在 model-call wrapper 内把单次生成改为采样 N 个候选，再用 verifier 选一个交给原 harness 执行；生成器和 harness 不变。
- 比较三种验证机制：listwise、pointwise、pairwise；pairwise 对候选做两两比较，再按 margin-weighted win rate 聚合最佳动作。
- 用 GPT-5.6 Sol 作为 teacher，收集 117k 条 pairwise 偏好，以 LoRA 微调 TMAX-9B 作为 verifier；只更新 verifier，不更新 generator。
- 决策-only 验证只输出 A/B 偏好，省去推理文本，降低 token 成本。

**关键结果**  
- TerminalBench-Lite，TMAX-9B base Pass@1 50.00。用 GPT-5.6 Sol 前沿 verifier（listwise, N=8）达到 68.03，证明候选集中有可被验证器利用的更好动作。
- 同一模型自验证时，更多候选不能弥补弱验证：N=4→8，listwise 仅从 49.32 到 51.02。pairwise 最有效：N=8 达 54.76；蒸馏 pairwise 再提升至 57.14。
- 离线蒸馏使 pairwise agreement 从 59.01% 提升到 74.58%，verification agreement 从 38.52% 到 57.79%。
- 与轨迹扩展组合：TMAX-9B Best-of-3 55.10 → + distilled Mid-Harness 66.33；SR R=1 55.10 → + distilled 60.20。蒸馏 Mid-Harness N=8 达到 Best-of-T=5 的 Pass@1，只需其约 1/3 token 成本；组合后超过 Best-of-T=7 且成本更低。
- 跨 benchmark/model 也有效：Terminal-Bench 2.1 从 21.72 到 27.34；FeatureBench-Mini 从 1.45 到 7.25（distilled）；4B/27B 均有提升。
- 决策-only 验证在 9B 上 Pass@1 超过 reasoning 版，token 成本降 20.9%-24.1%。

**一句话记忆**  
动作采样只有在可靠验证下才有价值；固定生成器时，pairwise 比较与 verifier 蒸馏是把候选多样性转化为轨迹成功的关键。
