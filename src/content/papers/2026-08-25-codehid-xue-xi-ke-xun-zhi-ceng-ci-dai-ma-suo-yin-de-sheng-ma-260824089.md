---
title: 'CodeHID: Learning an Addressable Hierarchical Code Index for Generative Code
  Retrieval'
title_zh: CodeHID：学习可寻址层次代码索引的生成式代码检索
authors:
- Zhen Li
- Yuhong Chen
- Wenhao Xu
- Xiaodong Li
- Hui Li
affiliations:
- Xiamen University
arxiv_id: '2608.24089'
url: https://arxiv.org/abs/2608.24089
pdf_url: https://arxiv.org/pdf/2608.24089
published: '2026-08-25'
collected: '2026-08-26'
category: GenRec
direction: 生成式检索 · 层级语义 ID
tags:
- Generative Retrieval
- Semantic ID
- RQ-VAE
- Code Retrieval
- Prefix-Aware Decoding
- Rank Distillation
one_liner: 将代码检索重构为层级语义 DocID 生成，以 kNN 伪标签学习前缀语义结构，并在训练与推理侧联合引导路径选择。
practical_value: '- 构建商品/内容语义 ID 时，不要只用 RQ-VAE 自重构；叠加 kNN 伪标签约束前缀共享，让相似 item 在浅层共享前缀、深层保留区分度，可形成类目/风格/价格带的多粒度索引。

  - 生成式推荐/召回训练时，除标准 next-token DocID loss 外，挖掘 query-item 相似度 TopK 的 hard negative
  DocID，加 pairwise margin loss 和 teacher-student rank distillation，能明显提升 Top1 命中；工业界可复用双塔打分作为
  teacher。

  - 推理时先粗召回 TopB 候选 item 构建合法前缀 trie，再做约束 beam search，并用 query-item 相关性作为 prefix-level
  lexical bonus 微调 beam 打分，比全空间解码更稳定、低延迟。

  - 采用 frozen encoder + LoRA decoder 架构，DocID 离线固定，线上只更新 query 到 DocID 的生成路径，适合快速迭代生成式召回模型。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

## 动机

代码检索主流仍是 flat matching：把 query 和候选 code snippet 分别编码后按相似度排序，候选之间相互独立，缺乏对代码语料内部语义结构和候选间关系的建模。生成式检索虽能构建可学习索引，但直接套用常见 DocID 前缀常常不对应明确语义区域，容易放大 surface bias，尤其难以区分功能相似但实现不同的代码片段。

## 方法关键点

CodeHID 将代码检索从扁平候选匹配重构为“由粗到细的语义地址生成”，核心是两个组件：

- **Pseudo-Neighbor Guided DocID Learning**：离线构建全局静态层级 DocID。基于 RQ-VAE 对代码嵌入做多层残差量化，得到 4 层 DocID（codebook size=256）；同时在连续语义空间建 kNN 图（k=8），结合层级相似度阈值生成伪标签，用 BCE 约束 soft code assignment 得到的前缀共享概率，使语义相近代码在合适深度共享前缀，同时通过负样本分离保持目标级可区分性。
- **Dual-Phase DocID Generation Guidance**：训练侧挖掘 query 条件下高相关非目标 DocID 作为 hard negatives（K=4），组成局部候选集；除 DocID 交叉熵外，加入 pairwise lexical consistency loss 和基于 teacher 相关性分布的 KL rank distillation，强化相似路径区分。推理侧先用 query-code 相似度召回 TopB=3000 候选 DocID 构建 trie，约束解码只允许合法前缀；再将 query 相关性分数传播到 prefix 级作为 lexical bonus 介入 beam search（beam size=20，β=0.1）。

实现上使用 frozen GraphCodeBERT encoder + Qwen2.5-Coder-7B decoder LoRA 微调。

## 关键实验

在 CoSQA、ProCQA-Python、ProCQA-Java 上对比 BM25、CodeBERT、UniXcoder、CodeSage、OASIS、CodeXEmbed、DSI、NCI、GLEN、RIPOR。CodeHID 在 CoSQA 上 Hit@1 达到 0.744（UniXcoder 0.518），MRR@20 0.766；ProCQA-Python Hit@1 0.597，MRR@20 0.706；ProCQA-Java Hit@1 0.520，MRR@20 0.654。1.5B 版本也超过同参数量级 dense baseline。消融显示去掉 DocID Learning 后 CoSQA Hit@1 掉到 0.399，去掉训练侧或推理侧引导也大幅下降；在 baselines top-5 失败的 query 上 Recovery@1 平均达 76.3%。

## 最值得记住的一句话

生成式检索的效果高度依赖具有语义前缀结构的固定 DocID 空间，以及训练/推理两阶段对候选路径的显式区分与校准。
