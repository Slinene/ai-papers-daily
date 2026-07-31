---
title: 'ROCS: Request-Oriented Compute Sharing for Efficient Large-Scale Recommendation'
title_zh: ROCS：面向请求的计算共享实现大规模推荐高效推理
authors:
- Yuxin Chen
- Liang Luo
- Buyun Zhang
- Jian Jiao
- Boda Li
- Haoyu Wang
- Tongyi Tang
- Ao Cai
- Zijian Shen
- Zhengkai Zhang
affiliations:
- Meta AI
arxiv_id: '2607.27744'
url: https://arxiv.org/abs/2607.27744
pdf_url: https://arxiv.org/pdf/2607.27744
published: '2026-07-30'
collected: '2026-07-31'
category: RecSys
direction: 请求导向计算共享 · 推理加速
tags:
- Request-Oriented Computing
- Inference Efficiency
- GPU Kernel Optimization
- Deep Cross Attention
- Generalized Layer Masking
- Recommendation Systems
one_liner: 通过GLM和DCA延迟交互并复用请求侧计算，配合IKBO内核优化，在不损失质量下最高获得3×QPS提升
practical_value: '- **改造现有交叉网络**：借鉴GLM思想，在DCNv2或FinalMLP等特征交互模块中，将输入分组为请求侧和候选侧，对线性层、MLP等施加下三角掩码，强制请求侧输出不依赖候选特征，从而可在多候选间复用。在电商排序中，每个用户请求评估数百商品，可节省大量重复计算。

  - **用户序列建模引入DCA**：对于用户行为序列，先用请求侧编码器一次得到各层表征，再在每层通过跨注意力进行候选条件检索，避免为每个候选重复跑序列模型。在广告推荐中，这能将序列计算复杂度从O(N×seq_len^2)降至接近O(seq_len^2)。

  - **工程实现使用IKBO**：在GPU推理时，不显式将请求张量广播到候选batch大小，而是通过索引映射在GEMM或注意力内核内部按需加载，并结合融合广播加法、持久化CTA和内存对齐优化。可用Triton编写定制内核，减少HBM带宽占用。

  - **计算重新分配策略**：节省的FLOPs可倾斜分配到请求侧（因被所有候选平摊），提升模型容量而不显著增加延迟。例如，在排序模型中，可将约80%的预算分配给请求侧，在几乎不增加推理成本的情况下提高AUC。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
现代推荐模型通过增强特征交互和序列建模来提升预测质量，但每次推理一个请求需评估多个候选物品，请求侧特征在所有候选间共享却仍被重复计算，导致算力浪费。已有方法如双塔模型限制交互，系统优化则受限于域干扰和蒸馏效率。ROCS 针对这一结构冗余，提出从模型架构层面暴露和复用请求共享计算。

## 方法关键点
- **总体思路**：延迟请求-候选交互点，构建一个可复用的请求侧子图，在请求级计算一次，候选级只计算不可共享部分。
- **广义层掩码（GLM）**：定义算子级依赖合约，强制每个算子输出组仅依赖输入的前序组（下三角掩码）。对于线性层、因子分解机等，通过屏蔽特定交互方向，确保请求侧输出不因候选变化而改变，从而可准确共享。
- **深度交叉注意力（DCA）**：将候选感知序列建模解耦为共享序列编码和逐层候选条件检索。请求侧自注意力独立于候选，其K/V投影计算一次后在各层被请求和候选查询跨注意力利用。
- **请求导向资源再分配（RRR）**：将节省的算力重新投入到请求侧（因被候选平摊），利用缩放定律提升质量-效率边界。
- **内核广播优化（IKBO）**：不显式将请求张量广播到候选批次，而是在GPU内核内通过索引映射直接加载请求侧贡献，融合GEMM与加法、持久化CTA、内存对齐等技术消除内存开销。

## 关键结果
- 公开基准：在KuaiVideo、KuaiRand、KKBox上，与DCNv2、FinalMLP、Wukong等骨干结合，ROCS-Scaled在同等NFLOPS@100下AUC胜出基线。
- 生产评估：短视频排序模型上相对LogLoss改善0.5%，QPS提升47%；广告检索模型QPS提升196%（约3倍）；广告排序模型QPS提升62%，质量持平。
- 在线部署：数十个Meta模型上线，短视频排名模型topline指标提升0.04%同时节省32%容量；广告检索模型topline提升0.2%且节省29%容量。
