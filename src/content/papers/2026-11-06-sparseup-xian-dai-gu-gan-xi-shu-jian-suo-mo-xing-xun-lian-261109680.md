---
title: 'SPARSEUP: Towards Better Recipes for Training Modern Learned Sparse Retrievers'
title_zh: SPARSEUP：现代骨干稀疏检索模型训练配方
authors:
- Thibault Formal
- Pierre Erbacher
- Cosimo Rulli
affiliations:
- Linkup, Paris
arxiv_id: '2611.09680'
url: https://arxiv.org/abs/2611.09680
pdf_url: https://arxiv.org/pdf/2611.09680
published: '2026-11-06'
collected: '2026-11-09'
category: Training
direction: 稀疏检索 · 训练配方
tags:
- Learned Sparse Retrieval
- Splade
- Logit Shift
- Fan-out
- Vocabulary Folding
- BEIR
one_liner: 用 logit shift、fan-out 与 vocab folding 稳定现代骨干的 Splade 式稀疏检索训练
practical_value: '- 电商搜索/召回里的 Splade-like 稀疏模型迁移 ModernBERT 等现代骨干时，先做 logit shift：用
  logits 在样本上的 99.9 分位数作为 θ，否则可能训练不稳定甚至失败；成本极低。

  - 用 per-position fan-out（top-f，f≈8-12）替代单纯加大 FLOPS 正则或后剪枝，能在相同 nnz 预算下拿到更高 nDCG，适合固定
  latency 的召回链路。

  - byte-level BPE 会把大小写/词边界变体拆成多个 vocab 维度，导致品牌词/型号词（如 iPhone vs iphone）匹配失败；训练与推理都做
  vocabulary folding，合并 surface forms，零参数且稳定提升。

  - 若线上需要固定 top-k 非零维，训练时对齐同一 top-k 有收益（k=64 时 +4 点），但该模型不泛化到更大 k；否则建议无约束训练 + 推理时剪枝。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
Learned sparse retrieval 是 dense retrieval 的高效替代，但 Splade 类模型训练条件苛刻，现代 backbone 直接迁移经常不收敛或效果低于 BERT-base。已有工作分别归因于 vocabulary gap 和 head scale，但缺少统一可复现配方。

**方法关键点**
- **Logit shifting**：预训练 softmax CE 对 logits 全局平移不敏感，但 Splade 的 log(1+ReLU(z)) 敏感。把 LM head logits 减去常数 θ，θ 取 logits 分布的 99.9 分位数（ModernBERT/Ettin θ=15，RoBERTa θ=56），使初始化更稀疏、梯度更有区分度。
- **Per-position fan-out**：每个 token 位置只激活 top-f 个 vocab 维度后再 max-pooling（f=12），限制每个位置的无关注入噪声，比 FLOPS 正则/后剪枝更稳且有效。
- **Vocabulary folding**：合并 byte-level BPE 产生的大小写/词边界变体，训练和推理都映射到 canonical token，参数零成本；ModernBERT vocab 从约 50k 降到 34k。
- 训练数据为 Embeddings-Fine-Tuning，InfoNCE + 7 hard negatives + FLOPS 正则，不依赖 cross-encoder 蒸馏；主模型在 LateOn backbone 上嫁接 ModernBERT MLM head。

**关键实验与结果**
在 Beir-13 上达到 56.4 avg nDCG@10，为 150M 以下 public vocabulary-based sparse encoder 最高；比同数据/同 backbone 的 DenseOn 仅低 1.5，decontaminated Beir 与 DenseOn 基本打平。消融显示 logit shift 与 fan-out 各自有效且可组合；训练时 top-k 仅在 k=64 强压缩时有明显收益且不泛化到更大 k。OOD 上 BRIGHT-Pro 超 DenseOn +4.9 nDCG@10；加入 KD 后 CURE-en +2.5、ChemTEB +3.3。

**最值得记住**：现代 backbone 训 sparse encoder，先把 logits 左移到 99.9 分位数，再做 per-position top-f fan-out，通常比调 FLOPS 正则更稳更好。
