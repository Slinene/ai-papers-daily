---
title: 'Before the Action: Benchmarking LLMs on Prospective Hypothesis Discovery'
title_zh: 行动前：评测LLM的前瞻假设发现能力
authors:
- Tianyun Zhong
- Wangyi Jiang
- Wei Wang
- Xuanang Chen
- Yaojie Lu
- Shiwei Ye
- Yuzhen Shi
- Boyu Yang
- Jinghang Wang
- Han Li
affiliations:
- University of Chinese Academy of Sciences
- Institute of Software, Chinese Academy of Sciences
- Alibaba Group
arxiv_id: '2607.15766'
url: https://arxiv.org/abs/2607.15766
pdf_url: https://arxiv.org/pdf/2607.15766
published: '2026-07-17'
collected: '2026-07-20'
category: Reasoning
direction: LLM 前瞻假设推理评估
tags:
- Prospective Hypothesis Discovery
- LLM Benchmark
- Arena Evaluation
- Reasoning
- Retrospective Context Regression
- Test-time Reasoning
one_liner: 提出前瞻假设发现任务与HypoArena基准，评测LLM在证据不足下自主构建可检验假设空间的能力。
practical_value: '- **Agent 的异常诊断与归因**：在电商/广告系统中，当指标异常（如CTR突降）时，可借鉴 PHD 框架让 Agent
  先自动生成多层次假设（模型更新、流量变化、A/B 实验干扰等），再调用工具验证，提升诊断效率和覆盖率。

  - **假设空间构建与评估方法**：HypoEval 的双向 pairwise + Bradley-Terry 排序和六维评分，可直接迁移到 Agent 输出的候选方案对比（如推荐策略多选项评估），用竞技场模式仲裁更符合实际决策场景。

  - **数据逆向构造方法**：Retrospective Context Regression 可从已完成的分析报告中剥离结论与因果归因，生成前结论状态的训练样本，用于微调业务
  Agent 的假设生成能力，解决“事后诸葛亮”的数据偏差。

  - **结构化技巧的权衡**：论文发现结构化分析技巧对弱模型有提升但可能损害强模型，提示在 Agent 中引入思维链等技巧需做模型层级的自适应，避免一刀切破坏原有推理优势。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：现有 LLM 评估多聚焦已知问题的问答，但真实场景（如事故分析、金融排查）的起点往往是碎片化异常与不确定证据，模型需先构建值得验证的假设空间，这种“前结论”的发现能力尚未被测量。

**方法**：定义前瞻假设发现 (PHD) 任务：给定不完整证据，生成有依据、可区分、可检验的假设集合。提出 HypoArena 基准，包含：1) HypoData，通过 Retrospective Context Regression 从已完成专家文档中移除结论、假设与因果陈述，保留事实基底，构建 988 个案例覆盖 6 个领域；2) HypoEval，采用双向成对评判 + Bradley-Terry-Davidson 聚合排序，辅以六维评分标准（如可检验性、区分度等），解决假设生成无单一正确答案的评估难题。

**关键结果**：在 15 个前沿 LLM 上测试，发现：1) 模型能力明显分层，顶尖模型与弱模型差距显著；2) 结构化分析提示对低性能模型有帮助，但部分强模型反而退化；3) 竞技场排序比绝对评分能捕捉更细粒度差异，聚合排名与人类专家及独立裁判高度一致，验证了 PHD 作为独立评测目标的合理性。
