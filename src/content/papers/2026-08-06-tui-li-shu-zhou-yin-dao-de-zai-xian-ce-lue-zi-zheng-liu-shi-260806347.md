---
title: 'RP-OPSD: Reasoning-Pivot-Guided On-Policy Self-Distillation for Multilingual
  Reasoning Transfer'
title_zh: 推理枢轴引导的在线策略自蒸馏实现多语言推理迁移
authors:
- Xinye Wang
- Junxiao Liu
- Shujian Huang
affiliations:
- National Key Laboratory for Novel Software Technology, Nanjing University
arxiv_id: '2608.06347'
url: https://arxiv.org/abs/2608.06347
pdf_url: https://arxiv.org/pdf/2608.06347
published: '2026-08-06'
collected: '2026-08-07'
category: Training
direction: 训练策略 · 推理枢轴引导
tags:
- Multilingual Reasoning
- On-Policy Self-Distillation
- Reasoning Pivot
- Knowledge Distillation
- Cross-lingual Transfer
- Token-Level Gating
one_liner: 通过对比有无英文参考解答的教师分布，定位推理枢轴并引导特权蒸馏，提升多语言数学推理能力
practical_value: '- **关键 token 定位**：在序列生成任务（如推荐理由、搜索 query 改写、商品摘要）中，可利用两个视图（有无特权上下文）的分布差异，自动识别影响下游推理/决策的关键
  token，不必依赖人工标注。

  - **蒸馏权重分配**：借鉴 PRS 得分与 RPT 门控，在模型蒸馏时将监督信号集中到“推理枢轴”token（如逻辑连词、状态更新词），避免在表面填充词上浪费容量，提升跨领域迁移效率。

  - **语言风格锚定**：引入冻结参考策略进行锚定损失，可在多语言推荐或广告文案生成中，既注入外部知识（如英文产品描述）又不破坏目标语言的流畅度，缓解 RL 或蒸馏带来的语言退化。

  - **训练稳定性**：门控分数来自同一模型的两个视图对比，无需额外教师网络，且运行时统计归一化适应不同训练阶段，可降低工程部署复杂度，适合在线蒸馏场景。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

## 动机
多语言大模型在低资源语言上的推理能力远弱于英语，现有迁移方法存在明显不足：SFT 使用翻译推导但存在离线偏差；GRPO 等 RL 方法仅有序列级稀疏奖励，难以塑造中间推理格式；在线策略自蒸馏（COPSD）虽提供 token 级密集监督，但对所有位置等权蒸馏，稀释了关键的推理信号。核心问题在于：目标语言思维链中哪些 token 才是真正决定推理走向的“枢轴”？

## 方法关键点
- **教师视图对比**：同一模型作为教师，构建两个视图——有英语参考解答的 solution-conditioned 视图 \(q^+\) 和无参考解答的 ablated 视图 \(q^-\)，它们共享双语问题与前缀，仅依据解答有无形成分布差异。
- **推理枢轴定位**：计算两个视图的 KL 散度 \(a_t = D_{KL}(q^+_t \parallel q^-_t)\) 作为 Privileged Reasoning Sensitivity (PRS)，使用运行统计归一化后经 sigmoid 得到 Reasoning-Pivot Transfer (RPT) 门控 \(g_t\)，高门 token 对应推理敏感位置。
- **双路径蒸馏损失**：\(\mathcal{L}_{pivot} = \frac{1}{N}\sum m_t g_t D_{KL}(q^+_t \parallel p_t)\) 将特权蒸馏集中在推理枢轴上；\(\mathcal{L}_{anchor} = \frac{1}{N}\sum m_t (1-g_t) D_{KL}(r_t \parallel p_t)\) 将其他 token 锚定到冻结的参考策略，保持目标语言表达。
- **纯在线、无额外模型**：学生生成 rollouts 后，教师视图来自同策略 stop-gradient 评估，参考策略为初始冻结模型，所有分布均基于完整词汇表。

## 关键实验
- 数据集：AfriMGSM（12 种非洲低资源语言，pass@12）与 PolyMath（5 种中高资源语言，难度加权准确率）。
- 基线：SFT、GRPO、MAPO-DPO、M-Thinker、PCS、COPSD、EGRSD。
- 主要结果：Qwen3-1.7B 上 RP-OPSD 在 AfriMGSM 平均 pass@12 达到 19.07（比 COPSD 高 2.37），在 PolyMath 平均 DW-ACC 达到 17.97（比 COPSD 高 1.98）；4B 模型同样取得一致提升。
- 分析：高门 token 主要对应推理控制词（如“所以”“但”）和问题特有状态更新词（如“梯形”“1.25v”），低门 token 多为表面符号；RP-OPSD 在英语未解出的难题上增益显著（超出英语可达性 +8.3 题 vs. PCS +4.0），且语言一致性优于 GRPO/COPSD。

**核心见解**：推理枢轴是影响下游推理状态的关键 token，通过对比有无特权解答的教师分布差异即可无标注地定位它们，进而实现更高效的多语言推理迁移。
