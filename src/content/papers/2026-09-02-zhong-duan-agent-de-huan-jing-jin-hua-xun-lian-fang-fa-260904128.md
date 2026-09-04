---
title: Environment Evolution for Terminal Agents
title_zh: 终端 Agent 的环境进化训练方法
authors:
- Zhiyuan Fan
- Tinghao Yu
- Yuanjun Cai
- Jiang Zhou
- Jiangtao Guan
- Jincheng Liu
- Yun Yang
- Dingxin Hu
- Zhuo Han
- Xing Wu
affiliations:
- Hunyuan Team, Tencent
arxiv_id: '2609.04128'
url: https://arxiv.org/abs/2609.04128
pdf_url: https://arxiv.org/pdf/2609.04128
published: '2026-09-02'
collected: '2026-09-04'
category: Agent
direction: 终端 Agent RL · 离线环境课程
tags:
- Environment Evolution
- RL Training
- Terminal Agents
- Multi-Agent
- Curriculum Learning
one_liner: 提出离线环境进化，沿多轮目标派生的三个难度方向逐步提升终端环境难度，并通过多 Agent 回路实现，提升终端 Agent RL 效果。
practical_value: '- 在电商/推荐 Agent 训练中，可将“用户任务/交互环境”当作可进化对象：把多轮任务目标显式展开，提取难度轴（如约束数量、工具噪声、状态分支），离线用
  LLM 多 Agent 生成逐渐变难的任务集，不用每次等在线 rollout，降低数据成本。

  - 用多 Agent 回路工程化合成环境：一个 Agent 负责提出 harder case，另一个验证可解性与难度，再一个做标注/清理，保证训练集中困难样本比例与模型能力匹配，可复用到导购、搜索、客服
  Agent 的场景生成。

  - 训练调度用“分代课程”：将进化后的环境按 generation 分块，训练时按模型 checkpoint 表现逐步解锁下一代，避免一次性给过难/过易环境；对应推荐
  Agent 的 RL 训练可做 curriculum。

  - 若做用户模拟器/环境生成，优先加入 off-policy 进化：不再依赖当前策略轨迹，能从历史或弱模型数据产生持续学习信号，适合业务环境噪声大、策略迭代快的场景。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：训练终端 Agent 需要大量可交互、可验证环境；静态/从头合成环境随模型变强而失去挑战，现有 co-evolution 依赖 on-policy rollouts 限制泛化与持续学习信号。

方法关键点：提出 environment evolution，离线增量提升环境难度，并按代调度训练；从多轮学习目标推导出三个影响难度的方向，通过 loop-engineered multi-agent harness 实现。引入 frontier models 定量验证环境难度。

结果：Hy4 preview、Claude Opus 5、GPT-5.6 Sol rollout 显示环境难度持续提升；在 Qwen3.6-27B 和 Qwen3.6-35B-A3B 上做 long-horizon RL，Terminal-Bench 2.1 分别提升 14.4 和 18.0 个百分点。
