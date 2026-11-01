---
title: Rethinking Neural Thickets Without Weight Perturbations
title_zh: 无权重扰动的神经丛林机制重审
authors:
- Nicolas Dufour
- Elouan Gardès
- Amil Dravid
- Patrick Pérez
- Loic Landrieu
affiliations:
- Kyutai
- Meta FAIR
- LIGM, CNRS, Univ Gustave Eiffel, ENPC, IP Paris
- UC Berkeley
- Google DeepMind
arxiv_id: '2610.40649'
url: https://arxiv.org/abs/2610.40649
pdf_url: https://arxiv.org/pdf/2610.40649
published: '2026-10-29'
collected: '2026-11-01'
category: Reasoning
direction: 推理时集成 · 输出空间扰动
tags:
- Logit Perturbation
- Self-Consistency
- Inference-Time Ensemble
- Reasoning
- Neural Thickets
- PSV
one_liner: 证明Neural Thickets的推理增益可仅凭冻结模型输出logit随机偏置、验证集选择与投票复现
practical_value: '- 在LLM生成推荐理由、商品文案、搜索词改写等推理链路里，可对logits加小随机偏置，再结合验证集或业务指标选高质输出投票；无需微调或权重扰动，部署仅改输出层，适合线上快速实验。

  - PSV提供比单纯采样自一致性更可控的多样性来源：显式logit偏置可以调节多样性与质量的权衡，比温度采样更容易复现和A/B。

  - 验证集选择可复用已有业务标注或线上反馈作为小验证池，淘汰低质扰动输出，降低投票噪声；对推荐系统里的开放域文本生成（如push文案、搜索query）尤其有用。

  - 一阶分析表明小权重扰动≈logit平移，如果已有weight perturbation ensemble，可直接替换为logit PSV，省去多份模型权重存储和推理成本。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：Gan & Isola 报告随机扰动预训练LLM权重可带来最高52.8个准确率点提升，并归因于权重空间中的任务专家丛林。本文复现增益，但质疑其几何解释。

**方法**：控制实验显示，只扰动单个decoder block已恢复大部分增益；完全冻结模型并给输出logit加随机偏置，在多数推理任务上匹配或超过全权重扰动。将这一过程抽象为 Perturb-Select-Vote (PSV)：生成扰动预测器、小验证集选择高表现成员、聚合预测。一阶分析表明小权重扰动主要通过诱导logit偏移起作用。分析还延伸到视觉域偏移任务。

**结果**：在语言推理任务上，logit PSV与全权重扰动相当或更优；视觉域偏移（包括地球观测）上logit PSV显著提升，全权重扰动几乎无额外收益。结论：所谓附近权重专家增益可由输出多样性、选择、投票解释，Logit PSV是冻结模型训练-free的简单替代。
