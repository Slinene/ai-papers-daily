---
title: 'Pinocchio: Fast Uncertainty Estimates for Black-Box Language Models'
title_zh: Pinocchio：黑盒语言模型的快速不确定性估计
authors:
- Kevin David Hayes
- Arka Pal
- Haosong Zhang
- Tom Goldstein
- Micah Goldblum
affiliations:
- University of Maryland
- Ritual AI
- Fudan University
- Columbia University
arxiv_id: '2609.24881'
url: https://arxiv.org/abs/2609.24881
pdf_url: https://arxiv.org/pdf/2609.24881
published: '2026-09-21'
collected: '2026-09-22'
category: Eval
direction: 黑盒LLM不确定性估计 · 外部校准器
tags:
- uncertainty estimation
- black-box LLM
- AUROC
- calibration
- text-only
- API
one_liner: 用外部校准器仅凭文本输出预测黑盒LLM回答的正确性，无需logits或微调
practical_value: '- 在Agent/LLM工作流中部署轻量外部校准器（如Pinocchio）作为gate，对LLM生成的推荐理由、商品描述、搜索query改写结果做正确性/可靠性打分，低于阈值触发人工审核或fallback策略。

  - 该方法只依赖文本输出，兼容闭源API（GPT/Claude等），适合电商环境中大量使用第三方LLM的场景；无需模型内部access，降低接入成本。

  - 跨模型零样本迁移结果表明，可在内部用少数模型标注数据训练一个通用不确定性估计器，直接应用于新模型或外部模型，降低维护成本。

  - 0.8B文本模型即可达到大模型AUROC，意味着可部署在CPU或边缘侧，适合在线实时过滤，不影响主链路延迟。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：LLM在医疗、法律等高风险决策中可能自信地给出错误答案，但闭源API模型（GPT、Claude等）不暴露log-probabilities或内部状态，传统不确定性估计方法失效。

**方法关键点**：提出Pinocchio，一个外部校准器，仅以模型的文本回复为输入，通过单次前向传播预测该回复是否正确。训练数据来自七个LLM的响应，模型无需目标模型的logits、权重或内部状态，因此完全适用于黑盒API。轻量0.8B参数的文本模型即可达到最大模型的AUROC。

**关键结果**：在同模型held-out数据上AUROC达0.862；零样本迁移到13个未见模型、覆盖8个组织。代码开源，仅需两行代码即可添加到现有repo中。
