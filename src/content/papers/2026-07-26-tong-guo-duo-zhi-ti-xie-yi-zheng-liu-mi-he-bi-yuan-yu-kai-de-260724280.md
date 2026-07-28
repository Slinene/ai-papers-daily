---
title: 'From Proprietary to Open-Source: Bridging the Distribution Gap via Multi-Agent
  Protocol Distillation in Agentic Search'
title_zh: 通过多智体协议蒸馏弥合闭源与开源Agent搜索的分布鸿沟
authors:
- Junlin Liu
- Jiangwang Chen
- Zixin Song
- Shuaiyu Zhou
- Chunji Lv
- Hank Wu
- Kailin Jiang
- Jinyang Wu
- Bohan Yu
- Chenxi Zhou
affiliations:
- University of Chinese Academy of Sciences
- Tsinghua University
- Peking University
- Beijing Institute of Technology
arxiv_id: '2607.24280'
url: https://arxiv.org/abs/2607.24280
pdf_url: https://arxiv.org/pdf/2607.24280
published: '2026-07-26'
collected: '2026-07-28'
category: Agent
direction: 多智体协议蒸馏 · Agent搜索
tags:
- Multi-Agent
- Knowledge Distillation
- Agentic Search
- Protocol Distillation
- RL
- Style Drift
one_liner: 提出结构化JSON协议作为中间表示，将闭源多智体的推理策略蒸馏到开源学生模型，显著缓解风格漂移和幻觉。
practical_value: '- **用结构化协议替代原始文本进行蒸馏**：在Agent搜索场景中，直接模仿闭源模型的自然语言轨迹会导致灾难性的风格漂移和幻觉，业务上若想用GPT/Claude蒸馏小模型，务必把推理过程抽象为JSON、流程图等结构化中间表示，剥离语言风格。

  - **离线多智体合成高质量训练信号**：用多智体系统（编排者+搜索者+修复者+协议者）提前生成高质量推理协议，训练时只复用协议，不增加在线推理开销。这种模式可迁移到电商导购Agent的多轮决策合成：用强模型离线生成“商品推荐-推理-校验”协议，蒸馏到线上轻量模型。

  - **在线自蒸馏与RL的联合训练配方**：将结构化协议作为特权信息（privileged information）输入教师分支，与学生分支做token级KL对齐，同时叠加GRPO稀疏奖励，λ=0.05附近是甜区。业务中复现类似流水线时，可直接参考该联合损失权重调优经验。

  - **跨教师模型的可迁移性**：结构化协议对不同闭源教师（Claude/GPT/Gemini）都有效，方差极小，意味着后续替换底层LLM API时无需重新调参，可大幅降低迭代成本。'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
在Agent搜索（多轮检索+推理）场景中，用结果监督的RL提供了稀疏奖励，而知识蒸馏可提供密集指导。但将闭源强模型（如GPT-5）作为教师，面临两大瓶颈：① tokenizer不同且logits不可见，传统KL蒸馏失效；② 直接模仿教师自然语言轨迹会导致学生学到冗余的风格表示，产生严重风格漂移和幻觉（纯OPSD在1.7B模型上仅得5.9%成功率）。因此需要一种能解耦核心推理策略与语言表层形式的中间表示。

### 方法关键点
- **结构化JSON协议**：将任务分解为 task_type、reasoning_plan（有序子目标）、grounding_facts（严格抽取的证据）、partial_findings、answer_verified 五部分，剥离教师的特定语言风格。
- **多智体合成流水线**：离线用闭源模型构建多智体系统（Orchestrator、Searcher、Repair、Protocolizer），通过多轮搜索、错误修复和质量门控（schema验证、EM一致性、事实校验、防泄漏检查）自动生成高质量协议，准确率达99.33%。
- **联合训练框架MAPD**：将协议作为特权信息输入教师分支，学生分支仅看到输入问题，两支路共享参数，用在线自蒸馏（OPSD）做token级KL对齐，同时联合GRPO稀疏奖励优化，蒸馏损失权重λ=0.05时平衡最佳。

### 关键实验
在NQ和HotpotQA上训练，评估7个知识密集型QA基准（单跳/多跳）。使用Qwen3-1.7B和4B作为学生。MAPD在两个模型上分别达到39.4%和44.4%平均成功率，超越最强基线SDAR（37.6%/43.0%）。尤其在多跳任务上增益更大（1.7B多跳平均增益7.9%）。消融证明：直接用原始自然语言轨迹蒸馏（30.1%）甚至不如不使用教师（31.6%）；引入结构化协议带来7.0点增益；加上MAS可进一步提升到39.4%。

### 核心启示
_“结构化协议是将黑盒强模型的推理能力迁移给小模型的安全、高效桥梁，彻底绕过风格模仿陷阱。”_
