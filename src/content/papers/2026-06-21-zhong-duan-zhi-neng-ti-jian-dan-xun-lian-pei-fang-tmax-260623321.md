---
title: 'Tmax: A simple recipe for terminal agents'
title_zh: 终端智能体简单训练配方 Tmax
authors:
- Hamish Ivison
- Junjie Oscar Yin
- Rulin Shao
- Teng Xiao
- Nathan Lambert
- Hannaneh Hajishirzi
affiliations:
- Allen Institute for AI
- University of Washington
arxiv_id: '2606.23321'
url: https://arxiv.org/abs/2606.23321
pdf_url: https://arxiv.org/pdf/2606.23321
published: '2026-06-21'
collected: '2026-06-24'
category: Agent
direction: 终端 Agent 强化学习训练配方
tags:
- RL
- terminal agents
- data generation
- open-source
- outcome-only reward
one_liner: 用分类法生成数据 + 仅结果奖励 RL，9B 模型在 Terminal-Bench 2.0 上达 27%，超越更大模型
practical_value: '- **数据生成策略可复用**：通过难度控制、角色多样化和验证器多样化生成大规模合成训练环境，这套方法可直接用于生成推荐系统智能体的指令或交互数据，尤其适合构建面向开发者的推荐工具
  Agent。

  - **仅结果奖励的 RL 简单有效**：在推荐 Agent 的在线学习场景中，无需设计复杂中间奖励，直接使用最终任务成功与否作为信号，降低工程开销，且对超参不敏感。

  - **开源基线可直接加速实验**：Tmax 的数据集（2.5 倍于先前最大公开集）和模型可作为起始点，快速验证终端交互类 Agent 在推荐基础设施运维或自动化部署中的应用。

  - **小模型通过 RL 可超越大模型**：9B 参数模型经过 RL 训练后性能超过 32B 模型，对资源受限的推荐团队有强提示：精调小模型 + 针对性的 RL
  数据可能比盲目上大模型更划算。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：终端智能体日益流行，但学术界缺乏面向 RL 训练的公开方案、足够的数据和简单基线。现有工作多停留在 SFT，RL 探索因基准困难、数据不足而滞后。

**方法**：提出 Tmax 配方。数据生成基于一种新颖分类法，融合**难度控制**（通过配置依赖复杂度）、**多样化角色**（模拟不同用户习惯）和**验证器多样化**（不同判分规则），低成本生成了超大规模终端环境数据集，比此前最大公开集大 2.5 倍。训练时仅使用**结果奖励 RL**（正确/错误），无需过程奖励，配方极简。

**结果**：在 Terminal-Bench 2.0 上，Tmax-9B 得分 **27%**，优于 Nemotron-32B、TerminalTraj-32B 等更大模型，也超越所有以前的公开 RL 配方，在 32B 参数以下模型里占据帕累托前沿。开源数据、模型和代码。
