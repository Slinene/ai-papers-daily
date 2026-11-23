---
title: 'The Dual-Tier Sentiment Framework: Scalable Multimodal UX Attribution in Web
  Search'
title_zh: 双层情感框架：网页搜索可扩展多模态用户体验归因
authors:
- Yi Ding
- Gaurav Kumar
- Rui Min
- Isabella Ye
- Bhavika Goyal
- Emilio Antunez
- Huihui Chen
- Ke Xu
- Xiaowei Sun
- Xin Xu
affiliations:
- Google
arxiv_id: '2611.27899'
url: https://arxiv.org/abs/2611.27899
pdf_url: https://arxiv.org/pdf/2611.27899
published: '2026-11-20'
collected: '2026-11-23'
category: Eval
direction: LLM 驱动的 UX 评估 · 多模态归因
tags:
- UX Attribution
- Multimodal LLM
- LLM Fine-tuning
- A-B Testing
- User Sentiment
- Prompt Optimization
one_liner: 提出双层情感框架，Tier1用微调LLM检测情感回归，Tier2用多模态LLM诊断视觉布局摩擦，将UX评测从周级压缩至小时级
practical_value: '- **分层评估架构可直接迁移到电商推荐**：Tier 1 用轻量微调 LLM 对 telemetry 特征做快速回归检测，Tier
  2 仅在异常时调用多模态 LLM 做细粒度归因。电商/广告落地页、商品卡片布局可用同样思路：先用行为序列、点击/转化、停留时长等特征训练一个小模型监测体验退化，再对可疑实验截图或页面渲染调用
  MLLM 诊断具体视觉问题，避免全量调用大模型。

  - **利用 telemetry 特征微调 LLM 替代人工问卷**：论文在 50 万样本上通过多任务正则化和上下文特征工程获得 +9.8% PR-AUC。推荐系统可以将
  session 行为、滚动深度、点击位置等隐式反馈作为输入，微调一个小 LLM 输出用户 sentiment 或体验评分，用于 A/B 实验中快速检测体验劣化，减少问卷依赖和延迟。

  - **“User Toil”可作为可量化体验指标**：用多模态 LLM 评估结果块视觉渲染与空间布局，量化用户到达满意结果所需努力。在电商详情页、搜索无结果页、活动落地页中，可引入类似指标，自动评估首屏信息遮挡、CTA
  可见性、价格/标题突出程度等，作为 UX 优化目标或护栏。

  - **RL 自动提示优化 + AI judge 可复用**：论文通过 RL 优化提示和 AI judge 判断 win/loss 模式提升 MLLM F1 >6.5%。内部搭建类似评估器时，可用该
  trick 减少人工 prompt 试错，并让 AI 对对照组/实验组进行 win/loss 判定，提高评估一致性和可扩展性。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**  
大型网页搜索的 A/B 实验需要可扩展的 UX 评测，但传统问卷周期长、瓶颈明显，自动化指标又缺乏诊断视觉/空间布局异常的粒度。

**方法关键点**  
框架分两层：Tier 1（Macro System）用基于 Gemini XS 微调的 encoder-decoder LLM 处理 telemetry 特征，通过多任务正则化与上下文特征工程，充当可扩展的用户情感回归检测器；Tier 2（Micro System）用 Gemini 3.0 Pro 多模态 LLM 原生评估结果块的视觉渲染与空间布局，将“User Toil”（达到满意结果所需估计努力）量化，并借助基于 RL 的自动提示优化和 AI judge 判断 win/loss 模式。

**关键结果**  
Tier 1 在 50 万+ 留出样本上 PR-AUC 提升 +9.8%，在 12 个留出实验中匹配基线召回且相对精度增益约 20%，生产环境将测量延迟从周级降至小时级，问卷开销减少 40%+；Tier 2 的 MLLM 在 F1 上提升 >6.5%。系统整体可每日处理 O(100k) 个 live 实验查询。
