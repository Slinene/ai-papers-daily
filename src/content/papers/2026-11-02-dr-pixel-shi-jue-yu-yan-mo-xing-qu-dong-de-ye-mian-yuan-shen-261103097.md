---
title: 'DR Pixel: Page-Native Deep Research with Vision-Language Models'
title_zh: DR Pixel：视觉语言模型驱动的页面原生深度研究智能体
authors:
- Tiansheng Hu
- Yichuan Wang
- James V. Talwar
- Nicholas Tomlin
- Chen Zhao
- Sewon Min
affiliations:
- NYU Shanghai
- University of California, Berkeley
- Rational Dynamics
- Toyota Technological Institute at Chicago
- New York University
arxiv_id: '2611.03097'
url: https://arxiv.org/abs/2611.03097
pdf_url: https://arxiv.org/pdf/2611.03097
published: '2026-11-02'
collected: '2026-11-03'
category: Agent
direction: 页面原生视觉深度研究智能体
tags:
- Deep Research
- Vision-Language Models
- Page-Native Retrieval
- Counterfactual Credit Reweighting
- Agent Training
one_liner: 首个开源端到端多模态深度研究代理，直接检索渲染页面图像并引入反事实信用重加权训练，超越 OCR 基线
practical_value: '- 对商品详情页、广告落地页等富视觉文档，可直接用页面截图作为检索与推理单元，替代 OCR 文本化，保留表格、价格、图片、规格等结构化信号，适合多模态
  LLM 在电商搜索/推荐中做页面级召回与问答。

  - 在 agentic 搜索/推荐流程中，减少中间 OCR 和文本转换步骤，可显著降低工具调用次数与延迟；页面原生检索对含促销规则、对比表、图表的复杂页面更鲁棒，可用于营销活动页理解和智能导购。

  - 训练 Agent 轨迹时，teacher trajectory 噪声大；可借鉴 counterfactual credit reweighting，按每个步骤对最终转化的反事实贡献做加权，提升
  SFT 数据质量，而非简单过滤失败轨迹。

  - 构建评测时，面向文档中混合文本、表格、图像、公式等多模态证据设计问题，比纯文本问答更能反映真实业务中商品详情、广告素材、规则文档的理解能力。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

动机：传统深度研究将科学论文等复杂文档降级为 OCR 提取文本，丢失表格、图、公式等结构信息；页面原生方式直接用 VLM 在渲染页面图像上检索与推理。

方法关键点：DR Pixel 是首个开源端到端多模态深度研究代理，以渲染页面图像为唯一检索与推理单元，覆盖 1.06M 页面；并构建 DRPixelBench 基准，要求对文本、图、表、公式综合推理。训练阶段，针对 agentic SFT 中 teacher trajectory 噪声问题，提出 counterfactual credit reweighting，按每一步对最终答案的反事实贡献加权推理与动作步骤。

关键结果：零训练页面原生 DR 在 GPT-5.4、Gemini-3.5-Flash、Qwen3.6-27B 上均优于 OCR 基线，且工具调用更少；加入训练后 retrieval recall 提升约 15 点，final accuracy 提升超 10 点，并在四个既有基准上优于未训练基线；在 OOD ViDoRe-V3 上比直接拿到黄金页的 oracle 仅差 1.8 点。结论：OCR-then-retrieve 管道不仅不必要，而且次优。
