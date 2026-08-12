---
title: 'Business Arena: Benchmarking LLM Agents in a Realistic Marketplace'
title_zh: 企业竞技场：在真实市场环境中评测大模型业务智能体
authors:
- Yijun Pan
- Yukun Lian
- Kunyu Shi
- Junbo Li
- Hongwei Xue
- Sicong Xie
- Guannan Zhang
- Xiaoying Xing
affiliations:
- Accio Team, Alibaba Group
- Yale University
arxiv_id: '2608.08621'
url: https://arxiv.org/abs/2608.08621
pdf_url: https://arxiv.org/pdf/2608.08621
published: '2026-08-08'
collected: '2026-08-12'
category: Eval
direction: 大模型业务智能体长周期评测
tags:
- LLM agents
- business simulation
- benchmark
- decision-making
- long-horizon evaluation
- diagnostic metrics
one_liner: 构建基于真实数据的跨境电商模拟环境，系统评估15个大模型，揭示最终净资产9倍差距和运营风格差异
practical_value: '- 借鉴其部分可观测、延迟反馈、运营约束的环境设计，在搜索推荐系统中构建更真实的长期离线评估，避免仅依赖即时点击率

  - 技能级诊断与动作级归因方法可直接用于分析推荐策略的复合效果：将最终GMV提升归因到具体的调价、广告、选品动作，指导强化学习的奖励塑形

  - 合规、客服等持续性义务的建模提醒电商推荐需纳入供应链、库存、售后成本，面向全链路收益优化而非孤立的CTR/CVR

  - 状态保存与分叉对比机制可用于A/B测试的离线版本，通过从同一业务状态出发并行评估不同策略，提高实验效率和可信度'
score: 9
source: huggingface-daily
depth: full_pdf
---

**动机**：现有LLM智能体评测侧重短周期、可验证任务（如修代码、网页导航），缺乏对商业运营核心挑战的覆盖：信息不完全且噪音多、经济反馈延迟且难以归因、市场持续变化、运营义务不可延期。直接部署到真实业务风险高，需要可控而逼真的评测环境。

**方法关键点**：
- 构建跨境B2B电商模拟市场，产品、供应商、价格、关税等均基于阿里国际站真实数据及权威来源校准
- 智能体需在30个模拟日内端到端运营店铺，覆盖市场研究、采购、库存、定价、销售、客服、合规、财务等全业务循环
- 提供60+工具，支持MCP调用、脚本撰写和文件持久化，信息暴露分层（趋势信号、日历事件、噪音事件），反馈滞后且后果耦合
- 引入专家设计的确定性策略作为机会上界参考，以及技能级指标（资本利用率、订单利润率、合规罚款等）和动作级归因，可将盈亏追溯到具体决策
- 实现状态保存-分叉-加载机制，支持从同一业务状态出发比较不同策略或模型

**关键结果**：
- 评估GPT-5.6 Sol、Gemini 3.1 Pro、Claude Fable 5等15个前沿模型，平均最终净资产从$20,856到$188,488，差距达9.0倍；51%的试验亏损，仅4个模型在所有10次重复中保持本金
- 最佳专家策略获得$436,195，是最好模型的2倍以上，表明巨大提升空间
- 机制消融证明利用市场需求信号、全成本定价、关税意识、合规遵守等正确商业行为都能带来显著正向收益，验证了评测的有效性
- 技能层面揭示不同运营风格：Gemini 3.1 Pro如“精品店”高利润低周转，GPT-5.6 Sol如“批发商”高周转中等利润；合规和客服维度排序与总排名不同，可暴露特定缺陷
- 动作归因可定位具体盈亏来源，如Gemini 3.5 Flash在正确计算路线成本时盈利，遗漏物流成本时亏损

**核心洞察**：现有LLM在长期商业决策中仍远逊于结构化专家策略，但通过诊断性评估可清晰定位其能力短板，为训练和部署提供明确改进方向。
