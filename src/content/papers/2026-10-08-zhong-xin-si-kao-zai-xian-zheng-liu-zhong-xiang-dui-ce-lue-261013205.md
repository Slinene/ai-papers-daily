---
title: Rethinking Relative Policy Differences Transfer of On-Policy Distillation
title_zh: 重新思考在线蒸馏中相对策略差异迁移
authors:
- Rong Wu
- Daocheng Fu
- Yu Yang
- Xuemeng Yang
- Siqi Li
- Shu Zou
- Yao Zhu
- Botian Shi
- Bo Zhang
- Cong Zhang
affiliations:
- Zhejiang University
- Shanghai Artificial Intelligence Laboratory
- Fudan University
- The Australian National University
- Renmin University of China
arxiv_id: '2610.13205'
url: https://arxiv.org/abs/2610.13205
pdf_url: https://arxiv.org/pdf/2610.13205
published: '2026-10-08'
collected: '2026-10-12'
category: Training
direction: LLM 后训练 · 相对策略差异蒸馏
tags:
- On-Policy Distillation
- Relative Policy Difference
- Implicit Reward
- Weak-to-Strong
- KL-Regularized Optimization
- LLM Post-Training
one_liner: 通过隐式奖励视角统一相对策略差异迁移，揭示任务定向差异强于规模差异，且参考过滤与目标兼容性决定迁移成败
practical_value: '- 在跨模型蒸馏或复用强模型能力时，优先取「任务定向优化产生的 update」（如 SFT/RL 后的 expert），不要直接拿更大参数的
  base 模型当老师；用 logπ_expert - logπ_ref 的隐式奖励替代绝对 logits，能降低对 teacher 绝对能力的依赖。

  - 参考模型不是随便选的：reference 应过滤掉与 expert 共享的通用行为，只保留增量。可以通过 top-k token overlap 选择低重叠
  reference；若目标模型与 proxy 不同模型族/代际，优先用与目标同 family 的 reference，可把失败迁移救回来。

  - 工程上可以用 top-16 token 分布近似，降低计算；训练时对 token 级 advantage 做 centering（减去当前策略期望）避免 intractable
  log Z；用 on-policy rollout + stop-gradient actor loss，直接适配 autoregressive 生成。

  - 蒸馏过程要同时监控 train 与 validation/held-out，关注目标与 expert 的 token overlap 提升；train acc
  上升但 val 不涨说明未泛化，应更换 reference 或 target，而不是继续多训。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
On-policy distillation 通常要求学生匹配更强 teacher 的绝对分布，导致 teacher 必须显著强于 student，限制了后训练结果复用。相对策略差异迁移只传 teacher 的“改进方向”，但哪些 policy difference 有用、哪些 target 能吸收，此前不清楚。

**方法关键点**  
- 从 KL 正则优化导出隐式奖励：proxy pair (π+φ, πφ) 的对数概率差 Δφ = log(π+φ/πφ) 等价于 token 级任务奖励 /τ 减去状态偏置 logZφ，可作为可迁移的稠密监督。  
- 定义 any-to-any 目标：最大化 E[αΔφ - βKL(πθ||πref)]，proxy reference 与 target reference 解耦；当两者相同时退化为常规 OPD。  
- 用 centering 去掉 logZφ，得到 on-policy actor loss；LLM 上按 token 计算，使用 top-16 token 分布近似。  
- 系统实验：Qwen3/Qwen2.5 系列，数学与代码任务；proxy pair 分别来自 RL、SFT 和纯规模差。

**关键结果数字**  
- 任务定向差异可迁移：RL/SFT pair 对 Qwen3-8B 的目标增益 GT +9.78~+32.23；纯规模差 pair 增益 -1.03~+8.23，远弱。  
- proxy gain 与 target gain 强相关（Pearson r=0.96），但更新幅度不能预测迁移：KInduced 0.353 的任务 pair 获得 +25.85，而 KInduced 0.418 的规模 pair 仅 +3.42。  
- 固定 expert Qwen3-4B-RL，改 reference 使 GT 从 +9.62（early-RL reference）到 +29.09（Qwen2.5-3B reference）；top-16 overlap 越低，残余能力转移越多。  
- 同一差异对不同 target 差异巨大：Qwen3 系列 +9.78~+29.09，Qwen2.5 系列 -2.46~+2.72；换用同代 reference 后 Qwen2.5 转正（+2.25~+6.74），是泛化问题而非训得不够。

**最值得记住的一句话**  
更强的老师不一定是更好的监督来源：迁移价值来自任务定向训练产生的相对策略差异，而不是模型规模带来的绝对分布优势；参考模型负责过滤共享行为，目标模型需要能朝 expert 方向泛化。
