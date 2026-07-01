---
title: Generative Skill Composition for LLM Agents
title_zh: LLM Agent 的生成式技能组合
authors:
- Xinyu Zhao
- Zhen Tan
- Vaishnav Tadiparthi
- Nakul Agarwal
- Kwonjoon Lee
- Ehsan Moradi Pari
- Hossein Nourkhiz Mahjoub
- Tianlong Chen
affiliations:
- University of North Carolina at Chapel Hill
- Arizona State University
- Honda Research Institute USA
arxiv_id: '2606.32025'
url: https://arxiv.org/abs/2606.32025
pdf_url: https://arxiv.org/pdf/2606.32025
published: '2026-06-30'
collected: '2026-07-01'
category: Agent
direction: 生成式技能组合 · 任务条件序列预测
tags:
- Skill Composition
- LLM Agents
- Structured Prediction
- Autoregressive Decoder
- Skill Library
- Code Agent
one_liner: 将技能组合建模为任务条件序列预测，用小型解码器联合决定技能子集、数量和顺序，兼顾精度与效率
practical_value: '- 可将推荐/广告系统的模块组合（如多路召回、策略组合）建模为任务条件序列生成，联合决定 Which/How many/Order，比单独检索或人工编排更准。

  - 冻结通用编码器+微型自回归解码器（3.9M）架构，参数极少、推理快，适合线上实时服务，可直接替换现有检索式路由。

  - 解码时引入 TF‑IDF 检索先验与集合成员先验，有效解决长尾模块选择，业务中可复用 BM25 或自定义相关性分作为 prior。

  - 利用模块依赖图自动合成训练数据，减少人工标注成本；电商场景可构建召回→粗排→精排→重排的模块图来生成序列样本。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机

LLM 代理在复杂任务中需要从大型技能库中选择合适的技能并确定执行顺序。现有方法要么让代理直面全部技能进行隐式推理，要么用检索返回无序技能子集，均忽略技能间的依赖与编排，导致组合误差。这个瓶颈在真实软件工程任务中直接影响代理成功率。

### 方法关键点

- **问题形式化**：将技能组合视为任务条件的技能序列预测，输出技能索引序列与 STOP 符，同时决定技能子集、所需数量和执行顺序。
- **SkillComposer 架构**：冻结文本编码器（Qwen3-Embedding-0.6B）将任务与技能元数据编码为稠密向量，3 层 Transformer 解码器（256 维，3.9M 参数）自回归生成索引。
- **辅助头监督**：基数头预测技能数量，集合头对每个技能做二分类打分，提供独立的“需哪些技能”和“需多少个”信号，缓解自回归训练的位置稀疏监督问题。
- **检索增强解码**：每步融合 TF‑IDF 任务‑技能相关性和集合头打分作为先验，显著提升长尾技能选择能力。
- **数据构建**：基于真实人工技能库，先建立技能依赖图，再生成单技能和多技能合成任务，得到 9,872 条任务‑序列对，覆盖依赖边与工作流边两种顺序监督。

### 关键结果

- **分布内测试**：SkillComposer 取得 Set F1 73.9%，以 **3.9M 参数** 超过全参数微调的 Qwen3‑0.6B（600M）的 71.1%，并大幅领先检索与 LLM‑judge 基线。
- **真实任务泛化**：在保留的真实软件工程任务上，SkillComposer 的 Set F1 达到 62.9%，比 SFT 基线高 **+19.3pp**，验证了冻结编码器+小解码器的强泛化能力。
- **下游执行效果**：在 GPT‑5.2‑Codex 上，SkillComposer 将 pass rate 从无技能时的 22.2% 提升至 **45.3%**，超过 top‑3 检索的 44.0% 且接近 gold 检索上界（44.0%），同时 prompt 消耗最低（1.03M tokens）。
- **消融确认**：移除集合头或检索先验分别导致 7.1pp 与 4.6pp 的 Set F1 下降；TF‑IDF 先验优于稠密向量，更适合短技能名的高精度匹配。
