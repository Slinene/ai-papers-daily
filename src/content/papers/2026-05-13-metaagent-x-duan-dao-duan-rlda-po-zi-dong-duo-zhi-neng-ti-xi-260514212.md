---
title: 'MetaAgent-X : Breaking the Ceiling of Automatic Multi-Agent Systems via End-to-End
  Reinforcement Learning'
title_zh: MetaAgent-X：端到端RL打破自动多智能体系统的天花板
authors:
- Yaolun Zhang
- Yujie Zhao
- Nan Wang
- Yiran Wu
- Jiayu Chang
- Yizhao Chen
- Qingyun Wu
- Jishen Zhao
- Huazheng Wang
affiliations:
- Oregon State University
- UCSD
- Amazon AGI
- Pennsylvania State University
- AG2AI, Inc.
arxiv_id: '2605.14212'
url: https://arxiv.org/abs/2605.14212
pdf_url: https://arxiv.org/pdf/2605.14212
published: '2026-05-13'
collected: '2026-05-19'
category: MultiAgent
direction: 自动多智能体系统的端到端联合训练
tags:
- End-to-end RL
- Multi-agent systems
- GRPO
- Hierarchical rollout
- Stagewise co-evolution
- Meta-agent
one_liner: 提出首个端到端RL框架，联合优化MAS的设计与执行，通过分层Rollout与阶段式共进化获得最高21.7%提升。
practical_value: '- **层次化信用分配**：将MAS设计质量与执行能力分开评估，设计奖励用多次执行均值，执行奖励在问题级归一化。复杂Agent链路（如推荐生成→验证→融合）可借鉴此解耦训练。

  - **阶段式交替训练**：交替更新设计者和执行者（例如每30步切换），避免非平稳环境导致的训练崩塌。在电商多Agent编排时，可先用固定执行器训练编排，再反过来微调执行器，形成稳定的共进化闭环。

  - **脚本化MAS生成**：让设计者输出可执行的Python脚本来实例化Agent工作流，便于在业务中快速构造和复用不同Agent拓扑。

  - **共享策略优于分离策略**：实验表明共用骨干的设计者与执行者比分离参数更有效，在资源受限时可直接用一种模型承担多种角色，简化部署。'
score: 10
source: huggingface-daily
depth: full_pdf
---

**动机**：现有自动MAS要么只在测试时搜索固定执行器下的工作流，要么仅优化顶层设计器而冻结执行器，导致性能天花板。端到端同时优化设计与执行可让两者相互促进，但需要解决信用分配和训练非平稳性。

**方法关键点**：
- **MetaAgent-X框架**：设计器生成任务特定的多智能体系统（输出Python脚本指定角色、交互、工具），执行器在环境中运行该系统，收集轨迹和结局奖励，用GRPO更新。
- **Executor-Designer分层Rollout**：每个问题生成M个候选设计，每个设计执行N次，形成M×N rollouts。设计器优势用M个设计的平均奖励归一化，执行器优势用问题内所有执行轨迹奖励归一化，平滑随机性，分离信用。
- **阶段式共进化**：训练交替以“执行阶段”和“设计阶段”进行（每30步切换），只更新活跃角色梯度，减少双方互为环境导致的非平稳冲突。
- **冷启动**：用DeepSeek-V3.2蒸馏生成3K设计样本+8K执行样本做SFT，再进入RL训练。训练数据混合数学和编码，GRPO batch size=8。

**关键实验**：在Qwen3-4B/8B上评估，使用AIME24/25、OlympiadBench、APPS、LiveCodeBench、CodeContests六个基准。MetaAgent-X RL相比单智能体GRPO在8B上平均提升+11.17%，超越现有自动MAS基线（如MaAS +6.11%）。消融实验确认分层Rollout（M=4,N=4优于M=8,N=1）和阶段式训练（比耦合训练/角色单独训练更稳定、最终分更高）的关键作用；共享策略优于分离策略。分析显示RL使设计者结构选择更合理（难题多用Reflection，简题用Single），同时执行能力也提升，55%的提升来自执行侧，45%来自设计者切换更优拓扑。
