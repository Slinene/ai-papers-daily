---
title: 'VIA-SD: Verification via Intra-Model Routing for Speculative Decoding'
title_zh: 通过模型内路由的分层验证推测解码加速
authors:
- Yuchen Xian
- Yang He
- Yunqiu Xu
- Yi Yang
affiliations:
- Zhejiang University
- Agency for Science, Technology and Research (A*STAR)
- National University of Singapore
arxiv_id: '2606.12243'
url: https://arxiv.org/abs/2606.12243
pdf_url: https://arxiv.org/pdf/2606.12243
published: '2026-06-10'
collected: '2026-06-11'
category: LLM
direction: 推测解码 · 分层验证 · 模型内路由
tags:
- Speculative Decoding
- Intra-Model Routing
- Hierarchical Verification
- LLM Inference
- KL Divergence
one_liner: 引入从大模型内部路由出的轻量分层验证器，处理中等置信度 token，减少大模型调用，提升推测解码速度 10-20%
practical_value: '- 分层验证思路可迁移到电商推荐多级排序：用轻量模型初筛，中等模型精排，大模型处理疑难 case，降低整体延迟。

  - 模型内路由（DIMR）允许从大模型直接裁剪出轻量验证器，无需额外训练或独立模型，利于内存受限的线上部署。

  - 利用 KL 投影设计中间验证器置信度阈值，指导业务中质量-效率权衡的参数调节。

  - 方法兼容现有 draft-verify 框架，可即插即用增强生成式推荐中 token 序列的生成速度。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**
推测解码用轻量 drafter 生成候选，大模型并行验证，但传统二元接受/拒绝机制在中等置信度 token 上造成大模型冗余计算。观察到大量 token 处于“中间地带”——drafter 输出不够准确但也不需完整大模型重算，由此引出分层验证的动机。

**方法关键点**
- 将推测解码重构为多级验证过程，从 KL 信息几何出发，以投影方式插入中间分布。
- 实现 VIA-SD 框架：drafter 提出候选块，然后通过两级验证门控（高置信度直接接受，中等置信度由 slim-verifier 重写，低置信度升级到大模型）。
- Slim-verifier 由大模型通过**动态模型内路由（DIMR）** 得到：按层 skip 比例 r 路由出子模型，通过最小化 KL 风格代价函数搜索最优路由掩码。
- 验证逻辑根据两个置信度阈值 α1, α2 区分区域，所有路由仅需一次离线搜索，推理时无需动态调整。

**关键实验**
在 T5, Gemma2, LLaMA2, Qwen 等模型对上进行测试，覆盖总结、翻译、QA、推理、代码任务。与 Speculative Decoding、Cascade SD、Faster Cascades 等基线比较，VIA-SD 将拒绝率降低 0.10–0.22，推理加速 10–20% over 最强基线，对 encoder-decoder 模型（如 T5）在 WMT14 上达 2.5–3.35× 加速。消融实验表明 DIMR 路由方式优于随机跳层或独立中间模型，且阈值设置具有鲁棒性。

**核心理念**
“多层级推测解码通过模型内路由出的中间验证器，在保持质量的同时大幅降低大模型调用频率。”
