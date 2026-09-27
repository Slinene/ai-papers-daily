---
title: 'SEEK: Skill-Routed Evaluation with Evolvable Knowledge for Industrial Search'
title_zh: SEEK：工业搜索中技能路由与可演化知识的评估框架
authors:
- Zhongxin Huang
- Songyang Li
- Renzhe Zhou
- Feiran Zhu
- Chenglei Dai
- Zhen Xiao
- Xuanping Li
- Jingwei Zhuo
affiliations:
- Peking University
- Kuaishou Technology
arxiv_id: '2609.29803'
url: https://arxiv.org/abs/2609.29803
pdf_url: https://arxiv.org/pdf/2609.29803
published: '2026-09-24'
collected: '2026-09-27'
category: Eval
direction: LLM-as-a-Judge 搜索质量评估
tags:
- Search Evaluation
- LLM-as-a-Judge
- Skill Routing
- Listwise Modeling
- Self-Evolving
one_liner: 提出 SEEK 框架，将搜索评估标准外部化为技能库，动态路由相关技能进行列表级评估与归因，并支持不重训模型的知识更新
practical_value: '- **技能化评估标准**：将多维度评估规则拆成独立技能（路由描述+操作指南），通过轻量路由器为每个样本选择相关子集，避免全量规则塞入
  prompt 导致的上下文冗余和标准干扰。业务中可用于搜索/推荐结果的自动评测，尤其适合规则多且频繁更新的场景。

  - **外部知识更新机制**：评估标准变化时只需修订技能银行的指南，冻结模型参数，通过重放验证保证不损害历史性能。这实现了轻量级快速迭代，无需重新训练评估 LLM，适合业务规则频繁调整的电商/广告场景。

  - **两阶段训练 + 层次化奖励**：先用教师模型生成证据轨迹和路由标签，再 SFT + DAPO 强化学习，奖励包含最终判断、技能诊断质量、冲突惩罚，提升列表级判断与归因一致性。可借鉴用于训练内部
  LLM-as-a-Judge，提高诊断可解释性。

  - **生产可行性**：LLM 评估在 24k 样本上达 0.842 准确率，比外包审核高 5.9 个点，耗时仅 0.9 小时（40 倍提速），说明可替代人工评估作为大规模质量监控和故障分析工具。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：工业搜索评估需页面级判断和归因，人工成本高且难以覆盖长尾；直接使用 LLM 会因打包所有标准导致上下文冗余和准则干扰，而通过后训练内化知识则使规则更新绑定模型重训。

**方法关键点**：
- 技能银行：将评估标准外化为 12 个诊断技能，覆盖相关性、质量、多样性、权威性、异质性五维度，每个技能包含路由描述和操作指南；
- 动态路由：轻量路由器为每个 query–result list 选择相关技能子集，平均 3.4 个技能，远少于全量 12 个；
- 列表级评估器：输入查询-结果页和选中技能指南，生成 good/fair/bad 页面标签和结构化归因；
- 两阶段训练：教师模型生成路由标签和证据轨迹，路由器多标签分类训练，评估器 SFT 后接 DAPO，层次化奖励包含任务正确性、技能诊断质量、冲突惩罚；
- 自演化技能银行：对生产反馈进行失败归因（路由错误/知识错误/执行错误），仅知识错误触发局部技能修订，并用重放门控验证保证历史稳定性。

**关键结果**：在快手 169k 训练、17k 测试数据上，SEEK 三维分类 Macro-F1 0.6555，优于同基座 SFT+GRPO 的 0.6418 和 GPT-5.6 Sol 的 0.6378；二元准确率 0.752；归因召回四个维度最佳。冻结模型仅更新技能库在持续适应中达到 Binary F1 0.7921，接近模型更新 0.7957，且遗忘仅 0.0008 vs 0.0076。生产评估 24k 样本准确率 0.842，超过外包审核 0.783，耗时 0.9 小时，提速 40.6 倍。

最值得记住：能力与知识分离——将评估知识外部化为可演化技能库，通过动态路由和局部修订实现快速适应，避免频繁重训评估模型。
