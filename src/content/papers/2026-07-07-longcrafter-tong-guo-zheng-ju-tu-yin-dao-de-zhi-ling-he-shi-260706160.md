---
title: 'LongCrafter: Towards Diverse Long-Context Understanding via Evidence-Graph-Guided
  Instruction Synthesis'
title_zh: LongCrafter：通过证据图引导的指令合成实现多样化长上下文理解
authors:
- Chenhao Yuan
- Yinhao Xu
- Shuwen Xu
- Xizhi Yang
- Jiaxiang Liu
- Chenxi Zhou
- Shaoping Huang
- Haolin Ren
- Pengfei Cao
- Jun Zhao
affiliations:
- University of Chinese Academy of Sciences
- Institute of Automation, Chinese Academy of Sciences
arxiv_id: '2607.06160'
url: https://arxiv.org/abs/2607.06160
pdf_url: https://arxiv.org/pdf/2607.06160
published: '2026-07-07'
collected: '2026-07-08'
category: Training
direction: 长上下文指令合成 · 训练数据增强
tags:
- Long-Context Understanding
- Instruction Synthesis
- Evidence Graph
- Fine-Tuning
- Lost in the Middle
one_liner: 提出证据图引导的长上下文指令合成框架，覆盖32种任务，训练数据显著提升长文本理解并缓解迷失中间问题
practical_value: '- 分层任务分类（局部/浅层 vs. 全局/深层）可指导电商场景中长文本训练数据的构造，例如用户长评论总结或长商品描述理解任务。

  - 证据图建模跨段落依赖并严格基于证据生成问答对，能保证指令的忠实度，可借鉴到可信长上下文数据合成，如从多段商品介绍中生成属性问答。

  - 合成数据覆盖不同难度且证据位置多样化，能有效缓解模型在长序列中的“迷失中间”问题，适合训练需要从长用户行为序列中精确定位的推荐模型。

  - 证据跨度定位提升了模型的可解释性和鲁棒性，可用于构建需要从长文档中提取关键信息的Agent系统。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：现有长上下文指令合成方法存在任务覆盖窄、难度不足、缺乏忠实性监督三大问题。

**方法**：LongCrafter 提出结构化合成框架，首先构建层次化任务分类体系，将长上下文理解分为局部/浅层和全局/深层，产出32种细粒度任务类型作为生成先验。然后，针对每个任务生成对齐的长上下文，并将其分解为显式证据图，建模跨段落依赖关系。基于证据图，在具体证据跨度上严格生成指令-响应对，确保难度可控且推理可追溯。

**关键结果**：在 LongBench、LongBench v2 和 LooGLE 上，基于 LongCrafter 数据微调的 Qwen2.5-7B 和 LLaMA-3.1-8B 模型超越所有 SFT 基线，甚至优于官方后训练模型，尤其在困难任务上提升最大。数据多样性分析表明其难度分布更均衡，模型在任何位置都能稳健定位证据，有效缓解“迷失在中间”现象。
