---
title: 'Tools Need Not Speak in Text: Latent Context Compression for Agents'
title_zh: 工具无需文本表达：面向智能体的潜在上下文压缩
authors:
- Yuetong Liu
- Zhehao Zhou
- Yitong Zhang
- Haorui Chen
- Jia Li
affiliations:
- Tsinghua AI Agent Group, Tsinghua University
arxiv_id: '2611.06500'
url: https://arxiv.org/abs/2611.06500
pdf_url: https://arxiv.org/pdf/2611.06500
published: '2026-11-03'
collected: '2026-11-08'
category: Agent
direction: Agent 工具输出潜在压缩
tags:
- Latent tokens
- Context compression
- LLM agents
- Tool use
- Action-preserving training
- Web search
one_liner: 提出Coca-Cola，用连续潜在token压缩工具观察，通过动作保持训练对齐决策分布，大幅降低token消耗并提升任务性能
practical_value: '- 在搜索/推荐 Agent 多轮工具调用中，商品列表、搜索结果、用户评论等长文本返回可用连续潜在 token 替代文本摘要或剪枝，大幅减少上下文长度；实现上用小规模
  encoder（如 4B）加 latent adapter 投影到主 LLM 输入嵌入空间，只训练 LoRA 和 adapter，主模型冻结。

  - 训练目标采用动作保持蒸馏：将 full observation 和 compressed latent tokens 分别喂给冻结 agent，对齐 next-action
  分布（KL 散度）并加 CE 监督，而不是重构原文。这在需要下游决策的压缩场景（如推荐排序、query 改写）比通用文本重建更有效，可直接复用。

  - 工程部署上，压缩器与主 agent 模型解耦，推理时主模型单 GPU 即可运行，压缩器可放另一 GPU 或同卡，论文中端到端延迟降低 24%–56%，对在线服务的成本与延迟优化有直接参考价值。

  - 潜在 token 数量是效率-性能权衡关键，128 个 token 得到最佳任务表现，但 16 个 token 也能维持较高压缩率和合理性能；在资源受限的电商场景可用较小预算做快速实验。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：LLM agents 在多步工具交互中，原始工具输出（如搜索结果）会迅速占据大部分上下文（论文统计第 4 步占 96.7%），导致计算开销剧增，同时冗余内容分散注意力、损害推理质量。现有文本压缩方法（token 剪枝、摘要）受限于离散 token 表示，压缩率有限。连续潜在 token 具有更高信息容量，且可端到端优化，为压缩工具输出提供新思路。

**方法关键点**：
- 提出 Coca-Cola，将工具观察压缩为少量连续潜在 token 直接注入 agent 输入嵌入空间，不再以显式文本传输。
- 模型结构：context-aware encoder（小型 LM）+ latent adapter。encoder 输入任务指令、当前推理轨迹和工具观察，adapter 将隐藏状态映射为固定数量（默认 128）的潜在 token，与目标 agent 的嵌入维度对齐，并用特殊边界标记包裹插入。
- Action-Preserving Training：冻结目标 agent，分别用原始观察和压缩潜在 token 计算 next-action 分布，用 KL 散度对齐两个分布，并用 CE 损失监督记录动作。只更新 encoder 的 LoRA 参数和 adapter，梯度通过冻结的 agent 反向传播，无需重构原文。
- 推理时每个工具调用后都将原始观察替换为潜在 token，支持多步交互。

**关键实验**：在 NQ、TriviaQA、2Wiki、HotpotQA 四个 QA 基准上，使用 Qwen3.5-35B-A3B+Qwen3.5-4B 和 GLM-4.7-Flash+GLM-Z1-9B 两套模型配置，对比 Vanilla、LongLLMLingua、LLMSummary、ICAE。Coca-Cola 将总 token 消耗降低 70.01%–89.24%，端到端运行时间降低 24.45%–55.97%，同时在 EM 和 F1 上均优于 Vanilla，在 13/16 个数据集-指标对中取得最优。消融显示 128 个潜在 token 效果最好；任务指令和推理轨迹作为上下文条件对性能有贡献。

**最值得记住的一句话**：工具与 agent 之间的信息交互不必依赖显式文本，通过连续潜在 token 加动作保持训练，可以在大幅压缩上下文的同时提升决策性能。
