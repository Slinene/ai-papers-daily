---
title: 'SynthDocBench: Controlled Benchmark for Long-Context Visual Document Understanding'
title_zh: SynthDocBench：长上下文视觉文档理解的受控基准
authors:
- Abhigya Verma
- Khyati Mahajan
- Amit Kumar Saha
- Shruthan Radhakrishna
- Sagar Davasam
- Vikas Yadav
- Sai Rajeswar Mudumba
affiliations:
- ServiceNow AI
- Mila
- Université de Montréal
arxiv_id: '2607.10400'
url: https://arxiv.org/abs/2607.10400
pdf_url: https://arxiv.org/pdf/2607.10400
published: '2026-07-10'
collected: '2026-07-16'
category: Eval
direction: 基准评估 · 长文档多模态理解
tags:
- Benchmark
- Synthetic Data
- Long-Context
- VLM
- Failure Analysis
- Visual Document Understanding
one_liner: 通过合成数据系统控制文档长度、布局、模态和问题类型，揭示VLMs在长文档上的三种失败模式
practical_value: '- **合成数据生成范式的复用**：用LLM管线生成可控变量（长度、布局、模态、问题类型）的文档，可迁移到电商商品详情页、广告落地页等多模态内容的理解评估，系统诊断模型弱点。

  - **位置敏感性发现**：中部段落准确率最低（5/6模型“Early→Late”负向趋势，最大降8.3个百分点），提示在构建RAG系统的检索上下文时，避免简单按序拼接长文档，应将关键信息前移或采用分段注意力增强机制。

  - **图表理解在长文档中崩坏**：长文档内嵌图表的理解错误高，对广告/推荐中常含图表的多模态素材，需单独提取图表区域进行专项编码，或限制上下文长度以避免干扰。

  - **防伪相关的随机覆写机制**：生成时用40%随机覆写防止模型利用虚假关联，在实际业务构建评测集时，可引入类似随机占位符或噪声注入，避免模型走捷径，提升评测稳健性。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有VLM基准（DocVQA、ChartQA等）混淆了文档长度、布局、模态和问题难度等多个变量，无法诊断具体失败原因。需要可控的实验环境剥离各因素的影响。

**方法**：构建完全合成的基准SynthDocBench，通过LLM管线生成六种布局原型的文档，采用组合设计独立改变文档长度、布局结构、模态组成（文本、表格、图表）和问题类型。引入40%随机覆写避免模型学习伪相关。最终文档长度和结构多样性远超现有基准。

**关键结果**：在7个前沿VLM上发现三个隐蔽失败模式：
- 随文档长度增加，性能急剧下降；
- 位置敏感性强，文档中间1/3部分准确率最低（5/6模型），Early→Late趋势负向，最陡降幅达8.3个百分点；
- 长文档中的图表理解能力崩溃。表明当前模型可能过拟合基准而非真正长上下文理解。
