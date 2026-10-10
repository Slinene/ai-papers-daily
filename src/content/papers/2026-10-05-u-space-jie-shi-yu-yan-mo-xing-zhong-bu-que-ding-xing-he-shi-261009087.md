---
title: 'U-Space: Uncovering When and Why Uncertainty Arises in Language Models'
title_zh: U-Space：揭示语言模型中不确定性何时何地产生
authors:
- Tobias Braun
- Nils Loose
- Alexander Herzog
- Virginia Ceccatelli
- Marcus Rohrbach
- Thomas Eisenbarth
- Lorenzo Cavallaro
affiliations:
- Technische Universität Darmstadt
- University College London
- Universität zu Lübeck
- Mila – Quebec Artificial Intelligence Institute
- Mohamed bin Zayed University of Artificial Intelligence
arxiv_id: '2610.09087'
url: https://arxiv.org/abs/2610.09087
pdf_url: https://arxiv.org/pdf/2610.09087
published: '2026-10-05'
collected: '2026-10-10'
category: Eval
direction: LLM 不确定性量化 · 可解释性
tags:
- uncertainty quantification
- mechanistic interpretability
- residual stream
- LLM reliability
- confidence estimation
one_liner: 提出无需训练、无需重复生成的 U-Space 子空间，将 LLM 逐 token 不确定性可视化和标量化，校准优于基线
practical_value: '- 在电商 Agent/工具调用链路中，可对 LLM 规划的每个步骤计算 U-Space 逐 token 不确定度，对高不确定性中间结论做早停、二次确认或转人工，避免错误随多步推理放大；无需重复采样，适合线上低延迟。

  - 用于生成推荐理由、商品卖点或搜索改写时，可把 U-Lens 聚合分数作为轻量 confidence gate：低于阈值不展示解释或触发模型重写/检索增强，降低幻觉文案对用户信任的伤害。

  - 做离线评测时，借鉴其 length-controlled evaluation：不要直接用生成长度作为质量/置信度代理，应分离长度相关与不确定性特定信息；U-Space
  提供无标注的 token-level 不确定 map，便于定位长回答中哪一段开始“不确定”。

  - 若业务已有 logits/隐藏状态可访问，U-Space 思路可低成本迁移：选定 few-shot 语义锚点构建正交基，不需要真实标签即可上线；与 supervised
  confidence 模型相比，跨分布迁移更稳。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：LLM 越来越多参与高风险决策，但模型可能用流畅表达掩盖错误，个体答案可信度难以判断。现有不确定性量化方法常需重复生成或独立训练组件，且只给标量分数，无法说明不确定性的来源与演变；同时生成长度与不确定性估计高度相关，导致评估混淆。

方法：受机制可解释性启发，作者提出 U-Space，一个低维子空间。首先为 doubt 和 certainty 定义语义锚点，将它们的 unembedding 方向映射回残差流空间，组合其对比方向得到正交基。U-Lens 把每个 token 的残差状态投影到这些基向量上，形成可解释的逐 token 不确定性图，可直接观察或聚合为标量分数。整个过程不需要正确性标签、重复生成或额外训练。

结果：在多个推理基准上，U-Space 的 confidence score 在标准评估和长度控制评估下均优于既有基线，且迁移到新分布时比 supervised estimators 更稳定。
