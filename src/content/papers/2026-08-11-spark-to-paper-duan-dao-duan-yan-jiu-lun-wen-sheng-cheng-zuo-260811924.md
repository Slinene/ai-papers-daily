---
title: 'Spark-to-Paper: End-to-End Research Paper Generation as a Composable Skill'
title_zh: Spark-to-Paper：端到端研究论文生成作为可组合技能
authors:
- Zhuoyang Qian
- Biao Wu
- Yiran Wang
- Chris D Yan
- Desan Dai
- Liangwei Zheng
- Jin Jiang
- Junsheng Zhang
- Wenhao Wang
affiliations:
- Vast Intelligence Lab
- University of Technology Sydney
arxiv_id: '2608.11924'
url: https://arxiv.org/abs/2608.11924
pdf_url: https://arxiv.org/pdf/2608.11924
published: '2026-08-11'
collected: '2026-08-14'
category: Agent
direction: Agent 可组合技能与长程生成
tags:
- Agent Skills
- Long-horizon Generation
- Self-Refutation Loop
- Citation Validity
- Figure Editability
- Deterministic Checks
one_liner: 在现有编码助手中以13个可组合技能实现端到端论文生成，靠分离规划与报告、确定性校验抑制自我反驳循环
practical_value: '- 在电商/广告实验分析与自动化报告中，借鉴“先定义证据指标，再根据结果生成结论”的模式：把 AB 实验报告、选品实验摘要和推荐效果分析拆成规划阶段与报告阶段，避免
  LLM 编造显著性结论。

  - 借鉴“确定性校验 + 自我批评”双轨：生成商品推荐理由、搜索词解释或广告文案时，对商品 ID、价格、库存、事实声明做可执行校验（查库/规则），再用 LLM
  自评修正，可显著降低幻觉。

  - 借鉴可组合技能而非重型多智能体平台：在现有代码助手或工作流引擎内，将选品、query 生成、素材审核等封装成原子技能，便于复用、版本管理与成本控制；该论文给出
  13 技能、11.9M tokens、$8.1/次的量化成本参考。

  - 注意长链路探索中的“自我反驳循环”：在自动调参、自动选品、策略探索 Agent 中设置目标维持预算和停止条件，当连续实验否定初始目标时切换到确定性审查或终止，防止无限烧
  token。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：研究想法到完整论文需要文献检索、实验设计执行、按证据修改声明、图表生成与长程一致性，单次文本生成不够。

**方法**：Spark-to-Paper 在现有 coding assistant 内实现 13 个可组合技能，无独立 agent 平台。关键分离：模型判断 vs 确定性操作（可直接执行检查）；实验规划 vs 报告，先指定所需证据再观察结果，避免声明漂移。可靠性方面组合确定性完整性校验与自我批评，并界定“自我反驳循环”失败模式，限制反复实验持续否定原目标。图表生成：实验图用程序化绘图，方法图用代码重建矢量图。

**结果**：8 个受控主题上 99.5% 引用有效，96.4% 图可编辑；受控消融中完整校验栈把虚构检测从单稿 14% 提升到 92%；对抗评审精确率 74%；完整系统平均 11.9M tokens、$8.1、3.2 小时。
