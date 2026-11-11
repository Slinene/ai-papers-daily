---
title: 'onóna: Twin Embeddings with Tied Unembeddings'
title_zh: Onóna：双表孪生嵌入与绑定解嵌提升输出表达力
authors:
- Cheng Luo
- Xinnan Dai
- Zhongzhu Zhou
- Zefan Cai
- Ruijie Zhu
- Tianyu Zhang
- Junjie Hu
affiliations:
- Independent Researcher
- Michigan State University
- Together AI
- University of Wisconsin–Madison
- University of California, Santa Cruz
arxiv_id: '2611.10556'
url: https://arxiv.org/abs/2611.10556
pdf_url: https://arxiv.org/pdf/2611.10556
published: '2026-11-06'
collected: '2026-11-11'
category: Training
direction: LLM 训练 · 权重绑定与输出表达力
tags:
- weight tying
- embedding
- unembedding
- softmax bottleneck
- language modeling
- training efficiency
one_liner: 提出双表 embedding/unembedding 共享参数化，门控混合两个 softmax 突破单表瓶颈，在多数架构和规模上降低损失并提升下游精度。
practical_value: '- 在电商 query 推荐 / 生成式推荐中，若输入与输出共享 token 表（如 Semantic ID、query 词表），可参考双表+门控结构，以极小参数代价缓解单
  softmax 瓶颈，提升 top-k 多样性和损失。

  - 门控仅依赖当前输入 token，推理前可预计算所有 token 的门控权重，不增加序列推理开销；只需额外一张 embedding 表和一次输出投影，适合线上延迟敏感场景。

  - 论文在 142M–1B 多架构验证有效，但 1B MoE 损失例外；部署到 MoE 生成模型时建议先小规模验证 gain，避免盲目替换。

  - 若团队训练中/小规模 LLM 用于商品文案、搜索 query 生成，可尝试在现有 tied embedding 基础上直接改造输出头，Transformer
  主体不用动，工程改动小。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：语言模型常用权重绑定节省参数，但传统单一绑定表输出 head 受 softmax bottleneck 限制，log-probabilities 矩阵秩最多 d+1，难以表达高秩 next-token 分布。

**方法关键点**：引入 onóna 双表参数化。Transformer 输入取两个 embedding tables 的平均，输出 head 将两个表产生的 softmax 分布按一个门控系数混合；门控仅由当前输入 token 决定，推理时可预计算，主体网络不变。训练时两个表同时参与输入和输出角色，保持权重绑定优势但增加输出表达力。

**关键结果数字**：在 Dense、Gated DeltaNet hybrid、MoE、Attention Residual 等架构，142M/330M/1B 规模，匹配 token 预算下，12 项对比中 11 项 lower final validation loss 和 external perplexity，10/12 项平均下游 8 任务准确率提升；唯一损失例外是 1B MoE。额外成本为一个 embedding table 和一个 vocabulary projection。
