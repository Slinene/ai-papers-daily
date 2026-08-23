---
title: 'Two-sided receptivity to conversational AI agents in online dating: Bilingual
  survey data from Fledge.Love'
title_zh: 在线约会中对话AI代理的双向接受度：Fledge.Love双语调查数据集
authors:
- Daria Leshchikova
- Valentina V. Kuskova
- Dmitry Zaytsev
- Valerii Klimov
affiliations:
- Fleamily, Inc., Delaware, USA
- Lucy Family Institute for Data & Society, University of Notre Dame, Notre Dame,
  Indiana, USA
arxiv_id: '2608.19545'
url: https://arxiv.org/abs/2608.19545
pdf_url: https://arxiv.org/pdf/2608.19545
published: '2026-08-20'
collected: '2026-08-23'
category: Agent
direction: 对话式AI Agent 用户态度数据集
tags:
- conversational AI
- user acceptance
- survey dataset
- agent receptivity
- generative AI
- cross-cultural
one_liner: 发布两个双语调查数据集，分离用户对部署自身代理与遭遇他人代理的接受度及对生成式AI功能的兴趣
practical_value: '- 调查设计将用户角色拆分为“代理部署方”和“代理遭遇方”，电商/客服场景中评估用户对 Agent 的态度时也应分开测量，避免混淆部署意愿与接受接触意愿。

  - 数据集发布流水线包含 k-anonymity 审计和双语 codebook，可复用为内部用户研究数据匿名化与文档规范，尤其适合跨境多语言产品的用户调研。

  - 对被动生成式 AI 功能（如自动摘要、消息建议）的兴趣测量，可直接迁移到电商详情页生成、客服话术建议等功能的 pre-launch 接受度调研。

  - 该数据集本身不涉及推荐算法，但可作为用户对生成式推荐解释或对话式购物助手态度的先验参考；若做类似用户研究，可借鉴其量表结构。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

动机：在线约会平台正快速引入自主对话代理与生成式AI功能，但缺乏用户态度数据，尤其缺乏“接收方”视角——用户如何面对机器生成的资料、消息或对话伙伴。现有工具多测量对 AI 的一般态度，未区分沟通委托中同时存在的“部署者”与“遭遇者”两个角色。

方法：论文发布两个来自 Fledge.Love 的匿名调查数据集。第一个数据集（N=2,617，俄语与英语双语）采用七项量表测量对自主对话代理的接受度，明确分离“部署自己的代理”与“遇到他人代理”两种角色，并附带六个序数协变量和两个辅助项。第二个数据集（N=2,894）测量用户对三种被动生成式 AI 功能的兴趣。数据发布包含模型派生得分（2,499 个完整案例）、双语 codebook、经过 k-匿名审计的匿名化管道、可执行分析笔记本和规范输出。

结果：提供的数据集填补了双向接受度测量的空白，支持人机沟通、推荐系统及跨文化技术接受研究复用。样本量总计超过 5,500，具有跨文化比较价值。
