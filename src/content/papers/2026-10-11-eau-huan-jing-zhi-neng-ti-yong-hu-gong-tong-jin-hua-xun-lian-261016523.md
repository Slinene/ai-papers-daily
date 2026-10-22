---
title: 'EAU: Environment-Agent-User Co-evolution for Training User-Centric Agents'
title_zh: EAU：环境-智能体-用户共同进化训练用户中心智能体
authors:
- Min Cai
- Dan Zhang
- Gao Xing
- Libin Ma
- Zhaohui Xu
- Xi Ye
affiliations:
- University of Alberta
- National University of Singapore
- Kuaishou Technology
- Alberta Machine Intelligence Institute (Amii)
arxiv_id: '2610.16523'
url: https://arxiv.org/abs/2610.16523
pdf_url: https://arxiv.org/pdf/2610.16523
published: '2026-10-11'
collected: '2026-10-22'
category: Training
direction: 用户中心 Agent RL 训练环境协同进化
tags:
- Meta-Agent
- RL
- User Simulator
- Environment Co-evolution
- Symbolic User
- LLM Agent
one_liner: 提出 EAU 元代理框架，在 RL 训练中在线诊断并修改用户模拟器、环境奖励与超参，实现三者协同进化
practical_value: '- 用户模拟器不稳定是对话式推荐/客服 RL 训练的常见痛点：可借鉴 symbolic user 规则化控制信息揭示，与 LLM
  模拟器按比例混合，获得稳定训练信号同时保留自然交互多样性。

  - 训练中让 meta-agent（或自动脚本）监控 rollout 日志、检测 deadlock/信息泄露/reward hacking，并热修复奖励规则或环境约束，避免重启；工程上可将
  user simulator、reward scale、max steps 等做成可编辑配置，支持在线调整。

  - PPO 训练对话 agent 时，critic 和 GAE 只计算 action tokens 的 advantage，防止 observation 文本稀释学习信号；这一实现细节可直接复用于多轮对话策略优化。

  - 跨 run 经验池：把每次训练发现的修改和效果记录下来供后续 run 复用，可加速迭代，适合业务中反复训练 agent 的场景。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
用户中心 Agent 需要多轮交互，但学习信号受用户模拟器和环境共同影响。LLM 模拟器可能随机、不一致、泄露信息；环境可能工具不可靠、验证器错误；且两者固定不变，随策略提升不再提供有效交互。以往方法仅改进 reward shaping 或 denser supervision，未触及信号源头。

## 方法关键点
- **EAU 元代理**：监控 rollout 轨迹、工具调用、奖励与训练统计，诊断失败来源，针对性修改用户模拟器规则、环境奖励、RL 超参。
- **Symbolic user + LLM user 混合**：引入确定性规则用户模拟器，控制信息揭示；与 LLM 模拟器按 ϵ 混合，兼顾可控性与自然性。
- **环境演化**：在稀疏奖励中注入中间奖励规则（如 first_tool、first_uid），修改 episode 长度等约束。
- **Agent 训练**：固定 PPO，使用 critic + GAE；advantage 只在 action tokens 上计算，避免 observation 文本稀释。
- **在线干预**：修改经完整性门控验证后热切换，支持 intra-run 与 inter-run；经验池跨 run 累积；元代理用 Claude Code/Codex 实现。

## 关键结果
在 UserGym、ColBench、τ2-bench 三个基准上，Qwen3-4B 和 Qwen2.5-7B-Instruct 两个骨干，整体得分较最强基线 InfoPO 提升 14.7-15.0%；ColBench Pass 达 0.685（+23.9%），Succ. 达 0.600（+36.7%）；τ2-bench 平均得分 21.5 vs PPO 18.5。消融显示 symbolic+LLM 混合优于单一模拟器，intra-run 干预带来额外收益。

## 最值得记住的一句话
把训练系统本身（用户模拟器、环境奖励、RL 超参）当作可优化的变量，让元代理在线诊断并修改它们，能大幅提升多轮用户中心 Agent 的 RL 训练效果。
