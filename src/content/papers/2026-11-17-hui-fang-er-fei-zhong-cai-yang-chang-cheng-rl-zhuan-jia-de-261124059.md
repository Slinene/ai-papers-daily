---
title: 'Replay, Don''t Resample: Off-Policy Consolidation of Long-Horizon RL Experts'
title_zh: 回放而非重采样：长程 RL 专家的离线策略合并
authors:
- Zhenrui Yue
- Gongxiaohui Chen
- Huimin Zeng
- Honglei Zhuang
- Jiashuo Sun
- Zhen Han
- Dong Wang
affiliations:
- University of Illinois Urbana-Champaign
- ANL
- Independent Researcher
- Amazon
arxiv_id: '2611.24059'
url: https://arxiv.org/abs/2611.24059
pdf_url: https://arxiv.org/pdf/2611.24059
published: '2026-11-17'
collected: '2026-11-20'
category: Agent
direction: 多专家 RL 合并 · 离线回放蒸馏
tags:
- Reinforcement Learning
- Policy Distillation
- Off-Policy
- Multi-Expert Consolidation
- LLM Agents
- Training Efficiency
one_liner: 复用专家 RL 训练日志按原始顺序回放，结合策略梯度与最终专家 KL 蒸馏，低成本合并多领域专家
practical_value: '- 保存每个领域专家 RL 训练时的完整日志：prompts、rollouts、采样 log-probs、rewards，并保持
  step 顺序。后续合并多专家模型时，直接回放这些日志，不重新采样、不调用环境，可将合并成本降至专家训练计算量的约 1/7。

  - 回放时严格按专家训练的 step 顺序聚合各域 batch，不要 shuffle。实验表明 shuffle 会导致性能显著下降（尤其无 KL 项时），顺序比数据量或
  reward 更重要，因为顺序保持了 quasi-on-policy，clip 比例仅 4%。

  - 蒸馏信号优先用最终专家分布的全词表 top-k 闭式 KL（k=256，β=1），而不是只对日志 token 的 sampled-token 估计。dense
  KL 收敛更快、clip 更少、整体高 0.4-0.5 分；forward/reverse KL 选择只在搭配 PG 项时有差异，默认 reverse KL。

  - 在业务中若需将多个搜索/推荐/查询改写 agent 合并成一个统一模型，可复用此方法：只需专家前向一次获得 top-k 分布，无需环境交互，每步耗时从 350s
  降至 110s（576 样本/步时仅 44s），适合快速迭代和降本。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
前沿 post-training 常按领域训练多个 RL 专家，再用多教师在线蒸馏（MOPD）合并。MOPD 需要学生重新在环境中采样、专家逐 token 打分，成本高，且学生只锚定最终专家，会继承最终专家的分布漂移。实际上，专家 RL 训练的日志已包含合并所需的一切：带采样概率和奖励的 rollout，且按学习顺序组织。然而直接回放面临 off-policy、无新鲜采样下的信号可靠性、日志顺序是否可 pool 三个挑战。

**方法关键点**  
- MRPD 将专家日志视为课程而非数据集：学生从与专家相同的初始化出发，按 step k 回放各域专家第 k 步的 batch，共 300 步。  
- 每个 token 位置损失由两部分构成：基于日志轨迹和 reward 重新计算的 GRPO 风格策略梯度（优势为 group-normalized reward，重要性比率以 logging policy 为分母）；以及对最终专家分布的 KL 蒸馏（默认 dense top-k reverse KL，k=256，β=1），在日志的每个 prefix 上计算。  
- 完全不采样、不调用环境或奖励模型，只需专家做一次前向得到 top-k 分布。由于学生沿专家训练轨迹前进，训练-推理 mismatch 保持在 clip 范围内，clip 比例最多 4%，属于 quasi-on-policy。

**关键结果**  
在推理（ReTool 数学）、搜索（Search-R1）和 SQL（Spider/BIRD）三个长程 agent 域上，基于 Qwen3-4B，MRPD 总体平均 58.6，超过 MOPD（58.1/58.2）和在线 RL（GRPO 52.5、PPO 52.6），仅比 GRPO 专家低 0.7。300 步训练仅需 9.2 小时，约为专家训练计算量的 1/7，是 MOPD 成本的 1/3；数据匹配版本仅 3.7 小时。消融显示：重放轨迹本身已带来大部分收益；PG 和 KL 两项均有贡献；dense KL 优于 sampled-token KL；**日志顺序比数据量或奖励更重要，shuffle 导致一致下降。**

**最值得记住的一句话：专家训练日志是课程，不是数据混合。**
