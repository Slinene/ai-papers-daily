---
title: 'LongWoF-Bench: Evaluating EvoMap Genes for Verifiable Long-Workflow Tasks'
title_zh: LongWoF-Bench：评估 EvoMap Gene 在可验证长工作流任务上的经验复用效果
authors:
- Xiao Zhang
- Qumeng Sun
- Jihao Li
- Yiming Ren
- Xiang Liu
- Haoyang Zhang
- Junjie Wang
affiliations:
- Infinite Evolution Lab, EvoMap
- Tsinghua University
arxiv_id: '2608.23200'
url: https://arxiv.org/abs/2608.23200
pdf_url: https://arxiv.org/pdf/2608.23200
published: '2026-08-23'
collected: '2026-08-26'
category: Agent
direction: Agent 经验复用 · 长工作流评估
tags:
- Long-Workflow
- Verifier-Grounded Experience
- Skill vs Gene
- Agent Memory
- Benchmark
one_liner: 提出 LongWoF-Bench，证明由 verifier 确认轨迹蒸馏的 EvoMap Gene 比 Skill 跨七个模型提升 8.7–15.5
  个百分点
practical_value: '- **沉淀可验证执行经验，而非通用 Skill**：在复杂流程（如广告投放配置、选品策略、活动执行）中，将成功轨迹中证明有效的策略、边界条件和失败修正提炼成结构化资产，跨模型复用。

  - **严格区分经验来源**：只有经过业务验证器/线上 A/B 确认的执行轨迹才值得沉淀；参考解蒸馏的经验可能反而有害。经验库要记录 provenance。

  - **一次推理复用经验，降低重复探索成本**：在复用经验时采用单次生成（one-shot）即可，避免多轮试错；论文中 Gene 比 Skill 少 9.9%
  token，比多轮发现少 45.8% token。

  - **优先在规则约束和接口一致性强的场景应用**：如合规审核、物流配置、多模块交付等，经验复用收益最大；纯推理能力瓶颈的任务收益有限。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
LLM 执行复杂工作流时常因后期决策依赖早期状态、接口约定、边界条件等，局部合理但全局失败。但成功执行经验通常只保存于单次运行中，后续模型从零探索。现有 Skill 封装程序性知识，但缺少 verifier 确认的执行经验。论文研究能否将验证过的轨迹外部化并复用。

**方法关键点**
- 提出 LongWoF-Bench，共 778 个机器可验证任务，分为代码生成、agent-环境合成、数学推理和规则遵从四类。任务定义为 T=(S,E,Y,V)，严格要求端到端验证。
- EvoMap Gene：由 Evolver 对任务执行「执行-验证-精炼」循环，得到 verifier 确认的轨迹后蒸馏为结构化 Gene，保存成功策略、先决条件、边界条件和失败修正；对比的 Skill 仅封装程序性知识。
- 评估协议：同一任务在 No Context、Skill、EvoMap Gene 三条件下比较，公共规范、运行时、私有验证器保持固定；七个模型（Claude Opus/Sonnet、Gemini Flash/Pro、MiniMax M3、Qwen 两个规格）作为消费者。

**关键结果**
- 在 252 个 Opus 确认轨迹的任务上，平均严格通过率从 No Context 的 41.0% 提升到 Skill 的 51.2%，再提升到 Gene 的 62.9%；所有七个模型中 Gene 比 Skill 高 8.7–15.5 个百分点。
- 在 526 个 reference-distilled Gene 任务上，Gene 反而比 Skill 低 3.3–11.3 个百分点，说明经验来源（provenance）比表示形式更重要。
- 对 Opus 自身，Gene 比 Skill 多解决 39 个任务，solve-time token 消耗减少 9.9%；与多轮发现相比，一次 Gene 复用减少 45.8% token。
- 分工作流看，agent 环境和规则遵从收益最大（+15.6~29.7 pp），数学推理收益最弱。

**结论**：验证过的执行经验可以外部化、跨模型复用，并能降低重复探索成本；仅靠紧凑表示或参考蒸馏无法获得同等收益。
