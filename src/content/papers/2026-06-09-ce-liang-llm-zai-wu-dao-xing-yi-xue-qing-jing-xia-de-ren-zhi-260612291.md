---
title: Measuring Epistemic Resilience of LLMs Under Misleading Medical Context
title_zh: 测量 LLM 在误导性医学情境下的认知韧性
authors:
- Hongjian Zhou
- Xinyu Zou
- Jinge Wu
- Sean Wu
- Junchi Yu
- Bradley Max Segal
- Tobias Erich Niebuhr
- Sara Amro
- Michael Petrus
- Sheikh Momin
affiliations:
- University of Oxford
- University of Washington
- University College London
- University of Waterloo
arxiv_id: '2606.12291'
url: https://arxiv.org/abs/2606.12291
pdf_url: https://arxiv.org/pdf/2606.12291
published: '2026-06-09'
collected: '2026-06-15'
category: Eval
direction: LLM 医疗评测 · 误导性攻击韧性
tags:
- epistemic resilience
- misleading context
- medical LLM evaluation
- adversarial robustness
- benchmark
one_liner: 当注入误导性上下文时，LLM 放弃原正确回答，准确率从 71.1% 暴跌至 38.0%
practical_value: '- 在电商 / Agent 场景可借鉴「误导注入」评测思路：构造用户提供矛盾或虚假先验知识的对抗性测试集，检验 Agent 是否坚持正确业务规则。

  - 重点关注权威性虚假信息的影响：如假官方文件、规则性伪造等，这类注入对模型误导最强，在推荐解释或政策咨询 Agent 中要防御类似攻击。

  - 评估代理能力（agentic capability）时，可引入误导性上下文观察模型是否盲目跟随，作为鲁棒性指标，类似本研究的“exception‑poisoning”测试。

  - 基准设计启发：将原有正确回答的问题作为种子，再注入不同类型误导，可低成本构建大规模针对性评测，评估模型知识保持力。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：LLM 在医学执照考试中达到专家级分数，人们误以为高分代表安全的医学判断。但真实应用中患者常带入误导性信息，模型可能轻易放弃正确回答。本文揭示此假设的脆弱性，并定义“认知韧性”——在对抗性上下文中保持正确判断的能力。

**方法**：构建 **MedMisBench**，包含 10,932 个医学问题及 48,889 个误导性上下文‑选项对，覆盖医学推理、代理能力和患者旅程评估。将误导注入原正确回答的问题，测试 11 个模型配置，记录准确率下降和攻击成功率。

**关键结果**：原始问题平均准确率 71.1%，注入集中式误导上下文后暴跌至 38.0%，攻击成功率 51.5%。最有破坏性的注入类型是**权威框架式虚假信息**（69.5% 攻击成功率）和**例外中毒声明**（64.1%）。14 人跨国临床专家组评审发现 38.2% 的案例存在严重潜在危害。

**结论**：现有医学 LLM 基准仅衡量“知道什么”，未衡量“能否在误导下坚持正确判断”，MedMisBench 暴露了这一结构性盲点。
