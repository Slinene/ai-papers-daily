---
title: 'Same Trajectory, Different Knowledge: Information-State-Aware On-Policy Distillation
  for Search Agents'
title_zh: 相同轨迹，不同知识：面向搜索 Agent 的信息状态感知 On-Policy 蒸馏
authors:
- Minhao Sun
- Xian-Ling Mao
- Eric Tao
- Zi-Ao Ma
- Zhijing Wu
affiliations:
- Beijing Institute of Technology
- Huawei
arxiv_id: '2611.01987'
url: https://arxiv.org/abs/2611.01987
pdf_url: https://arxiv.org/pdf/2611.01987
published: '2026-11-01'
collected: '2026-11-03'
category: Agent
direction: 搜索 Agent 的 on-policy 蒸馏与过程监督
tags:
- agentic search
- on-policy distillation
- process reward
- factual recoverability
- multi-hop QA
- credit assignment
one_liner: 提出 ISA-Distill，按学生状态的事实可恢复性加权 fact-use 与 evidence-seeking 双视图反馈，纠正 teacher
  特权信息偏差
practical_value: '- 在电商搜索/推荐 Agent 的 RL 过程监督中，不要把 gold answer 或完整 evidence 直接塞给 teacher；可增加一个“学生侧事实可恢复性”估计：用
  frozen policy 对 value-masked probe 采样 32 次，算 mean token NLL，再校准为 k∈[0,1]。按 k 加权“已知事实利用”和“缺失证据获取”两个
  teacher 视图，训练期仅增加约 4.3% 开销，就能缓解多跳商品问答中的 search 不足与过早作答。

  - 对多跳商品属性问答、活动规则查询、商品对比/导购等任务，可按 recoverability 动态分配 search budget：事实已知时少搜，事实缺失时多搜；论文经验是单跳调用
  -7.21%、多跳 +2.94%，整体 calls 更省且准确率提升。

  - 过程监督无需覆盖全轨迹 token：只对 `<search>` tag + query、`<conclusion>` tag + factual assertion
  等关键 span 做有界 local correction，监督 token 仅约 11.32% 也能获得稳定提升，适合预算受限的在线训练链路。

  - 若发现蒸馏后的推荐/搜索 Agent 搜索次数不足或过早停止，可做 paired evidence utility 诊断：给 teacher 加 gold
  fact，观察其对 search token score 的变化；positive-utility search 被大幅降分即存在 information-state
  mismatch，可引入 recoverability-aware 修正。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
On-policy distillation 训练 search agent 时，teacher 常拿到 supporting evidence、gold answer 或 hindsight context。若 teacher 依赖学生无法从当前状态可靠恢复的事实，会高估“直接用事实作答”的动作，低估能帮学生获取证据的检索动作。这种 information-state mismatch 使有用的 evidence-acquisition step 得不到充分 credit，导致多跳搜索不足或单跳过度检索。

## 方法关键点
- 对每个 sampled action 选一个 focal fact，构造 value-masked probe，用 frozen rollout policy 采样 32 条 local conclusion，取 mean token NLL，再经预拟合的 kernel smoothing 映射为 recoverability k∈[0,1]。
- 设计两个 teacher context：fact-use view 提供正确事实，引导利用已知知识；evidence-seeking view 只给信息需求，引导获取证据。
- 对同一 action token，分别计算两个 view 相对原 context 的 log-probability contrast，做 tanh 有界化，按 k 与 1-k 加权得到 local correction，加在 outcome advantage 上，用 GRPO + KL 更新。
- 监督只作用于关键 token span：搜索步的 `<search>` 与 query，非搜索步的 `<conclusion>` 与 factual assertion。

## 关键实验
在 NQ、TriviaQA、PopQA、HotpotQA、2WikiMQA、MuSiQue、Bamboogle 七个 benchmark 上，Qwen2.5-3B 的 macro EM 从 EviSD 42.6 提升到 43.9；Qwen2.5-7B 从 47.2 提升到 48.0；Llama-3B 也提升 1.3 点。相比 EviSD，7B 在单跳 QA 搜索调用减少 7.21%，多跳增加 2.94%，总调用下降 2.45%。Ablation 显示按状态加权优于 K-only、S-only 和固定 0.2/0.8 混合；训练额外开销仅 4.3%，监督 token 占比仅 11.32%。

## 一句话
Teacher feedback 应区分“学生需要建立事实还是使用事实”，用状态可恢复性加权过程反馈，能以极小开销改善 search agent 的准确率-检索效率 trade-off。
