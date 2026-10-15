---
title: 'Hindsight-Privileged RLVR: Single-Rollout Token Credit Without Group Sampling'
title_zh: 后见之明特权 RLVR：免组采样的单次轨迹令牌信用分配
authors:
- Wei Chen
- Yubing Wu
- Zhou Xu
- Haoyue Zhang
- Delu Zeng
- Jiahao Wang
- Junmei Yang
- Pan tiewen
- Jingfeng Liu
- Zhiheng Zhou
affiliations:
- 华南理工大学
- 清华大学
- 香港科技大学
- 华为2012实验室
- 深圳技术大学
arxiv_id: '2610.20497'
url: https://arxiv.org/abs/2610.20497
pdf_url: https://arxiv.org/pdf/2610.20497
published: '2026-10-14'
collected: '2026-10-15'
category: Training
direction: RLVR 单 rollout token 信用分配
tags:
- RLVR
- token credit
- hindsight
- GRPO
- single rollout
- JSD
one_liner: 用已验证轨迹的未来信息对单次 rollout 计算归一化 JSD token 权重，替代 GRPO 组采样，训练最高提速 2.30 倍
practical_value: '- 对交互成本高、rollout 贵的电商 Agent（如导购、多步搜索、谈判）可尝试 HP-RLVR 的单 rollout 方案替代
  GRPO：rollout 量降至 1/8，适合模拟器或真实用户反馈昂贵的场景。

  - 工程实现上无需额外 critic 或 reference model，只需用同一 frozen policy 做两次前向：因果视图与加入未来+verifier
  反馈的 hindsight 视图；verifier 结果渲染成文本 outcome descriptor，可直接复用现有推理路径。

  - 落地时建议监控 zero gradient records 与同质 reward group 比例：GRPO 在稀疏 reward 下大量梯度为零，HP-RLVR
  可以避免该问题，但历史 baseline 引入偏倚，需结合任务小规模 paired run 验证。

  - 注意该方法的精度 tradeoff 是任务相关的：数学任务占优，代码与 ALFWorld 低于 GRPO；业务侧不能默认单 rollout credit 一定更好，应先在小流量任务上对比
  best checkpoint 与完整训练耗时。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

动机：
- RLVR 用 terminal reward 训练 LLM，但把奖励分配到 token 困难；GRPO 需要每条 prompt 多次 rollout，且组内奖励同质时 advantage 为零，训练信号消失。
- 问题：能否只用一条已验证轨迹（无论成功或失败）就产生 token 级信用，降低成本且保持训练信号？

方法关键点：
- 单 rollout：每个 prompt 只采样一条轨迹，记录生成概率。
- 历史基线：用该 batch 之前已完成轨迹的平均奖励 bk 作为 baseline，得到有符号的 si=Ri−bk。
- 两种评分视图：对每个 token 位置 j，因果视图 pj=πθ_old(·|hj)；hindsight 视图 qj=πθ_old(·|hj, Fj, O)，其中 Fj 是已实现未来，O 是 verifier 结果渲染的文本描述。两个视图都由同一个 frozen generating policy 评分，不额外采样。
- token 权重：wj=JSD(pj,qj)/log2，取值 [0,1]；因果与 hindsight 分布差异越大，权重越大。
- 信用：Aj=(Ri−bk)wj，用 PPO clipped surrogate 更新；轨迹内按有效 token 平均，避免长轨迹获得过高整体权重。

关键结果：
- Qwen3-8B 在共享 100 步、4 prompts/step 预算下，HP-RLVR(G=1) 相比 GRPO(G=8) 训练加速：数学 1.21×、代码 1.46×、ALFWorld 2.30×。
- 数学 Avg@12 在 1.7B/4B/8B 三个尺寸 HP-RLVR 均高于 GRPO，8B 为 65.73% vs 63.07%；代码 Pass@1 和 ALFWorld 成功率则 GRPO 更高。
- ALFWorld 零梯度记录：GRPO 4B/8B 为 43.2%/49.0%，HP-RLVR 为 0%；4B GRPO 数学中 47.7% reward group 同质，没有 advantage。

最值得记住的一句话：用已完成轨迹的 future 作为 training-only privilege，将 terminal reward 拆成有符号历史中心奖励 × 归一化 JSD token 权重，实现单 rollout token 信用。
