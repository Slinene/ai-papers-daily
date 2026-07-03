---
title: 'PACE: A Proxy for Agentic Capability Evaluation'
title_zh: PACE：用原子评估低成本预测 Agent 能力的代理基准
authors:
- Yueqi Song
- Lintang Sutawika
- Jiarui Liu
- Lindia Tjuatja
- Jiayi Geng
- Yunze Xiao
- Daniel Lee
- Aditya Bharat Soni
- Vincent Lo
- Xiang Yue
affiliations:
- Carnegie Mellon University
- Salesforce AI Research
arxiv_id: '2607.02032'
url: https://arxiv.org/abs/2607.02032
pdf_url: https://arxiv.org/pdf/2607.02032
published: '2026-07-01'
collected: '2026-07-03'
category: Eval
direction: Agent 评估 · 代理基准构建
tags:
- Agent Evaluation
- Proxy Benchmark
- Instance Selection
- Regression
- Cost Efficiency
- LOOCV
one_liner: 从非 Agent 原子评估中选取少例子集构建回归代理，预测 Agent 基准得分，成本低于 1% 且 MAE < 4%
practical_value: '- **Agent 选型与模型路由的快速筛选**：面对 SWE-Bench、GAIA 等高成本 Agent 评测，可在内部构建
  PACE 类代理，用小批量原子任务（指令跟随、工具调用等）快速预估候选模型或变体的 Agent 能力，避免全量昂贵评测，适合电商搜索/推荐 Agent 的 A/B
  前筛选。

  - **实例选择策略可迁移至推荐离线评估**：PACE 的“目标相关局部选择 + 全局信息选择”组合，可借鉴到推荐模型的召回/排序评估中，从海量物品中选择少量
  proxy items，以低成本近似在线指标。

  - **解耦 Agent 能力画像**：通过分析所选代理实例，可识别特定 Agent 基准（如工具使用、长程规划）对哪些原子技能最敏感，指导电商 Agent 训练时针对性地补强薄弱环节。

  - **工程落地轻量**：仅需线性回归，无需复杂模型，适合在 CI/CD 中集成，作为每次模型更新的快速健康检查，成本几乎可忽略。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：评估 LLM Agent 的基准（如 SWE-Bench、GAIA）单次评测花费数千美元、耗时数天，成本极高；而测试单一能力（推理、代码生成）的非 Agent 基准则快速低廉。作者研究是否能用少量原子评估实例的得分，精确预测昂贵的 Agent 基准表现。

**方法关键点**：提出 PACE 框架。从候选非 Agent 实例池（覆盖指令跟随、规划、工具调用等）中选取一个紧凑子集，拟合线性回归，将模型在这些子集上的得分映射到目标 Agent 基准得分。实例选择结合两种策略：
- 目标相关局部选择（Target-relevance）：优先选与 Agent 目标统计相关的实例；
- 全局信息选择（Global selection）：保证子集能覆盖评估空间的信息多样性。
最终得到具体代理基准 PACE-Bench（4 个目标 Agent 基准、19 个源原子基准中选出的实例）。

**关键结果**：在 14 个模型上留一法交叉验证（LOOCV）表明：
- 平均绝对误差（MAE）< 4%；
- Spearman 相关性 > 0.80；
- 模型间相对排序准确率约 85%；
- 评估成本不到完整 Agent 评测的 1%。
分析所选代理实例，揭示了各 Agent 基准对特定原子能力的不同需求。
