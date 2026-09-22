---
title: 'RRSI: Regularized Recursive Self-Improvement of Agent Harnesses'
title_zh: RRSI：Agent 外壳的正则化递归自改进
authors:
- Peng Xia
- Rujun Han
- Zifeng Wang
- Yanfei Chen
- Yufan Zhang
- Yoonho Lee
- Chengsong Huang
- Han Yu
- Zhongying CuiZhu
- Yifei Ming
affiliations:
- Google Cloud AI Research
- UNC-Chapel Hill
- Stanford University
- Washington University in St. Louis
arxiv_id: '2609.24972'
url: https://arxiv.org/abs/2609.24972
pdf_url: https://arxiv.org/pdf/2609.24972
published: '2026-09-20'
collected: '2026-09-22'
category: Agent
direction: Agent 自改进正则化 · harness 进化
tags:
- Recursive Self-Improvement
- Agent Harness
- Regularization
- Overfitting
- LLM Agents
- Generalization
one_liner: 用 proposal 与 selection 两侧正则化约束 Agent harness 自改进，缓解在有限 evolve set 上的过拟合
practical_value: '- 在电商搜索/推荐 Agent 或购物助手做自动化 prompt、tool description、context 管理的 A/B
  调优时，很容易在内部小评测集上过拟合。可复用 RRSI 的 leakage screening：评估前先用 critic 过滤掉显式包含 task name、商品名、类目特定逻辑或实体值的候选，防止这类候选靠局部泄漏获得高
  evolve score 进入后续搜索。

  - 引入 noise band 接受 floor：先在固定 base harness 上重复评估估计噪声 δ，候选分数必须 ≥ S*-δ 才允许替换 incumbent。这能避免在搜索/推荐
  Agent 的策略迭代中，把随机噪声冠军当成稳定改进永久写入系统。

  - cost-aware acceptance 对生产很有用：任何候选若增加 policy tokens（例如更长的 few-shot 示例、更多 tool schema
  字段、额外 context 读取），必须用 ΔC ≤ β0 + β1 ΔS 证明收益。可以直接迁移到线上成本约束的推荐 Agent 或 LLM 链路，避免演进结果越来越贵但得分不涨。

  - 结构化探索和 evidence-aware history 可以复用到 query 改写策略、召回 prompt、排序 Agent workflow 的自动搜索：记录每轮修改的组件、假设和验证结果，停滞时优先探索从未改过的组件（如
  control flow / context 管理而非继续改 prompt）。另外可加一个跨模型验证步骤：搜索得到的 harness 若不随 backbone
  能力消失，才更像可复用机制而非策略专属补丁。'
score: 9
source: huggingface-daily
depth: full_pdf
---

## 动机
LLM Agent 的能力很大程度上来自包围 frozen backbone 的 harness：prompt、control flow、tool interface、memory 和 context management。近期方法用 LLM 自动迭代地提议和选择 harness 组件级修改，这形成了一种 agent-system level 的 recursive self-improvement (RSI)。但问题在于，这种演化反复复用有限的 evolve set 作为反馈，容易产生 adaptive overfitting：evolve set 上分数大幅提升，但 held-out 或 OOD benchmark 上的提升缩小甚至消失。论文将该问题拆成三类：benchmark-specific fitting、noise chasing、complexity accumulation。

## 方法关键点
RRSI 不限制 harness 可编辑范围，而是正则化搜索轨迹，分 proposal 和 selection 两侧：

- Proposal 侧正则化：
  - L0-style annealed update sparsity：单轮候选可打包的可独立归因 edit 数预算按余弦退火下降，早期允许较大修改，后期逼出稀疏、可归因的 edit。
  - Evidence-aware credit assignment：记录历史上每个候选修改的组件、假设、diff、得分与成本变化，后续 proposer 不能反复测试已被证伪的假设。
  - Structured exploration：当搜索在噪声带内停滞时，强制分配一部分预算给尚未探索过的 harness 组件，避免反复改写 prompt 而忽略机制性结构。

- Selection 侧正则化：
  - Leakage screening：正式评估前，critic 读 diff 拒绝包含任务名、实体名、任务特定值/答案或 inert machinery 的候选。
  - Noise-adjusted acceptance：用 base harness 重复评估估计噪声带 δ，候选须满足 Ŝ(H′) ≥ S★ - δ，防止噪声冠军被永久化。
  - Ridge/L2-style complexity-aware acceptance：候选的成本增长必须由分数收益证明，ΔC ≤ β0 + β1 ΔS，抑制无谓 token 增长。
  - Lasso/L1-style structural pruning：追踪窗口内无正贡献的 harness 组件，提交给 proposer 作为删除目标，保持结构稀疏。

## 关键实验与结果
在 coding、agentic workspace、engineering design 三个域共 8 个 benchmark 上评估：Terminal-Bench 2.1 演化，SWE-bench Verified 做 OOD；Harvey LAB 做 evolve 和 ID held-out，JobBench/GDPval/APEX-Agents 做 OOD；EngDesign 演化，Frontier-Eng 做 OOD。对比 H0 和 Meta-Harness、AHE、TTHE、HarnessX。

RRSI 在 evolve split 上最多 +14.1 点（Gemini 3.5 Flash 在 Terminal-Bench），但更关键的是 6 个 held-out splits 全部提升：SWE-bench Verified +1.8，Harvey LAB ID held-out +2.3，JobBench +4.7，GDPval +3.5，APEX-Agents +3.7，Frontier-Eng +4.3 Medal 点（相对 +24.3%）。在 agentic workspace 上，RRSI 的 OOD 平均分 43.6，显著高于未正则化演化的 40.3，同时 policy tokens 从 3.80m 降至 2.42m，约降 36%。跨模型实验中，用 Gemini 3.5 Flash 搜索出的 harness 在未见过的 Gemini 3.1 Flash Lite 上仍带来 +3.4 点提升，说明学到的是可迁移机制而非特定策略补丁。

## 最值得记住的一句话
不要把有限 evolve set 上的贪心优化当成 Agent 自改进本身；只有用正则化约束 proposal 与 selection 的搜索轨迹，才能把噪声反馈转化成可跨任务、跨模型迁移的 harness 机制。
