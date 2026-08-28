---
title: 'CaSKG: Counterfactual-Causal Skill Graphs for Scalable Agent Skill Retrieval'
title_zh: CaSKG：面向可扩展 Agent 技能检索的反事实因果技能图
authors:
- Zhiyuan Li
- Linyuan Gao
- Xuechun Ding
- Hongwei Chen
- Yuan Wu
- Yi Chang
affiliations:
- Jilin University
- Ant Group
arxiv_id: '2608.25500'
url: https://arxiv.org/abs/2608.25500
pdf_url: https://arxiv.org/pdf/2608.25500
published: '2026-08-25'
collected: '2026-08-28'
category: Agent
direction: Agent 技能图构建与图谱化检索
tags:
- skill graph
- counterfactual probing
- LLM agents
- Bayesian calibration
- personalized PageRank
one_liner: 用反事实因果探针校准技能图边置信度，在六模型两基准上全面超越 GoS 等检索基线
practical_value: '- 技能/工具库检索可拆成“高召回候选图 + 预算化边校准 + 状态门控发布”：先在离线阶段用多信号（语义、词法、I/O、结构）挖出候选边，再用有限
  LLM 预算只验证高价值边，线上只做轻量图传播；电商 Agent 工具库、SOP 流程库可以直接复用。

  - 用 LLM 反事实探针评估方向性依赖：对候选边做 remove/substitute/reorder 三类文本探针，能比相似度/共现更可靠地区分“前置依赖”和“只是相关”，适合做工具/API
  前置条件、状态变更、校验步骤的边质量评估。

  - 发布图时采用 confirmed/uncertain/rejected/scaffold 四态权重，而不是全量发布所有候选关系；可避免弱边在图传播中污染上下文，推荐/搜索知识图谱的边精选也可借鉴。

  - 在线检索用 query seed + personalized PageRank 在可靠性加权图上扩展，返回紧凑技能包；相比全文库塞入和纯向量检索，既省 context
  又能补回非字面相关但流程必需的技能，适合 LLM prompt 组装。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：技能库变大后，Graph retrieval 通过关系传播恢复 workflow context，但边质量决定检索质量；语义相似、共现或接口兼容边常常只是“看起来相关”，并不代表操作性依赖。因此问题不是建更大的图，而是决定哪些边该参与传播。

**方法关键点**：
- 候选图 induction：多信号（semantic、lexical、I/O、structural）高召回构建有向候选边，repair evidence 和可选 LLM judge 进一步 refine。
- 反事实探针：对每条候选边做三类方向一致测试——移除源技能、替换为低重叠技能、逆序；LLM 给 support score，分别度量 necessity、specificity、order dependence。
- Beta 平滑校准：将探针分数转为二元极性 + 距离质量，再用 Beta-form accumulator 得到 reliability score。
- 状态门控发布：confirmed / uncertain / rejected / unvalidated scaffold 四态权重，而不是全量发布候选边。
- 线上检索：query lexical/semantic seeds 初始化，personalized PageRank 在已发布图上传播，返回紧凑技能包，不改变下游 agent 策略。

**关键实验**：在 ALFWorld ID-140 和 ScienceWorld U211 上，联合六 LLM 骨干对比 Vanilla、Vector、GoS。CaSKG 在 12 个 model-benchmark 组合全部最高；相对 GoS，ScienceWorld 六模型平均分 72.62→80.50，ALFWorld success 80.01%→86.79%，同时平均环境步数更低。消融显示：semantic-only 候选 67.14 vs full 73.57；全量发布候选 71.43 vs 73.57；去掉 LLM judge 71.43 vs 73.57。

**最值得记住的一句话**：把边置信度校准作为可扩展技能检索的有效路径——先高召回构建候选图，再用反事实探针确认方向性依赖，最后在状态门控发布图上做 query-conditioned 扩展。
