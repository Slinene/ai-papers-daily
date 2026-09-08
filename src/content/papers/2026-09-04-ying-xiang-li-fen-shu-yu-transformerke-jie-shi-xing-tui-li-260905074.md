---
title: 'Influence Score and Transformers interpretability: Measure of the Effective
  Impact of Attention Heads at inference time'
title_zh: 影响力分数与Transformer可解释性：推理时测量注意力头的有效影响
authors:
- Lisa Bouger
- Yannick Teglia
- Philippe Loubet Moundi
affiliations:
- Thales CDI, France
- Inria Paris, France
- Sorbonne Université, France
arxiv_id: '2609.05074'
url: https://arxiv.org/abs/2609.05074
pdf_url: https://arxiv.org/pdf/2609.05074
published: '2026-09-04'
collected: '2026-09-08'
category: LLM
direction: Transformer 可解释性 · 注意力头归因
tags:
- Transformer interpretability
- attention heads
- prompt injection
- residual stream
- influence score
one_liner: 提出结合logits方向影响与残差流结构贡献的influence score，用于多尺度量化注意力头对分类决策的贡献
practical_value: '- 对部署在推荐/广告风控链路中的文本分类模型（如恶意query检测、prompt注入检测、低质内容过滤），可用influence
  score定位导致错误预测的关键注意力头，辅助badcase归因与模型调试。

  - 其“方向影响+结构贡献”的双信号设计可迁移到Transformer排序模型：对用户行为序列、特征交叉层做注意力头级贡献分析，识别冗余或高影响头，用于推理加速或蒸馏裁剪。

  - 多尺度分析框架（head/layer/network）可用作模型上线后的行为监控，检测决策模式漂移，尤其适用于数据不可控的外部安全分类器。

  - 主要价值在可解释性工具，电商推荐场景的直接业务收益有限，需结合具体模型验证。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

动机：LLM部署面临prompt injection与越狱攻击风险，通常前置Transformer分类器进行恶意query检测，但模型内部决策机制不透明，尤其在训练数据不可控时，需要可解释性手段评估可靠性、识别偏差。

方法关键点：提出influence score，对注意力头的有效影响进行量化。分数由两部分组成：一是对最终logits的方向性影响，二是该头在残差流中的结构性贡献。两者结合后，可在head、layer、network三个尺度上分析注意力头对分类决策的贡献。该方法应用于一个面向prompt injection检测的DeBERTa模型，定位不同层不同头在正确与错误预测中的角色。

关键结果：框架能揭示正确预测与错误预测之间不同的决策行为模式，例如错误案例中关键头的影响分布更分散或集中于特定层。方法在细粒度电路分析和全局输出归因之间取得折中，既保留头级解释能力，又避免完整电路发现的高计算成本。论文未给出定量性能指标，主要贡献为提供了一种系统化的Transformer分类器决策机制研究方法。
