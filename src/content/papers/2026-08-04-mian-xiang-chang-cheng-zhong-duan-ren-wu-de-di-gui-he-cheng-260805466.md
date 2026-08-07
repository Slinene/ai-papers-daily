---
title: Recursive Synthesis for Long-Horizon Terminal Tasks
title_zh: 面向长程终端任务的递归合成框架
authors:
- Zhongzhi Li
- Yucheng Shi
- Zongxia Li
- Ruhan Wang
- Anhao Li
- Zixun Huang
- Junyao Yang
- Lei Ke
- Ninghao Liu
- Haitao Mi
affiliations:
- Tencent HY LLM Frontier
- University of Georgia
- University of Maryland, College Park
- University of Pennsylvania
- Indiana University
arxiv_id: '2608.05466'
url: https://arxiv.org/abs/2608.05466
pdf_url: https://arxiv.org/pdf/2608.05466
published: '2026-08-04'
collected: '2026-08-07'
category: Agent
direction: 递归合成 · 终端Agent训练任务
tags:
- Recursive Synthesis
- Terminal Agent
- Long-Horizon Tasks
- Verified Data
- Agent Training
- Synthetic Data
one_liner: 递归扩展验证式合成，每任务$0.05且难度持续攀升，显著提升Agent长程执行能力。
practical_value: '- 递归合成框架可自动化生成难度递进的训练任务：从已有种子任务出发，扩展解决方案、重对齐验证器与指令，沙箱验证通过即接受，可用于构建持续提升的
  agent 训练课程。

  - 低成本大规模验证数据：每任务约 $0.05，且验证成功率高，对需要可执行、可验证的训练场景（如电商客服工具调用 Agent）有直接借鉴。

  - 多样性控制策略：通过种子 lineage 上限、重写操作符多样化、领域分布保持等手段，避免合成数据多样崩塌；可迁移到推荐或对话系统中自动生成多样化训练样本的流程。

  - 合成数据结合 PPO 训练可显著提升 Agent 长程规划与工具使用：Qwen3.5-27B 在 Terminal-Bench 2 上相对基座提升 20.0%，表明即使无人工标注，仅靠合成任务和可执行奖励也能获得强泛化能力。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：长程终端 agent 训练数据昂贵（单任务数百至数千美元），人工编写不可扩展，直接 LLM 生成易破坏指令-环境-验证器一致性。亟需低成本、可自动验证的规模化任务生成方法。

**方法关键点**：
- 提出 RST（Recursive Synthetic Terminal Tasks）递归合成框架，从 639 个已验证种子任务开始，每轮选一个重写操作符扩展解决方案，同步更新验证器、指令及环境，在新鲜沙箱中执行验证，通过的任务作为下一轮种子。
- 解决方案优先扩展：先增加命令、状态依赖、中间产物；再修改验证器针对新产出设置检查；最后修改指令描述目标，确保公共指令不泄露私有测试。
- 验证分两步：静态检查（防重复、防泄露）和沙箱 oracle 执行，失败任务允许有限修复后重试。
- 多样性控制：对父任务 lineage、领域、重写操作族、生成队列加帽，防止单一模式主导。

**关键实验结果**：
- 递归 15 轮生成 37,484 个验证任务，成本约 $0.05/任务，通过率稳定在 74.5%–81.5%。
- 难度大幅攀升：中位解决方案行数 67→374（5.6×），命令数 40→244（6.1×），指令长度仅增 1.4×；DeepSeek-V4-Pro pass@4 从 90% 降至 2.5%。
- 监督微调：Qwen3.5-27B 与 122B 在 Terminal-Bench 2、Hard、Long-Horizon 上最多提升 10 个百分点；PPO 训练后 Qwen3.5-27B 分别达 49.44%、32.00%、22.07%，相对基座提升 20.0%、41.2%、21.9%。
- 多样性保持：领域分布熵 0.821→0.817，40 个重写操作符中 36 个存活，无单一域或操作符垄断。

**值得记住的一句话**：$0.05 一个任务，15 轮递归无天花板，难度一路飙升而合成效率不降，合成任务训练的性能增益稳定且显著。
