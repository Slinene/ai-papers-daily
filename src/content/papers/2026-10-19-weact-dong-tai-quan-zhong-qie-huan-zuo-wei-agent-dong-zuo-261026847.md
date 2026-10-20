---
title: 'WeAct: Dynamic Weight Switching as Agent Actions'
title_zh: WeAct：动态权重切换作为 Agent 动作
authors:
- Rui Shi
- Xunjian Yin
- Jiacheng Sang
- Zichuan Liu
- Shuyan Zhou
affiliations:
- Carnegie Mellon University
- Duke University
- Meta MSL
arxiv_id: '2610.26847'
url: https://arxiv.org/abs/2610.26847
pdf_url: https://arxiv.org/pdf/2610.26847
published: '2026-10-19'
collected: '2026-10-20'
category: Agent
direction: Agent 模块化 LoRA 动态切换与持续学习
tags:
- LoRA
- Tool Calling
- Continual Learning
- Deep Research
- Agent
- Model Merging
one_liner: 把 LoRA 适配器切换做成 Agent 原生工具调用，冻结主干独立训练 Plan/Search/Writing 模块，在 deep-research
  任务上超越全参微调和静态合并
practical_value: '- **把流程阶段拆成可独立训练、可工具调用的 LoRA**：电商/搜索 Agent 可将意图规划、商品检索、参数对比、文案生成等阶段分别训成
  Plan/Search/Write 类 adapter，通过 `load_lora/offload_lora` 工具调用按需切换；新增能力只需注册新 adapter，不动已有链路。

  - **运行时选择优于静态合并**：论文显示 TIES/DARE-TIES/TSPA 等静态 LoRA 合并均导致专业化损失，甚至在无 rank 压缩下也有局部
  mismatch。业务中若已有多能力 LoRA，建议保留独立 adapter 并在推理时切换，而非合并成一个固定权重。

  - **工程实现复用原生 tool-calling 接口**：用 MCP 工具注册权重切换动作，不需要单独训练 router 或改造 forward pass；adapter
  常驻 GPU，切换时重建 KV cache，控制开销仅占 soft/hard 总时间的 8.2%/2.8%。

  - **模块化持续学习可落地到频繁迭代的环节**：只刷新 Writing adapter 即可提升报告质量，backbone 和其他 adapter 保持不变，无需回放历史数据；适合在商品文案生成、搜索
  query 改写等单一能力上做局部优化而不污染整体。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**
长 horizon Agent 需要规划、检索、验证、写作等异质能力，但共享参数联合训练会带来梯度干扰和灾难性遗忘；静态 LoRA 合并虽然隔离了能力参数，却用固定融合权重执行整个 trajectory，削弱各阶段需要的专业化。核心矛盾是：学习时要隔离，执行时要按需组合。

**方法关键点**
- 在冻结的 Qwen3-32B 上独立训练 Plan/Search/Writing 三个 LoRA adapter（rank 32/64/32），每个 adapter 只监督本能力阶段的 assistant tokens 和退出调用，前面的执行历史作为 causal context 保留。
- 将权重切换注册为原生 MCP 工具 `load_lora` / `offload_lora`；agent 通过 tool call 激活或释放 adapter，被选中的 adapter 接管后续推理和外部工具调用，共享同一条交互历史。
- 推理提供两种调度：WeAct-hard 按 Plan→Search→Writing 固定顺序强制加载，保证可靠触发；WeAct-soft 由模型根据任务状态灵活选择 adapter，受 harness 约束防止死循环。
- adapter 常驻 GPU，切换时重建 KV cache，避免重复 host-to-device 传输；新增能力只需注册新 adapter 别名。

**关键结果**
在 8 个 deep-research benchmark（GAIA、2Wiki、Bamboogle、MuSiQue、WebWalkerQA、xbench-DS、BrowseComp、FRAMES）上：
- WeAct-hard 平均准确率 45.47%，比 Full SFT 相对提升 6.2%，比最强静态 LoRA 合并方法相对提升 27.5%；WeAct-soft 平均 43.21%，排名第二。
- 训练 compute 低于 Full SFT；推理 latency 上 soft/hard 比 Full SFT 降低 33.4%/20.3%。
- 模块化持续学习：插入 Code adapter 不损害原有能力，Writing refresh 在 ResearchQA 和 DeepResearchBench 上分别 +2.40/+1.21。

**最值得记住的一句话**：把能力建模为可独立训练、可工具调用的权重模块，比共享参数或静态合并更能同时保留专业化并支持按需组合。
