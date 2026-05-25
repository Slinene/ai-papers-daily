---
title: 'ARES: Automated Rubric Synthesis for Scalable LLM Reinforcement Learning'
title_zh: ARES：面向可扩展LLM强化学习的自动化评分标准合成
authors:
- Xiaoyuan Li
- Keqin Bao
- Moxin Li
- Yubo Ma
- Yichang Zhang
- Wenjie Wang
- Fuli Feng
- Dayiheng Liu
affiliations:
- University of Science and Technology of China
- Alibaba Group
- National University of Singapore
arxiv_id: '2605.23454'
url: https://arxiv.org/abs/2605.23454
pdf_url: https://arxiv.org/pdf/2605.23454
published: '2026-05-22'
collected: '2026-05-25'
category: Training
direction: LLM 强化学习 · 自动评分标准生成
tags:
- Reinforcement Learning
- Rubric-based Reward
- Automated Data Generation
- LLM Training
- Open-Ended Tasks
one_liner: 从预训练文档自动生成问题及实例级加权评分标准，实现开放性任务的大规模强化学习
practical_value: '- 电商客服评价可借鉴：自动生成多维度加权评分标准（如态度、准确性、完整性），取代单一点赞/点踩信号，实现细粒度 RL 训练。

  - 生成式推荐中的解释文本评估可用类似 pipeline：从商品知识库生成问答对，合成评估标准，训练模型生成更符合多维质量要求的推荐理由。

  - 数据增强策略可复用：利用领域标签和角色信息控制生成多样性，结合 self-containment、faithfulness 等过滤器保证合成数据质量，适合构建领域
  RL 训练集。

  - 对于 Agent 工具调用等开放性任务，可将任务要求转化为评分标准，自动构造 RL 数据，减少人工设计 reward 的成本。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：LLM 强化学习（RL）依赖可验证奖励的范式（RLVR）在数学、代码等有标准答案的任务上有效，但难以扩展至医疗咨询、指令遵循等开放性任务。评分标准奖励（rubric-based reward）能处理多维度评估，但现有方法依赖专家撰写标准且为任务级固定，无法反映单个问题的评估要求，难以规模化。

**方法**：ARES 框架从原始预训练文档出发，自动生成自包含的问答对，并联合生成针对每个问题的加权评分标准，实现实例级奖励监督。为提升多样性与质量，ARES 以领域标签和角色信息为条件生成数据，并应用验证过滤器过滤掉问题不自包含、答案不忠于源文档、评分标准无效的样本。最终构建了覆盖十个领域、共 100K 条评分标准标注的训练数据。

**结果**：在七个基准上，基于 ARES 数据训练的评分标准 RL 模型性能超越继续预训练、监督微调和二元奖励 RL，尤其在医疗等复杂开放性任务上提升显著，证明了自动合成评分标准对于扩展 LLM 后训练的有效性。
