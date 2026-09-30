---
title: 'Marathoner: Ultra-Long-Horizon Autonomous Intelligence'
title_zh: 马拉松者：超长程自主智能体
authors:
- Zhang Ruiyang
- Ou Jinpeng
- Xie Yifan
- Zhou Jingang
- Pan Lirui
- Guo Qingpei
- Zheng Zhedong
affiliations:
- University of Macau
- Peking University
- Ant Group
arxiv_id: '2609.34378'
url: https://arxiv.org/abs/2609.34378
pdf_url: https://arxiv.org/pdf/2609.34378
published: '2026-09-27'
collected: '2026-09-30'
category: Agent
direction: 超长程自主编码 Agent 后训练
tags:
- Long-Horizon Agent
- Reinforcement Learning
- Rejection Sampling
- Task Synthesis
- GRPO
- Software Engineering
one_liner: 从 GitHub PR 自动合成任务、拒绝采样蒸馏与 GRPO+后期奖励，让 9B 开源模型具备 10+ 小时执行能力
practical_value: '- 任务数据合成：从业务系统（推荐服务代码库、数据管道、广告投放平台）的 commit/PR 自动构造带单元测试验证的长程 Agent
  任务；电商搜索推荐团队可基于历史工单、A/B 实验变更生成环境+指令+验收测试三元组，低成本扩充训练数据。

  - 后期阶段奖励：在对话式推荐/导购 Agent 中用 LLM 判断会话后半段是否有高价值动作（如用户改变偏好后的有效重新推荐、复杂比价后的正确总结），给予额外奖励，防止模型在长交互中过早收尾或重复无效询问。

  - 多样 harness 训练避免过拟合：针对 Agent 可能接入的不同执行环境（推荐 API、页面布局、工具集），在 RL 训练时轮换多种 harness，可提高跨场景泛化，与多环境交互评分/模拟器训练思路一致。

  - 拒绝采样蒸馏：先用闭源大模型在真实任务上生成成功轨迹，仅保留 reward=1 样本对开源小模型做 SFT 初始化，再进入 RL 微调；适用于电商客服、导购
  Agent 等需要长程规划的场景，降低对高质量标注轨迹的依赖。'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
闭源前沿模型（Fable 5、GPT-6-Astra）已能连续工作数天解决复杂问题，但训练细节不公开，开源模型缺乏超长程执行能力。作者旨在通过公开后训练流水线为开源模型注入真实的长时程 Agent 能力。

### 方法关键点
- 任务合成：从 10k 个多样化 GitHub 仓库挖掘 100k 个 major release PR，按新增代码行数分 Easy/Medium/Hard（100-200/200-1000/1000+，比例 2:3:5）。每个 PR 构建任务：代码库检出到 PR 前 commit，指令来自 PR 首条评论、发布说明或 LLM 生成，奖励验证器由 fail-to-pass 和 pass-to-pass 单元测试组成，统一用 Harbor 格式。
- Multi-Task Chaining：随机串联 5 个原子任务为 Frontier 任务，大幅提升难度与执行长度。
- 拒绝采样微调：用 Kimi K3 教师模型配合 Claude Code、Codex、OpenClaw 三种 harness 生成轨迹，仅保留 reward=1 的成功轨迹（共 40,820 条），对 Qwen3.5-9B 进行 256k 序列长度的全参数 SFT。
- 强化学习：采用 GRPO，在独立沙箱中真实交互，并轮换多样 harness。提出 Later Stage Bonus Reward：用 LLM 将轨迹总结为多个阶段，若后半段存在高价值操作（如修复隐藏 bug、关键优化）则额外奖励 0.5，最终奖励 = 正确性奖励 + 后期奖励。

### 关键实验
- 在 FrontierSWE、NL2Repo、SWE-Marathon、Terminal Bench 2.0、SWE-Bench Verified 五个基准上，Marathoner-9B 相对基座 Qwen3.5-9B 显著提升：FrontierSWE 10.2→26.4，NL2Repo 17.9→34.7，SWE-Marathon 0→8.2，Terminal Bench 2.0 27.3→57.2，SWE-Bench Verified 43.8→77.5，并在两个基准超过 Gemini-3.1-Pro。
- 消融显示 Multi-Task Chaining、多样 harness 轨迹生成、Later Stage Bonus Reward 均带来稳定提升；RL 训练任务数从 1k 扩到 8k，性能持续上升。
- 执行统计：FrontierSWE 平均 3.56 小时、648.3 次工具调用；在挑战性任务上可连续执行 10+ 小时、进行 1000+ 次工具调用。

### 最值得记住的一句话
用真实 PR 自动合成带验证器的长程任务，加上拒绝采样蒸馏和鼓励后期阶段有效操作的奖励设计，可训练出具备 10 小时级自主执行能力的开源 9B Agent。
