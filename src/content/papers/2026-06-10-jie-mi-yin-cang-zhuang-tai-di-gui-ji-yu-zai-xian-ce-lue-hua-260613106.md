---
title: 'Demystifying Hidden-State Recurrence: Switchable Latent Reasoning with On-Policy
  Reinforcement Learning'
title_zh: 揭秘隐藏状态递归：基于在线策略强化学习的可切换潜在推理
authors:
- Jiayu Yang
- Chao Chen
- Shengen Wu
- Yinhong Liu
- Yuxuan Fan
- Lujundong Li
- Songning Lai
- Chengwei Qin
- Zhijiang Guo
affiliations:
- HKUST(GZ)
- University of Cambridge
- NTU
- JoinQuant
- HKUST
arxiv_id: '2606.13106'
url: https://arxiv.org/abs/2606.13106
pdf_url: https://arxiv.org/pdf/2606.13106
published: '2026-06-10'
collected: '2026-06-13'
category: Reasoning
direction: LLM推理 · 潜在CoT与强化学习
tags:
- Latent CoT
- GRPO
- Hidden-State Recurrence
- Switchable Reasoning
- Mechanistic Analysis
- RL for LLM
one_liner: 提出Switch，通过<swi>/</swi>边界标记使隐藏状态递归潜在推理兼容GRPO，实现高效、可解释的推理
practical_value: '- 构建电商对话 agent 或推荐解释生成模型时，可引入 **<swi>/</swi> 开关机制**：模型在需要可读性的阶段生成显式文本，而在计算密集或简单步骤自动切换为隐藏状态递归，压缩推理
  token 成本，平衡可解释性与效率。

  - **GRPO 训练潜在推理**的范式可直接迁移到 RL-based 推荐 Agent 优化：将潜在步骤视为隐式“思考”，通过奖励函数（正确性+格式+潜在使用+长度）端到端学习何时压缩推理，实现自适应计算。

  - 论文中的**机械解释性分析工具**（probe、logit lens、因果干预）可用来诊断业务 Agent 中的推理行为：确认模型是否真正在“思考”还是空转，确保潜在步骤携带任务相关信号。

  - **分段梯度反向传播**技巧（按<swi>/</swi>切分 rollout，文本段反向传播，潜在段 no_grad）显著降低 RL 训练内存，对长轨迹强化学习（如多轮对话推荐）的工程实现有直接参考价值。'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
隐藏状态递归（Coconut 式）潜在链式思维让 LLM 在连续隐藏空间进行推理，压缩显式文本，但一直面临两大障碍：① 潜在位置不产生采样分布，标准策略梯度 RL（如 GRPO）无法直接使用；② 潜在计算难以分析，常被质疑是“惰性占位符”。Switch 发现这两个问题的根源是缺少显式边界标记。

### 方法关键点
- **边界标记设计**：新增 `<swi>`（进入潜在）和 `</swi>`（退出）两个普通 token，模型在边界内使用 `<latent>` 执行隐藏状态递归。边界使 GRPO 在文本位置策略比率有定义，也为机制分析提供抓手。
- **三阶段训练**：
  - Phase 1（SFT）：用高熵 CoT 片段标注 `<swi>/</swi>`，教会模型开关位置。
  - Phase 2（潜在课程）：并行逐步用 `<latent>` 替换边界内文本，逼迫模型在潜在空间计算。
  - Phase 3（Switch-GRPO）：在线策略 RL，正确性奖励为主，加入格式/使用/长度奖励，梯度仅流过文本段，潜在段依赖 KV cache 传播。
- **推理机制**：`<latent>` 的输入 embedding 为前一步的 last-layer hidden state，实现递归。引入最小驻留步数 \(K_{\min}\) 防止潜在块过早退出。

### 关键结果
- **MATH-500 准确率 79.3%**，比最强 Coconut 类基线高 25.7 点；GSM8K 达 89.2%。
- **Switch-GRPO 提升显著**：相比纯 SFT 课程，潜在条件准确率提高 12.6 点，潜在调用率从 81% 降至 58%，模型学会有选择地使用潜在推理。
- **机制分析**：① `<swi>` 是高度局部化的学习开关策略（排名≤1.7），非风格标签；② 潜在步骤因果重要，归零 hidden state 使诊断子集准确率从 100% 暴跌至 33%；③ 计算集中于进入潜在块后的**第一个隐藏状态转移**，\(K_{\min}\) 保证其不被跳过。
- 通过调整奖励中的长度惩罚，可实现**可调节的精度‑效率帕累托前沿**，输出长度最多减少 33% 同时保持竞争力。
