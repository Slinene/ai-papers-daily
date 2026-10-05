---
title: Planning to Learn
title_zh: 规划学习：按剩余训练预算在交叉熵与策略梯度间插值的 horizon loss
authors:
- Ian Osband
affiliations:
- Google DeepMind
arxiv_id: '2610.03667'
url: https://arxiv.org/abs/2610.03667
pdf_url: https://arxiv.org/pdf/2610.03667
published: '2026-10-02'
collected: '2026-10-05'
category: Training
direction: 训练损失函数 · 学习预算规划
tags:
- policy gradient
- cross-entropy
- horizon loss
- label noise
- learning budget
- classification
one_liner: 提出 horizon loss，依据剩余学习预算把交叉熵动态过渡到精确策略梯度，提升 top-1 准确率和抗噪能力
practical_value: '- 在 CTR/CVR 预估、多分类、生成式推荐的 Semantic ID 分类等以 top-1/accuracy 为目标的任务中，可尝试把每样本
  loss 改为 horizon loss：仅需计算 `σ(z+H)-σ(z)` 权重乘 `∇z`，不改模型结构；需按数据集标定 `κ` 为剩余学习率之和的换算系数。

  - 当训练数据存在点击噪声、错误标注或行为噪声时，cross-entropy 会在后期 memorization 噪声样本；horizon loss 会随着预算减少自动降低这些无法修复样本的权重，从而提升干净测试集
  top-1，效果随噪声率增大而增强。

  - 若目标是校准或 NLL（如知识蒸馏、温度校准），不要直接套 accuracy 版 horizon loss：应使用 planning cross-entropy（`P_H[CE]/(1-e^{-H})`），它会降低
  NLL 但可能牺牲 accuracy；目标不同要选择对应 planning objective。

  - 在 LLM post-training / RLHF 的 policy gradient 场景中，PG 的 myopic 分配缺陷同样存在；可以考虑在 policy
  gradient loss 中引入剩余 rollout 或训练步数作为 horizon，让早期像 likelihood、晚期像 reward，缓解对 lost
  causes 的过度投入。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**  
Policy-gradient 方法在强化学习和 LLM post-training 中很关键，但即使在无探索、无 credit assignment、无采样噪声的全信息分类中，exact policy gradient 的 expected accuracy 也远低于 cross-entropy（ImageNet ResNet-50 上 4.2% vs 62%）。原因是 exact policy gradient 只看当前一步的边际收益，权重为 `p(1-p)`，无法根据剩余训练预算调整分配；cross-entropy 权重为 `1-p`，等价于假设训练无限持续。训练本质是在有限预算下把学习资源分配到样本上，损失函数需要感知剩余预算。

**方法关键点**  
- 把分类器看作策略，定义 logit gap `z = f_y - logsumexp(f_{k≠y})`，正确标签概率 `p = σ(z)`。  
- exact policy gradient 对 `∇θp` 的权重是 `p(1-p)`；cross-entropy 对 `-∇θCE` 的权重是 `1-p`。  
- 提出 future error `C_H(z) = ∫_0^H [1-σ(z+s)] ds = CE(z) - CE(z+H)`，归一化得到 horizon loss `L_H(z) = C_H(z)/(1-e^{-H})`。  
- 其梯度权重为 `σ(z+H)(1-σ(z))`：当 H→0 退化为 exact policy gradient，H→∞ 退化为 cross-entropy。  
- 训练中设定 `H_t = κ Σ_{t≤t'<T} η_{t'}`，即剩余学习率之和，把损失从早期接近 cross-entropy 动态过渡到晚期接近 exact policy gradient。  
- planning operator `P_H[ℓ](z) = ∫_0^H ℓ(z+s) ds` 可应用到任意 per-example loss，例如得到 horizon cross-entropy。

**关键实验**  
在 MNIST（MLP）和 ImageNet（ResNet-50、ResNet-101、ViT-S/16）上，flat learning rate 下只替换 loss：  
- ImageNet top-1 准确率比 cross-entropy 提升 1.0–2.4 个点，expected accuracy 提升 4.7–5.4 个点；MNIST top-1 error 降低 0.16±0.04。  
- 标签噪声实验：ResNet-50 上 10% 噪声时 top-1 提升 3.3 个点，50% 噪声时提升 7.3 个点；MNIST 从 0.1 到 2.7 个点。  
- 只有 shrinking horizon 能复现增益，constant/fixed horizon 失败；晚期切换 cross-entropy→exact PG 的手工 horizon 能大致匹配，说明增益主要来自晚期策略转移。  
- planning cross-entropy 将 ImageNet test NLL 从 1.467 降到 1.364，但 expected error 从 0.378 升到 0.393，说明不同目标需不同 planning。

**最值得记住的一句话**  
损失函数应把剩余训练预算作为输入：早期 patient 地学交叉熵，晚期把预算收回，只救还来得及救的样本，能同时提升 top-1 准确率和标签噪声鲁棒性。
