---
title: 'AgentHijack: Benchmarking Computer Use Agent Robustness to Common Environment
  Corruptions'
title_zh: 计算机使用代理在常见环境扰动下的鲁棒性基准与增强
authors:
- Jingwei Sun
- Jianing Zhu
- Yuanyi Li
- Tongliang Liu
- Xia HU
- Bo Han
affiliations:
- TMLR Group, Hong Kong Baptist University
- The University of Texas at Austin
- Sydney AI Centre, The University of Sydney
- Shanghai Artificial Intelligence Laboratory
arxiv_id: '2605.25707'
url: https://arxiv.org/abs/2605.25707
pdf_url: https://arxiv.org/pdf/2605.25707
published: '2026-05-24'
collected: '2026-05-29'
category: Agent
direction: 计算机使用代理鲁棒性评估与增强
tags:
- GUI agents
- corruption robustness
- benchmark
- MLLM
- reinforcement learning
one_liner: 提出AgentHijack基准量化常见干扰对GUI代理的影响，并设计集成onlooker与DA-GRPO的框架提升鲁棒性。
practical_value: '- 在构建多步骤推荐或对话Agent时，可引入onlooker机制（行为总结与初始环境检查）以降低执行偏差；当出现非预期界面变化（如弹窗、网络错误）时，Agent能快速归因并回归主任务。

  - DA-GRPO（数据增强的群体相对策略优化）通过在不同干扰环境下采样轨迹，提升策略对视觉干扰、意外操作的鲁棒性，类似电商推荐中应对布局变化、突发遮挡的挑战。

  - 评估智能体时需涵盖真实环境中的常见扰动，不可仅依赖干净基准；可借鉴AgentHijack的9类可配置干扰设计，构建电商APP中的异常场景测试集（如弹窗、多app切换、网络波动）。

  - 将行为总结文本作为历史上下文的一部分，帮助Agent聚焦长期目标而不被临时弹窗或误触内容带偏，这一设计可迁移到多轮推荐对话中，提升对中断和话题偏移的恢复能力。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
现有基于多模态LLM的计算机使用代理在理想环境下表现良好，但真实操作环境充满弹窗、分辨率变化、网络错误等常见干扰，导致代理定位失败、决策偏离、盲目重试。已有基准多关注干净环境或对抗攻击，缺乏对这类常见扰动的鲁棒性评测。

**方法关键点**  
- 构建 **AgentHijack 基准**：在 OSWorld 上叠加 9 类可配置的常见干扰（弹窗、分辨率变化、标记、字幕、多应用、误触、应用最小化、网络错误、身份验证），生成 3,321 个任务，每类干扰支持参数调节。  
- 提出 **AgentHijack-Agent 框架**：  
  - **DA-GRPO**（数据增强的群体相对策略优化）：在不同干扰环境下采样多条轨迹，组合任务成功奖励与格式奖励，结合经验回放缓冲区解决奖励稀疏问题，增强行动生成器的视觉定位与抗干扰能力。  
  - **Onlooker 组件**：同时负责行为总结（将每步环境变化概括为简短文本，辅助历史记忆）和初始环境检查（从外部错误库验证环境是否正常，阻止异常状态下的无效探索）。  
- 整体流程：Onlooker 先检查环境，随后增强后的行动生成器基于用户指令、历史截图与行为摘要依次输出动作，Onlooker 持续更新摘要。

**关键实验结果**  
- 在 AgentHijack 上评测 9 款代表性代理（含 GPT-4o、Claude-3.7、UI-TARS 系列），UI-TARS-1.5-7B 在干净数据上成功率 24.21%，干扰下平均仅 18.74%。  
- AgentHijack-Agent 将平均成功率提升至 22.89%（+4.15%），在弹窗类干扰上提升 11.23%，验证类 +9.67%。  
- 消融实验显示各模块均有效，更强 onlooker 模型带来更大增益，且方法在不同干扰强度、内容、位置下保持稳定提升。

**核心洞察**  
“计算机使用代理对常见视觉干扰和环境错误极度脆弱，但通过引导代理关注行为总结、检查环境状态，并利用多环境 RL 训练，可以显著增强其真实场景下的可靠性。”
