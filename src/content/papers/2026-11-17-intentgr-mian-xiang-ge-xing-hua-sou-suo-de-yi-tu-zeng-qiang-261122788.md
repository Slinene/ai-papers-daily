---
title: 'IntentGR: Enhancing Intent for End-to-End Personalized Generative Retrieval
  in Search'
title_zh: IntentGR：面向个性化搜索的意图增强端到端生成式检索
authors:
- Gefan Ye
- Yanjing Wu
- Yinfu Feng
- Zhiqiang Wang
- Liang Li
- Jun Xiao
- Rong Xiao
- Xiaoyi Zeng
affiliations:
- Zhejiang University
- Alibaba International Digital Commercial Group
arxiv_id: '2611.22788'
url: https://arxiv.org/abs/2611.22788
pdf_url: https://arxiv.org/pdf/2611.22788
published: '2026-11-17'
collected: '2026-11-18'
category: GenRec
direction: 生成式检索 · Semantic ID · Query Intent
tags:
- Generative Retrieval
- Semantic ID
- Personalized Search
- Query Intent
- Long-tail Query
- E-commerce Search
one_liner: 在端到端生成式检索的输入、优化、训练分布与解码四处注入 query 意图，显著提升个性化搜索召回
practical_value: '- 电商搜索生成式召回中，除用户历史外，把同一 query 的历史点击/成交 item 序列 H_q 拼进 encoder 是一种低成本高收益输入改造；单独用
  H_q 做非参数召回也能达到接近生成式 baseline 的 69.36% Recall@10，可作为强 baseline 或冷启动召回通道。

  - QSA 的 query-to-item 双向对比损失可与 RQ-VAE tokenizer、生成 retriever 共享，让 Semantic ID 学习直接受搜索意图监督，适合迁移到电商
  SID 联合训练。

  - LQE 对长尾 query 做重采样 + query rewriting 增强，在工业数据集上 long-tail 提升明显，工程实现简单；注意只在训练集增强，验证/测试保持原分布。

  - QAM 是轻量 decoding 端 trick：把 query 聚合向量融合进 cross-attention context，α=0.8 时保留行为语义并强化
  query conditioning，可尝试用于 query 驱动的生成式排序或文案生成。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

动机：个性化搜索需要同时满足即时 query 意图和用户长期偏好。现有端到端生成式检索多把 query 当作普通输入特征，未显式引导 Semantic ID 学习与解码，导致生成的 identifier 偏向高频 token 模式，而非当前搜索意图；query 级行为证据也未被充分利用。

方法关键点：
- QBR：引入同一 query 的历史点击序列 H_q，作为 query-level collaborative filtering 信号，与 query、用户历史 H_u 拼成 [E_q; E_Hq; E_Hu] 输入 encoder，让模型定位与当前 query 相关的历史兴趣。
- QSA：把 query encoder 表示映射到 item 语义空间，与 tokenizer 重建 item 表示做双向 InfoNCE，在联合优化中显式对齐 query 与 item 语义。
- LQE：对训练集低频 query 按频率重采样并做 query rewriting，生成同意图变体，缓解 head query 对训练的支配。
- QAM：对 query token 聚合得到全局向量，以 α=0.8 融合进非 query 的 encoder states，再供 decoder cross-attention，强化解码时的 query conditioning。
- 训练沿用交替更新 tokenizer/retriever，并加入 SIA、PSA 与 QSA；之后冻结 tokenizer 做 GR fine-tuning。

关键结果：在 AOL4PS 上，IntentGR Recall@10 达 77.99%，比最强 baseline ETEGRec-Q 的 69.88% 高 8.11 个百分点；在阿里国际 AE 工业数据集上，Recall@10 从 22.40% 提升到 34.36%，高 11.96 个百分点。长尾 query 和低活用户提升更显著：AOL4PS low-frequency bucket Recall@10 从 41.47% 提高到 57.32%。

最值得记住的一句话：query 相关行为证据若只在输入层拼接，收益有限；必须在输入、联合优化、训练分布、解码四处同时注入 intent，才能让生成式 SID 从高频记忆转向意图匹配。
