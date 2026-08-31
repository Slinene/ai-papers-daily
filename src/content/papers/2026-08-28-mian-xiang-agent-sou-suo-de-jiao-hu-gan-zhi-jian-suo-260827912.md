---
title: 'ITER: Interaction-Aware Retrieval for Agentic Search'
title_zh: 面向 Agent 搜索的交互感知检索
authors:
- Haodong Chen
- Shuai Wang
- Yu Yin
- Shengyao Zhuang
- Guido Zuccon
- Teerapong Leelanupab
affiliations:
- The University of Queensland
arxiv_id: '2608.27912'
url: https://arxiv.org/abs/2608.27912
pdf_url: https://arxiv.org/pdf/2608.27912
published: '2026-08-28'
collected: '2026-08-31'
category: Agent
direction: Agent 搜索 · 交互感知稠密检索
tags:
- Agentic Search
- Dense Retrieval
- Interaction-Aware
- Trajectory Learning
- Deep Research
- Contrastive Learning
one_liner: 提出交互感知检索器 ITER，用历史查询与轨迹相对监督提升 Agent 搜索证据发现
practical_value: '- 在电商/导购 Agent 的召回或重排中，可将「主需求 + 当前 query + 已尝试 query 序列」作为排序输入，显式告知模型已探索方向；即使不换模型，也能减少已看商品/答案的重复置顶，优先曝光能补充新信息的候选。

  - 从用户或 Agent 轨迹构造三层负样本：已点击且有效作为冗余负样本（最高权重，如 3.0），已点击无效作为困难负样本（1.0），曝光未点击作为弱负样本（0.3）。这比传统随机负采样更贴合“边际增益”目标，适合精排/重排阶段。

  - 工程上可采用去重式结果接口：把已曝光/已点击的 item 移到侧栏但仍可访问，不占主列表坑位，从而提高后续 step 的新候选覆盖率；论文中该设置带来 26.7%
  的延迟访问正样本，对推荐/搜索 Agent 同样有借鉴意义。

  - 跨模型迁移时，避免把 free-form pre-search reasoning 作为核心特征；不同 LLM 表达差异大，AgentIR 虽然 search
  recall 高但 task success 不稳。结构化历史（主 query + 子 query 序列）具有更好的跨 backbone 鲁棒性，更适合多模型混用的线上环境。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：Deep-research Agent 需要多轮检索，但现有 retriever 只输入当前子查询，不感知已经搜过什么、看过什么，导致已访问文档反复占据高位，新证据被挤出 top-k。文档效用应随轨迹变化，由边际增益定义。

**方法关键点**：
- ITER 将 main question、当前 sub-query、历史 sub-queries 拼接成 history-conditioned query；默认不加入 visited docs 或 reasoning，因为 visited docs 会与冗余负样本冲突且跨模型不稳。
- 训练信号来自去重检索界面的 agent trajectory：把当前步后访问且被 LLM 判定 relevant 的文档作为正样本；负样本分三层——之前访问且 relevant 的文档作为 redundancy negatives（权重 3.0）、之前访问但 irrelevant 作为 hard negatives（1.0）、本步返回但从未访问作为 weak negatives（0.3）；用带 logit offset 的对比损失。
- 训练数据：10k InfoSeek 问题 × 4 个检索后端得到 40k trajectories，保留 20,893 个最终正确的轨迹，共 67,934 positive pairs。

**关键结果**：匹配 backbone（Tongyi-DeepResearch-30B）下，默认 ITER 在 InfoSeek-Eval 任务成功率 80.0 vs LRAT 72.7、SQ-only 76.7；BrowseComp-Plus 46.6 vs 43.4 / 43.7。跨 6 个 agent backbones，12/12 比较优于 LRAT，7 个显著；平均提升 InfoSeek-Eval +5.4，BrowseComp-Plus +4.3，且对 5 个未见 agent 任务成功率均高于 AgentIR。消融显示去掉 redundancy negatives 使 BrowseComp-Plus SR 从 46.6 降至 40.8；把 visited docs 加入 query 也明显掉点。

**最值得记住**：检索不应只优化单步相关性，而应优化轨迹中的边际增益；用历史子查询表示探索状态、用文档访问构造冗余负样本，是最稳的两个设计。
