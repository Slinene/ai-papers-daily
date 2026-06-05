---
title: Rethinking Continual Experience Internalization for Self-Evolving LLM Agents
title_zh: 重新思考自进化LLM智能体的持续经验内化
authors:
- Jingwen Chen
- Wenkai Yang
- Shengda Fan
- Wenbo Nie
- Chenxing Sun
- Shaodong Zheng
- Yangen Hu
- Lu Pan
- Ke Zeng
- Yankai Lin
affiliations:
- 中国人民大学高瓴人工智能学院
- 北京航空航天大学软件学院
- 美团
arxiv_id: '2606.04703'
url: https://arxiv.org/abs/2606.04703
pdf_url: https://arxiv.org/pdf/2606.04703
published: '2026-06-02'
collected: '2026-06-05'
category: Agent
direction: Agent 自进化 · 经验内化
tags:
- Experience Internalization
- Self-Evolving Agents
- Context Distillation
- Continual Learning
- LLM Agents
- Step-wise Injection
one_liner: 揭示经验内化在多轮自进化中的能力崩塌，从经验粒度、注入模式、内化策略三维度给出稳定方案
practical_value: '- **经验抽象为原则**：在电商导购、多步工具调用等Agent场景中，经验积累应提取可复用的决策原则与失败模式（原则级），而非保留具体域名、URL等轨迹细节（实例级），后者在多轮更新中迅速失效。

  - **逐步注入经验**：在训练Teacher模型时，根据当前交互状态动态选择相关经验（逐步注入），避免全局固定经验导致模型过早终止（如未搜索直接回答）。在长时任务中，该模式可降低“过早应答”率（本工作中从63%降至0%），保持后续迭代的经验使用能力。

  - **使用离线策略蒸馏**：多轮自进化时，建议从强教师（经验感知模型）直接生成并筛选高质量轨迹进行蒸馏（离线），而非从学生模型采样再纠正（在线）。离线蒸馏训练出的轨迹更短（平均2.5步
  vs 在线21.9步），且性能迭代更稳定，避免性能崩塌。

  - **监控经验使用能力**：在迭代内部化后，应评估模型在无经验和带经验上下文时的表现差距。如果差距消失或带经验反而下降，说明模型丢失了利用经验池的能力，会破坏下一轮Teacher的监督质量，需调整注入模式或经验提取策略。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
让LLM Agent从过往交互经验中持续学习并转化为自身参数能力，是实现自主自进化的关键路径。当前主流方法采用在线策略上下文蒸馏（on-policy context distillation），在单轮训练中表现良好，但在多轮迭代自进化中会出现严重的性能崩塌（如WebWalkerQA成功率从首轮约35%跌至三轮后不足20%），无法支撑持续学习。本文系统探究了经验内化在多轮设置下失效的本质原因，并提出稳定方案。

**方法关键点**
- **经验粒度**：比较实例级经验（保留具体URL、数字等轨迹细节）与原则级经验（抽象出搜索策略、失败模式），发现原则级经验更持久，因为它过滤了局部细节，提供可泛化的决策规则。
- **经验注入模式**：全局注入将固定经验上下文贯穿整个生成过程，逐步注入则根据当前交互历史动态选择相关经验。逐步注入能对齐经验与中间决策状态，在长时工具调用中避免过早终止，并保留模型在后续迭代中继续利用经验池的能力。
- **内化策略**：在线蒸馏在学生的错误状态上进行局部修正，监督信号零散且轨迹冗长；离线蒸馏由经验感知的教师直接生成完整成功轨迹并过滤，提供连贯的端到端经验引导信号，训练更稳定且轨迹效率更高（平均助手回合2.5 vs 21.9）。

**关键实验**
在WebWalkerQA、GAIA-Text-103、BrowseComp-ZH三个基准上，使用Qwen3‑4B/8B，进行三轮自进化。
- 原则级经验在多轮后仍高于基线，而实例级经验首轮后即下降。
- 逐步注入 vs. 全局注入：单轮WebWalkerQA（4B）从23.2%提升至31.2%（+8.0），且三轮后仍保持30.0%，全局注入则从25.9%跌至12.8%；全局注入的“过早应答”率高达63.82%，逐步注入为0%。
- 最终稳定配方（原则级+逐步注入+离线蒸馏）在三轮自进化中持续提升：WebWalkerQA 33.1、GAIA 33.3、BrowseComp-ZH 5.9，且模型仍能有效利用经验上下文。

**一句话总结**
多轮经验内化的可持续性取决于「抽象可复用原则 + 按状态对齐注入 + 从高质量演示学习」的组合，否则会陷入性能崩塌。
