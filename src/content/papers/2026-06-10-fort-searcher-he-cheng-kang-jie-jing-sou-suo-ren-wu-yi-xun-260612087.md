---
title: 'FORT-Searcher: Synthesizing Shortcut-Resistant Search Tasks for Training Deep
  Search Agents'
title_zh: FORT-Searcher：合成抗捷径搜索任务以训练深度搜索智能体
authors:
- Jia Deng
- Yimeng Chen
- Xiaoqing Xiang
- Ziyang Zeng
- Shuo Tang
- Wayne Xin Zhao
- Feng Chang
- Chuan Hao
- Yuan Wei
- Ran Tao
affiliations:
- Renmin University of China
- KAUST
- IQuest Research
- Shanghai Jiao Tong University
arxiv_id: '2606.12087'
url: https://arxiv.org/abs/2606.12087
pdf_url: https://arxiv.org/pdf/2606.12087
published: '2026-06-10'
collected: '2026-06-11'
category: Training
direction: 深度搜索Agent训练数据合成
tags:
- Shortcut-Resistant
- Data Synthesis
- Search Agent
- Supervised Fine-Tuning
- Trajectory Signatures
- Evidence Graph
one_liner: 提出抗捷径数据合成框架 FORT，通过控制证据共覆盖、单线索选择性等风险生成高难度搜索轨迹，仅用 SFT 训练即可在深度搜索基准上取得最优。
practical_value: '- **捷径风险检查**：在构造多步推理任务（如电商知识问答、商品溯源）时，应主动检查证据是否被同一条搜索结果覆盖、单条线索是否过于特化、表面文本是否泄露了中间关键实体，防止模型绕过搜索直接作答。

  - **对抗验证与自动修复**：利用强 Agent 对合成题目进行“试跑”，根据轨迹中的答案命中时间、先验绑定率等指标自动诊断并修复易走捷径的题目，可用于生成高质量
  Agent 训练数据，类似方法在推荐解释生成查询中同样适用。

  - **模糊化策略**：问题表述时用范围、类别、元属性代替精确值，可迫使模型进行多跳检索，这一思路可迁移到生成式推荐中的语义 ID 构建或查询改写，强化模型的信息获取能力。

  - **上下文重置机制**：当 Agent 陷入低效搜索时，清空历史并重启可显著提升复杂任务的成功率（在 BrowseComp 上提升 16.3 点），可作为
  Agent 推理系统中的兜底策略。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**：现有深度搜索数据合成方法依赖结构复杂度（如跳数、图形状），但实际执行时，智能体常通过证据共覆盖、单线索高选择性、问题表面暴露常量或直接调用先验知识等捷径，大幅缩减需要的搜索步数，导致训练数据无法有效激励长程信息获取。该文将此类现象形式化为捷径感知难度框架，并提出主动控制捷径风险的数据合成方法。

**方法关键点**：
- 定义四种可量化捷径风险：证据共覆盖（一条证据验证多个约束）、单线索选择性（单条线索即可识别答案）、暴露常量（问题直接给出中间实体名/精确值）、先验知识绑定（模型在检索证据前给出答案）。
- 设计 FORT 框架，分四阶段控制：① 实体选择：偏好长尾实体、用预挖掘的循环结构初始化证据图，减少先验绑定与常量暴露；② 证据图构建：多源采集分散证据、构造派生事实（如巧合桥接、计数聚合）、选择通用事实而非代表性事实，降低共覆盖和线索选择性；③ 问题表述：隐藏中间实体名、对精确值使用范围放松/元属性描述等五种模糊化策略，阻止查询可直接执行；④ 对抗优化：用强 Agent 试解，根据轨迹签名（答案命中时间、先验捷径率）自动化修复捷径易走或过度模糊的题目。

**关键实验**：以 Qwen3-30B-A3B（激活约 3B 参数）为基座，仅用 FORT 合成轨迹做 SFT，在 BrowseComp、BrowseComp-ZH、xbench-DeepSearch 等五个深度搜索基准上评估。可比规模开源 Agent 中，FORT-Searcher 总体平均分 66.2，超过 MiroThinker-1.7-mini（64.6）和 Qwen3.5-35B-A3B（59.9）；BrowseComp 上达 72.2（+4.3），BrowseComp-ZH 上达 75.0（+2.7），且超过部分更大规模开源模型。轨迹分析表明，FORT 数据使答案前搜索步数大幅增加（命中时间 47.0 vs 同类轨迹长度下的 22.3），先验捷径率降至 11.4%。
