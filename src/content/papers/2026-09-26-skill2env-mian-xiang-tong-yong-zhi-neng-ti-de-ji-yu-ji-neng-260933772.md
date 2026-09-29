---
title: 'Skill2Env: Capability-Oriented Environment Synthesis from Skills for General
  Agents'
title_zh: Skill2Env：面向通用智能体的基于技能与能力导向的环境合成
authors:
- Weiyi Xu
- Xiaowen Yang
- Wen Da
- Hang Xu
- Canwei Li
- Hongjie You
- Pusen Dong
- Yucheng Zeng
- Zhaokai Luo
- Mu Chuan
affiliations:
- AllSpark Team
arxiv_id: '2609.33772'
url: https://arxiv.org/abs/2609.33772
pdf_url: https://arxiv.org/pdf/2609.33772
published: '2026-09-26'
collected: '2026-09-29'
category: Agent
direction: Agent 训练环境合成 · 能力导向
tags:
- Skill2Env
- Agent Post-training
- Environment Synthesis
- Difficulty Patterns
- Iterative Task Hardening
- SFT
one_liner: 以技能为种子、能力需求为引导，通过难度模式与任务蓝图合成可执行环境，并用迭代硬化提升训练监督质量。
practical_value: '- 技能驱动的环境合成可迁移到电商导购/客服 Agent 的训练数据生产：把商品知识库、退换货 SOP、比价工具封装为 skills，按能力需求（环境理解、规划、工具使用、长程一致性、错误恢复）自动生成多步交互任务和沙盒环境，解决真实交互数据稀缺。

  - “任务蓝图”作为作者侧契约值得借鉴：生成指令/评测数据时显式分离 instruction、environment facts、information boundary
  和 acceptance criteria，避免关键信息泄漏进 prompt，同时为 rubric 打分提供可追溯依据。

  - Iterative Task Hardening 的课程式加难机制可复用到 Agent 训练/评测集：用 solver rollout 的满分率、交互轮数等执行证据定位“太简单”任务，再通过加
  pattern 强度（如分布式证据、schema mismatch、partial failures）逐步提升难度，比重新采样更高效。

  - Rubric 评估混合确定性检查和 LLM judge，并为每个 rubric item 记录证据；电商 Agent 自动评测建议采用这种“可程序化项用规则、开放项用模型、结果附证据”的打分方式。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
LLM 部署到真实工具使用和多步交互任务，需要可执行环境做 post-training，但手工构建指令、工具、workspace 和 evaluator 难以规模化。技能包含领域知识、操作流程和工具使用说明，但从技能到具体挑战性任务与可执行环境之间存在明显 gap。现有技能合成环境方法多关注覆盖与一致性，本文进一步追问：给定技能，如何按 agent 的能力需求来合成任务和环境。

**方法关键点**
- 从 47K+ ClawHub 技能中筛选出 3K+ 可执行技能，定义环境理解、规划、技能使用、长程一致性、错误恢复五维能力需求。
- 用 100 个可复用 difficulty patterns 将能力需求实例化为具体挑战，覆盖分布式证据、耦合约束、schema mismatch、partial failures 等。
- 为每个技能选择兼容 patterns，生成任务蓝图（objective、challenges、facts、information boundaries、acceptance criteria），作为作者侧契约，指导联合构造任务指令、执行基座、workspace 和 rubric evaluator。
- rubric 评估混合确定性验证和 LLM judge，权重归一；一致性校验排除无效执行证据。
- 提出 Iterative Task Hardening：solver rollout 后，对 reward>0.7 的任务进行诊断，强化已有 pattern 或引入新 pattern，更新蓝图与环境，共生成 2,963 个可执行任务。

**关键实验**
用 DeepSeek-V4-Flash 作 teacher 在生成任务上 rollout，保留 1.5K 条 reward>0.9 轨迹，SFT Qwen3.6-35B-A3B。在 7 个 agent benchmark 上平均分从 36.6 提升到 45.0（+8.4），其中 SkillsBench +14.34、Terminal-Bench 2.1 +13.5、SWE-bench Multilingual +7.7。硬化分析中，500 个配对任务 full-credit rate 从 48.40% 降至 24.80% 再到 15.40%，mean assistant turns 从 25.91 增至 36.54 再到 38.85；固定 500 条轨迹训练，平均分 40.58→42.51→42.87。

**最值得记住的一句话**
环境合成不应只扩展技能和任务覆盖，而应显式围绕 agent 被要求行使的能力组织任务构建。
