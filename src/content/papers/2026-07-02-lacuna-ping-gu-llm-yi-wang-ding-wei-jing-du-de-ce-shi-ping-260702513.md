---
title: 'LACUNA: A Testbed for Evaluating Localization Precision for LLM Unlearning'
title_zh: LACUNA：评估 LLM 遗忘定位精度的测试平台
authors:
- Matteo Boglioni
- Thibault Rousset
- Siva Reddy
- Marius Mosbach
- Verna Dankers
affiliations:
- Mila – Quebec Artificial Intelligence Institute
- McGill University
arxiv_id: '2607.02513'
url: https://arxiv.org/abs/2607.02513
pdf_url: https://arxiv.org/pdf/2607.02513
published: '2026-07-02'
collected: '2026-07-03'
category: Other
direction: LLM 知识遗忘评估 · 参数定位精度
tags:
- LLM Unlearning
- Localization
- Benchmark
- PII
- Resurfacing Attacks
- Knowledge Removal
one_liner: 首个提供参数级定位真值的 LLM 遗忘基准，揭示现有方法定位不准且易受攻击，精准定位可大幅提升遗忘鲁棒性。
practical_value: '- 在需严格删除用户隐私（如 GDPR 合规）的推荐或对话系统中，参数级精确遗忘比仅监控输出更可靠，可降低数据泄露风险。

  - 定位思想可迁移到模型纠偏或概念编辑：先定位存储不良偏见的参数，再定向修改，提升推荐公平性。

  - 提醒从业者：行为级遗忘评估（输出不可见）可能只是“掩藏”而非真正擦除，应增加参数级验证，防止被攻击还原。

  - 通过受控注入合成数据构建私有测试集的思路，可用于测试模型对特定知识（如促销活动）的记忆强度与遗忘效果。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：LLM 会记忆训练数据中的个人身份信息（PII），主流遗忘方法常采用“先定位、后遗忘”范式，但现有基准仅评估输出层表现，无法确认参数级知识是否真正擦除，面临重现攻击风险。  
**方法**：提出 LACUNA——首个带参数级定位真值的遗忘测试平台。通过掩码持续预训练，将合成个体的 PII 注入 OLMo 1B/7B 模型的预定义参数中，从而提供“哪些权重存储了知识”的地面真值。然后 benchmark 当前 SOTA 遗忘方法，直接比较其定位精度与真正需要擦除的权重。  
**结果**：现有方法在输出级表现良好，但参数定位极不精确，易被重现攻击提取出“遗忘”的信息。当人为给予精准定位后，即便是简单的梯度遗忘方法也能实现强擦除和高鲁棒性，凸显了精准定位的重要性。论文公开了 LACUNA 以推动基于定位的鲁棒遗忘研究。
