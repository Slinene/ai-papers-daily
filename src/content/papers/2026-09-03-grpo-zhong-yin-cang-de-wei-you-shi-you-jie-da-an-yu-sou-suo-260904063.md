---
title: Spurious Advantage Hidden in GRPO
title_zh: GRPO 中隐藏的伪优势：有界答案与搜索智能体中的猜测奖励
authors:
- Jiamian Wang
- Samyadeep Basu
- Koustava Goswami
- Tong Yu
- Zhiqiang Tao
affiliations:
- Rochester Institute of Technology
- Adobe Research
arxiv_id: '2609.04063'
url: https://arxiv.org/abs/2609.04063
pdf_url: https://arxiv.org/pdf/2609.04063
published: '2026-09-03'
collected: '2026-09-05'
category: Training
direction: RLVR 优势估计修正 · 防猜测偏差
tags:
- GRPO
- RLVR
- Advantage Estimator
- Reasoning
- Search Agents
one_liner: 识别 GRPO 优势估计在有限答案空间与搜索智能体中会奖励猜测行为，并提出 SIGNBALANCE 修正
practical_value: '- **在二元验证 reward 的 RLVR 场景里警惕候选空间大小**：电商/搜索 Agent 常把「点击/转化/找到商品」等做成二元
  verifier，如果某一步的候选答案集很小（如选品类、选广告位、选价格档），GRPO 的组内归一化优势会奖励撞对的 rollout，策略容易被带偏为猜测而非推理。训练前可先审计每个
  prompt group 的有效答案数量。

  - **优势估计不要直接用组内 std 归一化**：SIGNBALANCE 保持 verifier 的符号，使用全局尺度，并用 stop-gradient 按类别重缩放恢复零均值。工程上可以改成：对每个
  prompt group 计算 sign 后，用全局 running std 或固定 scale，再按正确/错误类别分别做 baseline 校正，避免组内 composition
  引入伪优势。

  - **搜索 Agent 的 credit assignment 要区分路径质量**：预算增加会让多条轨迹到达同一答案，GRPO 会奖励大量探索撞答案的轨迹。业务中训练搜索/推荐
  Agent 时，如果 reward 只给最终结果，建议在轨迹中间步加入过程 reward（如 query 改写是否有效、是否看了正确商品）或对同终点轨迹做加权，降低撞答案的收益。

  - **有界子任务单独处理**：开放答案任务中可能嵌套有界子问题（如多选筛选条件），可对这类子步骤单独建模优势，或在 prompt 设计上扩大候选空间，减少 GRPO
  伪优势的触发条件。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：RLVR 已成为 LLM 推理后训练的标准方法，GRPO 对每个 prompt 采样一组 rollout，用组内 reward 均值和标准差构造优势。表面上看，正确的 rollout 因推理而获得高优势；但作者发现一个被忽视的情况：当 rollout 只是猜中正确答案时，GRPO 公式仍会赋予其高优势，即「伪优势」。这在三类任务中尤为突出：候选答案集很小的有界答案任务；开放答案集中嵌套有界子问题；搜索 Agent 因预算增加而有多条路径可达同一答案。伪优势会误导策略偏向猜测式行为。

**方法关键点**：提出 SIGNBALANCE，核心是让优势 magnitude 不再依赖组内正确/错误组成。它保留 verifier 的符号（正确/错误），使用全局尺度代替组内归一化，并通过 stop-gradient 的按类别重缩放恢复零均值平衡。这样优势估计不再受到组内 composition 影响，减少对猜测 rollout 的奖励。

**结果**：在数学推理和搜索 Agent benchmark 上，多规模实验显示 SIGNBALANCE 在开放答案数学任务上与 GRPO 表现相当，在有界答案数学和搜索 Agent 任务上取得提升，验证了修正伪优势的有效性。
