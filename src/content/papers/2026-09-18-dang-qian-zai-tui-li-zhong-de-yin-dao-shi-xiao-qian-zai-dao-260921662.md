---
title: 'When Steering Fails in Latent Reasoning: A Latent-to-Language Transition Gap'
title_zh: 当潜在推理中的引导失效：潜在到语言转换差距
authors:
- Gaoxiang Huang
- Lei Qi
affiliations:
- HKUST(GZ)
- SEU
arxiv_id: '2609.21662'
url: https://arxiv.org/abs/2609.21662
pdf_url: https://arxiv.org/pdf/2609.21662
published: '2026-09-18'
collected: '2026-09-21'
category: Reasoning
direction: LLM 潜在推理可控性分析
tags:
- activation steering
- latent chain-of-thought
- interpretability
- LLM reasoning
- hidden states
one_liner: 发现 latent CoT 中激活引导对后续语言生成的影响远弱于显式 CoT，定位潜在到语言转换差距为核心障碍
practical_value: '- 在推荐/Agent 场景若引入 latent CoT 或 continuous thought 来降低推理 token 成本，不要假设通过
  steering hidden states 就能可靠地改变最终推荐解释、query 或对话行为；需在语言输出层或显式 CoT 阶段做干预。

  - 评估任何 latent reasoning 控制方法时，指标应使用最终生成文本的任务成功率/语义变化，而不是隐藏状态移动距离或 probing 准确率，因为存在
  latent-to-language transition gap。

  - 如果业务里需要用 activation steering 做风格/安全/品牌语调控制，优先对显式 CoT 或最终输出前几层施加，避免在连续推理中间层低效干预。

  - 在设计 latent CoT 架构时，可以将 transition boundary（hidden state -> language head）作为专门可学习的适配层或对齐目标，以缩小潜在干预到文本生成的衰减。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**  
Activation steering 已广泛用于显式 CoT 推理中控制语言模型，但将其扩展到 latent CoT 时效果未知。本文发现对连续思维施加 steering 对后续语言生成的影响明显弱于对显式 CoT 的 steering，即使隐藏表示被移动了相近的幅度。

**方法关键点**  
首先通过 probing 证明任务信息在 continuous thoughts 中仍然可识别，排除“信息丢失”解释。由此提出 **latent-to-language transition gap**：潜在空间的干预效应无法有效传递到语言生成。两个进一步实验支持该假设：
- 输出分布在从 latent 到 language 的 transition boundary 处发生突变；
- 任务相关方向在 latent CoT 中的双向控制能力远弱于在显式 CoT 中。

**关键结果**  
作者未给出具体量化数字，但定性对比显示：同样幅度的 hidden state 移动，在 latent CoT 中对最终语言输出的控制效果显著更弱；transition boundary 成为干预衰减的关键位置。这表明未来 latent-steering 方法的评估与设计应聚焦 latent-to-language 转换接口。
