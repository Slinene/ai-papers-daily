---
title: 'OS-Helix: Unifying GUI Interaction and Code Execution in Native Computer-Using
  Agents'
title_zh: OS-Helix：统一 GUI 交互与代码执行的计算机使用智能体
authors:
- Bowen Yang
- Kaiming Jin
- Zichen Ding
- Zhenyu Wu
- Zehao Li
- Zhoumianze Liu
- Kanzhi Cheng
- Fangzhi Xu
- Yanan Sun
- Qiushi Sun
affiliations:
- University of Science and Technology of China
- Shanghai AI Laboratory
- National University of Singapore
- Shanghai Jiao Tong University
- Fudan University
arxiv_id: '2610.22234'
url: https://arxiv.org/abs/2610.22234
pdf_url: https://arxiv.org/pdf/2610.22234
published: '2026-10-15'
collected: '2026-10-18'
category: Agent
direction: GUI 与代码统一动作空间的计算机使用智能体
tags:
- GUI Agent
- Code Execution
- Unified Action Space
- Online RL
- Step-balanced GSPO
- Multimodal
one_liner: 端到端训练统一 GUI 动作与代码执行空间，结合 SFT 与在线 RL 将 OSWorld 成功率提升至 66.44%
practical_value: '- 对需要同时操作 UI 与调用代码的 Agent（如电商 RPA、浏览器自动化、商家后台操作），不要靠 prompt 级工具组合，而应把
  GUI 动作与代码执行放进统一 action space，通过混合数据 SFT 内化 GUI/code 路由，避免“加 code tool 反而变差”的退化。

  - 用 application–artifact composition 生成带真实文件状态的可执行任务，配合 decoupled instruction/evaluator
  产出可自动验证的监督数据，适合电商场景批量构建可执行的 ground-truth 与回归评估集。

  - Step-balanced GSPO 按 action step 而非 token 聚合 importance weight，是处理长代码动作与短 GUI
  动作异质序列的 RL 稳定技巧，可直接迁移到多步推荐、对话式操作、工具调用等 RL 训练。

  - 冷启动 SFT + 在线 RL 在真实桌面环境迭代，这种“先行为克隆后环境反馈”的路线对构建生产级 Agent 可借鉴；若业务无桌面环境，可参考其可验证状态设计来构造环境反馈。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**  
真实桌面自动化既不是纯视觉也不是纯程序，Agent 需要同时理解界面并高效操作文件、脚本与系统状态。初步实验表明，简单给 GUI Agent 额外添加 code tool 会让成功率下降，说明 GUI/code 路由必须通过高质量混合数据的训练来内化，而不是靠 prompt 级工具组合。

**方法关键点**  
OS-Helix 是一个端到端训练的多模态 computer-using agent，将 GUI 动作与代码执行统一在一个 action space。监督信号构建上，提出 application–artifact composition，把桌面应用与真实文件 artifact 配对来实例化可执行的 Ubuntu 状态；同时提出 decoupled instruction/evaluator generation，生成环境锚定任务，其最终状态可验证，不依赖解决模态。训练路线为：先用过滤后的混合数据做 SFT 冷启动，再在 live 桌面环境中做在线 RL 提升。RL 提出 Step-balanced GSPO，按 action step 而非 raw assistant tokens 聚合 importance weight，防止长代码动作主导异构动作优化。

**关键结果数字**  
OSWorld-Verified 上，OS-Helix-27B 和 OS-Helix-35B-A3B 相对匹配的 Qwen3.5 hybrid baselines 分别提升 35.0% 和 33.7%；OS-Helix-27B-RL 进一步相对提升 42.9%，达到 66.44% 成功率。消融验证了 learned GUI/code coordination、可扩展可验证监督、action step balanced optimization 的贡献，并在 WindowsAgentArena 上展示跨平台迁移。
