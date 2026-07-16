---
title: 'TRACE: Turn-level Reward Assignment via Credit Estimation for Long-Horizon
  Agents'
title_zh: TRACE：通过冻结参考模型估计步骤信用实现长程 Agent 的稠密奖励
authors:
- Leitian Tao
- Baolin Peng
- Wenlin Yao
- Tao Ge
- Hao Cheng
- Mike Hang Wang
- Jianfeng Gao
- Sharon Li
affiliations:
- University of Wisconsin–Madison
- Microsoft Research
arxiv_id: '2607.13988'
url: https://arxiv.org/abs/2607.13988
pdf_url: https://arxiv.org/pdf/2607.13988
published: '2026-07-15'
collected: '2026-07-16'
category: Agent
direction: Agent 强化学习中的步骤级信用分配
tags:
- credit assignment
- reinforcement learning
- agent
- tool use
- Temporal Difference
- LLM
one_liner: 用冻结参考模型的金标答案对数概率变化作为工具调用步骤的即时信用信号，无需 Critic 或过程标签，显著提升长程 Agent RL 训练效率与效果
practical_value: '- **冻结参考模型作为价值探针**：无需训练额外 Critic 或 PRM，直接用初始化策略作为固定的前缀状态评分器，可稳定地为多轮工具调用提供稠密奖励，适合电商对话
  Agent、搜索 Agent 等需要长程交互的场景。

  - **Log-ratio 状态值设计**：通过计算金标答案对数概率的相对间隙闭合度（而非绝对变化），解决了不同置信度下概率变动尺度不一致的问题，能更准确地衡量中间步骤的进展，该方法可直接用于推荐或广告
  Agent 中关键决策步骤的信用评估。

  - **K-step TD 备份传播延迟信用**：支持将后续观察到的答案可预测性提升追溯到更早的搜索或文档打开动作，这对网页搜索、商品筛选等多步决策链条非常有益，避免只奖励最后一步而忽视前序关键操作。

  - **与结果奖励的混合优化**：将 TD 信用作为辅助信号与 GRPO 的结果优势相加，保持最终正确答案作为训练锚点，既缓解稀疏奖励，又防止局部进度信号主导优化方向，这种架构可复现于搜索推荐等需平衡即时反馈与最终目标的场景。'
score: 9
source: arxiv-cs.LG
depth: full_pdf
---

**动机**  
长程 Agent（如深度搜索、多步工具调用）在强化学习中面临严重的奖励稀疏问题：一个轨迹可能包含几十步动作，但只有最终结果验证提供单一奖励，既无法区分有用动作与冗余动作，也导致训练方差大、收敛慢。现有过程监督方法常需额外训练 Critic 或过程奖励模型，成本高且易漂移。该工作试图利用冻结参考模型，在不增加训练组件的前提下为每个工具调用步骤生成即时信用，使训练更高效。

**方法关键点**  
- **前缀状态定义**：把轨迹按工具调用边界分割为前缀状态 \(S_k\)（包含已执行的动作和观察），作为信用分配的基本单位。
- **Log-ratio 状态值**：用冻结的初始策略作为参考模型，计算前缀条件下金标答案的对数概率 \(\bar{\ell}_k\)，并转换为 \(V(S_k) = \log \frac{-\bar{\ell}_0+\epsilon}{-\bar{\ell}_k+\epsilon}\)，表示从初始到当前答案可预测性的相对提升。
- **TD 步骤奖励**：奖励定义为 \(\delta_k = V(S_{k+1}) - V(S_k)\)，正值表示动作使答案更可预测，零表示无贡献，负值表示导致偏离。
- **K-step 备份**：引入 K-step TD 备份传播延迟信用（\(K=3\)），解决动作效果滞后问题；末尾步骤额外加上带折扣的结果优势锚定，保持最终正确性目标。
- **与 GRPO 混合**：每 token 优势为 \(\alpha_{\text{out}} A_g^{\text{out}} + \alpha_{\text{turn}} r_{g,k}^{\text{turn}}\)，直接将步骤信用叠加到组相对结果优势上，沿用 GRPO 的 clip 更新。

**关键结果**  
在合成多文档搜索任务上训练，在封闭域 BrowseComp-Plus 上评估：
- Qwen3-4B 从基线的 7.2 提高到 35.6（+28.4），Qwen3-30B-A3B 从 8.4 提高到 42.6（+34.2），均远超 GRPO（30.0 / 36.4）。
- 开域迁移上，30B-A3B 在 BrowseComp 达 12.9，GAIA 达 52.0，xbench-DeepSearch 达 45.0，证明训练的策略不是简单记住检索库。
- 学习曲线显示 TRACE 起始提升更早、收敛更快，并能更早鼓励更长的交互轮次。
- 消融实验证实 log-ratio 形式优于原始增量或剩余隙方法；适中的步骤奖励系数和 K 值很重要；参考模型用初始检查点已足够。
