---
title: 'SCOReD: Student-Aware CoT Optimization for Recommendation Distillation'
title_zh: 面向推荐的师生感知型思维链优化与蒸馏
authors:
- Haz Sameen Shahgir
- Yufei Li
- Frank Shyu
- Luke Simon
- Sandeep Pandey
- Xi Liu
- Yue Dong
affiliations:
- University of California Riverside
- Meta AI
arxiv_id: '2607.05734'
url: https://arxiv.org/abs/2607.05734
pdf_url: https://arxiv.org/pdf/2607.05734
published: '2026-07-07'
collected: '2026-07-08'
category: GenRec
direction: 生成式推荐 · CoT 蒸馏优化
tags:
- CoT Compression
- Knowledge Distillation
- Generative Recommendation
- Attention-based Scoring
- Student-Aware
- LLM
one_liner: 通过学生注意力评分和奖励引导的编辑，压缩推荐推理链中的冗余验证，提升小模型蒸馏效果
practical_value: '- **CoT 蒸馏前先压缩冗余验证**：大老师在推荐排序中频繁重复检查但极少修改答案（79% 的验证不改变最终排名），直接 SFT
  会让小模型学会啰嗦而不修正。可借鉴论文的分段与重要性评分（用学生模型的 `</think>` 注意力分数）识别并剪枝无用的验证步骤，仅保留信息密集片段。

  - **奖励函数确保压缩后对学生友好**：采用 `logP(answer|edit) - α·Len - β·PPL` 选择编辑操作（保留/重写/融合/剪枝），既保证压缩后答案可预测，又避免高困惑度文本破坏小模型的训练稳定性（防止灾难性遗忘）。在业务中蒸馏推荐模型时可复用该公式，自动平衡压缩率与可学习性。

  - **避免极端压缩导致的格式崩溃**：纯 LLM 摘要压缩虽然大幅缩短长度，但导致 8.74% 的解析失败（如输出不足 k 个候选、重复索引），说明过度压缩会破坏输出格式。工程上应采取逐步编辑策略，保留必要结构。

  - **SFT 足够时，RL/on‑policy 增益有限**：论文在 SFT 模型已接近老师时，尝试了 DAPO 和 OPSD，均未带来稳定提升，提示在生成式推荐场景中，合理处理后训练阶段可能不需要额外
  RL 微调，节省计算资源。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
生成式推荐将排序转化为推理任务，通常由大模型生成思维链（CoT），再蒸馏给小模型以降低成本。但在推荐场景下，大老师的 CoT 存在独有的冗余模式：平均每条链重复验证 3.2 次，其中 79% 的校验不改变最终答案。直接 SFT 会让学生模仿这种啰嗦行为，既不修正也不高效。此外，推荐标签来自噪声用户行为，老师的推理本身具有高度不确定性，生成的 CoT 对学生而言往往分布外。因此，需要一种面向学生模型的 CoT 压缩方法，既去除冗余又保证压缩后文本对学生可学习。

**方法关键点**  
- **分段与类型标注**：先用 Gemma‑4‑26B 将老师 CoT 按语义切割为 6 类阶段（购买历史、偏好建模、候选分析、中间排序、验证、最终排序），发现验证段占比 33.9% 且多为无效重复。  
- **学生注意力重要性评分**：利用目标学生模型前向传播时 `</think>` 标记对各段的注意力权重，近似每个段对最终答案的贡献，将段分为高/中/低三档。  
- **奖励导向的编辑选择**：低分段可选融合或剪枝，高分段可保留或重写，中分段可重写或融合。编辑操作（除保留/剪枝外）均由 LLM 执行。最终选择使 `logP(answer|edit) - α·Len - β·PPL` 最大的操作，保证压缩后的段对学生模型保持高似然、低长度、低困惑。  
- **训练与后处理**：压缩后的 CoT 用于 SFT，之后可选择性应用 DAPO 或 OPSD，但实验发现两者均未带来额外增益。

**关键结果**  
在 Amazon Beauty Pretrain 数据集上构建的 10 选 10 重排序任务（11350 训练/4472 验证/4474 测试），以 Qwen‑3‑0.6B 为学生模型，SCOReD 对比原始 CoT SFT 基线：NDCG↑1.56%（0.7908 vs. 0.7786），Recall@5↑1.9%（0.7243 vs. 0.7108），同时平均推理长度减少 27.3%（6.2K vs. 8.5K chars），解析失败率从 2.82% 降至 1.52%。0.6B 学生模型甚至超过了 35B 的 Qwen‑3.6B‑A3B。而 LLM 一阶摘要压缩虽然长度更短（4.4K），但解析失败率高达 8.74%，性能大幅下降，说明压缩需考虑学生适应度。
