---
title: What Gets Unmasked First? Trajectory Analysis of Diffusion Models for Graph-to-Text
  Generation
title_zh: 扩散模型图到文本生成的首个解掩码轨迹分析
authors:
- Qing Wang
- Jacob Devasier
- Chengkai Li
affiliations:
- The University of Texas at Arlington
arxiv_id: '2605.31564'
url: https://arxiv.org/abs/2605.31564
pdf_url: https://arxiv.org/pdf/2605.31564
published: '2026-05-29'
collected: '2026-06-01'
category: LLM
direction: 扩散语言模型 · 图到文本生成 · 解码轨迹控制
tags:
- Masked Diffusion Language Models
- Graph-to-Text
- Trajectory Analysis
- Decoding
- BLEU
- Knowledge Graph
one_liner: 发现掩码扩散语言模型解码时天然优先还原实体，并针对微调破坏策略提出推理时结构词降权修正
practical_value: "- **电商商品描述生成**：若采用扩散模型从商品知识图谱生成卖点文案，可借鉴其“实体优先”的天然解码顺序，显式约束先输出关键属性（品牌、成分），再生成连接词，减少幻觉，确保信息完整。\
  \  \n- **扩散解码控制**：分析扩散语言模型的 token 解掩码轨迹，可发现业务数据中的类似模式（如首先生成关键实体，末尾为标点/助词），并设计针对性推理干预。`λ-scaled\
  \ structural decoding` 提供了一种简单、无需重训的降权方法，可避免过早确定序列长度，防止信息遗漏。  \n- **多模态结构融合**：`Graph-LLaDA`\
  \ 的图编码器+扩散解码框架可作为“结构化数据 → 流畅文本”的通用范式，适用于电商中表格数据、订单信息或商品关系图的自然语言生成，比自回归式更易控制实体顺序和覆盖率。\
  \  \n- **避免微调负效应**：观察到 SFT 会破坏扩散模型的自然解码策略（过早锚定结构 token），提醒在业务中使用扩散生成模型时，微调可能引入脆弱性，可考虑推理时修正或约束解码来恢复原有优势。"
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：图到文本生成需保障实体和关系的准确表达，传统自回归 LLM 从左至右线性生成，难以充分捕捉图结构，易遗漏或幻觉。掩码扩散语言模型（MDLM）通过迭代式解掩码提供了更灵活的生成路径，但其解码轨迹尚不为人知。  
**方法**：首次系统分析 MDLM 在图到文本生成中的解掩码顺序，发现其天然优先还原实体词，之后是关系和功能词，最终才处理结构 token（如标点、句尾）。进一步揭示有监督微调（SFT）会打乱这一策略，过早锚定结构 token，导致输出长度被锁定，引发信息缺失或幻觉。为此提出 λ-scaled structural decoding，一种训练无关的推理时修改，降低结构 token 的置信度权重，使模型回归实体优先的生成顺序。同时构建 Graph-LLaDA，将图 Transformer 编码器直接融入 LLaDA 的解码过程，显式注入关系图信息。  
**结果**：λ-scaled 方法在 BLEU-4 上提升 +9.4 分。跨数据集评测显示，基于 LLM 和 MDLM 的方法泛化显著优于先前为特定数据集设计的基线，后者存在过拟合问题。
