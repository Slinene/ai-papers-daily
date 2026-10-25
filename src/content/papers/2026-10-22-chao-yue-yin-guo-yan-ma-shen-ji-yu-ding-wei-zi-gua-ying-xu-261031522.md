---
title: 'Beyond Causal Masks: Auditing and Localizing Hidden Future-Token Leakage in
  Adaptive Sequence Models'
title_zh: 超越因果掩码：审计与定位自适应序列模型中的隐藏未来token泄漏
authors:
- Huiting Liu
- Jinsong Wu
affiliations:
- School of Artificial Intelligence, Guilin University of Electronic Technology
- Department of Electrical Engineering, University of Chile
arxiv_id: '2610.31522'
url: https://arxiv.org/abs/2610.31522
pdf_url: https://arxiv.org/pdf/2610.31522
published: '2026-10-22'
collected: '2026-10-25'
category: Eval
direction: 自回归模型因果性审计与泄漏定位
tags:
- causal masking
- future-token leakage
- teacher forcing
- model auditing
- prefix invariance
- adaptive routing
one_liner: 揭示自适应路由解码器中全序列summary造成未来token泄漏，提出审计与定位方法并修复验证
practical_value: '- 在电商/推荐场景使用 LLM 或生成式推荐模型时，若架构中包含序列级 pooling、动态路由、summary broadcast、时间卷积等模块，即使
  attention mask 正确，也可能引入未来 token 泄漏。应建立 prefix-invariance 审计流程，加入训练回归测试。

  - 评估生成式推荐或 Agent 策略模型时，不要只看 teacher-forced loss 的下降。必须补充自由运行生成评估（如参考模型 perplexity、生成质量指标），防止隐藏泄漏造成虚假架构收益。

  - 可复用 LeakScore（最大前缀输出差异）作为轻量诊断工具，在每次架构改动或新 checkpoint 上线前检测跨位置信息泄漏；尤其适合 MoE routing、自适应残差连接等动态路径。

  - 工程实现中，动态路由的 query 路径应只使用 prefix-only 统计量，避免广播全序列 summary；对 KV cache 在不同数值精度下的一致性也要纳入检查，防止类似泄漏。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

**动机**
隐藏未来 token 泄漏会制造虚假架构收益：自回归模型在 teacher-forced 评估下损失大幅下降，但自由运行生成质量反而恶化。这类泄漏常源于序列级 pooling、routing 或 summary 等操作，尽管 causal attention mask 本身正确。

**方法关键点**
研究对象是一个自适应残差路由解码器，其序列级路由 summary 让前缀位置暴露给未来 token。诊断工具包括 prefix-invariance 契约、最大前缀输出差异 LeakScore、行为指标与逐层剖析。通过逐层诊断和实现检查，定位到全序列 summary 经动态路由 query 路径广播的缺陷。随后训练两个独立的 12 层因果修复模型，消除可检测泄漏。

**关键结果数字**
异常 24 层 checkpoint 将验证损失从 baseline 的 3.5958 降至 1.4259，但未通过 prefix-invariance 审计，且生成阶段参考模型 perplexity 显著更高；因果修复后验证损失与参考 perplexity 回到对照水平，虚假优势消失。支持实验覆盖 6 个合成实现对、5 个模块族、干净预训练对照、故障注入及跨精度缓存一致性。结论强调：更低的 teacher-forced loss 必须结合全模型因果检查与自由运行评估共同解读。
