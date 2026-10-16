---
title: 'Each Reward to Its Relevant Tokens: Reward-Specific Token-Level Credit Assignment
  for Multi-Reward RL'
title_zh: 多奖励 RL 的逐奖励 Token 级信用分配
authors:
- Skylar Zhai
- Haonan Wang
- Zhining Liu
- Linxin Song
- Xuwei Ding
- Jingcheng Liang
- Jian Kang
affiliations:
- University of Minnesota
- National University of Singapore
- University of Illinois Urbana-Champaign
- University of Southern California
- University of Pennsylvania
arxiv_id: '2610.21439'
url: https://arxiv.org/abs/2610.21439
pdf_url: https://arxiv.org/pdf/2610.21439
published: '2026-10-15'
collected: '2026-10-16'
category: Training
direction: 多奖励 RL 令牌级信用分配
tags:
- RLVR
- Multi-Reward RL
- Token-Level Credit Assignment
- GRPO
- Tool Calling
- Text-to-SQL
one_liner: 用 verifier 信息 self-replay 定位每个 reward 的相关 token，把 advantage 按相关性重分配，加速并提升多奖励
  RL
practical_value: '- 对电商/Agent 里带多个可验证约束的生成任务（商品文案、广告标题、工具调用、SQL/API 生成），把每个 reward
  的 advantage 按 self-replay 的相关性分配到 token，而不是整段均匀；尤其格式类 reward 只落在标签/keyword/CTA 等少数
  token，能显著加快收敛。

  - 若 verifier 有可文本化信息（参考 query、执行 error、约束条件），可直接复用 MRTPO 的 leave-one-out replay：同一条
  response 在 P_all 和 P_\k 各 forward 一次，用 next-token 分布的 JS 距离得到 token 权重；无需额外模型或标注，成本只比
  GDPO 多 10–20%，且只在 reward 组内有方差时 replay。

  - β=0.5 是不错的默认值，前 10 步 smoothstep warmup；保留 1−β 的均匀份额避免重分配过激，并可对 reallocated part
  做二阶矩约束。这个方法正交于 SAW/DVAO 等 response 级 reward reweighting，可以叠加。

  - 做 prompt 约束（如“必须包含关键词、以某句结尾、加双引号”）时，直接去掉单个约束 replay 能定位到 checker 实际读取的 token；对
  IFBench 这类未见约束泛化提升最明显，适合冷启动或模板频繁变化的场景。'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
多奖励 RLVR（GRPO/GDPO 等）把每个 reward 的 advantage 均匀摊到整个 response 的所有 token，但一个 verifier 往往只看少数位置。错误 token 会收到大量无关 reward 的 credit/penalty，导致收敛慢，约束越多问题越明显。于是核心问题变成：能否把每个 reward 主要分配给真正相关的 token。

### 方法关键点
- **无需额外模型或标注的 token 相关性估计**：对每个 reward k，使用其 verifier 自身信息 Z_k（如参考 SQL/query、执行 error、单条约束）构造 P_all 和 P_\k（只去掉 Z_k），用行为策略重放已采样 response，计算每个位置两个 next-token 分布的 Jensen–Shannon 距离 q_{k,t}。
- **按相关性重分配 advantage**：权重 w_{k,t}=(1−β)+β q_{k,t}/q̄_k，β=0.5 且前 10 步 smoothstep warmup；每 token advantage = Σ_k A_k w_{k,t}，再做 batch 标准化。保留 1−β 的均匀份额，并用二阶矩约束防止过度重分配。
- **可叠加 response 级 reward reweighting**：MRTPO 只改变 advantage 落在哪些 token，和 SAW/DVAO 等正交。

### 关键结果
在 text-to-SQL、multi-constraint instruction following、tool calling 三个任务、六个模型（1.5B–7B）上，MRTPO 平均优于 GRPO/GDPO/OPSD/CoRT。text-to-SQL 平均执行准确率比 GDPO 高约 1.3–1.6 点；IFBench 高 2.4–3.2 点，尤其是训练未见过的约束；tool calling 的格式 reward 达到 0.8 所需步数从 GDPO 的 19 步、GRPO 的 34 步缩短到 13 步，10 步后格式率 97% vs GDPO 2%、GRPO 4%。消融显示 shuffle token 位置后增益消失，表明收益来自位置相关；replay 只增加 10–20% 训练时长。

最值得记住的一句话：多奖励 RL 不仅要决定每个 reward 给多少权重，还要决定每个 reward 落在哪些 token；verifier 自己掌握的信息就足够做无标注的 token 级 credit assignment。
