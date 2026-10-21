---
title: Progress-Aware Distillation for Mitigating Stagnation in Small Language Model
  Agents
title_zh: 用于缓解小语言模型智能体停滞的进展感知蒸馏
authors:
- Yuanpu Cao
- Saket Sathe
- Hanyu Wang
- Ziyi Yin
- Fenglong Ma
- Jinghui Chen
affiliations:
- The Pennsylvania State University
- Microsoft CoreAI
arxiv_id: '2610.19439'
url: https://arxiv.org/abs/2610.19439
pdf_url: https://arxiv.org/pdf/2610.19439
published: '2026-10-16'
collected: '2026-10-21'
category: Agent
direction: Agent 蒸馏 · 停滞抑制
tags:
- Agent Distillation
- Progress Stagnation
- SLM
- LoRA
- Preference Optimization
- CodeAct
one_liner: 提出 ProD，在蒸馏中显式惩罚学生轨迹停滞，提高小模型 Agent 成功率与推理效率
practical_value: '- 在电商搜索/客服/投放 Agent 的 SLM 蒸馏中，可直接引入 stagnation score：对最近 k 轮 action/query
  做 ROUGE-L 或 embedding cosine 相似度监控，识别反复调同一类 API、改写同一 query；离线训练时把这些信号做成动态 margin
  的偏好 loss。

  - 推荐用 ProD 式混合目标：L_PRO + λ L_SFT，λ=1；adaptive margin 采用 c0*(α*stagnation_gap + (1-α)*ans_mismatch)，α=0.5
  是稳健默认。可在现有 LoRA SFT 蒸馏后做 1-2 轮迭代，生成 on-policy 轨迹再更新。

  - 推理阶段 repetition penalty 或缩短教师轨迹不能真正解决停滞，需要训练阶段对 student 自身行为加约束；这样做能同时降低平均轮数约
  12%、token 约 21%，对生产时延和成本有直接收益。

  - 业务环境无法频繁调用 LLM-as-judge 时，用 lexical ROUGE-L 已足够作为停滞信号，和 semantic/judge 相关性 >0.92；在代码/API
  action 场景可优先使用。'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
LLM Agent 能力强但 token 消耗和推理延迟高，业界用 SFT 把 GPT-4.1 等教师轨迹蒸馏到小模型。蒸馏后的 SLM Agent 在长 Reason–Act–Observe 轨迹中容易出现 progress stagnation：反复执行相似失败策略，陷入无产出循环，且模型越小越严重。论文系统分析了这一现象，并量化 stagnation score。

### 方法关键点
- 定义 turn-level stagnation score：lexical ROUGE-L / semantic cosine / LLM-as-judge，比较当前 thought+action 与历史最近似内容的相似度。
- ProD 目标：在 SFT student 基础上，每次迭代用当前 student 生成轨迹，通过 pairwise preference loss 提升教师轨迹概率、压低学生轨迹概率；margin 由 student-teacher stagnation gap + answer correctness 动态决定。
- 保留 SFT loss 作为 anchor 防止 likelihood displacement；采用迭代式 on-policy 优化。
- 在 CodeAct 框架下，用 LoRA 微调，β=2.5，α=0.5，c0 按任务选择，λ=1。

### 关键结果
- 8 个 SLM（0.6B–8B）在 MATH/HotpotQA 及 OOD Omni-MATH/2WikiMultiHopQA 上，ProD 平均 ID 精度比 SFT 提高 4.7%，OOD 提高 4.9%，部分模型接近教师水平。
- ProD 显著降低三种 stagnation 指标；平均交互轮数下降 11.6%，token 消耗下降 20.7%。
- 消融显示 adaptive margin 和 SFT anchor 都重要；decoding-level repetition penalty 和 concise teacher data 均不如 ProD。

### 一句话
要让小模型 Agent 在长交互中不“鬼打墙”，只克隆教师成功轨迹不够，必须在训练时用学生自身轨迹的停滞程度动态做偏好惩罚。
