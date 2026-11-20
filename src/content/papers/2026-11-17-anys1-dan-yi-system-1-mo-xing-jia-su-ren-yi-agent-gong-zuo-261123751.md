---
title: 'Thinking Fast, Anywhere: One System-1 for the Decision Points of Any Agent
  Workflow'
title_zh: AnyS1：单一 System-1 模型加速任意 Agent 工作流决策点
authors:
- Rui Li
- Liyang He
- Zheng Zhang
- Zhenya Huang
- Qi Liu
affiliations:
- University of Science and Technology of China
- Nanyang Technological University
arxiv_id: '2611.23751'
url: https://arxiv.org/abs/2611.23751
pdf_url: https://arxiv.org/pdf/2611.23751
published: '2026-11-17'
collected: '2026-11-20'
category: Agent
direction: Agent 双系统决策加速与成本优化
tags:
- System-1
- Dual-system agent
- Agent skills
- Calibration
- Pointer model
- Cost reduction
one_liner: 从 procedural skills 自动挖掘决策点，训练 4B 校准 pointer System-1，降 Agent 成本 75–91%、模型时间
  63–92%
practical_value: '- 电商/客服/搜索推荐 Agent 工作流中，把「意图分类、选项选择、相关性/合规判断」这类可枚举节点从 LLM 中剥离，用
  4B 级 pointer/typed decision 模型一次前向打分，并设置置信度阈值（如 τ≈0.918 或 per-workflow 拟合）回落 System-2。在
  SOP 类流程上可减少 75–91% 单 episode 成本，单决策延迟从 1.5–1.8s 降到 20–30ms。

  - 训练数据别用 LLM 编造的 summary state，要在真实执行环境收集 fragment 化 tool outputs 和用户消息；用容器执行 synthesized
  tasks 或线上日志 replay，保证 state 分布与线上一致。实验显示真实容器状态比 LLM 合成状态在 held-out 决策上高 +18.8 点。

  - 标注时用 order-reversal 双老师共识过滤标签噪声，训练时用 label smoothing（ε=0.1）防止指针模型置信度饱和，这直接决定 deferral
  阈值能否跨域零样本迁移；否则硬标签 CE 会让 τ 膨胀到 0.998，gated agreement 下降。

  - 架构上保留 D/G/E 三类节点：deterministic 步骤代码化、open generation 仍走 LLM、只把 enumerable 决策交给
  System-1。不要整体替换 Agent 大模型，投资回报最高。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：主流 LLM Agent 每步都调用大模型（System-2），成本与延迟随轨迹增长，但大量中间步骤只是从少量已知候选中做选择。已有 dual-system 方法依赖手工为每个 workflow 定义决策点，难以泛化。AnyS1 观察到 procedural skills（SKILL.md）天然写明分支与候选，于是把 skills 当作通用决策点来源。

**方法关键点**：
- 离线从 1,072 个 public skills 用 LLM 三遍抽取 D/E/G 决策点，要求 verbatim quote，合并支撑度 ≥2 的 E 节点；为每个 skill 合成多阶段容器任务，用 OpenHands 执行得到真实状态，双老师 order-reversal 标注共识，构建 Any-DP：17,865 决策点、25,986 状态，教师一致率 89.2%。
- System-1 为 Qwen3.5-4B-Base + LoRA + pointer head，head 对候选选项做 position-free 双向注意力后与 ⟨dec⟩ 匹配输出 softmax；训练用 label smoothing ε=0.1，显式防止置信度饱和。
- 运行时把 E 节点交给 System-1，置信度 c(x)=max pf 低于阈值则回落 System-2；AnyS1warm 用 50 条未标注 workflow 轨迹拟合 τ，AnyS1cold 直接迁移全局阈值 τ=0.918。

**关键实验**：
- 在 SOPBench、ALFWorld、WebShop 三个 unseen benchmark，System-2 分别为 DeepSeek-V4.1-Flash 与 GPT-6 Sol，相对未编译 agent，AnyS1warm 降 episode 成本 75–91%、模型调用时间 63–92%，成功/Pass/Score 不降（平均 +0.5 pt）；AnyS1cold 降 87% 成本且几乎不打折扣。
- 消融：无 gate 的 All-S1 在 ALFWorld 从 96.3% 崩到 40.3%；真实容器状态比 LLM 合成状态 held-out dev 高 +18.8 点；label smoothing 保持 ECE 0.094 且 gated agreement 97.7%。

**值得记住的一句话**：把 skills 中的 if/else 变成可训练决策点，用真实执行状态 + 标签平滑 + 置信度门控，就能让一个 4B System-1 可靠地接管 Agent 大部分有界决策。
