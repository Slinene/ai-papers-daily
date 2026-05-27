---
title: 'L2Rec: Towards Dual-View Understanding of LLMs for Personalized Recommendation'
title_zh: L2Rec：面向个性化推荐的 LLM 双视图理解
authors:
- Pingjun Pan
- Tingting Zhou
- Peiyao Lu
- Tingting Fei
- Hongxiang Chen
- Chuanjiang Luo
affiliations:
- Netease Cloud Music
arxiv_id: '2605.26717'
url: https://arxiv.org/abs/2605.26717
pdf_url: https://arxiv.org/pdf/2605.26717
published: '2026-05-26'
collected: '2026-05-27'
category: RecSys
direction: LLM 推荐 · 参数级双视图融合
tags:
- LLM-based Recommendation
- Parameter-Level Adaptation
- Dual-View
- Personalized MoE
- LoRA
- Contrastive Learning
one_liner: 通过在参数层面为 LLM 注入行为与语义双视图 LoRA 专家，以个性化路由统一融合信号，显著提升推荐效果。
practical_value: '- **参数级融合思路**：将行为序列与文本语义在参数空间而非表示空间对齐，冻结 LLM 主干，仅更新视图特定的 LoRA 专家，避免了表示空间的分布不匹配。电商推荐中可借鉴，例如用户点击序列（行为）与商品标题/描述（语义）使用同样方法融合，降低多模态对齐难度。

  - **DPMoE 个性化路由**：共享专家捕获跨视图共性，视图特定专家由三信号路由（上下文、用户向量、上下文-用户交互）选择。这种“用户感知的专家激活”可迁移到多任务推荐或
  Agent 多模态输入——如协同商品浏览、对话意图等多视图，只需调整路由输入。

  - **轻量高效部署**：仅训练 5% 参数（~32M），主干冻结。线上 A/B 点击率提升 9.24%，证明参数级适配的工业可行性。可显式用于电商召回侧，作为上游表征模块，与下游匹配/排序无缝衔接。

  - **训练稳定技巧**：引入双向偏好对比损失（BPC）保持双视图表征一致性，以及负载均衡损失防止 MoE 路由坍塌。这些技巧在训练多视图 MoE 时可直接复用，尤其当多个视图共享专家时，避免特定专家被忽略。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：将 LLM 用于推荐时，如何融合行为信号（点击序列）和语义信号（商品文本）是关键。现有方法或先提取语义嵌入再塞给下游模型（输出级），或把 ID 嵌入注入 LLM 输入空间（输入级），均在表示层面融合，面临分布不匹配和优化冲突。该文指出更优的融合点在参数空间——同一套 Transformer 参数通过视图特定的低秩扰动即可承载两种信号，从而共享表示邻域，降低对齐难度。

**方法关键点**：
- **双视图输入构建**：语义视图将商品文本序列化保留 token 粒度；行为视图将商品嵌入池化后投影为序列，聚焦 item 级交互模式。
- **DPMoE 机制**：为 LLM 的每个 Transformer 块配备两组 LoRA 专家池——语义专家和行为专家，外加一组共享专家。视图特定的专家选择由个性化路由控制：输入上下文、用户表征和两者的交互三个信号经门控网络组合后 Top-N 稀疏激活。调整量的计算公式为 ΔW = Σ_{共享} BA + Σ_{视图特定} g·BA。
- **训练与推理**：双视图输出经残差投影和动态门控融合 (ACF)，用对比损失做召回训练，附加双向偏好对比损失 (BPC) 对齐双视图表征，以及负载均衡损失。仅微调 DPMoE 和 ACF，LLM 主干冻结。

**关键结果**：在 Amazon 三个域和千万级工业数据集上，L2Rec 对比 SASRec、BERT4Rec、LLaRA、LEARN 等 7 个基线，NDCG@10 相对提升 3.87%–8.02%。数据稀疏时优势更明显（10% 训练数据即超 LEARN 全量）。线上 A/B 测试（150 万 DAU 社交平台）点击率 +9.24%，回复率 +3.15%，统计显著。

**值得记住的一句话**：*“在参数空间进行双视图自适应，让 LLM 对同一用户产生互补的行为与语义适应，是跳出表示空间对齐困境的有效路径。”*
