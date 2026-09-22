---
title: LoRA-generating hypernetworks for efficient on-device LLM generative personalization
title_zh: LoRA生成超网络用于高效设备端LLM生成式个性化
authors:
- Sean Augenstein
- Li Ding
- Jihwan Lee
- Keith Rush
- Andrey Zhmoginov
arxiv_id: '2609.24979'
url: https://arxiv.org/abs/2609.24979
pdf_url: https://arxiv.org/pdf/2609.24979
published: '2026-09-21'
collected: '2026-09-22'
category: LLM
direction: 设备端LLM个性化 · 超网络生成LoRA
tags:
- LoRA
- Hypernetwork
- On-device LLM
- Personalization
- PEFT
- ICL
one_liner: 训练超网络将用户上下文映射为个性化LoRA，兼顾ICL计算可行性与PEFT权重修改优势
practical_value: '- 将 hypernetwork 生成个性化 LoRA 的思路用于用户级文案生成（如 push 消息、推荐理由），可避免对每个用户做云端微调或扩展
  prompt；设备端只需一次前向计算，延迟低且不增加输入长度。

  - 该架构共享基础 LLM 权重并仅需额外存储一个超网络，适合移动端/边缘设备部署；业务中若需为大量用户提供个性化生成能力，可考虑训练一个通用的用户编码器+超网络，而非保存大量微调模型。

  - 用户上下文 token 作为输入，可类比在推荐系统中将用户行为序列编码后生成适配参数；此方法可作为生成式推荐中轻量用户表征的一种实现，用于生成个性化语义 ID
  或推荐文案的 LoRA 适配。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：设备端 LLM（如手机）受限于计算资源，模型规模和质量有限，个性化能带来显著收益；但现有方法各有缺陷：ICL 需扩展输入序列导致延迟，PEFT 需反向传播和额外存储且难以在设备端进行。

**方法**：训练一个 hypernetwork，将用户上下文 token（如历史文本、偏好描述）映射为一组 LoRA 低秩适配矩阵；部署时，设备端仅需一次 forward pass 通过 hypernetwork 生成该用户的 LoRA，并将其叠加到目标 LLM。该架构部分复用目标 LLM 权重，额外存储极小。

**结果**：在多个个性化数据集上，尤其长文本生成任务，对比 ICL 和 PEFT 基线，在质量与效率（延迟、存储）之间取得更优平衡。
