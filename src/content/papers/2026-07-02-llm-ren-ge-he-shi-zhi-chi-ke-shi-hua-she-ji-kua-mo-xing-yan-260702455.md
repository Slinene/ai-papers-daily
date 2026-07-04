---
title: When Do LLM Personas Support Visualization Design? A Cross-Model Study of Color
  Assignment and Chart Choice
title_zh: LLM 人格何时支持可视化设计？跨模型颜色分配与图表选择研究
authors:
- Shahreen Salim
- Klaus Mueller
affiliations:
- Stony Brook University
arxiv_id: '2607.02455'
url: https://arxiv.org/abs/2607.02455
pdf_url: https://arxiv.org/pdf/2607.02455
published: '2026-07-02'
collected: '2026-07-04'
category: LLM
direction: 评估 LLM 人格模拟的可靠性
tags:
- LLM Persona
- Big Five
- Color Assignment
- Chart Choice
- Model Dependence
- Task Framing
one_liner: 评估 LLM 人格模拟在可视化设计中的稳定性，发现模型依赖性强，任务上下文比人格更能决定选择
practical_value: '- 用 LLM 模拟用户人格辅助设计决策时，必须加入“无 persona 基线”以剥离任务语义的驱动效应，避免将模型默认行为误判为人格效应

  - 人格-行为耦合高度依赖模型版本（GPT-4o-mini 全军覆没，GPT-4.1-mini 一致，GPT-5-mini 部分一致），切换模型需重新验证，多模型交叉对比可降低误判

  - 抽象概念（如品牌色感）的人格信号强，具体概念（如产品功能色）信号弱，模拟用户时对不同任务粒度需差异化建模

  - 推荐业务中若用 LLM persona 模拟用户偏好，优先关注任务上下文和 prompt 框架，人格标签的贡献可能被高估'
score: 6
source: arxiv-cs.HC
depth: abstract
---

**动机**：LLM persona 被越来越多用于早期可视化设计研究以近似不同用户，但个人信息（Big Five）调节的输出究竟是真实人格效应，还是模型与任务框架的产物尚不明确。若人格模拟不可靠，基于此的个性化设计可能误导决策。

**方法**：使用 43 个 Big Five 人格档案，在 GPT-4o-mini、GPT-4.1-mini、GPT-5-mini 三个模型上测试两项可视化相关任务：① 为抽象概念（如“信任”）和具体概念（如“香蕉”）分配颜色；② 针对不同任务上下文对图表类型（柱状图、散点图等）进行偏好评分。通过比较人格-输出一致性、模型间差异、有无 persona 基线的排名，评估人格效应的稳定性。

**关键结果**：颜色-人格耦合高度依赖模型：GPT-4o-mini 对所有六种概念均未表现出显著人格-颜色关联；GPT-4.1-mini 则一致地呈现关联；GPT-5-mini 仅在两种概念上部分关联。概念类型调节效应：抽象概念上人格解释的色调方差大于模型身份，具体概念上效应量小且二者相当。图表选择中，基于人格的聚类聚合虽产生了稳定排名，但“无 persona 基线”在 9 个模型-上下文组合的 8 个中恢复了相同首选图表，说明任务上下文是排名第 1 选择的主因。

**结论**：LLM persona 目前只能作为可视化设计的探索性探针，不能替代真实用户研究；未来工作需进行多模型验证、概念类型分解，并始终设置无 persona 基线。
