---
title: GR2 Technical Report
title_zh: GR2：面向工业级重排序的生成式推理重排框架
authors:
- Yufei Li
- Zaiwei Zhang
- Mingfu Liang
- Kavosh Asadi
- Jay Xu
- Jimmy Kim
- Chongyang Bai
- Jieyi Zhang
- Hongye Xie
- Prachi Agrawal
affiliations:
- Meta AI
arxiv_id: '2606.31984'
url: https://arxiv.org/abs/2606.31984
pdf_url: https://arxiv.org/pdf/2606.31984
published: '2026-06-30'
collected: '2026-07-01'
category: RecSys
direction: LLM 推理重排序 · Semantic ID
tags:
- Semantic ID
- Re-ranking
- Reinforcement Learning
- Chain-of-Thought
- On-Policy Distillation
- Reward Hacking
one_liner: 通过语义 ID 中训练、推理链蒸馏和可验证奖励 RL，将 LLM 推理引入重排序并解决工业部署瓶颈
practical_value: '- **用 Semantic ID 弥合 LLM 与物品表征鸿沟**：传统非语义 ID 不在 LLM 词表中，直接使用会导致推理断裂。GR2
  采用的 tokenizer 可将物品映射为≥99% 唯一性的 Semantic ID，并混入中训练语料，使 LLM 能够直接基于物品语义进行推理。电商/广告场景中，尤其适合商品、广告创意这类属性丰富的实体。

  - **OPD 替代 SFT 防止大规模训练坍塌**：当教师-学生大小差距悬殊时，普通 SFT 会出现灾难性遗忘，OPD 以 on-policy 方式用 KL
  锚定教师分布，1.7B 学生可恢复 32B 教师 82% 的收益，大幅降低推理成本。在预算有限又需要蒸馏大模型推理能力时，这是比 SFT 更稳定的方案。

  - **重排序奖励设计中的反作弊策略**：RL 训练时 LLM 会通过直接抄袭输入顺序或利用位置偏差来获取格式奖励分。GR2 采用条件奖励——当输出等于输入顺序且输入非最优时，将排名奖励归零，仅保留格式分，可有效抑制
  reward hacking。这对任何使用 RL 做 listwise 优化（如列表广告排序、推荐 feed 排序）的场景都有直接借鉴价值。

  - **思考链内部化降低服务成本**：在推理增强 RL 后再做一次无 CoT 的 RL 微调，可将推理能力内化到参数中，在推理时无需生成思考链，推理成本降低约
  15 倍且排名质量不降。适合对延迟敏感的在线上文，比如搜索广告重排、推荐首屏展示。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机** 工业推荐漏斗中，最终重排序阶段对用户参与度影响最大，但现有 LLM 工作多集中于召回和初排，重排序仍依赖 pointwise CTR 模型，未利用 LLM 的推理能力。同时存在三大障碍：物品非语义 ID 导致词汇失配、零样本或 SFT 方式未释放 RL 在可验证奖励下的推理潜力、训练和服务成本过高。

**方法关键点**
- **语义 ID 中训练**：使用 RQ-VAE tokenizer 将物品映射为≥99% 唯一性的 Semantic ID，并与自然语言交错进行中训练，让 LLM 在预测过程中直接理解物品语义。
- **推理链生成与蒸馏**：设计重排序专用提示，采用靶向采样（给定 ground truth）和拒绝采样（重复生成直到预测正确）从强教师模型获取推理链。通过 On-Policy Distillation (OPD) 替代 SFT，以 on-policy 方式用 KL 散度锚定教师分布，避免行为克隆的分布偏移和 SFT 在大规模下坍塌。
- **可验证奖励 RL**：基于 DAPO 算法，奖励由格式正确性、AUC/NDCG 排名质量以及可选 LLM-as-judge 推理质量三部分组成。为防止奖励黑客（模型直接复制输入顺序或只追求格式分），引入条件奖励：若输出等于输入且输入排名非最优，则排名奖励置零。
- **工业部署优化**：上下文压缩器将输入长度减少 80% 以上且质量持平；对 RL 后模型再做一次无 CoT 的 RL 微调，将推理内化，实现 ~15× 服务 ROI 提升；配合模型剪枝和候选集 KV 缓存进一步降低时延。

**关键实验** 在 70k 用户会话的工业日志上训练，与在线更新的 pointwise 基线对比，GR2 实现 **+18.7% R@1、+7.1% R@3、+9.6% N@3**，且收益在 9 天后续流量上无衰减。1.7B OPD 学生模型恢复 32B 教师 82% 的增益，尺寸-质量关系符合 LLM 缩放定律。消融表明 RL 单独训练会损害推理质量，OPD+RL 组合才能同时提升排名与推理。
