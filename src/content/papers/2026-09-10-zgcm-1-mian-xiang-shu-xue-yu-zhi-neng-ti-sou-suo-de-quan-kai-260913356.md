---
title: 'ZGCM-1: A Fully Open and Extremely Efficient Foundation Model for Math and
  Agentic Search'
title_zh: ZGCM-1：面向数学与智能体搜索的全开源高效基础模型
authors:
- Jiyan He
- Guang Liang
- Hao Liu
- Haoxiang Guan
- Jinbo Sun
- Junyi Guo
- Wenjun Feng
- Yantai Xie
- Yifei Shen
- Bin Shao
affiliations:
- Zhongguancun Academy
- Zhongguancun Institute of Artificial Intelligence
arxiv_id: '2609.13356'
url: https://arxiv.org/abs/2609.13356
pdf_url: https://arxiv.org/pdf/2609.13356
published: '2026-09-10'
collected: '2026-09-15'
category: Training
direction: 高效训练 · Agentic Search
tags:
- efficient training
- hybrid attention
- FP8
- Muon
- MDP mid-training
- agentic search
one_liner: 全开源 7B 模型，靠混合注意力、FP8/Muon 与 MDP 中训，在数学和 Agentic Search 上逼近大模型
practical_value: '- 混合注意力 5:1 SWA/global 可在 256K 上下文将 KV cache 降 6.4x、吞吐提升 3.94x：适合电商多轮对话、长用户行为序列或长文档检索场景，用
  7B 级模型支撑长上下文 Agent 而不过度消耗显存。

  - 把交互轨迹改写为 MDP 状态-动作对做稠密监督，比整段模仿学习更利于训练 Agent 在搜索/推荐中做局部决策（如何时调用搜索、扩展 query、停止迭代）；可直接复用到电商导购
  Agent 的工具调用数据构造。

  - FP8+Muon+TWEO 组合实现约 4.2x pre-training time-to-loss，内部迭代模型可行；尤其 TWEO 抑制激活 outlier
  是 FP8 稳定的关键，可在训练栈中尝试。

  - SFT 数据质量裁剪：约剪掉一半候选，六基准均值 67.78→68.83，证明高质量数据胜于堆量；对电商话术/导购数据可借鉴严格去污和分层过滤。

  - Agent 数据与 general 数据联合训练优于先 general 后 agentic 或只 agentic：对话式购物助手不应只用领域轨迹，需保留通用指令遵循能力。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**

大规模 reasoning / agentic 模型长期被百亿参数闭源系统垄断，学术与中小团队受算力与训练配方不透明双重限制。但紧凑模型不能靠被动记忆开放网络补齐知识，必须在参数容量约束下，通过内部思考与外部工具调用突破能力边界。

**方法关键点**

- **架构**：7.39B 稠密 decoder-only，32 层，hidden 4096，256K 上下文。采用 5:1 混合注意力：27 层 gated sliding-window attention（128 token 窗口）+5 层 global attention，KV cache 从 32GiB 降到 5GiB（6.4x），256K 下吞吐提升 3.94x。
- **预训练效率**：Muon 优化器 + hybrid FP8 + TWEO 激活正则，16K 训练 time-to-loss 相对 BF16/AdamW 加速约 4.2x；其中 SWA 1.4x、FP8 1.5x、Muon 1.8x、Pre-LN 1.1x。
- **中训课程**：600B tokens 分 16K→64K→256K 三阶段，将交互轨迹重构成 MDP 状态-动作对，提供稠密局部决策监督，同时逐步提高 agentic 数据占比。
- **后训练**：SFT 采用 think/no-think 混合模式，50% 质量裁剪带来稳定提升；agentic 数据与 general 数据联合训练优于单独 agentic fine-tuning；RL 用 GRPO 加长度惩罚稳定长程推理。

**关键实验**

在 14 个推理基准上，7B–8B 规模平均排名第一：MATH-500 97.1%，AIME 2026 75.0%，HMMT 2025 70.4%。Agentic Search 上，WebWalkerQA 63.1%、BrowseComp 19.4%、Binary Function Search 62%，与 GLM-5.1（66%）等大模型接近，远超同规模 Qwen3-8B（12%）。

**最值得记住的一句话**

紧凑模型的出路不是更强记忆，而是“内部思考 + 外部寻求”双引擎，配上高效训练栈，7B 也能在长程 Agentic 任务中逼近百亿级闭源系统。
