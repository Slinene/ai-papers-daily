---
title: 'OmniGameArena: A Unified UE5 Benchmark for VLM Game Agents with Improvement
  Dynamics'
title_zh: OmniGameArena：统一UE5游戏VLM Agent评测与改进动态曲线
authors:
- Mingxian Lin
- Shengju Qian
- Yuqi Liu
- Yi-Hua Huang
- Yiyu Wang
- Wei Huang
- Yitang Li
- Fan Zhang
- Zeyu Hu
- Lingting Zhu
affiliations:
- The University of Hong Kong
- LIGHTSPEED
- The Chinese University of Hong Kong
- Tsinghua University
arxiv_id: '2606.09826'
url: https://arxiv.org/abs/2606.09826
pdf_url: https://arxiv.org/pdf/2606.09826
published: '2026-06-07'
collected: '2026-06-09'
category: Agent
direction: VLM游戏Agent评测·自我改进曲线
tags:
- VLM Agent
- Game Benchmark
- Self-Improvement
- Reflection
- Multi-agent
- UE5
one_liner: 12款自建UE5游戏构建多模式Agent评测，IDC反射框架揭示自我改进轨迹与技能迁移规律
practical_value: '- **IDC的反射框架可直接复用到业务Agent自我优化**：自主工具调用（Explore/Diagnose/Validate/Distill）+
  有限工具面（只读、诊断、验证、写入），无需人工脚本，能自动从失败轨迹中提炼改进的skill prompt。电商推荐Agent（如选品策略、投放文案优化）可采用类似多轮反思循环，持续迭代策略自然语言描述。

  - **Best-skill rollback 防止灾难性遗忘**：当新一轮 skill 导致分数断崖下降时，自动回滚到最佳历史 skill 并继续反思，保证非单调改进环境中的稳定性。在线上策略自动演进中可借鉴，避免劣化版本持续生效。

  - **源任务改进 ≠ 迁移能力**的实验发现警示业务只盯着主任务指标：GPT-5.5在主任务上改进最小，但迁移到所有变体均正向；Opus 4.7主任务改进巨大，但迁移全负。电商多场景下应定期用
  held-out 场景检验策略的泛化性，避免陷入过拟合单一环境的“安全策略”。

  - **多智能体协同的评测设计**：PvP矩阵和Coop零和结果暴露了模型间的非传递优势（如Kim K2.5击败Claude但在Solo中弱），可为多Agent电商系统（如议价、库存博弈）的对手建模与角色分配提供评测范式。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：现有VLM游戏评测通常只报告单次冷启动分数，忽略Agent在重复交互中自我改进的动态过程，且几乎只覆盖单人模式，缺乏对对抗（PvP）和合作（Coop）场景的统一评测。评测环境多复用已发行游戏，面临预训练数据泄露风险。

**方法关键点**：
- 全新构建12款基于UE5的游戏，覆盖Solo（7）、PvP（3）、Coop（2），统一键鼠/手柄接口，支持商业VLM、开源VLM和专用游戏策略三类Agent。
- 提出改进动态曲线（IDC）框架：外层循环由经验采集（玩K局）、反射（reflector LLM仅通过工具调用自主分析轨迹、诊断失败、验证新skill、蒸馏知识）和持久化（笔记、已验证skill、回滚缓存）组成。
- 反射器通过四个自主阶段运行：Explore（选择性检查轨迹）、Diagnose（提交失败模式）、Validate（独立LLM judge裁决技能是否记忆地图或矛盾）、Distill（最终化skill并写笔记）。
- Best-skill rollback：当某轮分数低于最佳历史的50%时，自动回滚到下轮起点，避免 skill 崩溃。

**关键实验与结果**：
- 冷启动排行榜：12个agent在12款游戏中均无一家独霸，GPT-5.5在4个Solo游戏领跑，Claude Opus 4.6在CueChase领先显著（0.840），开源VLM和专用策略几乎全面崩溃。
- PvP中MidlineClash呈现非传递性：Kimi K2.5 1:0完胜Claude Opus 4.6，尽管后者Solo更强。Coop任务最高完成度仅0.368，揭示协调仍是巨大短板。
- IDC实验：4个顶尖agent在LastStand实现+130%~+437%的提升，但峰值多在中间轮次而非最终轮。技能迁移实验显示：**源任务增益量与迁移能力无关**：GPT-5.5在LastStand原任务增益最小（+130%）但三个变体全部正向迁移；Opus 4.7原任务增益+201%却在所有变体上负迁移，因为其技能收敛到“不动”的静态策略，不适应变体。

**最值得记住的一句话**：IDC揭示了单次评测无法观测的自我改进轨迹与迁移特性，最优改进策略可能恰好矛盾于泛化能力。
