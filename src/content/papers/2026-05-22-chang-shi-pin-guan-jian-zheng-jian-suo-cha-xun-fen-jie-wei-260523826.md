---
title: Decomposing Queries into Tool Calls for Long-Video Keyframe Retrieval
title_zh: 长视频关键帧检索：查询分解为工具调用与布尔合并
authors:
- Michal Shlapentokh-Rothman
- Prachi Garg
- Yu-Xiong Wang
- Derek Hoiem
affiliations:
- University of Illinois at Urbana-Champaign
arxiv_id: '2605.23826'
url: https://arxiv.org/abs/2605.23826
pdf_url: https://arxiv.org/pdf/2605.23826
published: '2026-05-22'
collected: '2026-05-25'
category: Multimodal
direction: 长视频理解 · 查询分解与工具调用
tags:
- Video Understanding
- Keyframe Retrieval
- LLM Planner
- Tool Use
- Query Decomposition
- GRPO
one_liner: ToolMerge 用 LLM 规划器将查询分解为多个轻量视觉工具调用，并通过布尔运算符合并排名，在长视频关键帧检索上取得领先
practical_value: '- **查询分解与工具融合范式**：在电商搜索或商品推荐中，可将一个复杂查询（如“红色连衣裙，有蕾丝，适合晚宴”）分解为多个独立检索流（颜色、材质、场景），每个流用专用
  scoring 工具，再用布尔 rank 合并（AND/OR）代替简单加权，可提升多属性检索精度。

  - **轻量级检索 + LLM 规划器分离**：工业级系统可沿用 SigLIP/CLIP 等轻量模型做粗筛，OCR 等规则做精准补充，再由 LLM 规划器决定如何组合，无需对每一帧或每一件商品调用大模型，大幅度降低延迟和成本。

  - **无标注 RL 优化检索策略**：GRPO 训练规划器时，仅使用基于时间戳的召回分数作为奖励，无需人工标注最优工具调用序列。这一思路可直接迁移到商品推荐或
  RAG 场景，用用户点击或检索命中率作为奖励，通过 RL 优化查询分解策略。

  - **NMS 去重维持多样性**：在最终帧选择中使用的贪婪 NMS（保证最小时间间隔），可借鉴到推荐系统的多样性约束，选择相似度高的候选项进行步进式过滤，平衡相关性和多样性。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**：长视频问答需要可验证的视觉证据，关键帧是最直接的方式，但查询内容差异巨大，有的关注整体场景，有的需要定位多个实体。现有方法或对所有帧打单一查询分数，或将查询硬编码为固定对象关系，缺乏灵活性。ToolMerge 提出基于分解与合并的检索：LLM 规划器根据查询特征动态选择工具组合并指定结果合并方式，适应不同检索需求。同时构建 Molmo-2 Moments（M2M）基准，每个问题强制锚定到视频中的特定时间段，直接评估关键帧检索质量。

**方法关键点**：
- **规划器**：纯文本 LLM（Qwen3-VL-8B）接收问题、选项和视频时长，输出若干工具调用（SigLIP-2 用于场景级视觉相似度、T-REN 用于实体/物体检测、OCR 自动运行）以及布尔组合表达式（AND 需所有条件共存，OR 为任一条件即可）。
- **执行与合并**：每个工具对所有帧独立评分，得到每帧排名；AND 取最差排名（要求所有元素同时出现），OR 取最好排名（任一匹配即可）。OCR 提取的文本经 LLM 法官过滤后直接插入最终排名首位。
- **帧选择**：从合并排名中贪婪式 NMS 挑选 k 帧，保证帧间至少间隔 τ 秒。该方法训练-free，也可用 GRPO 微调规划器，奖励函数仅依赖检索的帧是否落入真值时间区间，无需人工标注。
- **M2M 基准**：基于 Molmo2-Captioning 数据集，从视频片段描述生成 5 选 1 选择题，经 8 步过滤（盲 LLM 测试、范围验证、必要性/难度过滤等）和人工验证，得到 756 个测试问题，每个问题对应唯一的真值时间区间，支持检索（Hit@K）和 QA 双轨评估。

**关键实验**：在 LongVideoBench、Video-MME 和 M2M 上评估。ToolMerge 在 LongVideoBench 上 8 帧/32 帧分别达到 61.8/67.4（Qwen3-VL 答案器），超过 SigLIP-Q、WFS 等基线；在 M2M 的标题检索中，零样本 HIT@8 为 58.1%，GRPO 训练后提升至 61.5%，明显优于单查询 SigLIP-Q（52.7%）。消融实验表明，OCR 对带字幕数据帮助最大，T-REN 在视觉密集场景下作用显著，多工具组合及布尔合并策略均有益于性能。

**最值得记住的一句话**：简单的 SigLIP-Q 基线在许多任务上出人意料地强，但 ToolMerge 的分解-合并框架在需要多元素共现或跨模态检索时优势显著，且可通过 GRPO 无监督优化。
