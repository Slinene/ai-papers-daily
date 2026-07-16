---
title: Self-Evolving Agent Harnesses via Gated Semantic Quality-Diversity
title_zh: 自进化Agent Harness框架：基于语义质量多样性的可信增益
authors:
- Xiaotian Luo
- Fengxingyu Wang
- Chuanrui Hu
- Dizhan Xue
- Yafeng Deng
affiliations:
- EverMind AI
- Shanda Group
arxiv_id: '2607.13683'
url: https://arxiv.org/abs/2607.13683
pdf_url: https://arxiv.org/pdf/2607.13683
published: '2026-07-15'
collected: '2026-07-16'
category: Agent
direction: Agent自进化 · 质量多样性搜索
tags:
- Self-Evolving
- Harness
- MAP-Elites
- Significance Test
- Agent Optimization
- Pathology-Keyed Archive
one_liner: 将修改提议与可信度评估分离，通过统计检验和质量多样性归档实现harness稳健演化，跨七领域密封测试增益+9~+15.5pp
practical_value: '- **可信的Harness优化闭环**：把提示、知识注入、控制流等harness编辑的评估从模型自身剥离，用配对2σ显著性检验在密封测试集上判定增益，部署时可杜绝“幻觉式改进”，适合要求严苛的电商/搜索Agent运维。

  - **病理学驱动的归档（GSME）**：按*(where×why)*（编辑位置×失败原因）维护精英补丁库，支持跨细胞重组，防止搜索坍缩到安全提示微调。在搜索推荐Agent开发中，可借鉴此结构持续积累针对特定失败模式（如过早结束、空
  turn）的修复方案。

  - **诊断与信用分离模式**：强模型负责诊断和提出补丁，确定性代码负责采样、门控和统计检验，这降低了模型错误判断的风险，适合在Agent pipeline中构建自动化的自我改进模块。

  - **跨模型病理-补丁匹配规律**：发现harness增益高度依赖模型自身的失败分布，同一病理可能跨模型家族重现。在多模型部署场景下，可复用*诊断-信用*循环，快速为不同基座模型定制harness，而不是盲搬同一套配置。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**
LLM Agent 的真实表现严重依赖其运行时脚手架（harness）：系统提示、注入知识、控制循环、配置等。部署环境下模型权重冻结，harness 成为唯一可优化杠杆，但手工调整难以规模化。现有自进化方法多依赖噪声反馈，容易过拟合训练任务，无法保证增益可信。该工作旨在构建一个**可信、可泛化**的 harness 自进化循环。

**方法关键点**
1. **分离提议与可信度**：Evovler（更强的模型）诊断冻结 Agent 的失败并生成补丁，但所有**采样、测量、统计检验均由确定性代码执行**，包括：
   - 有效性门控：重跑环境故障，避免将基础设施错误计为模型失败；
   - 激活门控：仅当补丁实际触发时才计入效果；
   - **配对 2σ 显著性检验**：在训练后一次性评估的**密封测试集**上计算，确保提升不是噪声。
2. **Gated Semantic MAP-Elites (GSME) 归档**：
   - 编辑按 *(where×why)* 病理学分类归档，*where* 为 harness 可编辑表面（提示、知识、运行时、配置），*why* 为 LLM 诊断的失败原因；
   - 每单元格保留一个精英，支持跨细胞重组，**病理学键控作为抗过拟合偏置**，避免搜索坍缩到安全提示编辑。
3. **分层候选筛选**：锚点任务 K=1 低成本剔除明显劣化 → 全量 K=3 验证 → 幸存者经三重门控后才算作可信增益；并验证了**树感知分数借用**可减少 67% 的评估试次。

**关键结果**
- 在 terminal-bench-2、LiveCode、Omni-MATH、BrowseComp+、GDPval、AppWorld 六个领域（固定 Qwen3.6-27B），密封测试集增益：**+9~+15.5pp**，训练增益保留率 **86%–147%**（SWE-bench 因样本少未达显著性）。
- 跨模型实验（AppWorld）显示增益是**模型特异**的：同一病理（如 careless）在不同模型上匹配不同补丁（submit-verify checklist），且该匹配跨 Qwen 和 Google 家族再现。
- 消融：选择性恢复比增大 token 预算更有效（LiveCode +14.8pp vs. +6.5pp）；GSME 使最强 harness 多为重组体，编辑覆盖全部四个杠杆而非仅提示。

**核心观点**
Harness 演化本质上是**针对特定模型失败分布的修正补丁拟合**，可信的 diagnose-and-credit 循环才是可迁移资产，而非某个具体配置。
