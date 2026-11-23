---
title: 'Structurally Different, Functionally Persistent: Capability Regions Under
  Model Optimization'
title_zh: 结构异变，功能持久：模型优化下的能力区域
authors:
- Jiwoo Kum
- Chanwoo Kim
- Doyun Kim
- Seonghyeon Cho
- Sihyeon Lee
- Chanjun Park
affiliations:
- Soongsil University
arxiv_id: '2611.27445'
url: https://arxiv.org/abs/2611.27445
pdf_url: https://arxiv.org/pdf/2611.27445
published: '2026-11-20'
collected: '2026-11-23'
category: LLM
direction: LLM 能力区域功能持久性
tags:
- capability regions
- model optimization
- interpretability
- LoRA
- quantization
- pruning
one_liner: 发现 LLM 能力区域在量化、剪枝、LoRA 后参数重组，但原始区域消融仍有效，功能持久
practical_value: '- 在 LoRA 微调、量化或剪枝后，之前定位的特定能力区域（如商品文案生成、推荐解释）仍可作为干预目标，无需重新定位即可进行能力删除、抑制或增强。

  - 分区分析表明新旧区域的重叠子集贡献了大部分消融效应，提示部署时关注重叠参数即可实现精准能力干预，减少计算开销。

  - 对电商/Agent 场景中的模型维护：即使模型更新导致参数实现大幅变化，基于旧区域的功能开关（ablation/gating）依然有效，有利于安全上线和快速回滚。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：LLM 能力被证明定位于局部参数区域，可支持定向编辑和干预，但尚不清楚优化前识别出的区域在模型经过量化、剪枝或 LoRA 适配后是否仍能作为有效干预目标。

**方法**：在三个指令微调模型上，评估编码能力区域在量化、剪枝、LoRA 适配三种优化前后的功能持久性与参数重叠。分别消融优化前提取的原始区域和优化后重新提取的区域，并与 magnitude 匹配的对照区域对比；进一步通过分区分析，区分原始区域与重提取区域共享子集和独有子集的消融贡献。

**结果**：尽管重新提取的区域在参数位置上发生了实质性重组，但在几乎所有条件下，消融优化前的原始区域仍然消除或几乎消除编码性能，而对照区域保持性能。分区分析显示，在大多数条件下，原始区域与重提取区域的共享子集贡献了大部分消融效应。结论：参数重叠与功能持久性是两个不同的维度，能力区域可以在参数实现发生显著变化时仍保持因果有效性，可作为稳定的干预目标。
