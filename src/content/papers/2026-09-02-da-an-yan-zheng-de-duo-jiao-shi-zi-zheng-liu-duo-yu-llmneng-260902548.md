---
title: 'Learn from Whoever Is Right: Answer-Verified Multi-Teacher Distillation for
  Multi-Domain LLMs'
title_zh: 答案验证的多教师自蒸馏：多域LLM能力整合
authors:
- Xixiang He
- Xingming Li
- Baiqi Wu
- Qiyao Sun
- Xuanyu Ji
- Ao Cheng
- Qingyong Hu
affiliations:
- National University of Defense Technology
- Zhejiang University
- Intelligent Game and Decision Lab
arxiv_id: '2609.02548'
url: https://arxiv.org/abs/2609.02548
pdf_url: https://arxiv.org/pdf/2609.02548
published: '2026-09-02'
collected: '2026-09-03'
category: Training
direction: 多教师蒸馏 · 答案验证 · 多域LLM整合
tags:
- multi-teacher distillation
- answer verification
- self-distillation
- multi-domain LLM
- on-policy distillation
- policy optimization
one_liner: MT-SDPO用答案验证按样本选择正确教师，结合自锚定与特权蒸馏，将多域教师整合为单一LLM策略，提升最弱域并缩小域间差距
practical_value: '- 多域/多任务LLM post-training时，不要按领域标签路由教师；对有可验证答案的任务（如选品打分、参数判断、query改写），用程序化校验器按样本筛选正确教师，再聚合所有正确反馈，可提升最弱域并缩小域间差距。

  - Self-anchor 思路：先用学生自己生成且验证正确的 rollout 作为同组错误 rollout 的 privileged context，减少外部教师查询成本；只有学生失败时才查询外部教师，能明显降低训练开销。

  - 蒸馏 teacher feedback 时引入词法/规则 sanitizer，过滤掉泄露正确答案或参考选项的反馈，防止模型只学会背答案；电商推荐解释、搜索词生成的
  teacher feedback 同样需要这种防泄漏机制。

  - 工程实现：离线先缓存每个样本的 eligible teacher set，训练时不必重复回答；推理只保留 student，丢弃教师池、verifier 和
  EMA 副本，利于部署。负结果显示：若初始化已经均衡，在线蒸馏收益有限，应先评估最弱域 headroom 再决定是否投入在线阶段。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

## 动机
现代LLM按域分别训练专家教师（数学、代码、指令跟随等），部署时需要合并为一个统一策略。现有 MOPD 按领域标签把每个样本路由到匹配域的教师，但领域专长只是平均性质：实测匹配教师仅在 52.94% 的样本上正确，而按样本选择至少一个正确教师的覆盖率可达 65.69%。可靠教师应按样本而非按域确定。

## 方法关键点
MT-SDPO 建立在 Self-Distillation Policy Optimization (SDPO) 之上，训练单一学生，三个组件全部只在训练时存在：
- **Self-anchors**：每组采样 8 个 on-policy rollouts，验证器标记正确/错误；正确 rollout 作为同一组其他 rollout 的自我锚定，排除自身防止序列泄漏。
- **Answer-verified eligibility**：训练前每个教师私有回答，程序化验证器缓存正确教师为该样本的 eligible set；错误 rollout 只查询这些教师，反馈经 sanitizer 过滤泄露和漂移。
- **Privileged distillation**：将 self-anchor 和所有验证反馈拼接为 privileged context，只给 EMA self-teacher 读取；学生仅看问题，通过 token-level JSD 散度从 self-teacher 蒸馏，带重要性权重掩码。只更新学生，部署时丢弃教师、verifier 和 EMA。

## 关键实验
在 SciKnowEval L3 科学问答的化学、材料、物理三个域上，训练集 1953 题，测试每域 79 题，用 avg@16 指标。五个学生来自 Qwen3、Llama-3.1、OLMo-3 三家。Qwen3-8B 上，MT-SDPO 相比 Multi-Domain PT 提升 Macro 4.64 点、最弱域 14.79 点，域间差距从 20.96 降到 5.30，缩小 74.7%；也比三模型匹配教师参考高 3.79 Macro 和 11.15 Worst-domain。消融显示：去掉 cross-domain rescue 或 teacher aggregation 都会损失平衡或精度；去掉 verification 则 Macro 下降 6.56 点，低于初始化。Llama-3.1-8B-Instruct 因初始化已均衡，在线方法无收益。

## 最值得记住
Verified reliability, not domain membership, should decide who teaches.
