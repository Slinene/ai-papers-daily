---
title: 'MEMOIR: Temporal Behavioral Memory for Recommendation Across the Preference-Drift
  Spectrum'
title_zh: MEMOIR：面向偏好漂移的时序行为记忆推荐框架
authors:
- Younggue Bae
affiliations:
- Independent Researcher
arxiv_id: '2607.23986'
url: https://arxiv.org/abs/2607.23986
pdf_url: https://arxiv.org/pdf/2607.23986
published: '2026-07-27'
collected: '2026-07-28'
category: RecSys
direction: 时序偏好进化建模 · 对比学习
tags:
- Temporal User Modeling
- Contrastive Learning
- LLM-based Recommendation
- Preference Evolution
- Sequential Recommendation
one_liner: 用LLM编码时间窗口语义记忆并显式建模偏好进化轨迹，在高低偏好漂移用户上获得排序质量提升
practical_value: '- **时间窗口语义记忆**：将用户交互历史按日历月分窗，用自然语言描述每个窗口并送入 LLM 生成语义记忆嵌入，可作为电商中用户长期兴趣演化的轻量级表示。

  - **进化方向一致性约束**：引入 `L_dir` 惩罚连续进化方向向量的余弦偏差，对偏好单调漂移的用户（如从休闲转向正式）有用；在业务中可针对品类转换明显的用户群体单独启用该损失。

  - **进化感知聚合**：融合当前状态、进化方向与预测未来状态，让同一当前偏好但不同轨迹的用户得到不同向量，适合需要区分“新用户刚入圈”与“老用户稳定消费”的场景。

  - **漂移分层洞察**：论文发现 LLM 进化建模的优势集中在高/低偏好漂移用户群（NDCG@10、MRR 提升），对业务意味着可以在用户分群后对易漂移人群启用该模型，或作为重排序信号补充。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
序列推荐模型通常将用户偏好视为静态或仅作为下一项预测的副产品，忽略偏好随时间演化的轨迹。实际数据中，用户相邻月份品类分布的平均 JS 散度高达 0.795，92% 的交互物品是新物品，表明偏好漂移普遍存在，需要显式建模。  
**方法**  
- **时序分段与语义记忆**：按日历月将交互历史切分为窗口，每个窗口的内容序列化为自然语言（如“用户高度评价了跑步鞋，购买了蛋白粉”），用冻结的 TinyLlama 加 LoRA 生成窗口语义记忆嵌入序列。  
- **进化保留对比损失**：由两项组成：(1) 相邻窗口 InfoNCE 损失约束时态平滑；(2) 方向一致性损失 `ReLU(γ - cos(d_{t-1}, d_t))` 迫使连续进化方向对齐，适用于单调漂移用户。  
- **轨迹预测与聚合**：GRU 处理记忆序列，预测下一窗口嵌入；最终用户表示由当前加权平均、进化方向与预测未来拼接后经 MLP 得到，并加入行为一致性损失 `L_con` 将语义空间与物品空间对齐。  
**实验**  
- 数据集：Amazon Reviews 2023 的 Electronics 和 Clothing_Shoes_and_Jewelry 类别，99k 用户，平均 5.7 个窗口。  
- 对比基线：SASRec、UniSRec、SRA-CL 等 7 个模型。  
- 总体结果：NDCG@10 与 UniSRec 几乎持平（0.0643 vs 0.0641），MRR 略优，HR@10/20 略低。  
- 关键发现：**分层分析显示 MEMOIR 的优势集中在高偏好漂移和低偏好漂移的用户段**，在这些群体上 NDCG@10 和 MRR 优于 UniSRec；而在中等漂移用户中 UniSRec 全面领先。消融实验表明，单个组件（进化损失、方向损失、窗口分割）的移除对总体指标影响小（均<2%），因此漂移分层模式才是更鲁棒、可复现的结论。  
- 语义特征自身不直接带来提升：SASRec-Text（用 MiniLM 嵌入替代 ID 嵌入）性能显著低于原始 SASRec，说明语义空间与协同过滤行为空间存在错配，需要 MEMOIR 的进化感知聚合和行为一致性损失来弥补。  
**核心启发**  
单纯引入 LLM 语义不足以提升推荐；显式建模偏好进化轨迹、并在用户群体中区分漂移程度，才能在特定人群上获得排序质量的改善。
