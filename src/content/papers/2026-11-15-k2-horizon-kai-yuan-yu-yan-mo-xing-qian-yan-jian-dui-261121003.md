---
title: 'K2-Horizon: A Frontier Fleet of Open Source Language Models'
title_zh: K2-Horizon：开源语言模型前沿舰队
authors:
- K2 Team
- Zhengzhong Liu
- Haonan Li
- Xuezhe Ma
- Alexander Moreno
- Subham Sekhar Sahoo
- Rupesh Kumar Srivastava
- Mikhail Yurochkin
- Hadi Abdine
- Yash Akhauri
affiliations:
- Institute of Foundation Models
- Mohamed bin Zayed University of Artificial Intelligence
arxiv_id: '2611.21003'
url: https://arxiv.org/abs/2611.21003
pdf_url: https://arxiv.org/pdf/2611.21003
published: '2026-11-15'
collected: '2026-11-17'
category: LLM
direction: 大规模开源 LLM 训练与 Agent 后训练
tags:
- MoVA
- MoE
- Open Source LLM
- RL360
- diffusion decoding
- agentic training
one_liner: 发布六款完全开源 LLM（0.9B-375B MoE），提出 MoVA 与 softplus 门控，开源全训练链路及 10T 合成数据
practical_value: '- **Agent 数据早引入**：将 agentic trajectories 从 mid-training 阶段就混入（而非仅
  post-training），可提升长程工具调用与多轮交互能力；做电商导购/客服 Agent 时，可在继续预训练或 mid-training 阶段加入高质量真实/合成交互轨迹。

  - **MoVA 稀疏注意力 value 投影**：不增加 KV cache 且兼容 FlashAttention/GQA，适合线上低延迟但需要大容量的助手；可尝试在推荐/搜索的生成式排序或
  query 改写模型中用 MoE 思想稀疏化 value 计算，降低激活参数。

  - **推理加速**：Uno 无损扩散适配器解码加速 2.2x 且无需 draft model，在线部署可优先调研此类自蒸馏扩散方式，用于生成式推荐/query
  生成的吞吐优化。

  - **RL 专家分训 + 权重合并**：375B 按领域分别训练 RL experts 再用 ISO-RAM 合并，能快速组合搜索、工具、客服等能力；小模型用
  FTPO 从自身重复输出挖掘偏好对，防止长程任务陷入循环，可借鉴到多技能 Agent 的稳定训练。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：当前开源 LLM 众多，但绝大多数只公开权重，数据、中间检查点、训练日志和代码缺失，难以复现或科学比较。K2-Horizon 以 LLM360 完全开源定义发布 6 款模型，从 0.9B 密集到 375B-A23B MoE，覆盖端侧到多 GPU 部署，并公开全部开发历史、数据和代码，旨在推动可复现的 agentic 模型研究。

**方法关键点**：
- 架构：Grouped RMSNorm 稳定宽模型训练；MoVA 在注意力 value 投影引入 MoE（64 个专家激活 4 个），不增加 KV cache，兼容 FlashAttention/GQA；softplus 注意力门控可放大且初始化接近恒等。
- 训练：4 个模型共享同一 22T token 预训练语料，约 10T 为合成数据；预训练常数学习率，末尾 checkpoint 平均实现衰减；mid-training 将上下文从 32k 扩至 512k，并提前加入 agentic trajectories。
- 后训练：375B 分别训练搜索、知识工作、工具、科学推理、指令遵循+弃权五个 RL 专家，用 ISO-RAM 权重合并，再 SFT；小模型用 FTPO 防重复循环。
- 推理：Uno 无损扩散适配器，加速解码最多 2.2x 无需单独 draft model。

**关键实验**：375B-A23B 与同期 GLM-5.2、MiniMax M3、Nemotron 3 Ultra、Inkling 对比，在多数 agentic/coding 基准排第一或第二；Toolathlon-Verified 65.3 超过 GPT-5.6 Terra，接近 Luna；SWE-Atlas-QnA 48.4；τ3-Banking 超过 GPT-5.6。36B-A4B 激活 4.6B 参数，预训练 loss 接近 32B dense，下游仅差 1.2-3.7 分。7B/3.7B 在 SWE-bench Verified 显著领先同尺寸。

**最值得记住的一句话**：MoVA 在注意力 value 投影上做 MoE 且不增加 KV cache，使 36B MoE 以约 1/7 激活参数逼近同数据 32B dense 模型。
