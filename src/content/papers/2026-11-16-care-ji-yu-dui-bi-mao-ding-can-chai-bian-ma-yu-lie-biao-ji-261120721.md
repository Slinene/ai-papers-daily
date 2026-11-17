---
title: 'CARE: Contrastive-Anchored Residual Encoding with Listwise Reconstruction
  for Retrieval-Oriented Semantic IDs'
title_zh: CARE：基于对比锚定残差编码与列表级重建的检索导向语义 ID
authors:
- Yuan Xu
- Dawei Chen
- Xiaoguang Lin
- Xin Chen
- Yulong Ou
- Haijun Wu
affiliations:
- Tencent
arxiv_id: '2611.20721'
url: https://arxiv.org/abs/2611.20721
pdf_url: https://arxiv.org/pdf/2611.20721
published: '2026-11-16'
collected: '2026-11-17'
category: GenRec
direction: 生成式检索 · Semantic ID
tags:
- Semantic ID
- Generative Retrieval
- Contrastive Learning
- Listwise Distillation
- Residual Quantization
one_liner: 用对比锚定残差编码和列表级蒸馏构建检索导向 SID，无需训练生成器即可提升召回
practical_value: '- 做生成式推荐/搜索 SID 时，先确认上游 item embedding 是否已用搜索或交互数据做过对比学习；若是通用 embedding，在量化前加零初始化残差对齐网络
  + query-doc InfoNCE，并用 anchor loss 锚定原始 embedding，通常能带来明显召回提升；若已 search-tuned，提升较小，优先优化
  embedding 本身。

  - 用 listwise KL 蒸馏保持量化后排序：教师是原始 embedding 在候选列表上的 softmax cosine，学生是 SID 重建 embedding
  的 softmax；候选混合真实 funnel、ANN、随机样本，不需要点击或相关性标签。该 loss 对 SID 召回提升稳定，且不改变文档编码接口。

  - 保持 document-only encoding 接口并冻结一级码本：新文档可独立编码增量上线，前缀树稳定；部署时如果要更新二三级码本，需同步刷新 SID
  映射和用户历史，给下游 GR 模型留出重训时间。

  - 快速迭代 SID tokenizer 推荐用 row-budget recall 的 reconstruction view，辅以 bucketing view，不必每次训练生成器；精确计算部分消费
  bucket 的期望能减少噪声，并与后续 GR 排序保持一致。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
生成式检索中 SID tokenizer 决定生成器能召回哪些文档；但 RQ-KMeans、RQ-VAE、FSQ 等只优化文档自身失真或桶容量，不控制 query-document 关系，量化损失可能恰好破坏查询排序。因此需要以检索为导向做 SID，并在不训练 GR 模型的情况下直接评测 SID 级召回。

## 方法关键点
- **CARE-SID**：在残差量化前插入零初始化残差对齐网络，用 query-doc 双向 InfoNCE 学习检索对齐空间；anchor loss 与固定原始 embedding 的重建目标防止漂移或坍缩。量化核为 R3-VAE 的 reference vector + rating residual quantization。三阶段 warm start：RQ-KMeans → R3-VAE → 加对齐网络。
- **CARE-LR**：在 CARE-SID 上做列表级重建蒸馏。每个 query 的教师分布来自原始 embedding 在候选列表上的 softmax cosine，学生分布来自 SID 重建 embedding；候选来源混合真实搜索漏斗、ANN、随机文档。用 function-preserving 的 layer-resolved head 扩展，初始等价 CARE-SID。冻结一级码本保证前缀树稳定，只更新二三级码本与 head。
- **评估协议**：row-budget recall，精确计算部分消费 bucket 的期望；分 bucketing view 与 reconstruction view，不与 GR 训练绑定。

## 关键实验
在工业视频搜索数据（1,001,700 文档，2,990 queries）上，recon_P3@10：RQ-KMeans 62.75%，CARE-SID 65.23%，CARE-LR 66.09%；CARE-LR 较 RQ-KMeans +3.34 点，较 CARE-SID +0.86 点。消融显示主要增益来自 listwise KL，layer-resolved head 单独贡献不显著；冻结码本仅训练 head 也能达到 66.12%，说明收益主要走重建路径。对比两种 embedding：在未用搜索数据训练的通用 multimodal embedding 上，CARE-SID 比 R3-VAE 提升 +2.10@10；在搜索 tuned embedding 上仅 +0.07，表明 embedding 自身质量远比 tokenizer 重要。CARE-SID 已部署到工业视频搜索 GR 阶段。

## 最值得记住的一句话
量化前做检索对齐、量化后用 listwise 蒸馏保持排序，可以提升 SID 召回；但先有一个搜索 tuned 的 embedding，收益远大于换 tokenizer。
