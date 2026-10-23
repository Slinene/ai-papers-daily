---
title: Towards User Simulators That Stay On Task And Still Sound Natural
title_zh: 兼顾任务遵循与行为自然度的用户模拟器
authors:
- Mustafa Omer Gul
- Philippe Laban
- Tanya Goyal
- Jennifer Neville
affiliations:
- Cornell University
- Microsoft Research
arxiv_id: '2610.31512'
url: https://arxiv.org/abs/2610.31512
pdf_url: https://arxiv.org/pdf/2610.31512
published: '2026-10-22'
collected: '2026-10-23'
category: Eval
direction: 用户模拟器 · RL+对抗判别器
tags:
- User Simulator
- RL
- Adversarial Training
- LLM
- Evaluation
- Multi-turn Dialogue
one_liner: 用 RL 联合动态对抗判别器训练用户模拟器，有效对话率 46.2%，为最强现有模型的 3.3 倍
practical_value: '- 在需要模拟用户生成多轮对话的场景（如评估导购 Agent、电商客服助手），不要只用 prompt 大模型或纯 SFT；可借鉴
  SFT+RL+动态判别器配方：先 SFT 对齐真实用户语料，再用联合奖励优化任务完成度和自然度。

  - 自然度评估要避免 LLM-as-a-judge，用轻量判别器（如 ModernBERT）做对抗训练，每 N 步重训，防止 reward hacking；业务中可训练真实用户
  vs 模拟对话的判别器，作为线上模拟器的质量监控信号。

  - 设计 coverage 奖励时引入信息不对称：给生成模型的意图抽象、给 reward 的子目标具体，可防止模型逐字复述意图刷分，鼓励多样化合理行为；类似可应用于推荐解释生成或
  Agent 指令跟随训练。

  - 终止/质量奖励可作为必要的门槛：先检查角色切换、重复输出、提前终止等硬失败，再做细粒度打分；这能低成本过滤掉不可用样本，提升自动化评估信噪比。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**
多轮交互中 LLM 助手性能会退化，评估与改进依赖用户模拟器；但现有方案存在取舍：prompt 的强助手能遵循复杂意图却行为过于正式不自然，SFT 用户模拟器自然但常偏离任务，导致评估不可靠。

**方法关键点**
- 数据：WildChat-4.8M 过滤为 199,249 个多轮交互，SFT 得到初始化 UserLM-2.0-SFT。
- RL 目标：GRPO 联合奖励质量（阻止复述/角色切换）、覆盖率（LLM judge 评估子目标）、终止（与覆盖绑定：正确终止正奖励，提前终止负奖励）、自然度（判别器分>0.5 给 1）。
- 自然度核心：用 ModernBERT-Large 轻量判别器做对抗训练，每 25 步重训，动态适应模拟器输出，避免静态判别器被 reward hack；实验表明 LLM-as-a-judge 和固定判别器对自然度无效甚至有害。
- 防刷分：输入给模拟器的意图是抽象版 c，而 coverage 奖励使用详细子目标 c*，信息不对称防止逐字复述。

**关键结果**
在 2000 测试意图上，UserLM-2.0 有效对话率 46.2%，是 SFTUser-14B 的 3.28 倍；覆盖率 88.0%，自然度通过率 71.8%。高复杂度 7 子目标下有效 12.6%，此前模型接近 0。成本极低：每 100 有效对话 $0.11（GPT-5.6-Sol 为 $205.20）。与真人仍有差距（80.2% vs 46.2%）。

**最值得记住**：自然度要用动态对抗判别器而非 LLM judge，配合覆盖、质量、终止的联合 RL，是打破任务保真与行为自然度权衡的关键。
