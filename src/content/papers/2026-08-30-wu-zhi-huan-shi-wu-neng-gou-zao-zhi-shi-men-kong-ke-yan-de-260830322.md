---
title: Ignorance or Incompetence? Constructing Knowledge-Gated, Verifiable Tasks for
  LLM Agents
title_zh: 无知还是无能？构造知识门控、可验证的 LLM Agent 任务
authors:
- Hanlin Tian
- Minhao Li
- Yu Mi
- Sihan Zhu
- Zhao Yang
- Yuxiang Wang
- Hongquan Zhu
- Qiufei Hu
affiliations:
- DataGrids
- Shanghai University
- Peking University
- Northwestern Polytechnical University
- Nanyang Technological University
arxiv_id: '2608.30322'
url: https://arxiv.org/abs/2608.30322
pdf_url: https://arxiv.org/pdf/2608.30322
published: '2026-08-30'
collected: '2026-09-05'
category: Other
direction: LLM Agent 任务构造与评估
tags:
- knowledge gating
- agent evaluation
- task construction
- verifiable rewards
- LLM agents
one_liner: 提出知识门控任务构造协议，分离任务指令与私有工件，通过溯源与可执行见证验证知识依赖
practical_value: '- 用于内部 Agent 评测：把任务指令与领域私有规则/参考表/工具算子分离，在“提供 vs 不提供工件”两种条件下保持指令字节一致，可区分
  agent 是缺知识还是缺能力，适合电商 SOP、价格策略、客服话术等私有约定场景。

  - 用 deterministic solver 或规则语料生成结构化任务的精确 ground truth，避免 LLM judge 波动；对不可单一可执行 oracle
  判定的自由文本输出，采用命名 criterion-level rubric 分项考核，比整体打分更稳定。

  - 借鉴 leak audit 和 plausible-but-incorrect artifact 作负向控制：在构建企业私有 RAG/Agent 评测集时，检查是否存在数据泄漏，并加入“看似合理但错误”的知识工件，确保模型真的依赖给定知识而非记忆或猜测。

  - 小样本配置相对校准（如五试验经验门槛）可低成本淘汰不可靠任务，适合在业务迭代中快速筛选高质量评测样本，不必等全量评估。'
score: 6
source: huggingface-daily
depth: abstract
---

动机：专业 agent 任务经常依赖公共语料中不存在的内部约定、规则和表格，但现有基准很少控制 agent 是否拥有这些知识，导致无法区分其失败是“不知道”还是“不会用”。

方法关键点：论文提出知识门控任务构造协议，将任务指令与一个紧凑工件分离，工件包含私有约定、参考表和工具算子。通过构造时溯源、在提供/不提供工件两种条件下保持任务指令字节一致、泄漏审计和可执行见证，使任务对工件的依赖明确可测。结构化任务用确定性求解器和规则语料提供精确 ground truth；难以用单一可执行 oracle 判定的输出，采用命名准则级 rubrics。还引入配置相对校准筛选，保留满足五试验经验知识门控的任务。

关键结果：在 15 个校准任务上，一种前沿 agent 配置带工件通过率为 68.0%，不带工件为 0%；某个任务提供看似合理但错误的工件时，五试验通过率也为 0%。最终保留 7 个任务。作者强调实验验证的是任务构造协议行为，未证明这些任务能改善后训练。
