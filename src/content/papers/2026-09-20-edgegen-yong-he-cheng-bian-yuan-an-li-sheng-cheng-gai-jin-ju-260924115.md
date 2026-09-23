---
title: 'EDGEGEN: Improving Tool-Calling Agents Beyond Happy Paths with Synthetic Edge
  Case Generation'
title_zh: EDGEGEN：用合成边缘案例生成改进工具调用智能体
authors:
- Harshavardhan Abichandani
- Penny Chong
- Jiyuan Shen
- Gunraj Singh
- Ashutosh Hathidara
- Marcus Duigan Xing Yu
- Jane Lo
- Atin Ghosh
- Yipeng Li
- Daniel Dahlmeier
affiliations:
- SAP
arxiv_id: '2609.24115'
url: https://arxiv.org/abs/2609.24115
pdf_url: https://arxiv.org/pdf/2609.24115
published: '2026-09-20'
collected: '2026-09-23'
category: Agent
direction: 工具调用 Agent 合成数据与优化
tags:
- Tool-calling agents
- Synthetic data generation
- Edge cases
- Finetuning
- Harness optimization
- Policy compliance
one_liner: 从智能体规范提取合规规则，生成数据库接地的边缘用例任务，用于微调和 harness 优化，无需人工标注
practical_value: '- 在电商导购/客服 Agent 中，可从业务规范文档自动提取合规规则（如优惠叠加限制、售后时效、风控红线），反向构造违反规则的边缘对话任务，自动扩充测试与微调数据，低成本覆盖长尾异常场景。

  - 生成任务时绑定真实数据库状态（订单、库存、优惠券、用户画像），避免生成脱离业务上下文的任务；可复用“先抽规则→构造特定 DB 状态→生成违规任务”的流程做
  Agent 回归测试。

  - 微调与 harness 优化双路径：若模型推理能力弱，用合成数据直接微调；若只想调整系统提示、工具描述或调度逻辑，可用同一批数据做黑盒搜索，无需重新训练模型。

  - 全自动闭环无需人工标注，适合隐私敏感场景，可在内部数据不出域的前提下生成高质量任务，用于 Agent 上线前的鲁棒性验证。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**  
企业级工具调用 LLM Agent 需要高质量、多样化的任务数据来评估和优化，但真实数据受隐私限制难以获取；现有合成方法生成的通用任务忽略 Agent 底层状态或数据库，无法反映真实长尾场景。  

**方法关键点**  
EdgeGen 从 Agent 规范中自动提取合规规则，利用这些规则生成数据库接地的边缘用例任务，刻意违反规则以暴露 Agent 策略缺陷。这些任务可与现有合成数据技术结合，用于两条改进路径：微调模型或优化 harness（工具描述、系统提示等）。整个流程全自动化，无需人工标注。  

**关键结果**  
在 tau2-bench airline 域上，用 EdgeGen 数据微调带来一致的 mean progress 提升（+2% 到 +42%），而部分基线方法在某些模型上出现退化；harness 优化方面，Gemma-4-e4b 模型相比人工构建 harness 和基础 harness 分别提升 +10% 和 +30%。
