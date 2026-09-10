---
title: 'TRACE: Training Reasoning Agents for Causal Exploration with Synthesized Rewards'
title_zh: TRACE：用合成奖励训练因果探索推理智能体
authors:
- Rui Sun
- Zhan Shi
- Bing He
affiliations:
- Independent Researchers
arxiv_id: '2609.10315'
url: https://arxiv.org/abs/2609.10315
pdf_url: https://arxiv.org/pdf/2609.10315
published: '2026-09-09'
collected: '2026-09-10'
category: Training
direction: Agent 诊断推理 + 合成奖励 RL
tags:
- RLVR
- synthetic rewards
- tool-use agents
- diagnostic reasoning
- GRPO
- digital advertising
one_liner: simulator-oracle-RL 把隐藏干预变客观奖励，训练广告诊断 Agent，35B FullAttr@1 达 0.757，超前沿闭源基线
practical_value: '- 在电商/广告诊断场景，可复用 simulator-oracle-RL：先往离线广告数据或 sandbox 注入已知根因（如
  BUDGET_CAP、COMPETITIVE_PRESSURE、CREATIVE_FATIGUE），再生成指标观测；隐藏干预直接作为 RL reward，省去人工归因标注和
  LLM-as-judge。

  - 归因任务奖励设计值得抄：用 cause correctness 作为门控，driver slice 用 Jaccard 给部分分，再加 binary full-attribution
  reward；full-attribution 项对多维 audience/placement 切片很关键，2D slice 从 0.00 提升到 0.27，1D
  从 0.67 到 0.92。

  - SFT warm start 价值明显：先用 oracle-filtered 教师轨迹做 SFT，能让 decision-parse rate 从 0.53
  到 1.00，工具调用从 22.05 降到 10.75；后续 RL 只需少量额外工具调用就获得 12 个点 FullAttr@1 提升。

  - 可以做一个 oracle verifier，只读 agent 可见数据，检查信号可检测性、信噪比和 confounder 可区分性，过滤掉不可解或太简单的
  episode；这种 generation/acceptance 分离适合构造可扩展训练集。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**  
RLVR 在数学、代码上有效，因为答案可廉价验证；但复杂数据诊断（如广告指标异常归因）真因难标注、事后也可能模糊，LLM-as-judge 还会引入 reward hacking。本文问：能否用可控模拟器把验证不对称性“造”出来——先采样干预、注入模拟器、生成观测，再用隐藏干预作为 oracle label，从而得到客观、可扩展的奖励信号。

**方法关键点**  
- 提出 TRACE：数字广告诊断环境，12 类根因，分 campaign-wide / segment-mix / segment-specific / no-signal 四组；异常信号可从 impression volume、segment mix、per-segment rates 三条通道注入。  
- 每 episode 由 hidden cause、driver slice、signal strength、onset profile 生成；oracle verifier 只读 agent 可见数据，检查信号可检测、SNR ≥ 1、可区分 confounders 与竞争 cause，保证 episode solvable 但 non-trivial。  
- Agent 通过 Python + SQL 查询多表 fact tables，最终输出 root cause + affected segment slice；segment-specific 维度可为 1D 或 2D 交集。  
- 训练用 Qwen3.5-35B-A3B：SFT 先学 1200 条 oracle-filtered 教师轨迹；RL 用 GRPO，reward = 0.65 graded attribution + 0.30 full attribution + 0.05 format；graded slice = 0.5 + 0.5 × Jaccard，full attribution 要求 cause 正确且 slice 完全匹配。

**关键实验与数字**  
Held-out 235 episode，其中 164 个需要 driver slice，49 个 2D slice。Claude Opus 5 FullAttr@1 为 0.686；Qwen3.5-35B base 0.159，SFT 0.637，SFT→RL 0.757，超过所有 prompted baselines，并显著高于 prompted 122B 的 0.283。Full-attribution reward 对难例关键：1D slice 0.67→0.92，2D slice 0.00→0.27。SFT 使工具调用从 22.05 降到 10.75，SFT→RL 仅增至 11.73。代价是 no-signal accuracy 从 0.76 降到 0.49。

**最值得记住的一句话**  
当领域存在可控生成模型时，制造难题的干预本身就能提供验证器；对这类诊断任务，可扩展的客观训练信号比模型规模更关键。
