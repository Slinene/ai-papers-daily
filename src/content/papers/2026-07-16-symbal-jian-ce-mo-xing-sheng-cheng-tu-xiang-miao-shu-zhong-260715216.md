---
title: 'Symbal: Detecting Systematic Misalignments in Model-Generated Captions'
title_zh: Symbal：检测模型生成图像描述中的系统性错位
authors:
- Maya Varma
- Jean-Benoit Delbrouck
- Sophie Ostmeier
- Akshay Chaudhari
- Curtis Langlotz
affiliations:
- Stanford University
- HOPPR
arxiv_id: '2607.15216'
url: https://arxiv.org/abs/2607.15216
pdf_url: https://arxiv.org/pdf/2607.15216
published: '2026-07-16'
collected: '2026-07-18'
category: Eval
direction: 多模态生成内容审计·系统性错位检测
tags:
- MLLM
- Captioning
- Systematic Misalignment
- Benchmark
- Diagnosis
- Model Auditing
one_liner: 利用现成基础模型双阶段审计 MLLM 生成标题的系统性错误，实现 63.8% 准确率，比基线提升近 4 倍
practical_value: '- 可借鉴双阶段自动审计范式：先利用 CLIP 等现成模型聚类潜在错位模式，再用 LLM 总结为自然语言描述，用于电商商品图文一致性审计或广告文案质量检查，无需重新训练。

  - SymbalBench 的构造思路可复现到电商场景：通过组合视觉特征和人为标注的错误模式，构建特定领域的系统性错误检测基准，加速业务多模态模型验收。

  - 发现特定视觉特征（如黑色皮肤、医疗设备）与固定错误 caption 关联的统计方法，可迁移到推荐场景中检测特定用户群或商品类目的系统性偏差。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

**动机**：多模态大模型（MLLM）生成图像描述时常引入系统性错位，即特定视觉特征（如性别、肤色、医疗设备）与重复性错误描述强关联。现有评估缺乏自动检测此类模式的方法。  
**方法**：提出 SYMBAL，一个双阶段即插即用框架。第一阶段利用现成视觉编码器（如 CLIP）提取图像特征，通过聚类和统计检验识别与错误描述显著相关的视觉模式；第二阶段调用 LLM 将检测到的模式总结为自然语言报告。同时构建 SYMBALBENCH 基准，含 170 万图文对，来自自然和医学图像两大领域，划分为 420 个数据集，每个数据集注入人工定义的系统性错位（如“穿白大褂的人”总被误述为“医生”）。  
**结果**：SYMBAL 在 SYMBALBENCH 上正确识别 63.8% 数据集的系统性错位，较最佳基线（16.9%）提升近 4 倍。真实场景评估中，SYMBAL 成功审计了四个主流 MLLM（BLIP-2, LLaVA 等）生成的标题，并发现现有开源数据集（如 LAION）中的系统性偏差。方法无需访问目标 MLLM 参数，仅依赖其输出。
