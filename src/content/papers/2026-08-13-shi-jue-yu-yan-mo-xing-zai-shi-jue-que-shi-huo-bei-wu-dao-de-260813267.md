---
title: How Do VLMs Behave When Blind or Misled? Behavioral Evaluation of VLMs on Scientific
  Figures
title_zh: 视觉语言模型在视觉缺失或被误导时的行为评估：科学图表基准
authors:
- Paul Osemudiame Oamen
- Owusu-Banahene Osei
- Ananya Mukherjee
- Christian Greisinger
- Steffen Eger
- Pius Onobhayedo
- Wei Zhao
affiliations:
- University of Aberdeen, UK
- International Institute of Information Technology Hyderabad, India
- University of Technology Nuremberg, Germany
- University of Southern California, USA
arxiv_id: '2608.13267'
url: https://arxiv.org/abs/2608.13267
pdf_url: https://arxiv.org/pdf/2608.13267
published: '2026-08-13'
collected: '2026-08-16'
category: Eval
direction: VLM 不确定性行为评估与基准
tags:
- VLM
- Benchmark
- Hallucination
- Uncertainty
- Scientific Figures
- Behavioral Reliability
one_liner: 提出 SciFigBench 与 A-R-I 框架，系统评估 VLM 在科学图表上的不确定性行为，揭示高精度不等于高可靠性
practical_value: '- A-R-I 框架可改造成多模态商品理解质检：当商品图模糊、文字遮挡时，模型是否应承认“看不清”而不是编造卖点；可设置 blur/裁剪变换
  + 强制确认 unreadable 区域，评估模型在低质量图片上的拒答率。

  - resistance probes / caption-bias probes 可借鉴为“图-文不一致”检测：商品主图与标题/卖点描述冲突时，模型是否会被营销文案带偏？可构造对抗样本测试多模态推荐/审核模型的抗误导能力。

  - 将“高感知精度≠行为可靠”的结论用于模型选型：在商品图 OCR、广告素材审核等场景，除了 accuracy，还要看 hallucination rate 和
  uncertainty admission，类似 Gemini 3.1 Pro 在阻力分数上表现更强，可能更适合需要安全拒绝的业务。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：现有 VLM 基准侧重感知与推理准确率，忽略模型在视觉证据缺失或误导下的行为可靠性，而科学图表场景对不确定性处理要求高。

**方法关键点**：构建 SciFigBench，包含 250 张科学图表，人工标注三个方面；通过图像变换、推理问题、resistance probes、caption-bias probes、confirmed selective-blur targets 扩展至 34,000+ 评估设置；提出 A-R-I 框架，评估模型是否承认证据不足（Admittance）、抵抗误导上下文（Resistance）、从部分信息谨慎推断（Inductance）。

**关键结果**：GPT-5.2 描述质量最高（MQM 91.6）且推理准确率 78.4%，但在不可读内容上幻觉率 96%；Gemini 3.1 Pro 性能接近（MQM 90.2, 推理 81.0%），但承认不确定性 71%，阻力分数 0.91 最强。结论：高感知/推理精度不保证行为可靠性。
