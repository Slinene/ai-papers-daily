---
title: Global Optimization and Inference-Time Region Grafting for Agentic Workflows
title_zh: Agentic工作流的全局优化与推理时区域嫁接
authors:
- Donghyeok Koh
- Gyuwan Kim
- Jinyeong Bak
- Seung-Hoon Na
- Tao Yang
- Haneol Jang
- Cheoneum Park
affiliations:
- HBNU
- UCSB
- SKKU
- UNIST
arxiv_id: '2608.02353'
url: https://arxiv.org/abs/2608.02353
pdf_url: https://arxiv.org/pdf/2608.02353
published: '2026-08-03'
collected: '2026-08-04'
category: Agent
direction: Agentic工作流推理时动态局部优化
tags:
- agentic workflow
- inference-time adaptation
- label-free quality signal
- region grafting
- coupling guard
- training-free
one_liner: 在推理时对离线全局工作流进行局部区域替代，利用无标签质量信号实现单输入自适应，无需重训练
practical_value: '- **推理时动态流水线调优**：在电商/推荐的多阶段流水线（召回→粗排→精排→重排）中，离线搜索一个全局最优的算子组合，然后在每次请求时，利用无人工标注的代理信号（如多路召回结果的一致性、CTR预估的置信度、多样性等）对部分阶段进行局部算子替换，实现
  per-query 自适应，无需重新训练整个流水线。

  - **记忆化缓存获胜配置**：为相似请求特征（如用户意图标签、上下文类型）建立签名，缓存历史上对该签名有效的局部配置，大幅降低线上搜索开销。这类似于推荐系统中为相似用户或
  query 缓存个性化策略。

  - **耦合守卫确保全局稳定性**：当替换某个阶段（如精排模型）时，通过检查替换后输出与上下游的衔接一致性（例如新精排序列与上游召回集合的重叠度）来决定是否接受更改，避免局部优化破坏整体效果，尤其适用于有依赖关系的多步推理或搜索链路。

  - **低成本冷启动与新任务迁移**：当更换更强的基座模型（如从轻量级升级到千亿级大模型）时，无需重新搜索全局工作流，只需复用已有的全局结构并在推理时局部嫁接，即可获得性能提升，适合模型迭代时的快速上线。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**
现有 agentic 工作流优化方法（如 AFlow、MaAS）在离线搜索出固定结构后对所有输入统一使用，无法针对单个输入的难度与失败模式实时调整。MaAS 虽支持采样不同结构，但依赖离线学习的超网分布，无法在推理时根据实际执行质量信号进行适应。本文旨在实现一种推理时自适应机制，在不重新优化整个工作流的情况下，仅对局部区域进行替换，以适应每个输入。

**方法关键点**
- **全局工作流作为结构性先验**：离线阶段通过角色限定搜索（role-scoped search）得到一个任务级最优全局工作流 \(\mathcal{W}_{c^*}\)，将其分解为若干单入口单出口（SESE）区域，每个区域仅绑定特定角色（规划、证据、推理、验证、格式等）的算子。
- **局部区域嫁接（Region Grafting）**：推理时，对每个输入，提议器（proposer）基于 UCB 优先级选出需优化的区域；在角色限定的局部候选集内搜索替换算子，使用无标签代理信号（自一致性答案对齐度、证据支撑度、代码测试通过率等）评估候选质量，阈值过滤后仅接受能提升局部质量且通过耦合守卫（区域间一致性不下降超过 \(\epsilon\)）的替换。
- **耦合守卫与状态传播**：通过测量替换后输出对上游证据的支撑比例，确保局部修改不会破坏跨区域信息流；当下游区域因上游变化而标记为陈旧时，会在下一轮次重新评估。
- **记忆化重用**：将输入签名与获胜配置存入缓存，后续相似输入直接复用，摊销搜索成本，减少推理延迟。

**关键实验结果**
在 MaAS 评测体系（gpt-4o-mini 执行器）下，GRAFT 在 GSM8K（95.04）、MATH（62.89）、MultiArith（97.90）、HumanEval（94.66）、MBPP（86.70）上平均得分 87.44，比 MaAS 提升 3.85，比 AFlow 提升 5.19。在 BayesFlow 体系（Claude Sonnet）下，覆盖 HotpotQA、DROP、MMLU-Pro、GPQA 等任务，平均得分 84.1，持续最优。消融实验表明去除局部嫁接导致平均下降 4.10 分，无标签代理信号被随机噪声替换后下降 3.48 分。在数学类任务上代理信号与答案正确性的 Spearman 相关达 0.35~0.62，QA 类任务则低至 0.04~0.17。记忆重用率在 GSM8K 和 MATH 上高达 0.86~0.92，显著降低搜索开销。

**值得记住的一句话**：GRAFT 表明，优化后的工作流不应是静态的离线产物，而是一种可在推理时根据无标签反馈与更强执行器持续进化的执行策略。
