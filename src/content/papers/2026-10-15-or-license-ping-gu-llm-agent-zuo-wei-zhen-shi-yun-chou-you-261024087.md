---
title: 'OR-License: Evaluating LLM Agents as Real-World Operations Research Practitioners'
title_zh: OR-License：评估 LLM Agent 作为真实运筹优化实践者
authors:
- Peisong Wang
- Feixue Liu
- Yize Meng
- Bowen Liu
- Ruoyu Chen
- Gaoyang Dai
- Xing He
- Aiqian Li
- Fengchi Yuan
- Aochuan Chen
affiliations:
- HKUST-GZ
- HKU
- Qingzhi Optimization (Jinan) Information Technology Co., Ltd.
- Hunyuan, Tencent
- Tianjin Meta & Infinite Technology Co., Ltd
arxiv_id: '2610.24087'
url: https://arxiv.org/abs/2610.24087
pdf_url: https://arxiv.org/pdf/2610.24087
published: '2026-10-15'
collected: '2026-10-20'
category: Agent
direction: LLM Agent 端到端运筹优化评估
tags:
- LLM Agents
- Operations Research
- Benchmark
- Information Acquisition
- Feasibility
- Agent Evaluation
one_liner: 用 31 个真实付费 OR 项目构建基准，通过客户端模拟器评估 LLM Agent 从原始需求到可部署方案的端到端能力
practical_value: '- 在业务中让 LLM Agent 处理需求分析与建模时，不要只依赖初始 prompt，可引入受控的“客户模拟器”或澄清循环，显式管理信息获取阶段（澄清、建模、验证），并跟踪已确认问题的解决率。

  - 评估生成式推荐/优化系统时，除了软性质量指标，应加入可行性硬性检查与类似 DAQ 的“不可行归零”指标，避免模型产出无法部署的方案。

  - 对长链路 Agent 任务（如自动选品、库存规划、物流调度），可借鉴研究链完成率定位失败环节：问题表述、代码实现、结果验证，再针对性加入 RAG 或 self-correction。

  - 与专家解对比时注意信息边界：业务中 Agent 不应假设隐含专家知识，要显式建模信息获取过程，否则会高估条件质量而低估部署风险。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有 OR 基准多从自包含任务描述开始，忽视真实项目中从原始客户材料到专业方案的转化过程。论文构建 OR-License，包含 31 个实例、10 个工业场景，来自价值 368 万美元的付费 OR 项目，保留原始需求、数据、交付格式与信息边界。

**方法关键点**：引入 ORSim 作为受控客户端模拟器，只披露业务事实、不提供 OR 专业知识，用于评估 Agent 的信息获取能力。隐藏评估检查方案可行性，并以专家解为参考比较目标质量。提出 Deployment-Adjusted Quality (DAQ)：不可行方案计零分，可行方案按专家相对质量平均。

**关键结果**：11 个前沿 LLM 搭配 coding-agent harness，若干在条件目标质量上超过专家解，但 DAQ 无人达到 1。最强配置 Claude Code 严格可行性 88.39%，DAQ 0.87。信息获取延续到方案开发与验证阶段；任务均衡的研究链完成率仅 24%-45%，失败主要集中于问题建模与实现环节。
