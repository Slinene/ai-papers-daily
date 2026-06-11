---
title: 'Role-Agent: Bootstrapping LLM Agents via Dual-Role Evolution'
title_zh: Role-Agent：让单一 LLM 扮演代理与环境双重角色，自举式协同进化
authors:
- Xucong Wang
- Ziyu Ma
- Shidong Yang
- Tongwen Huang
- Pengkun Wang
- Yong Wang
- Xiangxiang Chu
affiliations:
- University of Science and Technology of China
- AMAP, Alibaba Group
arxiv_id: '2606.10917'
url: https://arxiv.org/abs/2606.10917
pdf_url: https://arxiv.org/pdf/2606.10917
published: '2026-06-09'
collected: '2026-06-11'
category: Agent
direction: LLM Agent 自举式协同进化 · 过程奖励
tags:
- LLM Agent
- Reinforcement Learning
- Self-Evolution
- Dual-Role
- Process Reward
- Failure Mode Retrieval
one_liner: 用一个 LLM 同时做 agent 和环境，通过预测未来状态和分析失败模式实现自举式共进化，平均提升超 4%
practical_value: '- **模拟环境自生成与针对性训练**：在对话推荐、客服 Agent 等场景，可用同一 LLM 根据历史失败交互（如用户不满意的对话）分析失败模式，自动检索并复现类似任务，实现针对性微调，无需人工构造样本。

  - **预测用户状态作为额外奖励信号**：在交互式推荐/搜索中，可在 agent 动作后要求其预测用户/环境下一步状态（如用户下一句话、页面跳转），将预测匹配度作为过程奖励来调制任务奖励，鼓励模型理解动作后果，避免随机成功带来的奖励误导。

  - **双角色复用降低工程复杂度**：无需额外部署专门的环境模拟模型或任务生成器，直接用同一个 LLM 切换角色完成数据增广和训练，适合资源受限或快速迭代的场景。

  - **状态分组优势计算**：借鉴 GiGPO 的状态分组思想，可按相同状态（如用户类似意图）对交互中的动作进行分组归一化优势，减少时序噪声，提升梯度的稳定性，可直接移植到
  PPO/GRPO 训练流程中。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：当前 LLM 代理（Agent）训练受限于静态环境，反馈稀疏且不针对弱点；合成环境虽可自适应但引入额外模型和高昂成本。该文探索能否用一个 LLM 既做代理又做环境，实现自举式协同进化。

**方法**：提出 Role-Agent，包含两个互补组件：
- **World-In-Agent (WIA)**：在每次动作后，要求代理预测未来 H 步状态；用最长匹配子序列（LMS）度量预测与真实状态的差异，将预测奖励乘性调制到任务奖励上（仅对有任务奖励的动作有效），防止“碰巧成功”的行动得到高优势。同时沿用 GiGPO 的状态分组机制，按状态哈希对动作分组计算状态级优势，降低时序冗余。
- **Agent-In-World (AIW)**：对失败轨迹，用同一个 LLM 分析失败模式（类型、根源、核心教训），并生成检索查询；随后在历史失败模式库中检索相似模式的任务，将其重新注入训练数据分布，实现“哪里薄弱练哪里”。该库仅存储少量唯一失败模式，存储和检索成本极低。

**关键实验**：在 ALFWorld（多步家务任务）、WebShop（模拟电商购物）和搜索增强 QA（NQ、HotpotQA 等）上，使用 Qwen2.5-1.5B/7B-Instruct 作为基础模型。Role-Agent 在 ALFWorld 上比 GiGPO 提升 4.2%（90.9% vs 86.7%，1.5B），在 WebShop 上提升 6.9%（71.9% vs 65.0%），在搜索 QA 任务上平均提升 3.7%（45.8 vs 42.1）。消融实验证实两个组件缺一不可，移除 AIW 导致 WebShop 成功率下降 5.0%。额外计算开销仅约 5.2%，且训练-推理 rollout 分布差异显著减小，训练更稳定。

**核心洞察**：单 LLM 的双角色设计能有效利用自身行为反馈，动态调整训练分布，同时通过未来状态预测强化对环境的内部建模，是一种低成本、高收益的代理自我进化范式。
