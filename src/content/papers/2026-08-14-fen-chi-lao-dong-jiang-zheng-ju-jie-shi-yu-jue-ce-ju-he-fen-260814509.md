---
title: 'Split the Labor: Separating Evidence Interpretation from Decision Aggregation'
title_zh: 分离劳动：将证据解释与决策聚合分开
authors:
- Zhelun Wu
affiliations:
- Atlassian
arxiv_id: '2608.14509'
url: https://arxiv.org/abs/2608.14509
pdf_url: https://arxiv.org/pdf/2608.14509
published: '2026-08-14'
collected: '2026-08-17'
category: LLM
direction: LLM 多源证据聚合与决策架构
tags:
- evidence aggregation
- decision making
- LLM
- calibration
- reliability
- reasoning
one_liner: 提出将证据解释与决策聚合分离，用四字段证据元组和校准对数似然比池化解决计数尺度漂移
practical_value: '- 在电商/推荐系统的多源信号融合中，将 LLM 的“证据读取”与“决策聚合”拆开：每个证据输出结构化 tuple（hypothesis,
  reliability bucket, rationale, provenance），后续用固定算术融合，便于溯源和跨场景复用。

  - 避免简单对多路召回得分、多策略 CTR 预估等做未归一化加权求和或投票阈值，因为阈值会随证据数量漂移；改用校准后的对数似然比池化（或等效的后验阈值），使决策一致且可比。

  - 对不可靠来源（如弱标注、用户生成内容）先做可靠度分桶，再参与聚合，可降低噪声主导风险；该 bucket 可作为先验指导模型对不同证据的信任程度。

  - 在 Agent 决策链中，将最终决策与中间证据解释分离，便于调试、审计和动态调整证据集；架构上无需大改，只需改变聚合的算术方式。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：主流 LLM 决策系统常把所有证据源拼接进一个 prompt，混淆了两种需求——解释证据需要模型容量和上下文，组合证据需要固定算术、跨实例可比性和可返回空。这种混淆导致溯源困难、决策不一致。

**方法**：提出将系统拆为两个阶段：证据解释与决策聚合。接口定义为一个四字段证据元组（假设、可靠度分桶、理由、来源），固定该接口即确定两端的实现。分离后暴露出“计数尺度漂移”问题：对未归一化权重求和再做阈值判定，工作点随证据数量滑动；当信源可靠度不同，投票规则与后验排序矛盾，无法用单一阈值调和。解决办法是对校准后的对数似然比进行池化，这是一项算术修复而非架构修复，可推广到分数求和分诊引擎、诊断面板等非 LLM 系统。

**结果**：在一个纵向语料上实例化两次：结果解决后按“读取”划分，结果解决前按“学习容量”划分。第二次实例中，小序列编码器执行辅助目标 + 树集成承载删失生存损失，AUPRC 达到 0.921，对比手工基线 0.805。论文还分离了可迁移组件与需按域重新估计的组件，并给出可证伪预测与负结果。
