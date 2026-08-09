---
title: Benchmarking and Enhancing LLMs for Rule-Intensive Review of National Standard
  Documents
title_zh: 国家标准文档规则密集型审查的LLM基准与多智能体增强
authors:
- Tao Wang
- Qihao Yang
- Rongjiao Liang
- Lianghong Lin
- Haitao Wang
- Xinyu Cao
- Tianyong Hao
affiliations:
- School of Computer Science, South China Normal University, Guangzhou, China
- School of Artificial Intelligence, Shanghai Jiao Tong University, Shanghai, China
- China National Institute of Standardization, Beijing, China
arxiv_id: '2608.06312'
url: https://arxiv.org/abs/2608.06312
pdf_url: https://arxiv.org/pdf/2608.06312
published: '2026-08-06'
collected: '2026-08-09'
category: Eval
direction: 文档审查基准与多智能体增强
tags:
- LLM Evaluation
- Multi-Agent Framework
- Document Review
- Rule-Intensive
- GB-T Standards
- Counterexample Generation
one_liner: 构建首个国家标准文档审查基准GB/T-Bench与多智能体GB/T-Reviewer，将最佳CMCS从0.3280提升至0.5094
practical_value: '- 多智能体架构可将文档审查知识模块化为专门技能（全局检查、目标诊断、规则扫描、结果验证），适合电商商品信息合规审核、广告文案规则检查等场景，直接复用“技能分工+结果验证”协作模式。

  - 可控反例生成机制（确定性规则+约束LLM重写）能低成本构造带细粒度错误标签的数据集，可迁移至推荐系统、对话系统等领域的负面测试用例构建。

  - 诊断型评估协议（精确匹配错误位置、审查维度和错误类型）提供了一种细粒度能力评估范式，可用于定位推荐理由生成或内容审核模型的薄弱环节。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：LLM 在专业文档审查中的规则密集型能力缺乏评估基准，国家标准文档（如 GB/T）具有长篇幅、强结构、显式规则等特性，是理想试验场，但人工审查成本高昂。为此，构建首个国家标准文档审查基准 GB/T-Bench，并探索多智能体增强方案。

**方法**：
- **GB/T-Bench**：设计分层审查分类法，涵盖文档结构、范围对齐、规范情态、术语一致性、规范引用 5 大维度，细化为 25 种可诊断错误类型；通过确定性规则引擎与约束 LLM 重写的组合，对 488 份标准文档注入 7,306 个可追溯的审查错误实例，确保每一处修改可回溯；采用诊断导向评估，要求同时精确匹配错误位置、审查维度和错误类型，并引入文档级覆盖率指标。
- **GB/T-Reviewer**：多智能体框架将审查知识转化为全局检查、目标诊断、规则扫描和结果验证四个专门技能智能体，通过结构化协调完成审查流程。

**结果**：测试 14 个主流 LLM，发现人机差距显著，最强模型 CMCS 仅 0.3280，而人类专家达 0.6640；GB/T-Reviewer 将最佳 CMCS 提升至 0.5094，验证了技能分工对规则密集型审查的有效性。
