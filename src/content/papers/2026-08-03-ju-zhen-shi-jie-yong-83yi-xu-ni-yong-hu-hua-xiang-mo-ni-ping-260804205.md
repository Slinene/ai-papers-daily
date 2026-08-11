---
title: 'MatrAIx: Simulating the World with 8.3 Billion Persona Agents'
title_zh: 矩阵世界：用83亿虚拟用户画像模拟评估AI系统
authors:
- Xiaomin Li
- Yuexing Hao
- Jianheng Hou
- Jintao Huang
- Qianfeng Wen
- Shirley Huang
- Yifan Liu
- Xiaoyi Liu
- Yilan Fan
- Yijun Wang
affiliations:
- Harvard University
- Massachusetts Institute of Technology
arxiv_id: '2608.04205'
url: https://arxiv.org/abs/2608.04205
pdf_url: https://arxiv.org/pdf/2608.04205
published: '2026-08-03'
collected: '2026-08-11'
category: Eval
direction: 大规模用户模拟评估基础设施
tags:
- Persona
- Simulated Users
- Evaluation
- LLM Agents
- Digital Products
- Population-scale
one_liner: 提出83亿虚拟画像的大规模用户模拟评估基础设施，在四种环境中完成18,189次试验，行为一致性达91.5%
practical_value: '- **可复用的结构化画像模板**：1290维的画像 Schema 可直接映射电商用户特征（购买力、品类偏好、决策风格），驱动
  LLM Agent 生成拟真的评价、购买意愿、价格敏感行为，用于推荐策略的预部署测试。

  - **四类评估环境开箱即用**：Survey 测价格弹性，Chatbot 测客服方案，Web 测商品浏览与选品体验，App 测购物流程与隐私控制。可直接改造为电商/信息流场景的
  A/B 测试沙盒。

  - **可迁移的任务库与指标**：1010 个预定义任务中包含价格敏感度、购买意愿、推荐满意度、留存意图等模板，提炼出“结果型验证器+过程型行为记录”的评估模式，能直接复用在推荐解释、搜索排序等产品实验上。

  - **一致性验证的方法论**：400 组对照试验中 91.5% 的行为表达/抑制成功率，说明结构化画像 + LLM 能产出有区分度的群体反馈，可作为推荐冷启动或人群包效果预判的低成本验证手段。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：现有的离线评测追求功能正确性，却忽略了用户多样性带来的交互差异。同样一个推荐或对话系统，新手用户和专家用户的满意条件截然不同。人工测试慢且贵，无法在产品迭代中高频覆盖不同人群。本文构建了一个大规模模拟用户评估基础设施 MatrAIx，通过结构化虚拟画像驱动 LLM Agent，在问卷、聊天、网页、应用四类环境中测试系统表现，替代部分人工评测。

**方法关键点**：
- **Persona 8B**：包含 83 亿条记录，每条用 1290 维分类属性描述背景、心理、能力、行为、生活方式。合成记录通过 DAG 条件采样保留属性相关性（如教育依赖年龄，英语水平依赖母语和地区）；人类锚定记录来自维基百科传记、亚马逊评论、开发者调查等 6 个来源，经 LLM 抽取映射到同一 Schema。最终发布 100 万条精华集，59.9 万来自真实数据。
- **MatrAIx Playground**：提供 Survey、AI Chatbot、Web、App 四种交互环境，以任务为单位调动画像 Agent 运行并记录轨迹，用程序化验证器或 LLM 法官评估结果。
- **1010 个评估任务**：覆盖电商、软件、金融、医疗等 25+ 领域，每个任务定义目标系统、画像队列、用户场景与目标、评估指标，可复用和重跑。

**关键实验**：
- 在 8 项代表性任务上用 GPT 5.5、Claude Opus 4.8、Claude Haiku 4.5 驱动画像 Agent，完成 18,189 次试验。价格敏感任务中，信任水平可显著区分不同画像群体的续购意愿（Cramér's V 0.23–0.36）。
- 400 组控制行为一致性测试中，10 种行为特征在四种环境下的表达/抑制成功率达 91.5%；Survey、Chatbot、Web 环境有 9/10 的特征达到强一致性。
- 抽取质量验证：100 条真实画像的人类评分为 4.135/5，GPT 5.5 和 Claude Opus 4.8 与人类评分一致性分别为 79.2% 和 93.8%。

**核心结论**：虽然模拟无法替代真实验证，但该基础设施能高效暴露不同用户群可能遇到的磕绊点，使产品团队可以在上线前进行低成本的多人群压力测试与版本对比。
