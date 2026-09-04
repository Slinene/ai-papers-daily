---
title: 'DRACO: Fine-Grained Credit Assignment with Dynamic Rubrics for Long-Horizon
  Agent Training'
title_zh: DRACO：动态评分标准驱动的长程智能体细粒度信用分配
authors:
- Shubham Gandhi
- Saurabh Goyal
- Kiran Kate
- Yara Rizk
affiliations:
- Carnegie Mellon University
- IBM Research
arxiv_id: '2609.04094'
url: https://arxiv.org/abs/2609.04094
pdf_url: https://arxiv.org/pdf/2609.04094
published: '2026-09-03'
collected: '2026-09-04'
category: Agent
direction: Agent 强化学习 · 步骤级信用分配
tags:
- Agent RL
- GRPO
- Rubric Reward
- Credit Assignment
- Outcome-Blind
- Long-Horizon
one_liner: DRACO 在 outcome-blind 设定下动态生成轨迹级 rubric，并把单标量奖励闭式重分配到步骤级优势，用于长程工具智能体 GRPO
  训练
practical_value: '- 在没有程序化 verifier 的客服、策略执行等业务场景，可用动态 per-trajectory rubric 代替 ground-truth
  成功信号：judge 根据任务指令和每组 rollout 生成 criteria，只保留组内有人失败的 criteria（discriminative dropout），并用
  pass/(pass+fail) 得到 outcome-blind 奖励；避免静态 rubric 训练早期就饱和丧失区分度。

  - 把 GRPO 的 trajectory-level advantage 按 judge 标注的 responsible steps 做闭式重分配：step
  quality Q_j=p_j/(p_j+f_j)，winner 加权 Q_j、loser 加权 1-Q_j，每个 step 的总贡献正比于 quality 而与
  token 长度无关，sum 守恒且 sign 保持。这个方法不需要额外训练 attribution 模块，可直接迁移到长程 Agent RL 的步骤级信用分配。

  - 成本敏感时可以用策略模型自己当 judge，配合 thinking enabled 和 k=3 一致投票，训练 judge 成本约降 5.1 倍（$1607→$316），仍接近或超过
  verifier-trained 性能；分析表明 self-judge 的 lenient 错误比 strict 错误对 GRPO 更新危害小。

  - 业务关注稳定完成率时，应报告 pass^k 而不仅是 pass@k：DRACO 的 TGC p3/p1 retention 明显高于 p1/pass@3，说明它主要提升重复尝试的成功一致性而非单纯发现能力。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**  
长程 tool-using Agent 常没有可验证的成功信号，outcome-blind 训练只能依赖过程性 rubric。但轨迹级单标量奖励对几十步的决策太粗，且静态 rubric 会在训练早期饱和。DRACO 针对两个问题：如何生成随策略能力变化的评价标准，以及如何把轨迹级 rubric 判断分配到具体步骤。

**方法关键点**  
- 动态 per-trajectory rubric：judge 先从任务指令提 criteria，再结合每组 rollout 扩展并合并去重；用 discriminative dropout 只保留某个 group member 失败过的 criteria。  
- 奖励为 outcome-blind 的 R_i=(p_i-f_i)/(p_i+f_i)，不接触任何 ground-truth verifier。  
- 步骤级信用分配：judge 对每个 criterion 标注负责步骤，步骤质量 Q_j=p_j/(p_j+f_j)；winner 按 Q_j 加权，loser 按 1-Q_j 加权。  
- 在 GRPO 内将 trajectory advantage A_i 重排为 step advantage a_j=A_i·Nw_j/(n_j∑w_k)，每个 step 总贡献只取决于质量而不取决于 token 长度，总 push 守恒且符号不被反转；gap tokens 不参与更新。  
- 该 step-credit 规则为闭式，无训练 attribution 模块。

**关键实验**  
在 AppWorld 训练、τ-bench 零样本迁移。Qwen3.6-27B 上，DRACO 相较 untrained base 在 AppWorld TN 的 TGC/SGC 从 69.4/41.1 提升到 85.3/70.6（+15.9/+29.5），且比用 ground-truth unit test 做 outcome reward 的 GRPO 还高 +5.3 TGC；AppWorld TC 的 TGC 从 49.7 到 61.5。τ-bench Banking 的 SR 从 15.8 到 20.4，self-judge 版本达 21.1。消融显示动态 rubric 与 step credit 组合是关键，单独提升有限；静态 rubric 训练 pass rate 约 95% 饱和，动态 rubric 保持约 74% 且重新用静态 rubric 评分有 91.3%，说明动态 rubric 覆盖静态 criteria。

最值得记住的一句话：在 outcome-blind 长程 Agent 训练的 reward 设计里，先动态生成可判定的轨迹级 rubric，再用闭式步骤信用分配把轨迹优势按责任步骤重排，能比直接用稀疏 ground-truth 奖励更有效，且不需要额外 attribution 模型。
