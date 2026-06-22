---
title: 'LegalHalluLens: Typed Hallucination Auditing and Calibrated Multi-Agent Debate
  for Trustworthy Legal AI'
title_zh: LegalHalluLens：面向可信法律 AI 的幻觉类型审计与校准多智能体辩论
authors:
- Lalit Yadav
- Akshaj Gurugubelli
affiliations:
- Independent Researcher
arxiv_id: '2606.18021'
url: https://arxiv.org/abs/2606.18021
pdf_url: https://arxiv.org/pdf/2606.18021
published: '2026-06-15'
collected: '2026-06-22'
category: MultiAgent
direction: 多智能体辩论校准与幻觉类型审计
tags:
- hallucination auditing
- multi-agent debate
- legal AI
- risk direction index
- typed claims
- calibration
one_liner: 按法律声明类型审计幻觉并引入风险方向指数，通过诊断校准多智能体辩论，减少45%捏造检测
practical_value: '- **幻觉类型化审计可迁移至电商文案/搜索答案**：将生成内容按数值（价格、折扣）、时间（活动期限）、义务/权利（优惠规则）、事实（商品属性）分类评估，能暴露聚合准确率隐藏的高风险区域，指导针对性优化。

  - **风险方向指数（RDI）用于权衡漏报与误报成本**：在推荐/搜索Agent输出中，区分遗漏（该推荐的没推荐）和捏造（虚构信息），根据业务成本选择模型或设置决策阈值，比如高客单价场景拒绝捏造优先。

  - **诊断结果驱动多智能体辩论校准**：使用类似 Skeptic 代理针对已知失败模式进行挑战（如专门检查数字一致性），配合非对称门控，可部署为生成式推荐的审核流，比通用辩论更高效，且允许使用较小模型（4B）达到商业API效果。

  - **面向Agent设计的可审计性**：借鉴框架中对Agent输出进行方向感知的审计，可构建用于电商Agent的合规监控模块，及时发现并修正方向性偏差，提升系统可信度。'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
法律 AI 幻觉率普遍接近 52%，但整体指标掩盖了错误在哪些类型声明上集中（数值、时间、义务/权利、事实）以及方向（遗漏 vs. 捏造），导致无法为可信部署提供可行信号。

### 方法
提出 **LegalHalluLens** 框架，分三步：
1. **类型化幻觉剖析**：在 CUAD 合同数据集上将模型输出按四类法律声明（数值、时间、义务/权利、事实）分类，测量各类别准确性。
2. **风险方向指数（RDI）**：将遗漏（欠置信）与捏造（过置信）偏差压缩为单一标量，使相同整体幻觉率的系统暴露出相反的方向风险。
3. **校准多智能体辩论管道**：基于诊断结果，配置 **Skeptic** 代理针对实测失败模式发起挑战，并设置非对称门控，以控制特定类型和方向的错误。

### 关键结果
- 在 510 份合同、249,252 条款实例上，发现义务/数值类与时间类之间存在 **38–40pp 的准确率差距**，聚合指标完全隐藏此差异。
- 两个幻觉率均为 52% 的系统可呈现 **相反的 RDI**，表明方向风险截然不同。
- 校准辩论管线将 **捏造检测减少 45%**，各类别收益与诊断一致，且仅用 4B 参数模型即匹配商业 API 性能。
- 类型化诊断与 RDI 不仅揭示隐藏的失败模式，还能有效校准多智能体审核管线，实现方向感知的可信部署。
