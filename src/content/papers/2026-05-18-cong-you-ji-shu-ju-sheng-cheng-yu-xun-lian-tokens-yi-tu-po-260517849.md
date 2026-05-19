---
title: Generating Pretraining Tokens from Organic Data for Data-Bound Scaling
title_zh: 从有机数据生成预训练 tokens 以突破数据墙
authors:
- Zichun Yu
- Chenyan Xiong
affiliations:
- Language Technologies Institute, Carnegie Mellon University
- Xlue
arxiv_id: '2605.17849'
url: https://arxiv.org/abs/2605.17849
pdf_url: https://arxiv.org/pdf/2605.17849
published: '2026-05-18'
collected: '2026-05-19'
category: Training
direction: 数据受限下合成数据生成
tags:
- Synthetic Data
- Pretraining
- Data-Bound Scaling
- Reinforcement Learning
- Faithfulness
- Model-Aware
one_liner: SYNPRO 通过忠实且模型感知的合成数据生成，让 LLM 从有限有机数据中榨取更多有效 token，实现最高 5.2 倍重复训练的效率提升。
practical_value: '- **用 faithfulness 奖励约束合成数据的分布一致性**：在电商推荐场景中，对用户行为序列（如点击流）做 rephrase
  或 reformat 生成训练样本时，必须强制生成内容忠于原始序列，避免引入幻觉或知识蒸馏，否则会导致分布坍缩，损害长期效果。

  - **模型感知的数据生成**：借鉴 SYNPRO 的数据影响奖励，在 Agent 多智体训练或生成式推荐中，可以动态评估当前模型在哪些样本上损失下降较大，引导数据生成器朝着模型当前不擅长的内容倾斜，类似在线课程学习，持续突破性能瓶颈。

  - **数据操作组合：rephrase + reformat**：Reformat 将源数据转化为 QA、对比分析、推理链条等任务形式，可迁移至电商搜索、推荐解释生成等场景；将用户序列或商品描述重新格式化为结构化常识推理段落，能帮助模型学到更深层的语义关联。

  - **多轮迭代合成与累积合并**：工作证实将历次生成的数据一起混合训练比只用最新一批更有效，工程实现上可以建立合成数据池，配合模型 checkpoint 迭代扩增，最大化有限原始数据的价值。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**  
大模型预训练正从算力约束转向数据约束：可利用的高质量人类文本远低于最优训练 token 需求（如 α=10%），简单重复训练回报急剧衰减。已有方法或造成分布坍缩，或只从现有数据中筛选，未充分挖掘有机数据的内在价值。  

**方法**  
- **SYNPRO 框架**：在有机数据上迭代执行“LM 预训练至饱和 → RL 更新生成策略 → 生成新合成数据并入训练集”三阶段循环。  
- **合成操作**：**rephrase**（保留语义的词汇/句法重写）和 **reformat**（将内容转为对比分析、知识亮点、推理轨迹等任务形式）。  
- **奖励设计**：质量奖励保证文本通顺；忠于源文档的 faithfulness 奖励（rephrase 用 BERTScore + 结构评分 + 长度限制，reformat 用训练的小型 faithful 判别器）；数据影响奖励引导生成器产出当前模型尚未吸收的内容。  
- **模型感知更新**：当参考损失饱和时，用当前模型检查点计算影响，更新策略使新数据更具信息量。  

**关键结果**  
在 DCLM-Baseline 上，400M/1.1B 模型仅用 10% 计算最优 token 量（0.8B/2.2B）。SYNPRO 有效 token 数达**重复训练的 3.7–5.2 倍**，在 1.1B 规模甚至超越训练同等数量唯一数据的 oracle 表现。消融证实 faithfulness 对避免分布坍缩至关重要，且模型感知奖励使生成器持续适应知识缺口，静态方法后期正向影响比例快速下降。
