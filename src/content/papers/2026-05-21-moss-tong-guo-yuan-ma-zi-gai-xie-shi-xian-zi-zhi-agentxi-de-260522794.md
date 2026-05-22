---
title: 'MOSS: Self-Evolution through Source-Level Rewriting in Autonomous Agent Systems'
title_zh: MOSS：通过源码自改写实现自治Agent系统的自我进化
authors:
- Qianshu Cai
- Yonggang Zhang
- Xianzhang Jia
- Wei Xue
- Jun Song
- Xinmei Tian
- Yike Guo
affiliations:
- University of Science and Technology of China
- The Hong Kong University of Science and Technology
- Hong Kong Baptist University
arxiv_id: '2605.22794'
url: https://arxiv.org/abs/2605.22794
pdf_url: https://arxiv.org/pdf/2605.22794
published: '2026-05-21'
collected: '2026-05-22'
category: Agent
direction: 自进化Agent · 源码级重写 · 生产部署
tags:
- Self-Evolving Agents
- Source-Level Rewriting
- Agent Harness
- Production Deployment
- Runtime Verification
- Container Swapping
one_liner: 让生产级agent系统通过源码自改写自主修复harness层故障，平均评分从0.25升至0.61
practical_value: '- **生产Agent的自我修复机制**：业务中大量使用的agent系统（如电商客服、订单助手）常常因路由/状态管理/hook顺序等harness层bug导致重复故障，MOSS提供了定向进化方案：从用户会话中自动检测失败片段，驱动源码级修复，而非仅修改prompt或技能文件。

  - **进化与业务部署的结合**：MOSS将进化流程与生产环境深度耦合：基于真实故障批次进行修复、在临时容器中回放原任务验证补丁、通过用户授权后进行容器热替换且支持健康探针回滚，可直接借鉴到需要高可用agent服务的场景。

  - **多阶段pipeline与外部代码工具解耦**：采用标准化七阶段（定位、规划、规划审查、实现、代码审查、任务评估、裁决），并将实际编码委托给可插拔的coding-agent
  CLI（如Claude Code、OpenAI Codex），降低了与具体LLM的耦合，可在自身系统中按需替换代码生成后端。

  - **运行时验证代替单元测试**：在临时容器中运行agent与真实任务交互来验证修复效果，而不是靠单元测试，这对动态、交互式的agent行为验证更为有效，适合推荐系统、对话agent等需要端到端行为验证的场景。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**：应用级自治agent（如OpenClaw）部署后常因harness层（路由、状态管理、dispatch等）的代码缺陷反复失败，但现有自进化系统只进化文本级构件（技能文件、prompt、记忆模式），无法触及harness代码。源码级改写是更通用的进化介质：图灵完备、严格超集文本可改范围、效果确定、不受长上下文稀释影响。本文在开源agent框架OpenClaw上实现MOSS，首次将源码自改写用于生产级agent系统，修复harness层bug。

**方法关键点**：
- 定向进化：从用户会话扫描自动提取失败片段（通过周期扫描和用户标记），以此组成修复批次，非随机突变或基准驱动的探索。
- 多级进化循环：包含基线评估→多次迭代（每轮7个阶段：定位、计划、计划审查、实现、代码审查、任务评估、裁决），直到批次修复或达到瓶颈，输出收敛的代码补丁。
- 外部代码工具解耦：代码修改由可插拔的coding-agent CLI（支持Claude Code等）完成，MOSS只负责流程和裁决。
- 运行时验证：在短暂容器中回放原始失败任务，评估agent行为变化，不使用单元测试。
- 安全热替换：经用户同意后，对运行中容器进行原地镜像替换，挂载同一数据卷保持用户状态，并带健康探针自动回滚。

**关键实验结果**：以OpenClaw + DeepSeek V3.2为基座，选取4个claweval合规审计任务作为进化批次和测试集。单次进化迭代后，4任务平均评分从0.2526提升至0.6100（提升0.3574），其中T138任务从0.209升至0.9049，所有试验均通过0.75阈值。修复直接修改了harness代码（3个文件，177行增加，1行删除），而非技能或prompt。
