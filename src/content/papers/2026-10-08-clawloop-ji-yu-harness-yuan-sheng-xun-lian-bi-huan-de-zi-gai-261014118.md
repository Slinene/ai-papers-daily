---
title: 'ClawLoop: Self-Improving Agents via Harness-Native Training Loop'
title_zh: ClawLoop：基于 Harness 原生训练闭环的自改进 Agent 框架
authors:
- Hansi Yang
- Linji Hao
- Hongyan Hao
- An Wang
- Han Wu
- Qi Gu
- Xunliang Cai
affiliations:
- Meituan
- Peking University
arxiv_id: '2610.14118'
url: https://arxiv.org/abs/2610.14118
pdf_url: https://arxiv.org/pdf/2610.14118
published: '2026-10-08'
collected: '2026-10-14'
category: Training
direction: 自改进 Agent 训练闭环 · Harness 原生任务合成
tags:
- self-improving agents
- harness-native training
- task synthesis
- GRPO
- SFT
- agent training
one_liner: 无外部教师模型下，通过任务合成-训练-诊断闭环实现 harness agent 自改进，并迁移到小模型
practical_value: '- 任务合成用可执行 generator 直接产出环境、答案 key 和 answer contract，避免让 LLM 直接生成答案；电商/搜索场景构造模拟任务（订单聚合、库存核对、报表生成）时可借鉴“生成代码而非标签”，把隐含业务规则写成
  skill/contract 文件，确保 reward 可验证且不泄漏。

  - SFT 阶段只对 agent action token 计算 loss，mask 掉环境观察 token；多轮 agent 训练中商品详情、日志、工具输出往往很长，不做
  mask 会主导梯度，这个 trick 可直接复用。

  - RL 用 GRPO 时引入 admission band [N_l, N_h] 只保留当前策略通过率居中的任务，太难或太易都不产生 advantage；推荐/对话策略的自我博弈或课程学习可以按通过率过滤样本，动态保持训练信号密度。

  - 诊断反馈闭环：让模型自己总结失败轨迹并聚合 failure patterns，驱动下一轮任务生成；可用于 query 改写、Agent 规划失败归因，自动生成针对性补强数据，不依赖人工分析。'
score: 9
source: huggingface-daily
depth: full_pdf
---

**动机**：LLM-based harness agent 能直接操作文件系统和 shell，任务复杂度远超固定工具调用，但现有后训练数据合成大多一次性完成且依赖外部强教师模型，存在能力上限，无法自我改进。ClawLoop 利用 harness 本身的可执行性与可验证性，实现无外部教师的自改进闭环。

**方法关键点**：
- 任务定义为 τ=⟨p, s0, A, F, Vτ⟩，所有阶段在同一 harness 环境运行，保证训练与推理分布一致。
- 三阶段闭环：任务合成与筛选、训练、诊断与反馈。
- 任务合成两条互补路径：capability-driven 从目标能力出发，LLM 写可执行 generator，执行后得到 s0、答案 key y 和 answer contract C，答案由代码计算而非模型生成；domain-grounded 从具体领域工具和图谱出发，提取 tripartite graph 聚类 skills，再构造抽象 task graph 并接地到领域，避免泄漏。
- 难度增长通过 multi-hop 和 dirtiness draw 控制，验证分 agent-free（oracle 通过、泄漏审计）和 agent-based（N=8 次 rollout，保留通过数在 [1,5] 的任务）。
- 训练采用自蒸馏 SFT（mask 观察 token）+ GRPO（group advantage），复用同一批 rollouts 做验证、SFT 和 RL。
- 诊断：对 held-out 失败轨迹做 structured summary，聚合出反复出现的 failure patterns，指导下一轮任务合成。

**关键实验**：以 Qwen3.6-27B 为 loop 模型，K=3 迭代，每轮合成 1024 个任务。在 SkillsBench、Claw-Eval-Live、ClawGym-Bench 上，ClawLoop 分别达到 57.2、76.9、68.4，超过 base（46.3、69.3、67.6）和 ClawGym（52.6、74.6、61.9）。小模型 Qwen3.5-4B/9B 用 ClawLoop 数据 RL 后也超过 ClawGym 使用更强教师模型的效果。消融显示两条合成路径和难度增长均有贡献，性能在 K=3 附近饱和。

**最值得记住的一句话**：可执行环境 + 可验证任务 + 失败诊断反馈，足以让 agent 在没有外部教师的情况下持续自改进；任务难度应通过当前策略的通过率动态筛选。
