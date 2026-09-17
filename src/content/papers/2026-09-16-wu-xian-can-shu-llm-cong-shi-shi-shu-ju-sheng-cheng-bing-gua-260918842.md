---
title: 'Infinite-Parameter LLMs: Generating and Adapting Weights from Live Data'
title_zh: 无限参数LLM：从实时数据生成并适应权重
authors:
- Jinli Hu
- Ross M. Clarke
- Yichuan Zhang
- José Miguel Hernández-Lobato
affiliations:
- Boltzbit Limited
- University of Cambridge
arxiv_id: '2609.18842'
url: https://arxiv.org/abs/2609.18842
pdf_url: https://arxiv.org/pdf/2609.18842
published: '2026-09-16'
collected: '2026-09-17'
category: LLM
direction: 超网络生成 LLM 权重 · 在线贝叶斯更新
tags:
- Hypernetwork
- Online Learning
- Bayesian Update
- Weight Generation
- MoE
one_liner: 用超网络从实时交互数据动态生成低秩权重，并以贝叶斯在线更新实现会话内持续适应
practical_value: '- 在长会话 Agent 或客服场景中，将用户实时提供的纠错、偏好、事实等写入模型权重而非每次拼进 prompt，可减少重复 token
  开销、释放上下文窗口，并让知识跨轮次持久化。

  - 借鉴超网络生成低秩调制权重的思想，在推荐系统中用超网络根据用户/物品特征动态生成个性化 adapter 或 FFN 权重，实现参数高效的动态用户建模，避免为每个用户存储大量个性化参数。

  - 采用贝叶斯在线更新 latent code 的方式维护用户或场景的隐状态，使模型行为随交互逐步调整，适合多轮推荐、动态创意生成等需要连续适应的任务。

  - 评估时设计对比 in-context learning 和 retrieval 的协议，重点考察权重化知识是否在计算摊销、泛化、持久性上优于 prompt
  方案，业务上可作为在线学习方案的验证框架。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：部署后的 LLM 面对实时交互中的新知识（用户提供的事实、纠错等）无法更新权重，通常只能将知识放入 prompt，每次请求重复读取并丢弃，造成计算浪费、上下文占用和跨轮次丢失。

**方法关键点**：受 MoE 启发，提出 Infinite-Parameter LLM，用紧凑超网络把运行时数据转化为共享基础网络的低秩调制，使 FFN 权重由实时数据生成而非固定存储。与传统权重生成器只读一次上下文不同，该方法对生成器的 latent code 维持贝叶斯信念并在线更新，有效权重随会话演进。存储占用固定，但可编译的权重空间实际无限。

**关键结果**：将知识写入权重而非 prompt，可摊销计算、释放上下文窗口、跨轮次持久化，并可能比 in-context 使用具有更好泛化。论文制定了评估协议，与 in-context learning 和 retrieval 直接对比；摘要未披露具体实验数值。
