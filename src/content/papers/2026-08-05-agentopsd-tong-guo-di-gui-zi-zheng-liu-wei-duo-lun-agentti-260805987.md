---
title: 'AgentOPSD: Recursive Self-Distillation for Agentic Reinforcement Learning'
title_zh: AgentOPSD：通过递归自蒸馏为多轮Agent提供回合级信用分配
authors:
- Zi-Han Wang
- Zhengxi Lu
- Zhiyuan Yao
- Jinyang Wu
- Jie Wu
- Zhengzhou Cai
- Yueqing Sun
- Ziang Ye
- Linji Hao
- Qi Gu
affiliations:
- 清华大学
- 浙江大学
- 美团
arxiv_id: '2608.05987'
url: https://arxiv.org/abs/2608.05987
pdf_url: https://arxiv.org/pdf/2608.05987
published: '2026-08-05'
collected: '2026-08-07'
category: Agent
direction: Agent 多轮交互的回合级信用分配
tags:
- Credit Assignment
- Agentic RL
- Self-Distillation
- Bayesian Belief Update
- Turn-Level
- GRPO
one_liner: 将自蒸馏的token级log概率差聚合成信念状态，通过贝叶斯递归更新定位关键回合，重塑轨迹级优势函数
practical_value: '- **Agent RL 训练的信用分配**：电商/搜索 Agent 的任务往往多轮交互（多步检索、筛选、比较），轨迹级奖励广播会模糊关键动作。AgentOPSD
  的递归信念更新提供了一种轻量替代方案：无需训练额外 critic，仅通过自蒸馏的 token 级 log 概率差来估计每个动作对最终结果的贡献，可迁移到商品搜索
  Agent 或对话式推荐 Agent 的强化学习微调中。

  - **自蒸馏信号的利用方式**：论文演示了如何将自蒸馏的 log 概率差转化为“证据”，并用于贝叶斯更新而非直接作为损失或缩放因子。在电商 Agent 中，业务特征（如用户停留、点击等）常作为特权信息仅在训练时可用，可仿照此思路构建
  teacher 分支，生成回合级证据并根据信念变化幅度动态调整优势权重，提升样本效率。

  - **多轮对话/交互的鲁棒性**：AgentOPSD 在长 horizon 任务上优势显著，且超参数不敏感（λ 除外）。对于广告多轮出价或多步推荐场景，该方法的衰减累积机制和基于信念状态饱和度的自适应门控（B(1−B)）同样适用，可避免早期冗余动作的噪声干扰，同时稳定训练。

  - **工程实现友好**：仅需一次额外 teacher 前向传播，无额外 rollout 或 critic 网络，可直接嵌入 GRPO 训练循环。对于已有 GRPO
  流程的团队，迁移成本低；且开箱即用的超参数（λ=0.5, γ=0.95）提供了直接参考。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：多轮 Agent 强化学习常只有轨迹级稀疏奖励（成功/失败），GRPO 等算法将相同的优势广播到所有 token，无法区分关键决策与无关动作。自蒸馏方法虽提供 token 级密集信号，但未考虑回合间历史依赖，且 token 与动作边界不对齐。需要一种能结合历史、在环境对齐的回合边界分配信用的方法。

**方法关键点**：
- **回合级证据聚合**：将 teacher（注入训练特权技能的 self-teacher）与 student 的 token 级 log 概率差求和，得到回合级证据 $e_k$，近似成功/失败的贝叶斯因子。
- **递归信念更新**：从组内成功率 $\bar{R}$ 初始化信念 $B_0$，在 log-odds 空间累积折扣证据 $c_k = \gamma c_{k-1} + e_k$，计算当前信念 $B_k = \sigma(\ell_k)$。每个回合的信用定义为信念修正量 $\Delta B_k = B_k - B_{k-1}$，并用 $B_{k-1}(1-B_{k-1})$ 自适应压制饱和区的影响。
- **信测对齐与重塑**：将 $\Delta B_k$ 乘以轨迹级优势的符号得到 $q_k$，在轨迹内标准化后剪切至 $[1-b, 1+b]$，作为乘数 $w_k$ 以 $\lambda$ 权重融合原始优势，得到回合级优势 $\tilde{A}_k$。全程无额外 rollout 或 critic。

**关键结果**：
- 在 ALFWorld、WebShop、Search-QA 三个环境及 Qwen2.5-3B/7B 上，AgentOPSD 超越 GRPO 及 SDAR、RLSD 等自蒸馏基线。Qwen2.5-7B 在 ALFWorld 达到 89.1% 成功率。
- 消融显示：去掉回合聚合用 token 级累积降至 85.9%，用原始局部 gap 替代递归修正降至 82.8%，去掉符号对齐降至 80.5%，移除经验先验 $B_0$ 降至 78.9%，验证了各组件贡献。
- 长 horizon 稳健性：任务所需回合数增加时，AgentOPSD 性能下降最平缓（每额外回合仅损失 0.54 成功点），远低于 GRPO 的 2.91 和 RLSD 的 3.59。

**一句话**：回合级信用应取决于动作对累积成功信念的修正幅度，而非孤立的局部信号。
