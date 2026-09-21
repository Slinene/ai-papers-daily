---
title: What Should We Ask Next? Retrieval-Aware Question Learning under Partial Evidence
title_zh: 下一步应该问什么？部分证据下的检索感知问题学习
authors:
- Lyucheng Qian
- John Yuehan Zhang
- Pingyu Wang
affiliations:
- Sichuan University
- University of California, Berkeley
arxiv_id: '2609.21924'
url: https://arxiv.org/abs/2609.21924
pdf_url: https://arxiv.org/pdf/2609.21924
published: '2026-09-18'
collected: '2026-09-21'
category: QueryRec
direction: 检索感知的提问策略学习 · RL
tags:
- Retrieval-aware RL
- Question Generation
- GRPO
- Interactive Retrieval
- Multimodal LLM
one_liner: 通过在线 RL 直接从检索排名反馈优化提问策略，替代离线 QA 排序模仿，五轮 R@1 提升 5.79 个点
practical_value: '- 用检索结果变化（如 reciprocal-rank gain 或业务指标）作为 reward 在线优化 Agent 的澄清提问/query
  生成策略，不要依赖人工标注的问题质量或静态候选区分度；GRPO 可稳定训练，且训练好的策略可跨 retriever 迁移。

  - 将当前 Top-K 候选项直接作为多模态上下文输入给策略模型，去掉 selector 等中间组件，让策略直接学习如何利用候选差异；在电商对话式搜索中可让 Agent
  直接观察当前召回 Top-N 商品图像/标题来生成澄清问题。

  - 实现一个 validity gate 约束生成，过滤掉候选索引引用、请求泄露记忆、重复提问等，防止 RL 策略走捷径；在训练和推理都使用，可大幅减少无效动作并避免策略崩溃。

  - 分析显示局部开放属性问题（如“什么颜色/材质”）比 yes/no 问题带来更大的检索增益，策略会自发将预算分配给这类问题；可参考该结论引导电商对话式搜索中的问题类型分配，优先问具体属性而非泛泛确认。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

## 动机
交互式检索中，一个问题没有孤立价值，其效用取决于引发的答案、对话状态及下游检索排序变化。现有方法多用离线行为克隆模仿候选 QA 排序，但分析发现：静态问题区分度与感知有用性与实际 rank 变化几乎无关（Spearman ρ≈0.05，点双列≈0.1），人类标注同样无可靠关联；模型对候选顺序/组成不敏感，说明离线监督难以捕捉问题的条件价值。因此，需要直接在完整的问题-回答-检索闭环中优化提问策略。

## 方法关键点
- **三阶段训练**：先训练冻结的 retriever（CLIP+IRRA）；再用 SFT 冷启动提问者（LLaVA-OneVision-Qwen2-7B + QLoRA）；最后用 GRPO 在线优化提问策略。
- **状态与动作**：策略观察初始描述、对话历史、累积检索文本、当前 Top-4 候选图像，但不观察私有记忆或目标 rank；动作是自由形式自然语言问题。
- **奖励函数**：基于 reciprocal-rank gain，额外给予 Rank-1 到达 bonus（0.35）和重复惩罚（-0.02），无效问题给 -0.2；仅对有效问题更新策略。
- **Validity gate**：训练和推理时均过滤候选索引引用、记忆转储、重复提问等，防止策略钻空子导致崩溃。
- **优化细节**：GRPO group size=8，SFT 检查点作 reference policy，KL 惩罚系数 0.03，仅更新 QLoRA adapter，视觉塔、answerer、retriever 冻结。

## 关键实验结果
- 在 Interactive-PEDES 五轮交互中，RA VEL 达到 73.73 R@1，比 LLaVA-ReID 的 67.94 高 5.79 点，BRI 降至 0.642。
- 迁移到 CUHK-PEDES、ICFG-PEDES、RSTPReid 三个 text-based ReID 基准，复用 IRRA retriever 时 RA VEL 分别提升 R@1 7.21、5.94、12.73 点，且可搭配 RDE retriever 进一步提升。
- 行为分析：RA VEL 将提问预算更多分配给局部开放属性问题（54% vs LLaVA-ReID 的 31%），该类问题平均检索增益 6.90（yes/no 仅 2.25）；最终 query 更短（90.8 vs 96.9 词）、负词减少、属性覆盖提升至 82%，对初始难查询增益最明显。
- 消融显示 SFT + 有 gate 的 RL 效果最佳；去掉 gate 会导致策略快速退化为无效动作。

## 最值得记住的一句话
问题价值必须通过答案和检索排名的闭环反馈在线评估，离线静态区分度或人工有用性判断几乎无法提供可靠监督。
