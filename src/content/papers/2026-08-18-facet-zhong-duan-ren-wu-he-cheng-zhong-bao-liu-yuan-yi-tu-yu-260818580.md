---
title: 'FACET: Preserving Source Intent and Executable State in Terminal Task Synthesis'
title_zh: FACET：终端任务合成中保留源意图与可执行状态
authors:
- Kou Shi
- Zun Wang
- Qisheng Su
- Shiting Huang
- Ziao Zhang
- Zhen Fang
- Qingnan Ren
- Jin Liu
- Yu Zeng
- Yiming Zhao
affiliations:
- University of Science and Technology of China
- Shanghai AI Laboratory
- Fudan University
arxiv_id: '2608.18580'
url: https://arxiv.org/abs/2608.18580
pdf_url: https://arxiv.org/pdf/2608.18580
published: '2026-08-18'
collected: '2026-08-20'
category: Training
direction: 终端 Agent 可执行任务合成与数据高效微调
tags:
- Terminal Agents
- Task Synthesis
- Executable Environment
- SFT
- Verifier Grounding
- Agent Training
one_liner: FACET 通过先构建并修复容器环境、以共享可执行状态串联指令/解法/验证器，合成高密度可验证终端任务，用 1.2K 成功轨迹显著提升多尺度模型
  Terminal-Bench 表现。
practical_value: '- 在构建 Agent 训练/评估环境时，优先先物化执行环境（文件、schema、服务、依赖），再生成指令、参考解和校验器；用真实落地状态作为共享
  grounding，能显著减少 schema/path/contract mismatch。

  - 顺序生成 I→S→V 且让 solution 实际执行后再生成 verifier，可以提高 solution–verifier 对齐；在业务中搭建离线模拟环境（如模拟用户、商品库、策略状态）时可直接套用该顺序。

  - 验证失败时通过执行 trace 路由到具体 artifact 单独修复，而不是整包重生成，可保留已有效组件、降低合成成本；适合用于构建数据合成 pipeline
  或 RL 环境。

  - 用更高密度的可执行检查（多个独立断言）能暴露“只差一两个条件”的失败模式，提供更细粒度训练信号；在标注成本高时，应优先提升单条数据的 grounding 与验证密度，而不是单纯扩大数量。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
训练终端 agent 需要可执行监督，但合成高质量终端任务困难：每个任务耦合 instruction、initialized environment、reference solution、executable verifier，任一不一致都会导致任务不可解或评估错误；多阶段生成还容易丢失源技能中的依赖、中间状态和流程约束。

**方法关键点**
- 三阶段框架：从 OpenClaw/ClawHub/GitHub 收集并过滤 71K skills，构建 scenario–skill repository；随后对 scenario 做五维重建（goal/context/capability/state/io-tool），生成 solution reference 和 instruction reference 并对齐。
- Stage 3 先根据 spec 规划并物化环境（Dockerfile、fixtures、services、dependencies），构建失败则按 trace 修复，最多 3 轮；成功后将 realized container state 作为 shared grounding。
- 按 I→S→V 顺序生成：instruction 基于实际存在的文件和服务，solution 实际执行得到 final state，verifier 基于 initial/final state 生成，优先采用行为和状态检查而非命令匹配。
- 验证与定向修复：从干净初始状态验证环境可建、初始非通过、solution 可执行、verifier 通过；失败由 router 定位到具体 artifact 单独修复，最多 5 轮。

**关键实验**
- 从 71K skills 生成 6,078 个验证任务，平均 22.77 个 executable tests/task；采集 1.2K 成功轨迹（teacher 为 DeepSeek-V4-Pro + Terminus-2）。
- SFT Qwen3.5-4B/9B/27B：Terminal-Bench 2.1 分别提升 +7.12/+8.24/+6.75；27B 达到 47.57，接近 397B 的 49.06。
- 生成顺序消融：Forward (I→S→V) 初始有效性 46.5%，最终 yield 83/100；优于 Reverse (24.2%/63) 和 Joint (37.5%/65)。
- 失败分析：89.40% 检查点被满足，但只有 20.94% 完整成功；54% 失败仅差 1-2 个检查点，说明难度来自组合需求而非主路径。

**最值得记住的一句话**
先把环境落地，再让指令、解法和验证器都锚定在同一个已实现容器状态上，配合顺序生成和定向修复，能用少量高质量轨迹高效提升终端 agent。
