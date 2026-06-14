---
title: 'See What I See, Know What I Think: Dense Latent Communication Across Heterogeneous
  Agents'
title_zh: 看见我所见，知晓我所想：异构智能体的密集隐空间通信
authors:
- Siyi Chen
- Xiaoyan Zhang
- Meng Wu
- Jonathan Tremblay
- Valts Blukis
- Stan Birchfield
- Rene Vidal
- Alvaro Velasquez
- Sijia Liu
- Qing Qu
affiliations:
- University of Michigan
- NVIDIA
- University of Pennsylvania
- University of Colorado Boulder
- Michigan State University
arxiv_id: '2606.13594'
url: https://arxiv.org/abs/2606.13594
pdf_url: https://arxiv.org/pdf/2606.13594
published: '2026-06-10'
collected: '2026-06-14'
category: MultiAgent
direction: 多智能体隐空间通信 · 异构KV缓存对齐
tags:
- KV-cache
- Multi-Agent
- Heterogeneous Agents
- Latent Communication
- Dense Alignment
- Information Bottleneck
one_liner: 提出异构多智体KV缓存密集对齐框架，实现跨模型知识迁移和高效通信，计算量降低2-3倍。
practical_value: '- **跨模型知识迁移**：在电商多模型 Agent 系统中（如不同尺寸LLM协作），可直接使用论文的两阶段训练（Phase I
  重建对齐，Phase II 生成微调）和跨模型 KV-cache 适配器，让大模型直接将自己的“思考状态”注入小模型，避免重复编码上下文，大幅降低推理成本。

  - **上下文不感知的高效通信**：当接收方 Agent 无法访问原始输入（如隐私限制或带宽限制），论文的密集对齐方法可作为现成方案，将发送方的知识与推理一并压缩进
  transformable KV-cache，接收方仅凭 cache 即可完成任务，这适用于电商推荐中跨域、跨设备的同步策略。

  - **稀疏推理信号与门控机制**：压缩感知分析指出上下文感知通信仅需少量 KV 组即可作为推理指引，可借鉴其按头组门控选择与重要性评分，在生成式推荐或 query
  理解中，对跨模型传递的“提示信号”进行选择性裁剪，兼顾精度与效率。

  - **位置解耦与层对齐**：论文中剥离 RoPE 进行内容匹配的设计，可迁移到异构 Transformer 间的特征迁移场景，例如将不同结构的推荐模型（双塔、多模态编码器）的中间表示进行对齐，实现模块级复用。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：基于 LLM 的多智体系统通常依赖文本通信，存在解码-重编码开销大、信息损失、无法直接共享丰富中间表示等问题。KV-cache 通信可避免这些，但现有工作主要针对同构模型，异构场景下由于维度、结构、位置编码差异难以对齐，且大多只在上下文感知（接收端仍看输入）下评估，仅传输稀疏推理信号。本文探索了更具挑战性的“上下文不感知”通信：接收端仅凭发送端的隐状态完成推理，需密集知识传递，相当于真正的“读心”。

**方法关键点**:
- **压缩感知分析**：对同构自通信下的 KV-cache 进行随机消融与 LASSO 回归，发现上下文感知仅需少量头部组传递推理信号（稀疏），而不感知需多达 87% 的 KV 组才能维持性能（密集），揭示信息结构二重性。
- **密集对齐框架**：学习一个跨模型缓存变换器，将发送方 KV-cache 映射为接收方兼容的 cache，包含：位置解耦（先剥离 RoPE，对齐内容后再恢复）；按层深度单调配对层；按 KV 组独立的小 MLP 变换与可学习门限，实现细粒度对齐。
- **两阶段训练**：Phase I 用接收方自身 cache 作为重建目标，强迫变换器在接收方“语言”中表达密集内容；Phase II 在上下文感知与不感知混合提示下进行生成微调，使对齐 cache 同时支持两种通信模式。

**关键实验**:
- 设置：Qwen3-4B/8B/14B 六个方向配对，在 GSM8K、MATH-500、ARC-C（域内）和 MMLU-Redux、MedQA、OpenBookQA（域外）上评估。
- 基线：文本通信（T2T）、基于 steering 的 cache-to-cache（C2C）和单 agent 裸接收端。
- 上下文感知结果：密集对齐在所有域内任务上匹配或超过 T2T（如 4B→14B GSM8K 92.95%），计算量仅为 T2T 的 1/2~1/3（21.5 TFLOPs vs 56.2）。C2C 显著低于本方法。
- 上下文不感知结果：T2T 和 C2C 几乎失效（C2C 准确率 0-2%），而本方法在 GSM8K 上达 81-91%，MATH 达 64-82%，且计算量更小（8B→4B 仅 6.6 TFLOPs，低于接收端裸推理），验证了密集知识转移的可行性与效率。

**核心洞见**：隐空间通信在上下文感知时仅需稀疏推理信号，而在上下文不感知时需密集保存知识，密集对齐为此提供了高效统一的解决方案。
