---
title: On-Policy Self-Distillation without Any Supervision
title_zh: 无监督在策略自蒸馏：仅依赖模型自身一致性
authors:
- Yijiang Li
- Bingyang Wang
- Yijun Liang
- Yunjie Tian
- Di Fu
- Nuno Vasconcelos
affiliations:
- UC San Diego
- Georgia Institute of Technology
- University of Maryland, College Park
- ByteDance
arxiv_id: '2608.06296'
url: https://arxiv.org/abs/2608.06296
pdf_url: https://arxiv.org/pdf/2608.06296
published: '2026-08-06'
collected: '2026-08-07'
category: Training
direction: 无监督自蒸馏 · 内部一致性
tags:
- Self-Distillation
- On-Policy
- Unsupervised
- Self-Consistency
- LLM Training
- Reasoning
one_liner: 用模型多路采样投票伪标签实现对未标注数据的高效在策略自蒸馏，在数学推理上超越有监督方法
practical_value: '- **无标签场景自蒸馏**：当推荐/搜索/Agent 场景缺乏标注反馈时，可利用同一请求的多路生成投票一致性构建伪标签，驱动模型自我改进，减少对人工标注的依赖。

  - **不一致轨迹定向蒸馏**：通过对模型输出不一致的样本进行集中蒸馏，定位并修正模型易错/混淆区域，类似推荐中利用用户反馈不确定性进行针对性优化。

  - **蒸馏散度选择**：Forward KL 显著优于反向 KL 或 JSD，可作为推荐模型知识蒸馏时的默认选择；教师模型使用 EMA 更新（衰减 0.995）比冻结更稳定，可参考用于在线蒸馏。

  - **完整性要求**：蒸馏必须使用完整推理轨迹而非仅最终答案，提示在生成式推荐（如商品文案）中保留完整生成过程作为教师信号更有效。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**  
现有在策略（自）蒸馏（OPD/OPSD）虽能减少训练–推理不匹配，但仍依赖外部监督（真值答案、环境反馈或更强教师），限制其在无标注数据上的扩展。本文探索能否仅用模型自身信息实现真正自蒸馏。  

**方法关键点**  
- 对每个未标注问题采样 G 个 rollout，提取最终答案，通过多数投票得到伪答案，仅当投票置信度超阈值 τ（设为 0.5）且存在不一致响应时训练。  
- 选择最短的投票一致 rollout 作为教师上下文（伪标签），不一致 rollout 作为学生轨迹。  
- 教师与学生共享参数但教师固定（初始权重），计算教师条件于伪标签与学生条件于问题的 next-token 分布的 Forward KL 散度，仅在学生不一致的 rollout 前缀位置进行蒸馏。  
- 教师可 EMA 更新以提升性能。  

**关键结果**  
- 在 Qwen3-4B/8B 非思考模式下，U-OPSD 在五基准（AIME24/25, HMMT25, MATH500, AMC23）上平均分别提升 8.5/10.7 百分点，超过有监督 OPSD 3.2/2.3 百分点。  
- 在思考模式下与 OPSD 基本持平（77.05 vs 76.20 和 77.99 vs 77.97），超越 GRPO。  
- 蒸馏必须使用完整推理轨迹，仅用伪答案损失 11.4–15.6 点；Forward KL 远优于反向 KL/JSD。
