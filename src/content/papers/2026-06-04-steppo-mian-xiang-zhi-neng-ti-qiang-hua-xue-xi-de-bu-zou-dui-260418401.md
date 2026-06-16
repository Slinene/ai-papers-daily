---
title: 'StepPO: Step-Aligned Policy Optimization for Agentic Reinforcement Learning'
title_zh: StepPO：面向智能体强化学习的步骤对齐策略优化
authors:
- Daoyu Wang
- Qingchuan Li
- Mingyue Cheng
- Jie Ouyang
- Shuo Yu
- Qi Liu
- Enhong Chen
affiliations:
- University of Science and Technology of China
arxiv_id: '2604.18401'
url: https://arxiv.org/abs/2604.18401
pdf_url: https://arxiv.org/pdf/2604.18401
published: '2026-06-04'
collected: '2026-06-16'
category: Agent
direction: 智能体强化学习 · 步骤级策略优化
tags:
- Step-Level MDP
- Credit Assignment
- Agentic RL
- PPO
- LLM Agents
- Multi-turn Interaction
one_liner: 将智能体RL从令牌级MDP重构为步骤级MDP，通过步骤级信用分配和重要性采样，显著提升多步交互任务性能。
practical_value: '- **步骤级信用分配适用于多步交互场景**：在电商搜索、多轮对话推荐等需长链路决策的任务中，将信用分配到具体交互步骤（如搜索、点击、信息获取）比平铺到所有token更能识别关键动作，可直接借鉴步骤级GAE取代令牌级或轨迹级优势估计。

  - **步骤级重要性采样稳定多token动作更新**：当智能体每步生成多个token时，采用几何平均重要性比率可避免长动作的极端梯度，适合业务中工具调用、长文本生成等场景，直接应用于PPO更新。

  - **工程上采用步骤原生轨迹表示**：训练框架以步骤为单元存储状态、动作、奖励，实现更紧凑的上下文管理与前缀复用，能降低多步交互的推理与训练成本，适合生产环境异步训练与混合智能体管理。

  - **对架构与数据管线的启示**：通过网关+数据池解耦智能体与训练系统，支持异构智能体（规则、黑盒、白盒）异步贡献轨迹数据，可迁移至多来源推荐/客服智能体的持续优化。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
现有LLM智能体强化学习沿用RLHF/RLVR中的令牌级MDP，以token为优化单位，而智能体实际通过完整步骤（观察→生成动作→环境反馈）与环境交互，造成建模粒度与决策粒度的错配。这种错配导致令牌级信用分配过于局部，轨迹级又过于粗糙，不利于多轮长程任务中识别关键中间决策。  
**方法关键点**  
- **步骤级MDP重构**：将智能体执行建模为步骤级马尔可夫决策过程，状态为当前交互历史，动作为完整环境响应（含推理与工具调用），奖励和观测按步骤聚合。  
- **步骤级信用分配**：在步骤边界估计状态价值，用GAE沿步骤时间轴传播奖励，得到步骤级优势，再广播给该步内所有有效token，使信用信号与决策边界对齐。  
- **步骤级重要性采样**：以几何平均聚合步内各token的重要性比率，避免因动作长度差异导致策略比例剧烈波动，提升长步更新的稳定性。  
- **系统支撑**：设计步骤原生的轨迹表示、前缀树复用降低计算开销、异步训练架构及网关+数据池的数据管理，为步骤级优化提供工程可行路径。  
**关键结果**  
在HotpotQA、RealResearchQuery、ALFWorld、WebShop四个智能体场景中，StepPO（基于Qwen3-1.7B/4B）均优于PPO、GRPO、GiGPO等基线。例如Qwen3-4B版本在HotpotQA准确率达63.78%（GRPO 56.61%），WebShop任务得分77.52。消融显示移除步骤级GAE或步骤级重要性采样均导致性能下降，步骤级GAE在低γ时对奖励信号衰减更鲁棒。训练曲线表明StepPO获得更高回报且价值估计更准确，长程任务中额外步数更少。结果表明步骤对齐能稳定提升多步交互任务的决策质量。  
**最值得记住的一句话**  
“智能体以步骤为决策单位，优化也应落回到步骤——StepPO通过步骤级MDP、信用分配与重要性采样，让RL真正对齐交互粒度。”
