---
title: Self-Compacting Language Model Agents
title_zh: 自压缩语言模型智能体：基于评分规则的自适应上下文压缩
authors:
- Tianjian Li
- Jingyu Zhang
- William Jurayj
- Xi Wang
- Chuanyang Jin
- Mehrdad Farajtabar
- Eric Nalisnick
- Daniel Khashabi
affiliations:
- Johns Hopkins University
- Apple
arxiv_id: '2606.23525'
url: https://arxiv.org/abs/2606.23525
pdf_url: https://arxiv.org/pdf/2606.23525
published: '2026-06-21'
collected: '2026-06-23'
category: Agent
direction: 自适应上下文压缩 · 评分规则栅控
tags:
- context rot
- rubric-gated compaction
- adaptive summarization
- long-horizon agent
- KV-cache reuse
- training-free
one_liner: 提出训练无关的自适应上下文压缩方法，通过轻量规则让模型自决定压缩时机，避免固定间隔压缩破坏中间推理
practical_value: '- **长轨迹Agent的上下文管理**：可借鉴评分规则（rubric）用于决定何时压缩历史，避免在模型推导或搜索中途破坏信息，尤其适合电商客服、推荐解释生成等需要多轮推理的场景，提高答案正确性并降低上下文长度。

  - **低成本KV-cache复用**：压缩触发时仅追加总结指令，重用已有缓存的trajectory tokens，几乎零预填充开销，相比重新编码大量上下文可节省30%-70%的计算成本，适合部署在在线服务中。

  - **任务特定规则设计**：根据任务特性编写轻量级栅控提示（如数学中的“是否已得最终答案”、“是否陷入停滞”），无需训练即可引导模型在安全点压缩，可直接迁移到搜索推荐中的多步检索、方案生成等流程。

  - **训练无关的元认知增强**：暴露“压缩工具”并配合规则，让模型表现出类似元认知的自省能力，可适用于任何支持工具调用的开源模型，无finetuning成本，可快速实验。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：长轨迹Agent（如数学推理、深度搜索）随着思考链增长会积累大量过时、错误或无关的上下文，即“上下文腐烂”（context rot），锚定后续生成并导致性能下降。现有固定间隔压缩或阈值触发方法无视轨迹结构，常于推导中途或搜索过程中丢弃关键中间结果，造成答案错误或成本浪费。有必要让模型自主识别何时已解决子任务、何时可以安全压缩，而非依赖僵化的token数阈值。

**方法关键点**：
- **SELFCOMPACT框架**：在推理时向模型暴露一个内联的**压缩工具**，并配以**轻量评分规则（rubric）**，后者在定期探测点（每N个生成token或工具调用）判断是否触发压缩。
- **规则设计**：针对数学任务，检查三项条件：①是否已给出最终答案（Q1=ANSWER）；②最近两轮是否无新事实且卡住（Q2=STUCK）且有明确下一步（Q3=HAS-NEXT）。规则为真则输出COMPRESS，否则CONTINUE。搜索任务有类似的结构化检查点。
- **KV缓存复用**：压缩工具通过追加总结指令（而非替换整个前缀）重用缓存，仅对总结指令和生成的摘要产生预填充开销，大幅节省成本。
- **无需训练**：整个机制仅靠提示工程和工具调用，适用于任何工具调用能力的开源模型。

**关键结果**：
- 在IMO-Answerbench、HMMT Nov/Feb等数学基准上测试4款Qwen模型，SELFCOMPACT在11/12个配置下超越固定间隔压缩，且与无压缩基线相比，Qwen3.5-9B提升高达18.1个百分点。
- 在BrowseComp、BrowseComp-Plus、DeepSearchQA等搜索任务上用GLM-4.7-Flash、MiniMax-M2.5、Mimo-V2-Flash测试，精度相对基线提升5~9个百分点，同时每问成本降低30%~70%（例如MiniMax-M2.5在BrowseComp-Plus上成本从$0.19降至$0.07）。
- 消融实验表明，移除评分规则会令性能下降5.4个百分点（Agent搜索平均），证明规则的栅控作用对安全压缩至关重要。
- Oracle分析显示，若能在固定间隔中智能跳过不必要的压缩（仅压缩错误状态），理论上可获得更大幅度提升，表明“何时压缩”仍有优化空间。

**核心洞见**：上下文腐烂的识别可在推理时刻通过少量规则提示注入模型，无需将决策能力固化为模型权重，即可在开放权重模型上实现自适应的长时Agent。
