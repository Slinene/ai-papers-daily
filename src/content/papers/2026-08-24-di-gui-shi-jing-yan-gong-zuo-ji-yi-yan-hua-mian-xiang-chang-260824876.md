---
title: Recursive Experiential-Working Memory Evolution for Long-Horizon Agent Harnesses
title_zh: 递归式经验-工作记忆演化：面向长程 Agent 的验证门控记忆架构
authors:
- Zhaochen Yu
- Yingcheng Wu
- Zhenfei Yin
- Kaiyuan Chen
- Zhe Zhao
- Mengdi Wang
- Shuicheng Yan
- Ling Yang
affiliations:
- NUS
- Stanford University
- University of Oxford
- Princeton University
arxiv_id: '2608.24876'
url: https://arxiv.org/abs/2608.24876
pdf_url: https://arxiv.org/pdf/2608.24876
published: '2026-08-24'
collected: '2026-08-26'
category: Agent
direction: Agent 长期记忆与递归自改进
tags:
- Recursive Self-Improvement
- Working Memory
- Experiential Memory
- Long-Horizon Agents
- Agent Harness
- Validation-Gated Evolution
one_liner: Recuris 用工作记忆驱动技能调用，将失败定位到记忆组件并验证门控演化，在长程任务上提升成功率
practical_value: '- 长程电商/客服 Agent 的状态管理：把会话目标拆成 pending/done/blocked 的 verified state，每个
  goal 带支持证据；只在执行事件（如确认下单、改地址、退款调用前）由 harness 注入对应技能，而不是把全量 SOP 或工具说明放 prompt。全量注入在本实验中反而比无技能更差（模型控制
  65.6 vs 无技能 82.0），说明“何时调用”比“内容多少”更关键。

  - 失败复盘与技能库更新：记录结构化 trace（状态→调用技能→动作→环境反馈→提案状态→检查器判定），用固定 Meta-Agent 把失败归因到技能缺失、状态更新错、调用时机错、校验器误判四类组件；只修补命中组件，再经
  held-out 验证门控。可以迁移到 agent 评测流水线或 SOP 迭代，避免全量重写记忆。

  - 验证门控的必要性：候选补丁必须在修复源失败的同时不回归 anchor tasks。电商技能库更新时也建议保留历史成功案例作为回归集，避免新规则破坏已有能力。

  - Test-time adaptation：对高价值单任务（如大订单异常、投诉处理）可用多次尝试 + 一位 verifier 的反馈，在局部更新经验记忆后重试；但一定要与
  budget-matched 简单重试对照，否则会混淆增益来源。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
长程 Agent 执行中，交互历史不断增长，模糊任务状态、使技能调用错位；现有经验记忆要么从初始指令检索、要么从全历史检索，不可靠。递归自改进的瓶颈不是缺少经验，而是缺少紧凑且可靠的任务状态来持续对准“当前需要”与“已存经验”。

## 方法关键点
- 记忆架构 M_k = (E_k, W_k, ρ_k, C_k)：经验记忆、工作记忆规范、调用策略、检查器集。
- 任务内 EM-WM 耦合：工作记忆维护结构化目标状态（pending/done/blocked + 证据）；调用策略在特定执行事件（如起草状态变更调用时）按当前状态和事件检索技能；环境反馈必须经检查器验证后才提交状态更新，不能仅凭模型自述。
- 跨任务递归演化：结构化 trace Γ 记录每步 (w_t, E_t, a_t, o_t, 提案状态, 检查器判定)；固定 Meta-Agent 定位失败到 E/W/ρ/C 组件，生成组件级补丁；验证门控在失败任务和 held-out dev set 上通过才接纳。
- 递归有界：底层 LLM、Meta-Agent、门控等外部流程固定，仅在外部记忆控制层演化；另有单任务 test-time adaptation 模式。

## 关键结果
在 τ2-Bench Retail/Airline、SkillFlow、Terminal-Bench 2.1 四个长程基准、10 个模型上，35/37 model-benchmark pairs 提升。τ2-Retail 上 GPT-5.6 Sol +17.8（58.3→76.1）、Claude Opus 5 +15.6（72.4→87.9）、部署模型 Doubao-2.0-Pro +23.3；SkillFlow 上 Qwen3.6-27B/35B 分别 +16.6/+13.5。优势随 horizon 增大：最长任务 +32.2；六类失败模式下降最多 80%。消融显示仅加经验记忆 +2.0 点、仅加工作记忆 +23.9 点、完整 +25.4 点；同样技能库由模型全量注入仅 65.6，Recuris 83.6，说明调用控制比技能内容更重要。机制消融发现 τ2-Airline 关键在 write review、τ2-Retail 关键在 status board，呈双分离。故障定位：只看任务结果仅 13.0%，结构化 trace 达 64.8%。两个 Meta-Agent 实现收敛，第二轮演化可再 +6.98 点。

> 最值得记住：**经验记忆是调用条件化的——它的价值更取决于“有东西知道何时用它”，而不是它包含什么内容。**
