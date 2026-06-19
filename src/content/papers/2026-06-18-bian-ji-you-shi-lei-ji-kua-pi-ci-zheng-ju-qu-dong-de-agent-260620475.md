---
title: Marginal Advantage Accumulation for Memory-Driven Agent Self-Evolution
title_zh: 边际优势累积：跨批次证据驱动的 Agent 记忆自进化
authors:
- Mingyu Yang
- Keye Zheng
- Congchao Cheng
- Yujie Liu
- Xingkang Lu
- Fan Jiang
- Yefei Zheng
affiliations:
- Alibaba International Digital Commerce Group
arxiv_id: '2606.20475'
url: https://arxiv.org/abs/2606.20475
pdf_url: https://arxiv.org/pdf/2606.20475
published: '2026-06-18'
collected: '2026-06-19'
category: Agent
direction: Agent 记忆自进化 · 跨批次证据累积
tags:
- Marginal Advantage Accumulation
- Agent Self-Evolution
- Trace Distillation
- Offline Memory Optimization
- EMA Evidence Accumulation
- Semantic Identity Merging
one_liner: 通过差分信号与 EMA 累积跨批次操作级证据，解决离线记忆蒸馏中的信号矛盾问题
practical_value: '- **记忆更新的离线优化范式**：当 agent 需要从历史执行痕迹中抽取可复用记忆（如电商导购策略、广告投放流程模板），可采用
  MAA 的‘提案-评分-差分-EMA 累积’流水线，完全避免线上 rollout 的高成本，适合高延迟、高成本的真实业务环境。

  - **差分评估消除批次混杂**：直接把操作评分作为优化信号容易受批次难度影响，借鉴 MAA 的‘同一批次内 baseline 与候选同步打分再求差’的设计，可得到跨批次可比的操作优势方向信号。在推荐
  agent 的策略搜索中，可以用 LLM 对候选策略与当前策略在同一批请求上同时打分再差分，得到更干净的优化方向。

  - **基于语义合并的跨批次操作追踪**：对 agent 输出的文本操作（如改写规则、新策略片段），可通过 embedding 相似度合并语义等价的候选项，避免因表述差异导致的证据碎片化。该技巧可直接用于线上记忆管理系统的操作去重与合并。

  - **EMA 证据累积与三种操作模式识别**：通过 EMA 跟踪每个操作的边际优势，可以自动区分‘稳定有效’、‘虚假相关’和‘场景特定’三类操作，实现安全的离线记忆演化。在搜索广告的查询改写记忆或
  prompt 库优化中，可避免单次正样本就把噪声策略写入长期记忆。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

## 动机
在 Agent 自进化中，离线轨迹蒸馏是主流范式：从历史执行轨迹中压缩出可复用的记忆（如规则、技能片段）注入后续推理。但一个根本问题被忽略——同一操作在不同批次可能收到相反反馈（如“补充坐标轴标签”在二维图批次有用，在热力图批次有害），而现有方法仅在单批次内做决策，缺乏跨批次的操作级证据累积机制，导致无法区分稳定有效的操作与偶然命中。任务越复杂、轨迹越长，该问题越严重。

## 方法关键点
MAA 将问题形式化为两大结构需求：**可对齐性**（跨批次识别同一操作）与**可比性**（跨批次信号可加和）。以此为设计原则：
- **地址化记忆库与语义身份合并**：每个操作由 (类型, 锚点 ID, 内容嵌入) 标识，新候选与已有单元余弦相似度 ≥0.85 时合并，避免表述差异造成的证据碎片。
- **边际优势差分构造**：对当前批次，Score 通道以 LLM 并排评估 baseline 记忆与施加候选操作后的记忆，通过差分 `δ = u(M_i, B) - u(M, B)` 将绝对评分转化为相对 baseline 的边际优势，消除批次难度混杂，使跨批次信号可比。
- **跨批次 EMA 累积**：对每个操作维护 EMA (β=0.9)，跨批次累加差分信号。方向一致的信号被放大，方向交替的信号正负抵消，并在偏置校正后稳定到真实方向。
- **候选池管理与 top-k 更新**：按累积量排序，仅应用 top-k 个正优势操作，设置生存时间与下界淘汰，结合验证集最佳检查点回滚。
方法完全离线，不用线上 rollout，仅凭现有轨迹与 LLM 代理评分驱动，计算成本仅为在线方法的约 1/4。

## 关键实验
在 ScienceAgentBench、ALFWorld、SpreadsheetBench、HotpotQA 四个基准上，测试 Qwen3.7‑Max、Qwen3.6‑Flash、GPT‑5.4、DeepSeek‑V4‑Flash 四个模型，对比冻结基线、单次蒸馏、反应式更新、Trace2Skill、在线方法 SkillOpt。**MAA 在 16 个设置中取得 14 个最优**，在强模型上全面超越 SkillOpt（如 GPT‑5.4 科学任务 +0.9 pp），且优化阶段 token 消耗减少约 75%，训练时间从 12‑14 小时缩至 2.5 小时。
消融显示，差分构造是主要增益来源，连续幅度提供额外排名精度。方向诊断表明差分符号的一致性达 88.7%‑95.1%，与真实增益方向对齐准确率 61.5%‑73.8%，为 EMA 收敛提供基础。证据轨迹生动展示了稳定有效、虚假相关、场景特定三类操作的累积曲线。

**最值得记住的一句话：通过差分将绝对评分转化为跨批次可比的边际优势，再以 EMA 累积操作级证据，让 Agent 记忆演化首次拥有“假设检验”能力，不再被单批次噪声误导。**
