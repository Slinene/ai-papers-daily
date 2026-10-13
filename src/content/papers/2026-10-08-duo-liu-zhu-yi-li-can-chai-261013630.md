---
title: Multi-Stream Attention Residuals
title_zh: 多流注意力残差
authors:
- Xiaohan Qin
- Xiangdong Zhang
- Tuo Dai
- Sunan Zou
- Huaijin Wu
- Yebin Yang
- Zhuo Xia
- Lin Yao
- Yuliang Liu
- Junchi Yan
affiliations:
- School of AI, Shanghai Jiao Tong University
- Shanghai Innovation Institute
- Dots Studio, Xiaohongshu Inc.
- School of CS, Peking University
arxiv_id: '2610.13630'
url: https://arxiv.org/abs/2610.13630
pdf_url: https://arxiv.org/pdf/2610.13630
published: '2026-10-08'
collected: '2026-10-13'
category: Training
direction: 高效 LLM 预训练 · 深度残差架构
tags:
- Multi-Stream Attention
- Residual Connections
- MoE
- Scaling Laws
- LLM Pretraining
- Depth Attention
one_liner: 将单流深度注意力残差扩展为多流深度注意力，通过多尺度因果卷积生成多样化上下文视图，在 MoE 大模型上取得 1.58 倍预训练加速
practical_value: '- 若业务需要自研或微调大模型作为排序/召回/Agent 底座，可评估用 MSAR 替换标准残差连接：保持单流存储、按需扩展多流深度检索，iso-loss
  预训练加速 1.58×，对 MoE 架构尤其明显。

  - 多尺度因果卷积生成不同上下文视图的思路可迁移到用户行为序列建模：使用不同 kernel size 的因果卷积提取短期点击、中期会话、长期兴趣等多时间尺度表示，再通过自适应混合融合，增强序列建模能力。

  - 轻量自适应混合多个检索流的机制，可作为推荐模型中多兴趣/多视图融合的替代方案：避免显式维护多流表示和通信开销，降低工程实现复杂度。

  - 需注意该工作验证于 18B/28B 大规模 MoE 语言模型预训练，直接搬到电商推荐的小模型或非 Transformer 结构收益未知；引入多流机制可能增加调试复杂度，建议先在离线评测中验证深度特征稀释问题是否真实存在。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现代 PreNorm Transformer 深度扩展时，残差流以单隐藏状态轨迹累积信息，早期特征在深层被稀释，后期层难以有效检索，导致深度缩放效率下降。AttnRes 将深度轴视为单流 softmax 注意力，实现内容依赖的跨层检索，但仍只有单一检索视角。

**方法关键点**：MSAR 将 AttnRes 扩展为深度轴多头注意力。不同头通过多尺度因果卷积从序列上下文获得不同视图，检索历史表示时关注不同时间尺度；检索到的多流表示经轻量自适应混合生成单流层输入。核心设计是保留单流源，按需扩展多流计算，不需要持久多流存储或通信，额外开销极小。

**关键结果**：在 18B 和 28B MoE 规模、12 个下游基准上，MSAR 一致优于标准残差、mHC 和 AttnRes。Scaling-law 实验显示 iso-loss 计算加速比标准残差基线高 1.58×，AttnRes 为 1.35×，mHC 为 1.30×。
