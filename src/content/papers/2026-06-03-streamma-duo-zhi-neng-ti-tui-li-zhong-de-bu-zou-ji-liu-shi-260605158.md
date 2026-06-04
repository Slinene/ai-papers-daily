---
title: Streaming Communication in Multi-Agent Reasoning
title_zh: STREAMMA：多智能体推理中的步骤级流式通信协议
authors:
- Zhen Yang
- Xiaogang Xu
- Wen Wang
- Cong Chen
- Xander Xu
- Ying-Cong Chen
affiliations:
- HKUST(GZ)
- Alibaba Group
- ZJU
- HKUST
arxiv_id: '2606.05158'
url: https://arxiv.org/abs/2606.05158
pdf_url: https://arxiv.org/pdf/2606.05158
published: '2026-06-03'
collected: '2026-06-04'
category: MultiAgent
direction: 多智能体推理 · 流式通信协议
tags:
- Multi-Agent Reasoning
- Streaming Communication
- Pipeline Parallelism
- Step-Level Scaling Law
- KV-cache Reuse
- LLM
one_liner: 将通信粒度从完整响应改为推理步骤，流式转发实现流水线并行，同时因步骤质量头部可靠尾部易错而提升效果。
practical_value: '- 多智能体协同推理系统可采用步级流式传输，减少端到端延迟，且利用推理步骤的头部可靠、尾部易错特性，仅用早期步骤即可让下游智能体形成独立推理路径，提升最终效果。

  - 借鉴步级缩放律（Step-Level Scaling Law）：固定智能体数量，通过提示工程增加每智能体推理步数，可同时提升准确率和加速比，为多智能体推理扩展提供新维度。

  - KV-cache复用可大幅降低多智能体推理成本，结合现代推理引擎（vLLM、SGLang），相邻智能体共享上下文前缀，使解码成为主要开销，整体成本可比串行协议更低。

  - 当任务可分解为多步推理（如商品信息分析、多步决策），可将智能体输出设计为“先可靠后弱化”模式，以释放Stream协议优势；若任务难度过高导致全链步骤不可靠，则单一智能体更优，需根据任务特性选择。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**：现有生成式多智能体系统采用“生成后传输”串行协议，延迟与流水线深度线性增长，下游必须等待上游完成全部响应；同时多步推理中步骤质量非均匀，早期步骤更可靠，后期易出错。

**方法关键点**
- 提出 **Stream 协议**：将通信粒度从完整响应改为推理步骤，每个步骤生成后立即转发下游，实现流水线并行。
- 建立统一分析框架：通过步级正确性概率 $p_j$ 定义三种模式（Stream、Serial、Single）的 sCorr 指标，推导六种有效排序定理（Theorem 1），以头部加权均值 $p_{head}$、均值 $\bar{p}$、尾部加权均值 $p_{tail}$ 与阈值 $p^*$ 的关系判定最优协议。
- 给出加速比上限（Theorem 2）与精确成本比（Theorem 3），并在 KV-cache 复用下进一步降低成本。

**关键实验**
- 8 个基准（AIME 2025/2026、HMMT 2026、GPQA-Diamond、HLE、LiveCodeBench 子任务），2 个前沿 LLM（Claude Opus 4.6-high、GPT-5.4-medium），3 种拓扑（Chain、Tree、Graph）。
- STREAMMA 在 Claude 上平均超过 Serial **+7.3 pp**，峰值 **+22.4 pp**（HMMT 2026，Chain）。
- 发现 **步级缩放律**：固定智能体数 A=64，将每智能体步数 S 从 LLM 自主决定扩大到 64，准确率从 68.2% 升至 73.5%，同时获得 **26.9×** 墙钟加速（达到理论上限的 83%）。
- 成本-准确率帕累托前沿：Stream ×4 ($2.75, 90.9%) 优于 Serial ×16 ($5.46, 89.4%)，且 KV-cache 命中可将成本进一步压缩约 1.7×。

**最值得记住**：流式传输不仅降低延迟，更因多步推理中 **“何时收到上下文”比“收到多少上下文”更重要**——利用头部可靠、尾部易错的特性，稀释错误影响，实现效果提升。
