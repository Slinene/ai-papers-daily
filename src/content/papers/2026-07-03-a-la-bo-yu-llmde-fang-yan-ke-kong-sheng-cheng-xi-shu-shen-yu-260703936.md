---
title: Can Dialects Be Steered Like Languages? Sparse Neurons and Distributed Directions
  in Arabic LLMs
title_zh: 阿拉伯语LLM的方言可控生成：稀疏神经元与分布式向量引导
authors:
- Kareem Elozeiri
- Mervat Abassy
- Omar Kallas
- Fahim Dalvi
- Preslav Nakov
- Kentaro Inui
- Nadir Durrani
affiliations:
- Mohamed bin Zayed University of Artificial Intelligence
- Qatar Computing Research Institute, Hamad Bin Khalifa University
- Tohoku University
- RIKEN
arxiv_id: '2607.03936'
url: https://arxiv.org/abs/2607.03936
pdf_url: https://arxiv.org/pdf/2607.03936
published: '2026-07-03'
collected: '2026-07-12'
category: LLM
direction: 推理时干预 · 模型可解释性
tags:
- dialect steering
- sparse neurons
- vector steering
- inference-time control
- Arabic LLMs
- interpretability
one_liner: 通过识别并操控稀疏神经元或注入方言向量，在推理时无微调控制LLM方言输出
practical_value: '- 推理时引导（steering）可零成本切换LLM输出风格，无需微调。在电商客服、商品描述生成中，可注入“亲和力”或“专业度”向量控制语气。

  - 神经元稀疏分析定位领域知识（如品牌、品类），用于可解释性调试与受控生成，辅助发现模型内部的概念神经元。

  - 向量抽取方法（对比样本对计算差异向量）可提取任意属性的激活方向，在推荐文案或Agent交互中实现细粒度属性控制，如情感倾向、正式度。

  - 干预强度可调，提供“风格强度”旋钮，适合在线A/B测试与个性化体验的渐进式优化。'
score: 6
source: huggingface-daily
depth: abstract
---

动机：阿拉伯语LLM因训练数据中方言稀缺，过度生成标准阿拉伯语（MSA），难以满足多样化的方言生成需求。

方法：提出了两种推理时干预策略，兼具可解释性探针功能。1）神经元引导：通过对比方言与MSA的激活差异，定位稀疏的方言编码神经元（前0.5%-1%），在推理时放大或抑制这些神经元，直接修改输出方言倾向。2）向量引导：利用对比样本对（同一语义的方言 vs MSA）抽取方言激活方向，构建“方言向量”，在推理时以可调节强度注入隐藏状态，实现平滑控制。实验使用Jais和AceGPT等阿拉伯语LLM，评估海湾、埃及、黎凡特等方言的生成准确性。

关键结果：两种方法均显著提升目标方言生成比例，神经元引导精确但易产生脆性，向量引导更鲁棒、强度可控。可解释性分析表明方言知识既存在于少数关键神经元中，也分布于更广的激活模式内。该框架无需方言微调，为低资源方言的风格控制提供了普适方案。
