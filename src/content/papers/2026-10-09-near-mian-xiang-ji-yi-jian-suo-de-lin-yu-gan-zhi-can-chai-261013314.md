---
title: 'NEAR: Neighborhood-Aware Residuals for Memory Retrieval'
title_zh: NEAR：面向记忆检索的邻域感知残差框架
authors:
- Han Luo
- Zhan Zhuang
- Xu He
- Jujia Zhao
- Yu Li
- Suqin Yuan
- Dong Li
- Lei Feng
affiliations:
- Southeast University
- MemoraX AI
- Leiden University
- University of Sydney
arxiv_id: '2610.13314'
url: https://arxiv.org/abs/2610.13314
pdf_url: https://arxiv.org/pdf/2610.13314
published: '2026-10-09'
collected: '2026-10-12'
category: RAG
direction: 记忆检索 · 邻域残差投影
tags:
- memory retrieval
- training-free
- residual representations
- ANN search
- long-term memory
- embedding calibration
one_liner: 训练无关地用邻居方向构造投影残差，把共享主题带来的干扰记录转为匹配信号，单次 ANN 检索提升记忆召回。
practical_value: '- 可把“同品牌/同店铺/同话题商品的向量相似但证据不相关”问题转化为局部参考：离线对每个 item/memory 用 top-k
  邻居均值方向做投影残差，抑制类目/品牌共性，放大差异；适合商品召回、内容去同质化。

  - training-free + 固定索引：残差和原向量拼接成静态 key，线上只做一次内积 ANN（如 HNSW），不用改 encoder 或做多路召回，便于接入现有
  embedding 库。

  - query 侧参考由 16 个 anchor 的 spherical K-means + softmax 路由生成，避免在线先检索邻居，工程轻量；可迁移到
  query embedding 的在线局部校准。

  - 存储/延迟可控：NEAR 未压缩是 Base 2x 存储、约 2.39x 延迟；用 SQ4 可压到 Base FP32 的 0.36x，Recall 几乎不变。适合大规模
  item/memory 索引，结合业务接受度调节 residual weight/depth。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
长期记忆检索中，多条记录常共享人物、话题、事件。只靠 query-memory 向量相似度排序，容易让“相似但无证据”的记录排在正确答案前。NEAR 的出发点不是把这些共享内容当噪声，而是反过来利用它们构造局部参考方向，把干扰源变成匹配信号。

**方法关键点**  
- 每个 memory 取当前表示下余弦 top-k 邻居，平均方向单位化后作为局部参考 c_i；移除记忆向量在该方向的投影，得到残差 r_i = h - (h^T c)c。可迭代多层，每层用归一化残差继续。  
- query 侧为避免在线先检索，离线用 spherical K-means 聚类记忆表示，得到 anchor；每个 anchor 存其簇内记忆参考方向的均值。query 选最相似 R 个 anchor，softmax 加权生成自身参考，再做同样投影。  
- 原始向量与各层残差表示按 τ_l 缩放后以 α 融合；通过 key/query 拼接，最终得分仍是一个内积，memory keys 离线建好，线上单次 ANN 检索。  

**关键实验与结果**  
在 8 个 LMEB 检索基准、9 个 frozen embedding 模型上，NEAR 平均 Recall@10 和 NDCG@10 均有提升。例如 Qwen3-Embedding-4B 的 Recall@10 从 62.67 升到 69.76，NDCG@10 从 47.88 升到 55.33。下游 QA 上，LoCoMo 用 Qwen3-30B-A3B 回答时 Accuracy 提升 9.6 个百分点。消融显示，局部参考、memory-reference 对应关系以及 query+memory 双侧残差都关键；SQ4 量化可把存储降到 Base FP32 的 0.36x，质量几乎不变。

**最值得记住的一句话**  
共享内容不一定是噪声：用邻居构造成局部参考方向做残差投影，能让检索系统在不重训 encoder 的情况下稳定提升召回。
