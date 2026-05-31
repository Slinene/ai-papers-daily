---
title: On the Construction and Implications of Low-Loss Valleys in LoRA-based Bayesian
  Inference
title_zh: LoRA空间中低损失谷的构建及其对贝叶斯推断的意义
authors:
- Daniel Dold
- Emanuel Sommer
- Julius Kobialka
- Oliver Dürr
- David Rügamer
affiliations:
- HTWG Konstanz
- LMU Munich
- Munich Center for Machine Learning (MCML)
- TIDIT.ch
arxiv_id: '2605.29580'
url: https://arxiv.org/abs/2605.29580
pdf_url: https://arxiv.org/pdf/2605.29580
published: '2026-05-28'
collected: '2026-05-31'
category: LLM
direction: LLM微调 · LoRA贝叶斯推断
tags:
- LoRA
- Bayesian Inference
- Uncertainty
- Curve Parameterization
- Ensembling
one_liner: 提出分段贝塞尔曲线连接独立LoRA最优解，形成连续低损失谷，提升不确定性估计和功能多样性
practical_value: '- **低成本贝叶斯集成**：利用分段贝塞尔曲线在LoRA空间内连接多个独立微调点，只需少量曲线参数即可实现参数空间遍历，为推荐模型的多样性预测提供比传统deep
  ensemble更轻量的方案。

  - **不确定性校准**：通过沿低损失谷进行参数扰动（结合flat-minima扰动）生成多样化预测分布，可直接用于电商搜索/推荐场景的置信度估计，缓解过度自信。

  - **功能多样性正则化**：引入Jensen-Shannon散度正则项鼓励不同曲线点的预测差异，可迁移至多任务推荐模型训练，促进多专家或子网络的功能多样化，提升集成互补性。

  - **连续模式连接优于离散集成**：实验表明线性插值遇损失障碍，而曲线版连续路径有效，提示在LoRA微调推荐大模型时，应避免简单参数平均或独立集成，可采用路径化方法获取更平滑的不确定性面。'
score: 7
source: arxiv-stat.ML
depth: abstract
---

**动机**：LoRA微调虽为LLM标准方法，但缺少原则性的认知不确定性估计。已有研究显示LoRA空间内离散多模态（如deep ensemble）相比单模态无明显增益，这与深度学习中独立最优模式可通过连续低损失谷连接从而提升贝叶斯平均的普遍观察矛盾。探索LoRA空间中是否存在此类连续结构及其功能多样性的影响尚未研究。

**方法关键点**：提出LoRA-Curve——在LoRA参数空间构建分段贝塞尔曲线，提供两种配置：(1)free配置联合学习所有控制点；(2)anchored配置用曲线连接独立微调得到的多个LoRA最优解。理论上证明损失沿曲线满足连续性及李普希茨平滑性。训练时联合flat-minima扰动与Jensen-Shannon散度正则项，以增强沿曲线的预测分布互信息。

**关键结果**：在Qwen2.5 7B的推理与分类评测上，线性插值遭遇显著损失障碍，而anchored多段曲线成功连接独立最优形成连续低损失谷。方法在保持原有性能的同时，显著提升预测分布的互信息（即更高功能多样性），建立了参数空间连续遍历与功能多样性的直接关联。
