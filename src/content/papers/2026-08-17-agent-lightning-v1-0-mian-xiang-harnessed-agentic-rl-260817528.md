---
title: 'Agent Lightning v1.0: Towards Harnessed Agentic RL'
title_zh: Agent Lightning v1.0：面向 Harnessed Agentic RL
authors:
- Zhiyuan He
- Siwei Zhang
- Zhiwen Zhou
- Yuqing Yang
- Yu Kang
- Yuge Zhang
- Luna K. Qiu
- Tin Yan Tsui
- Jiahang Xu
- Chong Luo
affiliations:
- Microsoft
- Fudan University
- Zhejiang University
- University of Edinburgh
arxiv_id: '2608.17528'
url: https://arxiv.org/abs/2608.17528
pdf_url: https://arxiv.org/pdf/2608.17528
published: '2026-08-17'
collected: '2026-08-20'
category: Training
direction: Agentic RL 训练框架与挑战
tags:
- Agentic RL
- RLHF
- Training Framework
- Harnessed RL
- GRPO
- LLM Agents
one_liner: 系统刻画 harnessed agentic RL 的 retokenization、advantage 与 loss 归一化挑战，用 3.5k
  行框架验证 coding agent 提升 14.6%
practical_value: '- 借鉴 proxy 解耦架构：电商导购/客服 Agent 线上 harness 可直接接 RL 训练 LLM 代理，无需改动
  Agent 代码即可采集训练轨迹，显著降低 train-serve skew。

  - 训练样本合并不要依赖文本前缀：必须基于 token 级精确前缀判断合并，否则会引入 off-policy 偏差；资源有限时采用 best-effort merging
  最实用。

  - Advantage 与 loss 应在 rollout 级别计算：当 Agent 内部存在子任务、上下文摘要或 retokenization 导致一个 rollout
  产生多个训练样本时，按 sample 数归一化会引入梯度偏差，建议使用 rollout-level token-mean loss。

  - 工程上可复用 collocated async RL 让推理与训练共享 GPU 池，比同步约快 2x 且省卡；同时用幂等 API + 重复 LLM 请求去重处理网络重试，适合大规模
  rollout 场景。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
现代 Agent 并非裸 LLM，而是运行在管理工具、上下文与控制流的 harness 中。传统 agentic RL 要求训练引擎拥有环境交互循环，难以直接复用部署 harness，导致 train-serve 偏差。近年 proxy-based 方法让 harness 参与 RL 训练，但带来 retokenization、sample merging、advantage、loss normalization、backend scheduling 等新问题，现有框架处理不一，训练可能不稳定。该工作首次系统定义并刻画这一“harnessed agentic RL”范式。

**方法关键点**
- 训练引擎仅观察 LLM 请求-响应对，harness 拥有上下文构建与工具执行；一个 rollout 可能产生多个训练样本。
- retokenization 导致 token 前缀断裂：chat template 非合成、decode-retokenize 漂移、输出转换均会破坏 token 连续性；采用 best-effort merging，仅当 token 级前缀匹配时合并，否则独立序列，保证 on-policy。
- advantage 与 loss 归一化在 rollout 级别计算：避免因样本分裂导致的梯度偏差，选用 rollout-level token-mean loss。
- 系统仅约 3500 行代码，由 API Gateway、Rollout Controller、Customized Trainer 组成；支持 Kubernetes Job 调度、collocated async RL、幂等 API 和重复 LLM 请求去重。
- 针对 coding agent 提供数据清洗（去空问题、缺分支、>200 测试，模型难度过滤）和 reward hacking 防护（禁用 git、网络白名单）。

**关键实验**
- Search agent（Llama-3.2-3B + GRPO）：验证 reward 25.1% → 41.7%（+16.6%）。
- General instruction-following（Qwen3-4B + RLOO）：51.9% → 70.2%（+18.3%）。
- Coding agent（Qwen3.5-9B + SWE-smith 6K 样本）：SWE-bench Verified 41.8% → 56.4%（+14.6%）。消融显示 Rollout-level Advantage + Rollout-level Norm 最优，验证 reward 38.2% vs 35.0% baseline。

**最值得记住的一句话**：在 harnessed agentic RL 中，所有 advantage 与 loss 归一化都应在 rollout 级别完成，否则样本分裂会引入系统性偏差。
