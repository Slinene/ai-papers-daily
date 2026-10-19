---
title: 'DuoDiscover: Scaling Autonomous Discovery Beyond the Evaluation Bottleneck'
title_zh: DuoDiscover：联合发现优化目标与廉价评估器
authors:
- Shubham Agarwal
- Akshat Gupta
- Mike Heddes
- Dilara Soylu
- Rui Meng
- Patrick Tser Jern Kon
- Jiefeng Chen
- Mert Cemri
- Shu Liu
- Abe Gonzalez
affiliations:
- Google
- UC Berkeley
- Stanford University
arxiv_id: '2610.17184'
url: https://arxiv.org/abs/2610.17184
pdf_url: https://arxiv.org/pdf/2610.17184
published: '2026-10-11'
collected: '2026-10-19'
category: Agent
direction: 多 Agent 协同与多保真评估
tags:
- LLM
- Agent
- Multi-fidelity
- Evaluation
- Code Optimization
- Orchestrator
one_liner: Agent联合发现优化目标与廉价代理评估器，突破昂贵评估瓶颈
practical_value: '- 当线上 A/B、全量 benchmark 或 serving trace 评估很贵时，可以让每个 agent 为选定模块自动设计轻量
  proxy（如关键子集、小规模负载、成本模型），在 proxy 上秒级迭代；真实评估只用于确认候选，并用 Kendall τ 定期校验 proxy 排序保真度，漂移即失效。这种「昂贵评估只做确认、廉价评估负责搜索」的模式可直接用于推荐系统的离线评测、A/B
  前筛选和 LLM serving 性能调优。

  - 多 agent 编排采用 bottom-up：没有中心化任务分解，轻量 orchestrator 只管理昂贵的真实评估分配、终止停滞 agent、spawn（fresh/transfer/combine）和
  brief。这个模式适合把多 agent 优化引入广告出价、精排模型搜索等评估成本高的业务，不必重写搜索逻辑。

  - 用 Amdahl 定律做目标剪枝：agent 估计目标代码模块对总指标贡献占比 w，用 1/(1-w) 判断最大潜在收益，优先优化高上限目标。对应到推荐/广告系统，可以先估算某个环节（召回、粗排、特征计算、在线打分）对最终指标贡献上限，再决定是否投入
  agent 搜索。

  - 论文本身不解决推荐/检索建模问题，但可作为「LLM 驱动的系统优化 + 多保真评估」参考架构，尤其适合有昂贵端到端评估（全量 trace、仿真、大模型评测）的业务团队。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
LLM 加搜索在数学、算法和系统优化中有效，但真实工程中评估往往是瓶颈。一次完整 benchmark 或 serving trace 可能几十分钟到几小时，单个 agent 只能做几十次真实评估。仅优化搜索 harness 不够，因为不知道优化哪块代码，也没有便宜可靠的 proxy。

## 方法关键点
- **联合发现 target 与 yardstick**：每个 worker agent 选定一个代码区域作为 target，并自己写一个廉价代理评估器 yardstick（如只跑小规模负载、关键子集、成本模型）。agent 先估计 target 对真实分数的占比 w，再用 Amdahl 定律判断最大潜在收益 1/(1-w)。
- **双循环搜索**：快速内循环在 yardstick 上做秒级爬山，编辑-评分-保留/回滚；慢速外循环用真实评估确认收益。
- **保真测试**：orchestrator 用 Kendall τ 比较 yardstick 与真实评估的排序，只统计真实评估噪声可区分的 pairs，τ≥0.5 为 validated；每次真实评估后重测，漂移则 invalidated，agent 需重建或换目标。
- **bottom-up fleet**：orchestrator 轻量管理，终止停滞 agent、spawn 新 agent（fresh、transfer best、combine 多 agent 已验证修改）、brief 他人发现，不做中心化分解。

## 关键结果
- 仓库优化：SWE-fficiency 15.02×，超过 expert patch 6.90× 和 Claude Code 12.81×；FormulaCode 2.156×，比最强 agentic 基线高 21%。
- GPU/TPU kernels：SOL-Exec 平均 79.74% SOL，121/235 第一，212 前三；FA4 11.97%；JAXBench 4.62×；TPU-Inference 2.68×。
- 真实系统：vLLM 1.92×（Claude Code 1.07×），SQLite 1.38×，zstd 1.16×；CPU 预取器 DPC4 6.31% 增益，超过 ArchAgent v2 3.82% 和最佳人类设计 3.52%，且 16.7 天 vs >40 天。
- 效率：yardstick 比真实评估快 22×/53×，中位 Kendall τ 0.66/0.76，约 41%/45% 因漂移失效；在 SOL-Exec 上达到 Claude Code 最终分数仅需 2.8 小时、74% 更少 tokens、83% 更少真实评估。

## 最值得记住的一句话
昂贵的真实评估不该是搜索的默认评分器；让 agent 同时发现「优化什么」和「如何廉价评价」，再用排序保真测试防止 proxy 被 hacking。
