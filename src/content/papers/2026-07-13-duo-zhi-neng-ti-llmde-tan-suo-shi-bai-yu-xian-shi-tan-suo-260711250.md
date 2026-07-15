---
title: Multi-Agent LLMs Fail to Explore Each Other
title_zh: 多智能体LLM的探索失败与显式探索框架MACE
authors:
- Hyeong Kyu Choi
- Jiatong Li
- Wendi Li
- Xin Eric Wang
- Sharon Li
affiliations:
- University of Wisconsin–Madison
- University of California, Santa Barbara
arxiv_id: '2607.11250'
url: https://arxiv.org/abs/2607.11250
pdf_url: https://arxiv.org/pdf/2607.11250
published: '2026-07-13'
collected: '2026-07-15'
category: MultiAgent
direction: 多智体协作中显式探索方法
tags:
- Multi-Agent
- Exploration
- Contextual Bandit
- LLM Agents
- Peer Selection
- Regret
one_liner: 发现LLM agent在多智能体环境中普遍探索不足，提出MACE通过上下文赌博机显式引导探索，显著提升协作质量
practical_value: '- 在多智能体协作场景（如多agent推荐、多agent竞价）中，LLM原生缺乏有效探索，容易过早锁定次优agent。可借鉴MACE的LinUCB框架，将agent选择建模为上下文赌博机，通过显式不确定性奖励驱动探索，避免in-context
  selection的过早收敛。

  - 特征工程上，可设计关系特征：agent响应与当前答案的差异（信息增益潜力）、agent之间的差异性、历史准确率、交互轮次。这些特征能编码协作的结构化信息，比单纯的计数或成功率更有效。

  - 在线学习时，使用LinUCB维持设计矩阵A和奖励向量b，利用公式(4)选择agent，实时更新(5)。该方法轻量，无需复杂协调协议，适合工程化。

  - 理论表明，agent能力异质性越大，探索收益越高。当agent池存在显著能力差异（如不同模型、不同专家）时，应加大探索系数。对于能力相近的agent，探索价值有限，可适当降低探索。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
现代LLM智能体在多智能体系统中常需自主选择合作者以完成复杂任务，但其先天探索能力不足。论文首先通过一个简单的两臂赌博机实验证明：即使GPT-4、GPT-5也表现出过早锁定某一peer并拒绝探索的倾向，导致高遗憾。在真实的异质多智能体环境中，这种缺陷会更严重，因为agent能力或上下文不同且不可直接观测。然而，有效探索是多智能体可靠自主性的基础。

**方法关键点**  
- 将多智能体探索问题形式化为部分可观测随机博弈（POSG），提出Multi-Agent Contextual Exploration (MACE) 框架。  
- MACE将联合问题分解为每个agent独立的上下文多臂赌博机，用LinUCB选择交互对象。  
- 设计结构化关系特征：响应多样性（peer回答与当前agent的差异）、Peer差异性（与其他agent的差异）、历史表现（成功率）、交互轮次。这些特征编码了交互的非平稳性与关系结构。  
- 采用乐观探索原则，根据公式 $a_{i,t} = \arg\max_a [ \hat{\theta}_{i,a}^\top x_{i,a,t} + \alpha \sqrt{x_{i,a,t}^\top A_{i,a}^{-1} x_{i,a,t}} ]$ 选择peer，最后用得到的奖励更新设计矩阵和权重。  

**关键实验**  
在两个异构设定下测评：上下文多样性（HotpotQA，10个agent各持部分证据）与参数多样性（Math500、GPQA，4个不同模型）。对比In-Context Exploration、Random、Pre-defined baseline。  
- In-Context Exploration经常比随机更差，agents锁定特定peer，不随任务变化。  
- MACE在试验阶段和后续纯利用阶段均显著降低累积遗憾，且学到的策略可迁移至未见过的2WikiMultiHopQA。  
- 理论证明MACE的遗憾为 $\mathcal{O}(\sqrt{T\log T})$，非探索策略遗憾为 $\Omega(\delta T)$，探索收益随agent能力多样性 $\delta$ 增大而增大。
