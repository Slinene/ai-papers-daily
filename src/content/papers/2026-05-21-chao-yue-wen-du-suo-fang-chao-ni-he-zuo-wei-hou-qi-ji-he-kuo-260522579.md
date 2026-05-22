---
title: 'Beyond Temperature: Hyperfitting as a Late-Stage Geometric Expansion'
title_zh: 超越温度缩放：超拟合作为后期几何扩展
authors:
- Meimingwei Li
- Yuanhao Ding
- Esteban Garces Arias
- Christian Heumann
affiliations:
- Department of Statistics, LMU Munich
- School of Computer and Information Engineering, Henan University
- Munich Center for Machine Learning (MCML)
arxiv_id: '2605.22579'
url: https://arxiv.org/abs/2605.22579
pdf_url: https://arxiv.org/pdf/2605.22579
published: '2026-05-21'
collected: '2026-05-22'
category: Training
direction: LLM 微调 · 生成多样性 · 机制分析
tags:
- Hyperfitting
- Rank Reordering
- Late-Stage LoRA
- Token Diversity
- Greedy Decoding
- Mechanistic Interpretability
one_liner: 揭示超拟合通过动态排序重排而非分布锐化提升生成多样性，并仅微调最后 5 层即可复现该效果
practical_value: '- **终端层高效微调**：Late-Stage LoRA 仅更新最后 5 层就能复现完整超拟合带来的多样性提升，在 1.5B-2B
  模型上减少约 78-83% 训练参数，大幅节省 GPU 小时，可快速迁移到电商对话或商品文案生成。

  - **过拟合亦可有益**：在极小数据集（2000 条）上训练到近零损失，反而增强了贪婪解码的词汇多样性与连贯性，这提示我们在数据稀缺场景（如特定品类描述）可主动推进过度拟合以打破重复模式，而非提前停止。

  - **确定性解码的多样性诊断**：通过跟踪 token 的来源排名分布（Top-1 一致率、深层尾 token 提升比例）和最终层有效维度变化（∆Dim ≈
  +80），可量化模型是否学到真正的“排序重排”，避免仅依赖困惑度等指标误导，可用于监控推荐文案生成质量。

  - **上下文感知的多样性提升**：静态偏置注入实验表明，超拟合不是全局词汇偏置，而是动态、语境相关的排序改变。这暗示在电商推荐中，若想生成多样化的商品描述，应避免简单规则（如禁止重复
  n-gram），而应通过微调让模型在不同上下文中自主决定何时使用高频词或长尾词。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**  
语言模型在贪婪解码时普遍陷入重复循环，近期发现“超拟合”（在极小数据集上训练到近零损失）反而能显著提升词汇多样性（TTR）并降低重复率，但其机制未明。一个直接假设是它等价于降低解码温度（分布锐化），但若如此则不能解释为什么相同熵水平下多样性仍大幅领先。本文旨在 1) 证伪温度缩放假设，2) 揭示真正的机制——排序重排与几何扩展，3) 利用发现提出更高效的微调策略。

**方法关键点**  
- **严格对照实验**：熵匹配实验——找到温度 T≈0.59 使原模型输出熵与超拟合模型相同，对比 TTR、重复率。  
- **排序分析**：跟踪超拟合模型每次 greedy decode 的 Top‑1 token 在原模型中的原始排名，观察来自深层尾巴（Rank>10）的比例。  
- **静态偏置消融**：抽取超拟合模型中提升最大的 500 个 token 的平均 logit 偏移，注入原模型，验证是否为全局偏置。  
- **层间机制定位**：逐层计算余弦相似度、L2 距离、参与比率（有效维度），定位“终端扩展”现象。  
- **Late-Stage LoRA**：基于发现仅将 LoRA adapter 加在最后 5 层，冻结其余部分，复现超拟合效果。

**关键实验与结果**  
- 在 TinyLlama-1.1B 上，超拟合后 TTR 从 0.40 升至 0.68，而熵匹配的温度缩放模型 TTR 仅 0.40，且 bigram 重复率 0.60（超拟合仅 0.14），证明非简单锐化。  
- 超拟合后 39.1% 的生成 token 来自原排序非 Top‑1，其中 12.9% 来自 Rank>10 的深层尾 token，温度缩放无法做到。  
- 静态偏置注入在任意 α 下均恶化重复和多样性，说明排序重排是动态、上下文依赖的。  
- 层间分析发现最终 transformer 块（Layer 22）L2 距离由 21 层的 22.0 跳升至 81.6，有效维度扩张 ∆Dim≈+80.8，前期层几乎不变。  
- Late-Stage LoRA 在 TinyLlama 上 Top‑1 一致率 0.517（Full LoRA 0.523），bigram 重复率 0.345；在更深的 Qwen2.5-1.5B 上甚至超越 Full LoRA（TTR 0.591 vs 0.575，重复率 0.213 vs 0.248），且 LLM-as-Judge 评估显示连贯性提升 16.1 个百分点。  

**值得记住的一句话**  
超拟合并非简单增加信心，而是通过最终层约 +80 维的几何扩展，动态地将深层尾候选 token 提升到 Top‑1，仅需微调最后 5 层就能以极低成本复现这一效应。
