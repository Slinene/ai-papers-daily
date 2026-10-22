---
title: Memory-Centric Continual Learning for AI Agents
title_zh: 面向 AI Agent 的记忆中心持续学习
authors:
- Dongfang Li
- Zhuoen Chen
- Bonian Jia
- Zixuan Liu
- Zhengxuan Lu
- Can Deng
- Yukun Shi
- Yuhang Meng
- Xin Zhang
- Jiahe Huang
arxiv_id: '2610.29357'
url: https://arxiv.org/abs/2610.29357
pdf_url: https://arxiv.org/pdf/2610.29357
published: '2026-10-20'
collected: '2026-10-22'
category: Agent
direction: Agent 记忆与持续学习
tags:
- Continual Learning
- Memory
- AI Agents
- Evaluation Protocol
- Scaling Laws
one_liner: 提出以记忆是否改进未来行动为核心的三轴分类、双循环生命周期与评测协议
practical_value: '- 将记忆系统从“能检索到什么”转向“是否改善下游动作”，在推荐/广告 Agent 中可定义以最终转化/点击增益为记忆更新信号，而非仅记录历史会话

  - 采用双循环生命周期：内层快速更新交互记忆（如用户偏好、上下文），外层以任务反馈（如 session 成功率）调整记忆写入、淘汰、检索策略，可类比在线学习中的
  meta-policy

  - 借鉴三轴分类（substrate/ asset/ policy）对现有 RAG、向量库、参数微调等记忆方案做架构审计，明确不同记忆的存储位置、资产形态与管理策略，避免混用

  - 资源分配框架可用于决定非参数记忆（向量库）与参数记忆（LoRA 模块）的容量与读取预算配比：当总预算增长时，按最优路径扩增容量与读取资源，而非盲目加大 retrieval
  top-k 或模型参数'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有 AI Agent 依赖固定权重与有限上下文，外部记忆系统大多只是被动检索缓存，评估只看能否回忆事实，无法判断是否真正带来持续学习。

**方法**：提出以记忆是否改善未来行动为判据的 MCCL 框架，包含三部分：三轴分类法（substrates/ assets/ policies），定义内外双循环生命周期——内循环更新记忆状态，外循环基于任务反馈优化管理策略；评测协议从 retention under interference、adaptation to change、task transfer 三个维度隔离行为增益；记忆 scaling 框架建模非参数与参数记忆在经验、存储、计算预算下的性能增长与最优资源分配。

**结果**：给出资源受限下的最优分配路径与参数记忆容量、经验量对 excess loss 的影响，为自改进 Agent 提供原则性路线。
