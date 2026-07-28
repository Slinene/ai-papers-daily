---
title: 'Multi-Head Latent Control: A Unified Interface for LLM Agent Decision Making'
title_zh: 多头潜在控制：LLM Agent推理决策的统一接口
authors:
- Amirhosein Ghasemabadi
- Ruichen Chen
- Bahador Rashidi
- Di Niu
affiliations:
- University of Alberta
- Huawei Technologies Canada Co., Ltd.
arxiv_id: '2607.14277'
url: https://arxiv.org/abs/2607.14277
pdf_url: https://arxiv.org/pdf/2607.14277
published: '2026-07-14'
collected: '2026-07-28'
category: Agent
direction: Agent 推理时控制接口与多模型路由
tags:
- Latent Control
- Model Routing
- Tool Use
- Agent Decision Making
- Deployment-time Control
- Self-awareness
one_liner: 通过读取冻结LLM的隐状态轨迹，轻量控制头在推理时做出模型选择与干预决策，大幅降低大模型调用成本。
practical_value: '- 在推荐系统的多模型级联（小模型→大模型）中，可借鉴 Capability Head，从生成隐状态预测小模型是否足够，仅必要时调用大模型，节省成本；特别适合基座模型频繁换代的环境，无需重训基座。

  - 对于涉及工具调用的推荐 Agent（如实时查询商品价格、库存），可用 Resolution Head 决定调用时机，减少不必要的工具调用，同时避免遗漏关键调用，提升决策准确率。

  - 该轻量控制层只需要冻结基座模型的隐状态，训练成本低（单卡一日内完成），适合业务快速实验和部署；训练数据混合多任务、多模态，使控制信号泛化性更强。

  - 前缀预测实验表明，仅用部分生成轨迹即可提前判断模型能力，可在生成早期就决定是否升级模型，进一步降低延迟和计算浪费。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：LLM 作为 Agent 时，可靠的 agentic 行为不仅需要正确的生成，还需要在推理时做出何时 defer 到更强模型、请求信息、调用工具或弃权等控制决策。现有方法多依赖输入侧信号或外部编排，成本高、难以随基座模型更新而维护。本文提出从模型自身生成过程的隐状态中直接推断这些决策，实现轻量、可迁移的控制层。

**方法关键点**：
- 在冻结的 LLM/VLM 上附加两个轻量控制头：**Capability Head** 预测当前模型是否足以解决实例，若不足则 transfer 到强模型；**Resolution Head** 在保留本地模型时决定是否请求澄清、调用工具、弃权或直接回答。
- 控制头读取模型生成时的隐状态轨迹（Capability Head 用最后一层，Resolution Head 用中间层），通过压缩为固定长度表征再预测。
- 训练时基座完全冻结，只用生成的隐状态轨迹与基于 LLM-judge 的评分进行监督，不依赖模型表面回答的正确性。
- Capability Head 训练数据采用混合 120K 样本，覆盖视觉 QA、推理、工具使用等多模态任务，以学习可泛化的 adequacy 信号。

**关键结果**：
- 在多模型路由（小模型 + 大模型）场景下，AndroidWorld 中减少大模型调用 **90.7%**，成本降低 85.8%，且成功率从 0.47 提升至 0.60；在 6 个多模态基准上平均节省成本 27-53%，同时保留大部分大模型性能。
- Resolution Head 在 WHEN2CALL 基准上，相比骨干模型原生行为，F1 最多提升 11.7 点，准确率提升 12.4 点；在 TriviaQA 的网页搜索决策中，得分相对提升最高达 158.9%，遗漏必要工具调用减少 65.5%。
- 前缀时间预测表明，仅用 200 token 前缀即可获取有意义的 adequacy 信号，经前缀训练后信号质量接近全轨迹。

**核心洞察**：冻结 LLM 的隐状态轨迹提供了可扩展的基板，能够快速附加轻量控制层，实现推理时模型选择与干预决策，无需修改基座。
