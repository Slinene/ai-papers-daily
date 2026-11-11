---
title: 'FINCOSMOS: An Open-World Evaluation Paradigm for Agents in Finance'
title_zh: FINCOSMOS：金融智能体开放世界评估范式
authors:
- Yupeng Cao
- Xueqing Peng
- Lingfei Qian
- Haohang Li
- Yangyang Yu
- Anke Xu
- Wenbo Cao
- Yan Wang
- Yuechen Jiang
- Yuyan Wang
affiliations:
- The Fin AI
- Stevens Institute of Technology
- University of Manchester
- MBZUAI
- University of Montreal
arxiv_id: '2611.07464'
url: https://arxiv.org/abs/2611.07464
pdf_url: https://arxiv.org/pdf/2611.07464
published: '2026-11-04'
collected: '2026-11-11'
category: Eval
direction: 开放世界Agent评估与可信性
tags:
- Agent Evaluation
- Open-World
- Finance
- Trustworthiness
- Program Verification
- Benchmark
one_liner: 提出开放世界金融Agent评估范式，用隐藏用户策略、Web取数与程序验证暴露静默失败
practical_value: '- 评估设计思维：不要把任务、数据、时间线固定死。对搜索推荐Agent，可让模型自己从商品库/Web获取数据、自己建索引或回测，并重点检查时效性（价格、库存是否用了未来信息）。

  - 程序化 veto checks 值得落地：用可执行校验代替人工评分，比如电商推荐Agent输出后自动检查是否包含下架商品、是否违反过滤条件、是否用训练后数据泄漏，任一命中直接判负。

  - 隐藏用户策略与主动追问：模拟用户只按需暴露需求，评估Agent是否追问缺失约束（预算、品类、时间窗口）。可借鉴到对话式推荐评估，衡量Agent对模糊Query的澄清能力。

  - 失败反馈闭环：论文中带持久记忆的Agent靠反馈学会全部任务，说明可建立评测失败案例库，让线上Agent从历史错误中迭代。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：金融场景中语言Agent在开放Web执行任务，但信任最难：数据必须来自Web、策略在用户脑中、正确性依赖时间，Agent可能静默失败——用了用户没要求的策略、未验证数据、或回测用到未来数据，报告却像正确的一样。现有基准封闭了任务/数据/时间线，反而移除了这些失败。

**方法关键点**：FINCOSMOS 让模拟用户持有从组合语法采样的隐藏策略，只在被询问时透露；Agent 没有数据，必须从Web获取数据，在数据截止下自建回测并交付可验证结果。评分无需参考答案：程序验证时点正确性并重算所有报告指标，交付策略对比隐藏规格，只有用户满意且15项veto检查全部通过才接受。

**关键结果**：四个编码Agent和一个无工具模型共150个会话，**无一会话被接受**：所有用户签署的会话都未通过程序检查；Agent只提出54–64%未被告知的细节；人类专家将88.33%的失败归因于Agent。而利用FINCOSMOS反馈，带持久记忆的Agent学会了全部十个任务。
