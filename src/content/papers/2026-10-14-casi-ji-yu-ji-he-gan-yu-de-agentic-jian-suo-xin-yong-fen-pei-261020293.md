---
title: 'CASI: Credit Assignment via Set Intervention for Agentic Retrieval'
title_zh: CASI：基于集合干预的 Agentic 检索信用分配
authors:
- Xinyi Cheng
- Tianfu Zhang
- Jiwen Li
- Xuesen Zhang
- Shihao Yu
- Pengfei Zhu
- Renhuan
- Heda Wang
affiliations:
- Xiaohongshu Inc.
arxiv_id: '2610.20293'
url: https://arxiv.org/abs/2610.20293
pdf_url: https://arxiv.org/pdf/2610.20293
published: '2026-10-14'
collected: '2026-10-15'
category: QueryRec
direction: LLM 多 query 联合生成与信用分配
tags:
- Credit Assignment
- LLM RL
- Sponsored Search
- Shapley
- Multi-Query Retrieval
- Agentic Retrieval
one_liner: 用快照集合干预构造反事实子集价值，Shapley 聚合加有界零和优势整形，实现多检索动作的上下文相关信用分配，线上广告主价值提升 3.51%
practical_value: '- 在多 query/多策略并行召回或 rewrite 场景，不要直接 broadcast set-level reward；可复用「一次生成+一次检索，缓存各
  action 结果，只改 coalition 组合，用冻结 evaluator 批量打分」的做法，不增加线上生成/检索成本。

  - m≥4 时 singleton、leave-one-out、full-set 不能唯一确定 Shapley 分配；业务里如果 action 数≥4，仅按单
  action 或 leave-one-out 赋 reward 会丢中间 coalition 信息。additive 价值下三者等价，所以先判断是否真的需要中间
  coalition 查询。

  - 有界零和 advantage shaping 值得直接抄：对 credit 先 within-rollout center，再用 group-level 共享
  scale 归一化，最后投影到 sum=0、∞≤κ 的 box；避免独立 clip 破坏零和导致 advantage 漂移。token 级 implementation
  把 action 内 token 赋 action advantage，shared token 保持 base。

  - 训练用 surrogate evaluator 替代线上 auction replay：m=5 时 31 个 coalition 打分不是 31 次 auction
  replay；但上线前必须审计训练 evaluator 与 replay/production 的 size-resolved sign agreement，否则
  CASI 可能不优于 Singleton。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
LLM 在赞助搜索/检索式推荐里会一次生成多个 query 或 rewrite，其候选池合并后进入下游排序与拍卖，但训练通常只有集合级 reward。Broadcast reward 虽是集合目标的合法 score-function 梯度，却不提供 action 在集合内的上下文依赖归因。尤其 m≥4 时，singleton、leave-one-out、full-set 端点观测并不能唯一确定 Shapley 分配。

## 方法关键点
- **快照集合干预**：对每个 realized action set，只做一次生成+一次检索，缓存每个 action 的召回结果；固定可回放 snapshot，改变 coalition 组合，用冻结 evaluator 打分得到子集价值。
- **Shapley 聚合**：遍历全部 2^m−1 个非空 coalition，计算 action 在每个 predecessor coalition 下的 marginal，按 Shapley 权重聚合为 within-set credit。空集价值设为 0。
- **有界零和优势整形**：先对 credit 在 rollout 内 center；用 group-level 共享 std 归一化；再投影到 sum=0、||z||∞≤κ 的 box；最终 advantage 为 base broadcast advantage + β·z。action token 接收 action-level advantage，shared token 保持 base。
- **计算成本**：m=5 时 Broadcast/Singleton/LOO/CASI 分别需 1/6/6/31 个 evaluator 打分，均来自缓存结果，不涉及重复检索或 auction replay。

## 关键实验
在 5-action 赞助搜索场景，离线 auction replay 覆盖 1200 个请求、31 个 coalition、每个重复 3 次。结果：
- 64.4% 的 action 对交互为负，7.4% 为正，说明 coalition 依赖显著。
- 在训练 evaluator 下，CASI 与 replay-defined Shapley reference 的 median cosine 为 0.4237，高于 Singleton 的 0.3877（+0.036，95% CI [0.0036,0.0677]）；LOO 仅 0.2269。
- held-out replay 集价值：CASI 66.70±3.40，Singleton 55.00±4.00，Broadcast 43.30±4.70，SFT 60.32。
- 线上 7 天 10% 流量 A/B：advertiser value 提升 3.51%，search-ad spend 增加 5.08%。

最值得记住的一句话：一次生成与检索、缓存 action 结果、构造 coalition 反事实并用 Shapley 归因，是低成本把联合 action 交互信息注入 RL 的实用路径。
