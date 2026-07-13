---
title: Test-Time Scaling for Small VLMs on Multilingual Visual MCQ
title_zh: 小型视觉语言模型多语言视觉多选题的测试时缩放研究
authors:
- Spiros Baxevanakis
- Peng-Jian Yang
affiliations:
- University of Amsterdam
arxiv_id: '2607.09438'
url: https://arxiv.org/abs/2607.09438
pdf_url: https://arxiv.org/pdf/2607.09438
published: '2026-07-10'
collected: '2026-07-13'
category: Reasoning
direction: 测试时缩放 · 小型VLM推理
tags:
- test-time scaling
- vision-language models
- multilingual reasoning
- self-consistency
- parseability
- process reward model
one_liner: 揭示可解析性和解码预算才是小VLM测试时缩放的关键，而非复杂搜索或验证
practical_value: '- **提示工程确保输出可解析**：在要求LLM/VLM生成推荐理由、商品标签或搜索 query 时，显式添加答案格式约束（如“最终答案：”），并后置修复漏答的推理链，能大幅提升解析成功率和准确率

  - **优先增加单链 token 预算而非采样数量**：对于资源受限的小模型，把单链最大 token 数从1k提升到2k即可挽回3.7个百分点，而采样数翻倍几乎无益，可在Agent推理链路中调整max_tokens参数以成本更低的方式增强性能

  - **自一致性投票足够可靠**：在决策融合阶段，简单 majority voting 在准确率上往往优于昂贵的PRM引导搜索或训练验证器，适合作为推荐Agent中多路推理结果的低成本聚合方案

  - **模型自身能力是最大杠杆**：升级基础策略模型带来11.4pp提升，远高于任何后处理技巧，因此在实际业务中，优先迭代模型或适配领域数据比过度设计推理策略更高效'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：测试时缩放（TTS）在大型语言模型的推理中有效，但能否迁移到小型开放视觉语言模型（VLM）仍不明确，尤其是在资源受限（单A40 GPU、≤7B参数）的多语言视觉多选题场景。

**方法关键点**：在EXAMS-V多语言基准上，对比了自一致性、描述-推理+PRM引导束搜索、以及两种后验选择器，分别使用Qwen2.5-VL-7B-Instruct和Qwen3.5-4B模型。核心发现是TTS的运行条件而非搜索/验证机制决定效果。最大因素是**可解析性**：早期提示格式下许多推理链正确但未输出答案字母；统一答案提示和引导修复步骤解决了大部分问题。其次，**解码预算**：将每链token上限从1k提高至2k可额外挽回3.7pp，而采样更多链（8→16）仅增加0.15pp。当链有足够空间完成推理后，复杂方法贡献甚微：PRM引导束搜索比简单自一致性低0.39pp且成本超8倍，无论是无训练的生成式验证器还是训练后的多模态PRM，多数投票均优于它们。最大增益来自策略模型本身（+11.4pp）。

**关键结果**：最佳配置在ImageCLEF 2026测试集上达到84.1%准确率，位列Visual MCQ排行榜第一，验证了在不依赖昂贵搜索的前提下，小VLM可通过充分的解码空间和可解析输出取得强劲推理性能。
