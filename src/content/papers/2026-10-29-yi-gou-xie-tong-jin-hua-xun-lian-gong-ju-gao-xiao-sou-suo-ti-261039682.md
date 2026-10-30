---
title: Heterogeneous Co-Evolution Learning for Tool-Efficient Search Agents with Zero
  Labels
title_zh: 异构协同进化训练工具高效搜索智能体的零标注框架
authors:
- Qin-Wen Luo
- Sheng Ren
- Xiang Chen
- Rui Liu
- Jun Fang
- Naiqiang Tan
- Jun Wang
- Hua Chai
- Sheng-Jun Huang
affiliations:
- Nanjing University of Aeronautics and Astronautics
- Didichuxing Co. Ltd
arxiv_id: '2610.39682'
url: https://arxiv.org/abs/2610.39682
pdf_url: https://arxiv.org/pdf/2610.39682
published: '2026-10-29'
collected: '2026-10-30'
category: Training
direction: 搜索 Agent 零标注协同进化训练
tags:
- Search Agent
- RLVR
- GRPO
- Zero-label
- Tool Efficiency
- Self-Play
one_liner: 零标注下用异构 proposer–solver 协同进化同时优化搜索智能体准确率与工具调用效率
practical_value: '- 用海量无标注 query 日志替代人工 QA：从用户 query 出发，先让 proposer 生成实体答案，再用检索构造证据路径并做程序化校验；电商搜索/推荐
  Agent 可直接复用会话 query 和商品知识库生成训练任务，省去标注成本。

  - proposer 与 solver 解耦且可异构：3B/4B 小模型就能给 7B/8B solver 出题，任务生成成本与求解器规模解耦，跨模型族还能带来互补先验；线上可用便宜模型持续产出课程任务。

  - 中间难度奖励 4*Acc*(1-Acc) 自动筛选约 50% 通过率的前沿任务，避免全对/全错无效信号；业务 RL 任务生成或课程学习可直接复用，奖励任务生成器追求
  mixed group。

  - 工具调用效率奖励：对同一任务的 K 条轨迹，把 search call 次数按组内最大值归一化后乘 correctness，只让答对且调用少的轨迹拿高分；商品搜索/Agent
  里的 API/检索调用可用 task-local 惩罚控制成本且不明显掉点。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
搜索 Agent 的 RL 训练有两个痛点：一是固定题目集合无法随 Agent 能力进化，二是 outcome-only reward 无法区分正确答案背后的冗余搜索，导致准确率和工具成本冲突。标注搜索轨迹成本高，因此需要零标注、能动态调整难度且显式优化搜索效率的训练框架。

## 方法关键点
- **零标注任务生成**：从无标注参考问题出发，先生成实体答案（target entity），经实体识别和检索支持验证；再从答案节点反向构建 source-supported 多跳证据路径（轻量检索 + 句级共现），条件生成多跳问题；整个过程用程序化校验，不引入额外 LLM。
- **异构 proposer–solver 协同进化**：proposer 生成任务，solver 搜索回答；两角色可选用不同模型规模/家族。proposer 用 REINFORCE++ 优化，solver 用 GRPO 优化。
- **非对称奖励**：proposer 奖励 `R = 4*Acc*(1-Acc)`，鼓励中间难度任务；solver 奖励 `R = R_correct * (1 + λ*R_tool)`，其中 `R_tool` 是组内归一化的负搜索次数，只惩罚正确轨迹的冗余搜索。

## 关键结果
在 NQ、TriviaQA、PopQA、HotpotQA、2Wiki、MuSiQue、Bamboogle 共 7 个 benchmark 上，仅用 NQ question text 生成训练任务。Qwen2.5-7B-Base 平均 EM 从 21.8 提升到 38.2（+16.4），同时平均 queries 从 1.59 降到 1.16；用 3B/4B 异构 proposer 或跨家族 LLaMA 也能稳定提升。Search-R1 和 ZeroSearch 继续训练后分别 +4.9 和 +3.9。消融显示：中间难度奖励把 mixed question 比例从 12.81% 提升到 21.63%，all-wrong 从 83.95% 降到 43.80%；证据路径引导把 2-hop question 从 4.8% 提升到 37.7%，3-hop 从 0 到 7.6%。

**最值得记住**：不要固定题库，用轻量 proposer + 证据路径 + 中间难度过滤 + 组内工具归一化奖励，就能在零标注下同时提升搜索 Agent 的准确率和工具效率。
