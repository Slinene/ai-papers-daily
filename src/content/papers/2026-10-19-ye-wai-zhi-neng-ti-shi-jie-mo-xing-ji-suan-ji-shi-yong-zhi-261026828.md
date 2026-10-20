---
title: 'Agent World Model in the Wild: Computer-Use Agent Environment Synthesis'
title_zh: 野外智能体世界模型：计算机使用智能体环境合成
authors:
- Zhaoyang Wang
- Qianhui Wu
- Haorui Wang
- Simon Yu
- Baolin Peng
- Canwen Xu
- Hao Cheng
- Wenlin Yao
- Boyi Liu
- Yite Wang
affiliations:
- UNC-Chapel Hill
- Microsoft Research
- Georgia Tech
- Northeastern University
- Independent Researcher
arxiv_id: '2610.26828'
url: https://arxiv.org/abs/2610.26828
pdf_url: https://arxiv.org/pdf/2610.26828
published: '2026-10-19'
collected: '2026-10-20'
category: Training
direction: 训练环境合成 · CUA · RL
tags:
- Computer-Use Agents
- Environment Synthesis
- RL
- GUI-MCP-CLI
- Open-Source Models
- Quality Gates
one_liner: 开源流水线合成 GUI/MCP/CLI 跨界面环境与长程任务，用质量门控与 RL 训练出跨 8 个 OOD 基准泛化的 CUA 智能体
practical_value: '- 对电商 Agent 训练：可借鉴 WildAWM 的「可执行世界 + 五类质量门控」生成带验证器的多步任务，尤其 Counterfactual
  Probe 能防 LLM 法官谄媚，适合审核购物车/下单/售后等长流程合成数据。

  - RL 奖励设计：把最终成功与子任务 checklist 部分得分结合，给长程任务更密集监督；Format penalty 对 GUI 动作解析很重要，可迁移到
  App 操控或网页购买 Agent。

  - 全开源栈（GLM-5.2 + OpenCode）证明环境合成无需闭源模型，业务上可低成本自建仿真环境，不必依赖外部 API。

  - 世界合成用 persona + multi-day day plan 积累状态，可生成带用户历史/商品/库存的连续环境，用于推荐或搜索 Agent 的长期交互训练。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**  
LLM Agent 从人类数据学习成本高，直接在真实世界做 RL 有安全与重置困难；合成环境成为训练通用 CUA 的关键。现有方法通常只覆盖单一界面，且多依赖闭源模型。WildAWM 旨在用全开源模型合成跨 GUI、MCP、CLI 的可执行个人电脑环境与可验证长程任务。

**方法关键点**  
- 世界合成：从 persona 与多日 day plan 出发，用 coding agent 逐日生成网站、MCP 服务与本地文件，并用可复用 skill 库与确定性重放保证状态一致性。
- 任务合成：生成必须同时使用 GUI/MCP/CLI 的跨界面任务；收集 18 个开源模型×harness 的 rollout，并经过程序化 verifier、LLM judge、agent judge 三层判断。
- 五类质量门控：Judge Consistency、Initial Unsatisfaction、Task Solvability、Task Difficulty、Counterfactual Probe，分别保证判定一致、非平凡、可解、有难度、验证器不受谄媚影响。
- RL 训练：GRPO 中融合二进制成功奖励与 checklist 部分得分，加入 format penalty，并用 EMA 动态决定 rollout 组大小以增强奖励多样性。

**关键结果**  
- 合成 341 个环境-任务对，平均 4.2 个子任务、3.1 次界面切换，GPT-6-Astra 仅解决约 60%。
- 在 8 个 OOD 基准上，Qwen3.6-35B-A3B 平均分从 42.84 提升至 53.42（+10.58），Qwen3.5-4B 从 21.83 提升至 30.04（+8.21）。
- 验证器与多数 agent judge 一致率达 95%，Cohen κ 为 0.90；消融显示去掉任一质量门控都会使 OOD 平均分下降 2.6–9.3 分。

> 最值得记住的一句话：全开源模型可以合成具备跨界面长程任务与可靠验证器的可执行世界，并在其中训练出跨 8 个 OOD 基准泛化的 computer-use agent。
