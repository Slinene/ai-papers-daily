---
title: 'Qwen-Planner-Agent: A Closed-Loop AI-for-AI Framework for Real-World Mobile
  Planner Agents'
title_zh: Qwen-Planner-Agent：面向真实移动规划智能体的闭环 AI-for-AI 框架
authors:
- Tingyu Qu
- Weigao Sun
- Yuecheng Liu
- Yucheng Zhao
- Yi Zhu
- Yifeng Ding
- Qiyi Wang
- Sihan Cao
- Pengkun Jiao
- Hanlei Xie
affiliations:
- MAI Team
- Alibaba Token Hub
- Alibaba Group
arxiv_id: '2609.29892'
url: https://arxiv.org/abs/2609.29892
pdf_url: https://arxiv.org/pdf/2609.29892
published: '2026-09-23'
collected: '2026-09-25'
category: Agent
direction: Agent 闭环训练与模型-Harness 协同进化
tags:
- Mobile Agent
- AI-for-AI
- Agentic RL
- Model-Harness Co-evolution
- CARE
- Memory
one_liner: 构建闭环 AI-for-AI 框架，通过 AI 生产数据、CARE 智能体强化学习与模型-Harness 协同进化，在 MobilePA-Bench
  以 27B 取得最高综合分 77.05%
practical_value: '- 混合环境策略可迁移到电商导购/搜索 Agent：用沙箱覆盖可复现工具调用，LLM 仿真覆盖长尾场景，少量真实设备/线上会话做高保真验证，能显著降低真实交互成本，同时保留关键执行反馈。

  - CARE 的按组成功率分档值得直接借鉴：任务成功率低时给过程奖励，混合时只给结果奖励，成功后转向效率优化；并用 success-anchor 校准 advantage，避免模型为省
  token 而过度压缩推理或工具调用，适合对 LLM 成本敏感的推荐解释生成、对话式搜索、商品导购等场景。

  - 模型-Harness 分离设计适合工具/货架频繁变化的电商场景：模型参数不绑定具体工具清单，Scenario Adapter 按当前可用工具注入操作说明，Memory
  按证据分级管理，支持大促、多租户、多行业工具切换而无需反复重训模型。

  - AI-for-Data 飞轮可复用：保留失败轨迹并做能力归因，根据验证集弱点生成新任务和重采样，而不是只按原始语料频率训练；这可用于 query 改写、搜索
  suggestion、推荐理由生成等任务的持续迭代优化。'
score: 9
source: huggingface-daily
depth: full_pdf
---

**动机**  
移动规划要求智能体跨应用分解长程任务、持续状态跟踪、失败恢复并验证最终结果，真实设备交互成本高、难以并行，导致开发规模化受限。该工作把移动规划作为 AI-for-AI 的试验场：让 AI 不仅作为被开发系统，也参与数据生产、训练和部署改进，形成执行反馈驱动的闭环。

**方法关键点**  
- **AI for Data**：构建人工把关的数据飞轮。任务构建智能体按场景覆盖与能力覆盖生成可执行任务；自动收集多步交互轨迹，并保留失败轨迹用于诊断。数据组合不按原始语料比例采样，而是按能力、难度、来源加权；根据验证集弱点生成新任务、对不稳定行为上调采样权重、对已掌握任务降采样。
- **混合环境**：组合 programmatic sandbox、LLM-simulated environment 与少量 real-device sessions，分别承担可复现任务、长尾交互、高保真验证，统一 action-feedback-verification 契约。
- **AI for Training**：先用规划导向 SFT 冷启动，按 turn 级错误掩码学习任务分解、工具调用与恢复；再做 hybrid-environment online agentic RL。核心是 CARE：按轨迹组成功率分三档——progress shaping、outcome consolidation、efficiency refinement；并用 success-anchor 校准 advantage，防止成功饱和后微小效率差异被标准化放大。
- **AI for Harness**：部署时用统一 Harness 连接 Planner Model 与外部资源，提供 Scenario Adapter 注入工具相关 Skills、Persistent Memory 管理用户偏好与历史证据、执行反馈回传。离线诊断区分模型侧失败与 Harness 侧失败，分别指导模型训练和 Harness 修订，形成模型-Harness 协同进化。

**关键结果**  
在 MobilePA-Bench（1,700+ 可执行任务、200+ 工具、13 个 query-task 域）上，Qwen-Planner-Agent 27B 综合得分 77.05%，超过 GPT 6 Astra 的 76.84% 和 Claude Opus 5 的 75.71%；相比 Qwen 27B 基线从 67.22% 提升至 77.05%，35B-A3B 从 54.90% 提升至 69.91%。Tool Use 77.79%、Memory 74.76%、Skills 86.25%。输出成本也低于对比商用模型，估计为 $2.41/1K tasks 级别。CARE 相比 Vanilla RL 在精度持平时减少 32.5% 输出 token。

最值得记住的一句话：**用执行证据把数据生成、训练策略和运行时 Harness 三者耦合，模型每次交互都变成下一轮开发的养料，而不只是最终成功标签。**
