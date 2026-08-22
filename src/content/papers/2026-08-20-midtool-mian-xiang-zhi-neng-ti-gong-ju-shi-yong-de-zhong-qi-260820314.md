---
title: 'MidTool: Mid-training Data Synthesis for Agentic Tool Use'
title_zh: MidTool：面向智能体工具使用的中期训练数据合成
authors:
- Fengqing Jiang
- Yite Wang
- Boyi Liu
- Zhaoyang Wang
- Canwen Xu
- Zhewei Yao
- Radha Poovendran
- Yuxiong He
affiliations:
- University of Washington
- Snowflake
- University of North Carolina at Chapel Hill
arxiv_id: '2608.20314'
url: https://arxiv.org/abs/2608.20314
pdf_url: https://arxiv.org/pdf/2608.20314
published: '2026-08-20'
collected: '2026-08-22'
category: Training
direction: Agent 工具使用 · 中期训练数据合成
tags:
- Mid-training
- Tool Use
- Agentic Trajectory
- Data Synthesis
- Function Calling
- MCP
one_liner: 构建首个通用工具使用中期训练语料MidTool-Mix，显著提升4B/8B模型在函数调用、多步交互和MCP任务上的表现
practical_value: '- 将工具文档、API schema、代码仓库等非结构化数据合成 agentic trajectories 用于 mid-training，可让模型提前学会参数
  extraction 和 workflow composition；电商推荐 Agent 可借鉴此思路，针对商品搜索、订单、优惠券等内部 API 构建专属语料，减少对
  post-training 的依赖。

  - 两条合成分支分别针对 grounding（从文档/PDF生成 QA 和轨迹）和 execution（从真实 API/MCP 生成可执行轨迹），且必须组合才能全面收益；业务上可分别构建「文档问答+多轮调用轨迹」与「真实工具交互轨迹」两个数据管道，避免单一类型导致能力偏科。

  - 数据配比约 42% web + 26% code + 23% PDF + 9% native agentic trajectories，其中 9% 的 native
  轨迹对精确函数调用贡献最大；在构建内部工具使用语料时可参考此比例，优先保底 code/文档，但必须预留一部分真实可执行轨迹。

  - 训练顺序上先 mid-training 再 SFT/RL 能显著提升多轮交互和 unseen tool 泛化，且 SFT 收敛更快；如果业务已有工具调用 SFT
  数据，可先做一轮小规模 mid-training 初始化，再用原有 SFT 数据微调，投入产出比高。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

**动机**  
LLM 的工具使用能力几乎完全依赖 post-training 阶段的 SFT/RL，但原子能力如 tool recognition、schema-grounded argument construction、clarification under missing information、multi-step execution 难以从狭窄的轨迹监督中习得；且工具使用的底层知识分散在文档、代码、API schema 等非结构化语料中，很少以干净演示出现。论文提出将通用工具使用能力前移到 mid-training 阶段，通过大规模合成语料注入先验。

**方法关键点**  
- 数据源四类：web（FineWeb 2020-2025）、PDF（FinePDFs 英文子集）、代码（GitHub 仓库，排除 benchmark）、结构化工具（REST API 和 MCP skills）。  
- 两分支合成：① context-grounded trajectory augmentation，从 web/PDF/code 文档生成 QA 和多轮轨迹，教模型从 messy artifacts 中识别工具边界、推断参数、恢复工作流；② native agentic trajectory synthesis，直接从真实 API/MCP 生成可执行轨迹，强调 multi-turn planning、clarification、recovery，并通过 schema grounding、turn order、required arguments 验证。  
- 最终 MidTool-Mix 共 20.3B tokens，配比为 web 42%、code 26%、PDF 23%、native agentic trajectories 9%。

**关键结果**  
在 Qwen3-4B/8B Base 上 mid-training 后接 SFT/RL，在 BFCLv3、τ2-Bench、MCP-Universe 上评测。以 4B 为例：BFCL overall 从 SFT-only 的 39.73% 提升到 MidTool-Mix+SFT 的 50.25%，再加 RL 达 54.18%；τ2-Bench Pass@1 从 8.54% 提升到 12.23%（+RL 后 19.96%）；MCP-Universe overall score 从 13.20 提升到 18.66（+RL 后 23.80）。8B 趋势一致。消融显示两个分支互补：单独 native agentic trajectory 在 BFCL 上更强，但 context-grounded 在 τ2-Bench/MCP 上更有利，组合后才在所有指标上超过 no mid-training。

**最值得记住的一句话**  
通用工具使用应当通过专门的中期训练提前注入，且 grounding 和 execution 两类监督缺一不可。
