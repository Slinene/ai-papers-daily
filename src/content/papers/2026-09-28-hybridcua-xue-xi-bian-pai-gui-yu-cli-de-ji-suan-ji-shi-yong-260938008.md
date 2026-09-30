---
title: 'HybridCUA: Learning to Orchestrate GUI and CLI for Computer-Use Agents'
title_zh: HybridCUA：学习编排 GUI 与 CLI 的计算机使用智能体
authors:
- Tongbo Chen
- Junbo Niu
- Zhengxi Lu
- Niu Lian
- Fei Tang
- Yuchen Yan
- Yike Hong
- Yong Du
- Yizhou Liu
- Bofan Chen
affiliations:
- Zhejiang University
- Peking University
- Tsinghua University
arxiv_id: '2609.38008'
url: https://arxiv.org/abs/2609.38008
pdf_url: https://arxiv.org/pdf/2609.38008
published: '2026-09-28'
collected: '2026-09-30'
category: Agent
direction: Agent 多模态交互与工具编排
tags:
- Computer-Use Agents
- GUI-CLI Orchestration
- RLVR
- Multimodal Agents
- Action Space
- Tool Use
one_liner: 通过统一 bash 动作空间与 CLI-aware 奖励，让 CUA 学会何时用 CLI、如何可靠执行，OSWorld 准确率 53.6% 且步骤减半
practical_value: '- **工具接口统一化**：在电商导购 Agent 中，把点击/输入等 GUI 操作与搜索 API、筛选工具统一成同一种 action（如
  `execute`），模型只需学习一个动作语法，降低调度复杂度；本论文统一 bash action 比分开 GUI/CLI tools 高 7.2 个百分点。

  - **显式奖励工具选择**：对 Agent 的工具使用做两层 reward——任务级根据标签奖励“是否选择了合适的工具”（如该用 API 批量操作时不用 GUI
  一步步点），步级惩罚执行失败（如 API 参数错误、SQL 出错），比只给最终成功奖励更能塑造高效且可靠的行为。

  - **混合数据构造**：从单一 GUI 轨迹转换成等价 CLI 命令并重放验证，可低成本生成混合工具使用数据，不必从头收集。电商场景可以把已有“点击操作”轨迹改写为“调用搜索/下单
  API”轨迹，保留成功回放，用于 SFT 温启动。

  - **SFT+在线 RLVR 两段训练**：先 SFT 混合轨迹让模型学会工具切换，再用可验证奖励在线微调，能同时提升任务完成率和降低交互步数（步骤减少 29.3%）。适用于电商
  Agent 的购物任务、订单处理等可验证场景。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
现有计算机使用智能体（CUA）要么只依赖 GUI 点击/键盘，通用但低效且长序列易累积错误；要么接入应用特定 API/tool，高效但每个应用都要单独开发，难以扩展。GUI+CLI 混合是自然出路：GUI 提供视觉交互通用性，CLI 用一条命令替代长串 GUI 操作。但简单给模型暴露 shell 反而会降低性能——现有模型不知道何时该用 CLI、如何可靠执行。训练数据中各接口轨迹割裂，监督信号也不包含接口选择信息。

**方法关键点**
- 构建 HybridCUA-8K：5K 条轨迹覆盖 GUI only、CLI only、interleaved 三种模式；3K 个可验证 RLVR 任务，每个任务标注 CLI 是否有明显执行优势。
- 统一动作空间：所有可执行操作封装为同一个 `bash` action，GUI 操作用 Python heredoc 包 `pyautogui`，CLI 直接 shell 命令，避免模型在两种工具间切换时产生语法冲突。
- 两阶段训练：先用三类轨迹做 SFT，学会统一动作格式和接口切换；再做在线 RLVR，用 GRPO 优化。
- CLI-aware 奖励：任务级 `R_CLI` 奖励“是否按标签选择性地使用 CLI”，步级 `r_exec` 对 shell 执行失败给予 -1 惩罚，两者分别监督“何时用”和“如何用”。

**关键结果**
HybridCUA-9B 在 OSWorld 上达到 53.6% 准确率，比 base Qwen3.5-9B 提高 14.8 个百分点，平均步骤从 31.6 降到 14.0。比 GUI+API 的 ToolCUA-8B、AutoGLM-OS-9B、UltraCUA-32B 分别高 6.8、4.7、9.9 个百分点。SFT 混合数据优于任何单一类型；RL 进一步从 46.0% 提升到 53.6%，步骤减少 29.3%。消融显示去掉任务级 `R_CLI` 导致 CLI 使用率下降且效率提升减弱，去掉步级 `r_exec` 使命令执行错误率回升到 16.5%。在 WindowsAgentArena 上达 36.0%（+4.0），OSWorld-MCP 上达 47.1%（+9.1），表明跨平台迁移的是“何时委托给 shell”的策略，而非记住的命令。

**最值得记住的一句话**：把接口选择作为显式训练信号（任务级偏好 + 步级执行反馈），让 agent 学会何时用高效工具而不是一味使用，是同时提升任务完成率和效率的关键。
