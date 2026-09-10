---
title: When Does Low-Bit Quantization Preserve the Decisions of Vector Search?
title_zh: 低比特量化何时能保持向量搜索的决策？
authors:
- Wenxuan Xiao
- Xu Cao
affiliations:
- Astrmira Tech.
arxiv_id: '2609.09854'
url: https://arxiv.org/abs/2609.09854
pdf_url: https://arxiv.org/pdf/2609.09854
published: '2026-09-09'
collected: '2026-09-10'
category: RecSys
direction: 向量检索 · 量化决策保真
tags:
- low-bit quantization
- vector search
- decision flip
- Vamana
- margin analysis
- quantization robustness
one_liner: 提出基于比较翻转的量化向量搜索分析框架，精确边际预测翻转率显著优于全局秩相关。
practical_value: '- 评估量化方案别再看平均失真或全局秩相关，直接监控 exact margin 分布和比较翻转率，特别是在大规模 ANN 召回中，这更能预测线上相关性丢失。

  - 上线低比特索引前，用 held-out block certificate 对冻结量化规则进行选择性失败风险评估，避免特定 query 或 segment
  上召回崩塌。

  - 对 Vamana / HNSW 等图索引，用耦合定理诊断量化引入的边分叉，定位对量化敏感的具体剪枝步骤，针对性加保护或回退高精度。

  - 如果嵌入具有对齐双线性结构，可考虑确定性幅度位等几何设计，在相同码率下提升比较保真；注意残差间共享 query 导致的强相关，评估时采用协方差感知指标而非独立假设。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：低比特量化在不同向量表示上表现差异巨大，如 2-bit 坐标码在 Cohere 文本嵌入上恢复 95% 精确最近邻，在 GIST 图像描述子上仅 2%；平均失真和全局秩相关无法解释这一现象。图搜索算法消费的是比较而非距离估计，比较翻转是量化噪声跨越特定决策边界的结果。

**方法**：提出分布自由分解：比较翻转概率 ≤ 精确边际近零概率质量 + 校准残差尾部概率。考虑共享 query 或图节点的残差依赖，用协方差感知二阶矩和联合 MGF 尾界。对 Vamana 邻居选择证明确定性耦合定理：近似回放得到相同邻居列表当且仅当所有候选级剪枝动作与精确一致，首次分歧标识输出分叉边。通过高斯 oracle、对齐双线性模型和稀有污染构造连接表示几何，并给出 held-out block certificate 从数据评估冻结量化规则的选择性失败风险。

**结果**：在学习的、经典、合成嵌入上，标准化精确边际预测 held-out 翻转率的 Spearman 相关为排名 0.97、剪枝 0.99，对比全局秩相关 0.74 和 0.05；耦合恒等式在 9 个数据场景成立。框架统一适用于 coordinate binary codes、RaBitQ、Lucene BBQ 和 product quantizers。
