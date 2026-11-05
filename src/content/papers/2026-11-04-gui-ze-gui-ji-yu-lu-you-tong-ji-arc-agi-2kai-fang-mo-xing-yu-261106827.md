---
title: 'Rules, Traces and Routing Statistics: Training and Calibration Data for Open
  Models on ARC-AGI-2'
title_zh: 规则、轨迹与路由统计：ARC-AGI-2开放模型训练与校准数据
authors:
- Nguyen Minh Thang
- Trinh Thi Phuong
affiliations:
- VNU University of Science
arxiv_id: '2611.06827'
url: https://arxiv.org/abs/2611.06827
pdf_url: https://arxiv.org/pdf/2611.06827
published: '2026-11-04'
collected: '2026-11-05'
category: Training
direction: 训练数据与推理优化
tags:
- ARC-AGI-2
- fine-tuning
- synthetic data
- MoE pruning
- reasoning traces
- KV cache
one_liner: 研究开放模型在ARC-AGI-2上的训练与校准数据选择，结合推理轨迹微调和MoE路由裁剪，最高得分56.67
practical_value: '- 合成数据过滤可借鉴三层机制：行为签名去重、最近竞争规则反驳、捷径求解器筛选，适用于构建电商推荐或Agent生成任务的高质量训练集，避免冗余与捷径特征。

  - 推理轨迹微调时优先保留模型自身正确答案的轨迹，效果优于混合他模型轨迹；业务中训练Agent对话/规划轨迹可从高质量自身采样入手。

  - 在serving engine中强制思考上限、回答后调用工具校验（如程序/规则检查器）能显著提升Agent复杂任务成功率，且实现成本低。

  - MoE路由裁剪方法：按激活显著性剪枝专家并保留程序token所需专家，可提升长上下文KV cache容量和并发，适合生成式推荐/Agent大模型部署优化。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

**动机**：在离线四张L4 GPU、12小时限制下，探究哪些训练与校准数据能提升开放模型在ARC-AGI-2抽象推理任务上的表现。

**方法关键点**：
- 对NVARC Qwen3-4B网格模型，构建带类型的可执行规则语料（12,000条规则、95,993个任务），通过探测集行为签名去重和捷径求解器过滤筛选任务；但合成任务未能提升真实任务模型。
- 对Qwen3.8-27B推理模型，仅微调其自身正确最终答案的推理轨迹（1,036条），并设计推理过程：在serving engine限制思考上限，每次回答后检查Python程序，每个输入先长尝试一次。
- 对Qwen3.8-Flash-Next MoE模型（125B参数，6B激活），通过路由加权激活显著性剪枝从512到384个专家，KV cache从0.55M提升到1.39M tokens；进一步用ARC路由统计适应到296专家并保留程序token专家，加上FP8索引缓存，达到1.96M。

**关键结果数字**：
- Qwen3-4B网格模型微调后平均得分从28.96提升到33.06（最好34.86），合成数据无额外增益。
- Qwen3.8-27B推理模型得分从26.81提升到44.03，主要来自推理过程而非微调。
- Qwen3.8-Flash-Next MoE模型配合程序检查工具得分56.67，为最佳结果。
