---
title: Flattening Every Memory Peak in Long-Context Mixture-of-Experts Training
title_zh: 抹平长上下文 MoE 训练的所有显存峰值
authors:
- Shrey Pandit
- Xuan-Phi Nguyen
- Yiran Zhao
- Shafiq Joty
affiliations:
- Salesforce AI Research
arxiv_id: '2609.14306'
url: https://arxiv.org/abs/2609.14306
pdf_url: https://arxiv.org/pdf/2609.14306
published: '2026-09-12'
collected: '2026-09-18'
category: Training
direction: 长上下文 MoE 训练显存优化
tags:
- MoE
- Long-Context Training
- Memory Optimization
- Expert Parallelism
- Checkpoint Offload
- Optimizer Offload
one_liner: 针对长上下文 MoE 训练四大显存瓶颈提出四种精确调度，将 120B-667B 模型训练扩展到 1M 上下文，吞吐最高提升 10.4 倍
practical_value: '- 若在业务中训练长上下文 MoE（如融合用户长期行为序列、Agent 记忆的推荐/广告模型），优先采用固定 GPU working
  set 的调度思路，而不是只看平均显存；PipelinedLLEP 与 Ring-DTP 都能在不改精度下显著压峰值。

  - OffloadStreamAdamW 将 CPU optimizer offload 的串行 Adam 改为 bucket 流水线，能直接加速大规模 embedding/排序模型训练中的
  offload 更新；若你已用 CPU offload 放优化器状态，可参照其分桶流水实现。

  - SCO 只把 checkpoint 边界最占显存的长生命周期张量 offload 到 CPU，适合处理用户长序列的生成式推荐/Agent 轨迹训练，能在基本不增加复杂度的前提下扩大
  context 长度。

  - 这些方法只改变执行顺序和搬运粒度，梯度与 loss 严格一致，便于在 FSDP/Megatron 等框架上增量实现，风险低。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：MoE 模型在长上下文/大 batch 训练下，常见并行方案只优化平均显存，四个组件峰值仍无界：expert dispatch 路由矩阵、vocab projection tokens×vocab、gradient checkpoint 深度×序列长度、optimizer state 参数量。哪个先 OOM 取决于模型/上下文/设备数，压下一个会暴露下一个。

**方法**：PipelinedLLEP 给 least-loaded expert parallelism 的每个 dispatch chunk 设 token 上限；Ring-DTP 在 vocab projection 用环形传递 activations/weight shards，并用在线 log-sum-exp 折叠 logits；SCO 把每个 checkpoint 边界的一个长生命周期 tensor 放 CPU；OffloadStreamAdamW 将串行 CPU Adam 更新变成 bucket 流水线。四种只改计算/搬运顺序和粒度，loss 与梯度精确不变。

**结果**：单组件测试中，MoE dispatch 峰值降 59.3% 且不损失吞吐，vocab projection 峰值降 86.6%，offloaded optimizer step 快 2.05×；组合在 120B-667B MoE 上以 1M context 训练，达到调优 FSDP2 基线的 8-32 倍可达范围，吞吐最高 10.4×。
