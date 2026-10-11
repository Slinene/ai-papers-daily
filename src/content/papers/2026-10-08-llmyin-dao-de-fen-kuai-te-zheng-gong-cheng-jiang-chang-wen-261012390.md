---
title: 'Long Text to Predictive Features: LLM-Guided Blockwise Feature Engineering
  via Executable Program Search'
title_zh: LLM引导的分块特征工程：将长文本转化为可执行预测特征程序
authors:
- Ziming Dai
- Dabiao Ma
- Ziheng Guo
- Jack Dong
- Zimu Zhou
affiliations:
- City University of Hong Kong
- Qfin Holdings, Inc.
- Tianjin University
- Carnegie Mellon University
arxiv_id: '2610.12390'
url: https://arxiv.org/abs/2610.12390
pdf_url: https://arxiv.org/pdf/2610.12390
published: '2026-10-08'
collected: '2026-10-11'
category: LLM
direction: LLM 驱动的自动化特征工程 · 程序合成
tags:
- Automated Feature Engineering
- LLM
- Program Synthesis
- Blockwise Search
- Risk Control
one_liner: LLM-BlockFE离线把长文本构造成可执行特征程序，在线零LLM调用，用带回滚和并行轨迹的分块搜索提升特征质量
practical_value: '- **在线零 LLM 调用**：在推荐/搜索/广告的高 QPS 场景，把 LLM 仅用于离线生成特征代码块，线上只执行提取逻辑，避免大模型推理时延与成本。适合处理商品评论、用户反馈、搜索日志等长文本，转化为可复用结构化特征。

  - **可解释且可维护的特征工程**：生成的是可执行代码块而非黑盒向量，便于沉淀到特征平台、版本管理和审计，满足风控、广告审核等强合规场景。

  - **块级回滚与多轨迹搜索**：用 depth-calibrated credit allocation 识别低质量代码块并回滚，减少贪心搜索局部最优；交错推进多条搜索轨迹共享方向描述，降低冗余探索，适合在特征探索阶段降低
  LLM 调用次数与成本。

  - **业务迁移方向**：可用于电商退货/纠纷预测、广告点击转化中的文本信号提取，例如从商品标题和评论中自动构造用户意图、质量风险、价格敏感度等特征，替代部分人工特征工程。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：工业风险控制等预测系统要求低延迟和可维护性，依赖结构化数据模型，但大量有效信息隐藏在长文本中。人工特征工程成本高，在线让 LLM 处理每条实时输入又会带来延迟和算力问题。

**方法关键点**：LLM-BlockFE 在离线阶段将长文本转化为可执行特征程序，在线只运行程序抽取结构化特征。构造过程按不可变代码块增量追加，用下游模型评估候选特征。为解决普通贪心搜索易陷入局部最优，引入块级回滚机制，通过 depth-calibrated credit allocation 对代码块贡献进行回溯评估；同时以交错方式推进多条独立搜索轨迹，并通过共享固定探索方向描述减少冗余探索。最终冻结并部署搜索得到的特征程序。

**关键结果数字**：在 2 个公开数据集和 2 个私用数据集上，相对各数据集最强基线的 AUC 绝对提升为 0.0069–0.0358；在 5 个已上线金融风控应用中，相比现有人工策略，KS 绝对提升 0.02–1.56 个百分点。
