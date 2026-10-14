---
title: From a Large-Scale Teacher to Efficient Multimodal Students for Search Relevance
  Prediction
title_zh: 从大规模教师到高效多模态学生：搜索相关性预测蒸馏
authors:
- Tomasz Gniazdowski
- Mohammadreza Momenifar
- Nadia Vase
- Shahram Khadivi
- Wiktor Walentynowicz
- Nicola Ueffing
- Jan Pawlowski
- Piotr Szymanski
- Abraham Bagherjeiran
affiliations:
- eBay
- Tooploox
arxiv_id: '2610.16569'
url: https://arxiv.org/abs/2610.16569
pdf_url: https://arxiv.org/pdf/2610.16569
published: '2026-10-12'
collected: '2026-10-14'
category: RecSys
direction: 搜索相关性预测 · LLM蒸馏多模态学生
tags:
- LLM-as-a-Judge
- Knowledge Distillation
- Multimodal LLM
- Relevance Prediction
- E-commerce Search
- FP8
one_liner: 用GPT-4.1当裁判生成48万条相关性标签，蒸馏到Gemma-3多模态小模型，精度接近教师、吞吐大幅提升
practical_value: '- 用高能力闭源LLM作为标注器（LLM-as-a-Judge）批量生成query-item相关性标签（含解释），再用这些数据SFT小模型。如果业务有大量未标注query-item对，可以先小规模人工标注校准prompt，再放大生成训练集，成本远低于人工标注。

  - 蒸馏时保留“先给标签再给解释”的respond-then-explain格式，并让生成解释参与训练，能显著提升小模型在难样本/边缘类上的F1（Test1 F1从68.32提升到76.19）；业务落地可以只输出标签、按需输出解释，推理成本分离。

  - 多模态学生模型用更低分辨率图像（300px）训练即可接近高分辨率，但提升到900px在难样本上有1-2点收益且不影响Gemma-3推理延迟（内部统一256视觉token）。电商场景商品图往往很大，不必过度压缩。

  - FP8量化在单卡H100上无解释吞吐从194 req/s提升到271 req/s（+39%），精度几乎不降，适合高吞吐在线相关性服务；选型上12B模型在精度/吞吐Pareto前沿优于27B。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：电商搜索相关性标注传统依赖人工，贵且慢；LLM-as-a-judge准确但推理成本高、吞吐低。需要把LLM的标注能力压缩成可线上部署的高效模型。

**方法关键点**：
- 先构建小规模三标注人工数据集Test1（239样本）和单标注Test2（233样本），用于校准教师prompt和最终评估。
- 设计结构化prompt，包含任务指令、四档相关性定义、边界规则、few-shot示例，经迭代优化后GPT-4.1在Test1达到83.7%准确率。
- 用该教师对48万条query-item对生成标签+解释，balance类别和类目，得到训练集。
- 学生采用Gemma-3系列多模态模型（4B/12B/27B），SFT时冻结视觉编码器，使用轻量prompt，训练时同时拟合标签和解释。
- 超参搜索：bs 512-2048、lr 2e-5、epochs 2、weight decay 0.1、warmup 0.1。
- 部署时只生成标签可大幅提速；FP8量化进一步提升吞吐。

**关键结果**：
- 12B学生Test1 acc 81.59 vs 教师83.68；Test2 acc 65.24 vs 教师64.38，已经超过教师。
- FP8 12B无解释吞吐271 req/s，FP16为194 req/s；有解释55.98 req/s。
- 消融：训练数据从5.2万增至48万，Test1 F1提升明显（12B从64.20到76.96）；训练包含解释使Test1 F1提升约5-8个点；图像分辨率900px比300px在Test1 acc提升1.67点（12B）。
- 20次运行稳定性标准差约0.2%，模型输出稳定。

最值得记住：用高水准LLM生成带解释的大规模标签，再蒸馏到多模态小模型，可以在接近教师精度的同时获得数量级吞吐/成本优势，是搜索相关性等标注密集型任务落地的可复制路径。
