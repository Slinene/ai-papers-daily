---
title: 'MINT: A Universal Zero-Shot Predictor for Transaction Data'
title_zh: MINT：交易数据的通用零样本预测器
authors:
- Parameswaran Kamalaruban
- Viktor Drobnyi
- Maeve Madigan
- Julia Rozanova
- David Sutton
- Stuart Burrell
affiliations:
- Visa Inc.
arxiv_id: '2608.14198'
url: https://arxiv.org/abs/2608.14198
pdf_url: https://arxiv.org/pdf/2608.14198
published: '2026-08-14'
collected: '2026-08-17'
category: Multimodal
direction: 多模态交易推理 · 嵌入注入 LLM
tags:
- transaction embeddings
- multimodal LLM
- zero-shot prediction
- instruction tuning
- LoRA
- sequence encoder
one_liner: 用冻结交易序列编码器+LoRA适配LLM，通过嵌入注入实现高效零样本预测问答
practical_value: '- 行为序列嵌入注入代替文本拼接：电商/推荐系统用户行为序列长、token 多，可预训练行为序列编码器生成紧凑嵌入，只训练 connector
  + LoRA，显著降低输入 token、在线延迟与显存，适合实时排序或用户表征注入 LLM 生成解释。

  - 两阶段训练：先模态对齐（行为摘要 caption）再指令微调（QA + CoT 混合），提升 OOD 泛化。业务中构建预测/归因类任务时，可合成行为摘要和推理链，增强模型对未见问题的能力。

  - 按任务类型选择表示：预测性任务用嵌入更好，提取式/事实查询用文本序列更优。推荐系统做可解释推荐或问答时，可根据是预测未来兴趣还是检索历史事实选择输入模态，或采用混合策略。

  - LoRA 适配可插拔：领域特化会损失通用能力，但 PEFT 允许禁用 adapter 恢复 base LLM。部署时保留通用与垂直两套模式，切换成本极低。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

# 动机
交易序列数据是金融行为分析的基石，涉及欺诈检测、信用评估、个性化等任务。传统 Foundation Models 虽能生成交易 embedding，但缺乏灵活的零样本推理接口；直接用文本序列化交易记录给 LLM 则面临 token 成本高、长历史无法扩展、结构化数值/时间信号未被充分利用等问题。MINT 旨在通过多模态嵌入注入结合预训练交易编码器与 LLM，实现高效且可泛化的交易预测问答。

# 方法关键点
- 冻结预训练交易序列编码器（Transformer，采用 autoregressive next-event prediction 预训练），输出每笔交易的上下文 embedding；数值特征 log 变换、类别特征查表，field-level + sequence-level 层次编码。
- 可训练 MLP connector（LayerNorm + GELU + Linear）将交易 embedding 投影到 LLM hidden space；用 <emb> 占位符在 prompt 中注入，避免文本序列化。
- Decoder-only LLM 通过 LoRA（rank 64 等）进行参数高效适配；两阶段训练：先仅在 caption 数据上训练 connector 做模态对齐，再在 caption + QA + CoT 混合数据上联合优化 connector 和 LoRA。
- 使用大规模真实交易数据；QA 分为 extractive（43 个 ID 问题类型，9 个 OOD）和 predictive（26 个 ID 类型，10 个 OOD），并合成 CoT 理由。

# 关键结果
在 predictive QA 上，MINT (h=1) 取得 ID 0.830 / OOD 0.805，显著优于文本序列化 LLM SFT（h=1 0.794/0.704，h=5 0.811/0.750），且仅用一个交易 embedding。在 extractive QA 上，文本序列化在 ID 上略优（0.893 vs 0.861），但 MINT 在 OOD 上反超（0.621 vs 0.605）。推理效率方面，MINT (h=5) 比 LLM SFT (h=1) TTFT 低 18%、decode throughput 提升 2.4×、峰值 VRAM 降低 11%、输入 token 减少 26%。消融显示：CoT 监督普遍提升性能；OOD 最优配置为 LoRA rank 32、connector hidden 512；历史长度增大只对 extractive QA 单调提升，对 predictive QA 不敏感甚至有害；倒数第二层 embedding 有利 ID，最后一层有利 OOD。

# 最值得记住的一句话
紧凑的交易嵌入比文本序列化更适合预测性推理，并且大幅降低推理开销；冻结行为序列编码器 + LoRA + 指令微调是高效多模态推理的实用范式。
