---
title: 'MiniVer-V: Identifying Minimal Sufficient Evidence for Short Video Verification'
title_zh: 短视频事实核查中最小充分证据的识别基准与框架
authors:
- Leran Chen
- Lingnan Kong
- Zile Cai
affiliations:
- The University of Sydney
arxiv_id: '2610.11233'
url: https://arxiv.org/abs/2610.11233
pdf_url: https://arxiv.org/pdf/2610.11233
published: '2026-10-08'
collected: '2026-10-11'
category: Reasoning
direction: 多模态事实核查 · 证据充分性选择
tags:
- short video verification
- evidential sufficiency
- multimodal evidence
- fact-checking
- abstention
- LLM verifier
one_liner: 提出基于证据充分性的短视频核查方法，用16%证据达到与全量证据相当的准确率，并显式输出“证据不足”
practical_value: '- **充分性驱动的增量证据检索**：在 RAG 或 Agent 系统中，不必一次性加载全量文档，可借鉴其贪心搜索：每次选择最可能提升信心的证据，直到达到充分性阈值即停止，可显著降低
  token 成本和上下文噪声，尤其适合实时性要求高的搜索推荐场景。

  - **显式弃权机制**：当证据候选池耗尽仍达不到充分性时输出“insufficient”，避免模型硬给结论。推荐系统可对低置信度的生成结果（如商品推荐理由、广告文案）增加弃权分支，触发补充数据或转人工，减少幻觉风险。

  - **两层验证架构分离内部一致性与外部事实性**：先验证视频/商品页面内部信息一致性，再用外部知识做事实判定，能提升生成内容的可信度。例如电商直播间商品描述核验：先比对主播口播与商品详情页，再检索外部标准或百科验证功效。

  - **多模态证据选择思路**：将视觉帧、语音转录、外部网页统一作为证据单元，按充分性而非相关性选择，对多模态搜索或直播内容审核有直接参考价值。'
score: 6
source: arxiv-cs.MM
depth: abstract
---

**动机**
短视频已成为虚假信息传播的主要载体，但自动化事实核查需要确定哪些证据足够支撑结论。现有方法要么把全部证据丢给验证器，引入噪声；要么按主题相关性选证据，混淆了“相关”与“充分”。核心问题：如何找到最小但充分的证据子集。

**方法关键点**
构建 MiniVer-V 基准：195 个短视频，三路标签（supported / refuted / insufficient），5,510 个多模态证据单元（关键帧、语音转录、外部检索源）。提出两层验证框架：第一层评估 claim 与视频内容的一致性（基于内部证据）；第二层做事实判定，需要额外外部佐证。证据选择上，采用充分性驱动的贪心搜索：逐个加入证据直到满足充分性阈值；若候选池耗尽仍不满足则输出“insufficient”，不强制作出裁决。

**关键结果数字**
使用 Claude Sonnet 4 作为验证器时，平均仅用 4.5 个证据单元（全量证据的 16%）即达到 Macro-F1 0.510，与全量证据基线（0.518，27.7 个单元）统计上无差异，同时显著提升对“证据不足”类别的识别。效率优势在 GPT-5.5 上复现，但在开源 Qwen2.5-72B 上仅部分成立。消融显示外部证据对事实判定不可或缺，内部视频证据则用于 grounding claim-video 一致性。
