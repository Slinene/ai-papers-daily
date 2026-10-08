---
title: 'SkillForge: Co-Evolving Skills and Agents via Dynamic Skill Lifecycles'
title_zh: SkillForge：以动态技能生命周期协同进化技能与智能体
authors:
- Yuyao Ge
- Yiwei Wang
- Yuchen He
- Baolong Bi
- Lingrui Mei
- Jiayu Yao
- Lizhe Chen
- Shenghua Liu
affiliations:
- Institute of Computing Technology, Chinese Academy of Sciences
- University of California, Merced
- Tsinghua University
arxiv_id: '2610.09832'
url: https://arxiv.org/abs/2610.09832
pdf_url: https://arxiv.org/pdf/2610.09832
published: '2026-10-06'
collected: '2026-10-08'
category: Agent
direction: Agent 技能库生命周期管理
tags:
- Skill Library
- Agentic RL
- GRPO
- Memory-Augmented
- Lifecycle
- LLM Mutation
one_liner: 用 fitness 驱动的技能生命周期和 LLM 变异，让技能库与 RL 策略协同进化，避免低效技能污染上下文
practical_value: '- 技能/工具/规则库不能 append-only：在电商 Agent 或导购 SOP 库里，为每个技能维护 usage 与 success
  计数，计算 fitness，并设置预退休与运行时退休机制，主动淘汰过期或低效条目，避免上下文被污染。

  - 生命周期状态机可直接落地：用 trial/active/stable/retired 四态加 hysteresis（stable 先 demote 才能 retire），既保护已稳定技能不被瞬时波动误杀，又能快速淘汰长尾低质技能；generation-aware
  保护期可迁移到新上线的工具或规则。

  - LLM 变异可用于自动优化 prompt/SOP：按 1−fitness 加权选择低效技能作为 parent，结合失败轨迹让教师模型改写生成 trial 子技能，再通过真实反馈决定去留；这可用于电商导购话术、搜索
  query 生成策略的持续自动迭代。

  - 预退休阶段值得借鉴：在把外部知识、规则或技能注入线上 RL 或 SFT 数据前，先用 base model rollout 做一轮离线 fitness 评估，过滤掉低质量种子，能显著降低训练噪声，提升最终性能。'
score: 8
source: huggingface-daily
depth: full_pdf
---

动机：把技能库作为 LLM agent 的长期记忆，检索注入上下文能提升复杂任务成功率。但现有 skill-augmented RL 普遍把技能库当成 append-only，随着策略提升，过时甚至有害的技能持续累积，导致上下文噪声与 delayed obsolescence（曾 stable 的技能 fitness 后来跌破退休阈值）。因此需要把技能库从被动累积改为主动“锻造”。

方法关键点：
- 三阶段：先用 base model rollout 评估种子技能的 proto-fitness，低于 δ_pre=0.3 且 usage≥3 的技能预退役；再用剔除退役技能后的成功轨迹做 SFT，得到 π_sft 作为 RL 初始化和参考策略；最后进入 GRPO RL，每 10 步执行一次 forging cycle。
- 技能生命周期：每个技能维护 usage/success，fitness=success/usage（不足 5 次用 0.5 默认）。状态在 trial→active→stable→retired 间迁移，阈值 δ_retire=0.4、δ_demote=0.5、δ_stable=0.7；stable 需先 demote 到 active 才能退休，generation-0 技能有更高 usage 保护。
- LLM 变异：fitness 落在 [0.4,0.7] 的 active 技能进入变异池，按 1−fitness 加权选 parent，教师模型结合失败轨迹生成 child，child 以 trial 状态进入库；每轮最多 5 个变异、3 个退休，并按 Smax 裁剪。

关键结果：在 ALFWorld、WebShop、Search-Augmented QA 分别达到 92.4%、78.4%、48.7% 的 success/micro-accuracy；相对最强 baseline SkillRL，WebShop 相对提升 7.8%，ALFWorld 相对提升 2.8%。Ablation 显示去掉整个 lifecycle 在 WebShop 掉 7.4%，其中 pre-retirement 贡献最大；库从 121 技能压缩到 95 后性能反升，说明质量而非规模驱动收益。SKILLFURNACE 数据集共 5,852 条记录，退休事件统计显示 57.2% 的技能曾达 stable 后才退役，平均 peak fitness 0.667，实证了 delayed obsolescence。

**最值得记住的一句话**：技能库也应像策略一样被持续训练与治理，用 fitness 生命周期和 LLM 改写淘汰过时技能，比一味扩库更有效。
