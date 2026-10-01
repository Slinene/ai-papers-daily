---
title: Learning Functional Subspaces for Neural Network Compression
title_zh: 学习功能子空间实现神经网络压缩
authors:
- Massimo Bini
- Anders Christensen
- Stephan Alaniz
- Judah Goldfeder
- Ole Winther
- Yann LeCun
- Ravid Shwartz-Ziv
- Zeynep Akata
affiliations:
- Helmholtz Munich
- Technical University of Munich
- Télécom Paris
- Columbia University
- New York University
arxiv_id: '2609.40127'
url: https://arxiv.org/abs/2609.40127
pdf_url: https://arxiv.org/pdf/2609.40127
published: '2026-09-30'
collected: '2026-10-01'
category: Training
direction: 低秩压缩 · 功能子空间学习
tags:
- low-rank compression
- LLM
- KV cache
- knowledge distillation
- orthogonal projection
- model compression
one_liner: 用端到端学习的正交投影子空间替代逐层闭式低秩截断，显著提升LLM/ViT高压缩比下的精度与推理效率
practical_value: '- 在电商/广告/搜索的LLM部署中，可用LSP对底座或领域模型做低秩压缩：用线上日志、商品语料或搜索曝光文本作为校准集，冻结原权重、以KL蒸馏学习要删的子空间，比SVD/剪枝更适合极限压缩。

  - 直接复用「按输出KL边际成本分配rank」：Q/K/V往往比MLP更可压，注意力层可更激进地降秩；避免均匀分配浪费参数，分配阶段无需梯度，便于工程落地。

  - 借鉴tied projector共享Q/K/V输入因子：KV cache只存一个窄潜在向量，可显著降低长上下文用户序列、Agent记忆或会话历史的显存占用；配合Palu/MLA类实现效果明显。

  - 训练后合并为标准低秩矩阵，无额外算子，容易接入TensorRT/vLLM等推理框架；warm-up、direction dropout和正交惩罚等技巧可直接迁移到自研压缩流程。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有低秩压缩通常按层闭式选择要删除的子空间：激活能量、层重构误差或损失的二次近似。这些准则只看单层，忽略误差沿深度传播，高压缩比下误差逐层累积，性能崩溃。因此需要学习全局「功能子空间」：保留网络输出真正依赖的方向，而不是仅按谱能量截断。

### 方法关键点
- LSP为每个线性层或共享输入激活的tied group（如Q/K/V、gate/up）分配正交投影器P=I-UU^T；优化U（用无约束V和QR保正交），冻结预训练权重，端到端最小化与dense模型输出分布的KL或原始任务损失。
- 初始化来自whitened SVD截断，扩展到tied group；rank分配按每个投影器单独造成的输出KL边际成本，逐参数选择最便宜的删除量。
- 训练使用activation-space形式、warm-up、direction dropout和正交惩罚；训练后投影器合并为低秩因子，共享tied group的输入因子，实现更少的小矩阵乘和更窄的KV cache。

### 关键结果
- 在OPT-125M/1.3B、Qwen3-4B、Llama-2-7B上，LSP在全部12个模型-压缩比设置中取得最低困惑度；Llama-2-7B在-70%压缩下WikiText-2 PPL为10.9，最强基线SVD-LLM为13.3，未学习的NoLSP为222.8。
- 零样本平均准确率在Llama-2-7B -70%达42.2%，基线最高36.0%；ViT-B/16上对校准分布偏移最鲁棒，diverse无标签数据下迁移最好。
- 推理效率：Llama-2-7B解码最多比dense快1.56倍；128k上下文下权重+KV cache内存缩小13.5倍，而untied因子化最多6.5倍。

### 最值得记住的一句话
「Spectral energy is not function」——要压缩的不是统计冗余方向，而是输出最不依赖的方向，并且这些方向应当端到端学习。
