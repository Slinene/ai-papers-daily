---
title: How Does Reasoning Flow? Tracing Attention-Induced Information Flow for Targeted
  RL in LLMs
title_zh: 信息流推理：用注意力图追溯回答导向的推理骨干，实现精准token级信用分配
authors:
- Zhichen Dong
- Yang Li
- Yuhan Sun
- Weixun Wang
- Yijia Luo
- Zinian Peng
- Taiheng Ye
- Chao Yang
- Wenbo Su
- Yu Cheng
affiliations:
- Shanghai Jiao Tong University
- Alibaba Group
- Shanghai Artificial Intelligence Laboratory
arxiv_id: '2606.10646'
url: https://arxiv.org/abs/2606.10646
pdf_url: https://arxiv.org/pdf/2606.10646
published: '2026-06-09'
collected: '2026-06-10'
category: Training
direction: 推理信息流引导的token级RL信用分配
tags:
- RL
- Credit_Assignment
- Attention
- Reasoning
- Information_Flow
- LLM
one_liner: 将LLM推理过程建模为注意力引导的有向无环图，通过回答条件化的流守恒变换识别关键推理骨干token，用于强化学习的细粒度信用分配
practical_value: '- 利用内部注意力图构建回答导向的信息流骨干，对token进行重要度排序，可借鉴到对话生成、Agent轨迹的细粒度信用分配，强化关键决策步骤而抑制无关填充。

  - Doob‑h变换实现流守恒，保证中间节点不因路径长度而稀释或膨胀影响力，该归一化思想可直接移植到其他基于图的影响力传播任务（如推荐中的用户行为传导、物品关联）。

  - 固定top‑40%高流量token进行GRPO loss重加权，超参简单且表现稳定，工程上仅需一次额外前向传播（2‑4%时间开销），适合在线RL训练环境。

  - 中间层注意力包含最丰富的推理结构，避免使用全部层导致信号稀释，这对注意力分析的应用（如可解释性、模型诊断）提供了实用的层选择经验。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：强化学习训练LLM时，token级信用分配是核心难题。传统方法均匀奖励所有token，无法区分关键推理步骤与日常填充，导致学习信号噪声大。现有启发式（熵、注意力分数等）仅考虑点式特征，忽略全局信息传播结构。因此，需要从模型内部注意力图中提取回答导向的多跳推理骨干，以实现更精准的信用分配。

**方法**：FlowTracer框架将生成过程建模为注意力诱导的有向无环图（DAG），节点为token，边权重为聚合注意力值。为解决原始注意力图不满足流量守恒且包含大量与答案无关的路径，引入Doob‑h变换：定义回答终点为汇点，计算每个token到答案的全局可达性潜力h，然后用Wik·h(k)/h(i)重加权边，保证中间节点出流和为1，且只保留能抵达答案的影响。从问题token注入单位流，在前向传播后得到每个token的吞吐量f(k)，高吞吐量token（如标点、重复变量）构成推理骨干。将此骨干作为信用分配依据，选择top‑40%高流量token，在GRPO损失中将其γ因子设为1.5，其余token为1，从而实现非均匀策略更新。

**关键结果**：在Qwen3‑4B/8B和Llama‑3.1/3.2上，多个数学推理基准（AIME24/25、AMC23、MATH500、Olympiad）以及Countdown、CrossThinkQA任务中，FlowTracer一致超越GRPO和其他启发式信用分配方法。例如Qwen3‑8B平均准确率从39.4%提升至43.4%，长上下文（8K）场景下优势更明显（+3.8%），单次额外前向传播的开销仅2‑4%。消融实验证实，top‑40%高流量token的选择、中间层注意力以及1.5的强调因子可获得最佳效果，且结构化分隔符（标点、换行）是提升的主要来源。
