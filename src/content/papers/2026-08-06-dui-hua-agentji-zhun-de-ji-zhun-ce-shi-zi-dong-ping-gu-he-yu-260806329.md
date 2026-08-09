---
title: 'Benchmarking the Benchmarks: Evaluating Benchmarks for Conversational Agents'
title_zh: 对话Agent基准的基准测试：自动评估合成与人工基准的质量
authors:
- Noam Koren
- Roy Bar-Haim
- Abigail Goldsteen
affiliations:
- IBM Research
arxiv_id: '2608.06329'
url: https://arxiv.org/abs/2608.06329
pdf_url: https://arxiv.org/pdf/2608.06329
published: '2026-08-06'
collected: '2026-08-09'
category: Eval
direction: 对话Agent基准质量自动评估
tags:
- benchmark quality
- LLM judge
- conversational agents
- evaluation
- policy coverage
- synthetic data
one_liner: 提出使用LLM评委自动评估对话Agent基准的一致性、复杂性和策略覆盖，经验证能区分基准质量水平
practical_value: '- **对话Agent评估集的自动质检**：在构建电商客服、导购对话等场景的测试集时，可直接采用LLM评委对已有基准进行一致性、复杂性和策略覆盖率诊断，快速发现逻辑矛盾任务或过于简单的场景，避免线下指标误导线上决策。

  - **生成式对话数据筛选与优化**：当使用LLM自动生成多轮对话评估集（如模拟用户咨询、售后政策）时，可集成该框架作为质量过滤器，筛除不一致或覆盖不全的样本，提升合成数据的可用性。

  - **对话系统策略覆盖检查**：对于涉及多步骤业务策略（如优惠查询、退换货规则）的对话应用，可用其策略覆盖维度自动检验现有测试是否涵盖了所有关键策略分支，指导增补评估用例。

  - **LLM法官选择的成本与一致性权衡**：论文验证了不同法官模型（如GPT-4、较小模型）的评估一致性，业务落地上可选择更便宜的模型作为近似评委，降低自动化评估的成本。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：任务型对话Agent的评估依赖于人工或自动生成的基准，但基准本身的质量缺乏系统检查。低质量基准可能含有不一致任务、过于简化的场景或策略覆盖不全，导致评估不可靠。随着自动生成基准的增多，亟需一种自动评估基准质量的方法。

**方法关键点**：提出一个无参考评估框架，利用LLM评委对基准的三个维度进行打分：一致性（任务是否逻辑自洽，无矛盾）、复杂性（场景是否足够真实多步）和策略覆盖（是否覆盖了所需的关键策略点），同时给出弱点的诊断建议。框架不依赖人工标注或额外参考，直接分析基准中的对话任务描述和预期行为。

**关键结果**：通过人为注入可控的降质扰动（如制造不一致、简化任务）以及与独立人工标注的比对，验证了所提指标能有效区分不同质量水平的基准。在不同领域和不同能力的LLM评委下，指标均表现出稳定区分力，并且可应用于人工构造的基准，证明其实用性。这表明LLM评委可以作为基准质量的自动监控工具。
