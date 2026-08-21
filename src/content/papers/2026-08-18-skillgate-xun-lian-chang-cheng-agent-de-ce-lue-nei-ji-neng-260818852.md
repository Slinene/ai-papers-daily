---
title: 'SkillGate: Training In-Policy Skill Selection in Long-Horizon Agents'
title_zh: SkillGate：训练长程 Agent 的策略内技能选择
authors:
- Qingyao Li
- Wenxiang Jiao
- Shuai Shao
- Kangning Zhang
- Yuan Lu
- Yi Guo
- Weiwen Liu
- Weinan Zhang
- Yong Yu
affiliations:
- Shanghai Jiao Tong University
- Xiaohongshu Inc.
arxiv_id: '2608.18852'
url: https://arxiv.org/abs/2608.18852
pdf_url: https://arxiv.org/pdf/2608.18852
published: '2026-08-18'
collected: '2026-08-21'
category: Agent
direction: Agent 技能选择 · 信用分配
tags:
- Agent
- Skill Selection
- Credit Assignment
- GRPO
- Reinforcement Learning
- Long-Horizon
one_liner: 识别选择器信用饿死问题，分离执行与选择 token 信用通道，将 9B 策略成功率从 40.8% 提升至 53.2%
practical_value: '- 在电商搜索/Agent 场景中，当 LLM 在长对话里选择 query 改写、营销话术或工具时，不要把最终成交 reward
  直接广播到全部 token；应将“选择 token”（如 query 或 skill 名）与“执行 token”的 loss mask 分离，避免下游执行失败反向惩罚正确选择（对应论文中
  selector credit starvation）。

  - 对选择动作构造局部信用：仅当轨迹中唯一选择为 oracle（正确 query/skill）时给 +1，否则给 0，并在同一 prompt group 的候选动作上做
  group centering，去掉标准差归一化；这比给整条轨迹加分、或只奖励第一次正确选择更有效（可参考消融表 2）。

  - 工程上可用 token span 标注 identity 区域，并在 mask 构建/分片/loss 三处断言两个 credit channel 的 support
  不相交；对 selector channel 做长度无关重加权，使每个 credited action 的总权重恒为 N/M，避免长轨迹稀释关键决策。

  - 业务上不要过度依赖外部 router/reranker：论文显示路由准确不等于下游成功，训练策略内部选择能力可同时降低交互成本（读更少技能、更少 turn）和上下文成本（按需加载
  vs 预加载 k 个候选）。'
score: 8
source: huggingface-daily
depth: full_pdf
---

动机：
长程 agent 中，技能以 `SKILL.md` 形式按需读取，策略在 episode 中根据候选名和一行描述选择读哪个 skill。已有 outcome-only RL 训练该选择会失败，因为选择 token 只占轨迹极小比例，且下游执行失败会给正确选择带来负 advantage（`selector credit starvation`）。审计 12,800 条 on-policy 轨迹发现：选择 token 的中位 loss 权重仅 0.14%，且随轨迹长度稀释约 7 倍；大约 40% 的正确读取继承了负 advantage，最长轨迹上超过 50%；但正确读取仍值 +11.2pp 成功率。

方法关键点：
- 将轨迹 token support 划分为两个不相交 credit 通道：执行 token 接收 group-normalized outcome advantage，但整个 read call（包括 skill 名字）从 task mask 中删除；选择 token 接收 action-local advantage，效用定义为轨迹中唯一读取且为 oracle 时=1，否则=0，并在同一 prompt group 的 read actions 上 center，不做标准差归一化。
- 每个通道总 token 权重均归一为 N，使选择决策权重不随轨迹长度变化；selector 系数 λ=0.20，目标为 clipped GRPO surrogate + KL 惩罚。
- 实现上通过 token span 标注 identity 区域，并在 mask 构造、分片、loss 三处断言 support 不相交。

关键实验：
在五个 agentic benchmarks（Claw-Eval, SkillsBench, SETA, SWE, Terminal-Bench 2.0）和 16 候选混合 slate 下，Qwen3.5-9B 从 SFT 的 40.8% 提升到 SkillGate 的 53.2%，显著超过 outcome-only RL 的 47.0%，并超过 27B 参考模型和部分 397B 模型。SkillGate 将 misleading 曝光从 69.6% 降到 21.8%，oracle 读取从 54.3% 升到 83.9%，且读 skill 更少、交互成本更低。消融显示只有将 credit 落在 identity tokens 且要求 single-read 才能转化为任务成功；外部 router 或 oracle-only 注入也验证了内部选择训练的价值。

最值得记住的一句话：当一条轨迹混合不同性质的决策时，把 token support 按决策类型分区，分别给局部 credit，是比统一广播 advantage 更便宜且可验证的替代方案。
