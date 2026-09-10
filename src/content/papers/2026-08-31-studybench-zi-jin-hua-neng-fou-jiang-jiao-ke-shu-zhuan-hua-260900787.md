---
title: 'StudyBench: Can Self-Evolution Squeeze Textbooks for Olympiad Capability?'
title_zh: StudyBench：自进化能否将教科书转化为奥赛能力？
authors:
- Yinghao Chen
- Zixi Chen
- Bingxiang He
- Ziqing Qiao
- Huan-ang Gao
- Yinuo Xu
- Yuxin Zuo
- Zeyuan Liu
- Yuhao Zhan
- Chaojun Xiao
affiliations:
- Tsinghua University
- Zhejiang University
arxiv_id: '2609.00787'
url: https://arxiv.org/abs/2609.00787
pdf_url: https://arxiv.org/pdf/2609.00787
published: '2026-08-31'
collected: '2026-09-10'
category: Eval
direction: 自进化能力评测基准
tags:
- self-evolution
- benchmark
- LLM
- transfer learning
- compute plateau
- guidance gap
one_liner: 提出受控物理基准 StudyBench，量化自进化从教科书到奥赛能力的吸收与迁移效率，并揭示 Guidance Gap 与 Compute Plateau
practical_value: '- 在自研 Agent/LLM 持续学习或微调项目中，引入「吸收集/迁移集」双层评测，区分同分布刷分与跨分布可迁移能力，避免被
  Application Set 式指标误导。

  - 当新知识或业务文档以 in-context 形式输入时模型表现明显优于微调后，说明存在 Guidance Gap；此时优先考虑 RAG/上下文增强，而不是急于微调。

  - 监控 Compute Plateau：在数据或算力预算远未耗尽时指标已饱和，需要回头审视训练方法、知识表示或合成数据策略，而不是盲目增加数据或训练步数。

  - 在搜索/推荐中的 LLM 任务（query 改写、文案生成等）引入持续业务知识时，用受控基准隔离数据、算力、方法因素，能更准确判断迭代方向。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：人类只需少量优秀教科书即可掌握学科并挑战最难问题。理想的自进化方法应同样能从原始训练材料中自主获得可迁移的解题能力，但现有评测缺乏对这一转化效率的直接测量。

**方法关键点**：提出 StudyBench，一个受控物理基准，将测试集分为 Application Set（困难教科书题，评估知识吸收）和 Transfer Set（奥赛级题，评估跨难度迁移）。在三个基座模型上评测多种代表性自进化方法，并进行 guidance ablation（将同样材料作为 in-context 指导，作为能力上限参考）。

**关键结果**：Application Set 上的提升很少迁移到更难的 Transfer Set；即使最强自进化方法，也只缩小了同材料作为 in-context guidance 所解锁能力的一小部分，暴露明显的 Guidance Gap；所有方法都在耗尽 compute budget 之前饱和，存在 Compute Plateau。剩余差距来自方法本身，而非数据或算力不足。
