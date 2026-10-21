---
title: Harness Self-Evolution for Long-Horizon Terminal Agents
title_zh: 长程终端智能体的 Harness 自进化框架
authors:
- Ruhan Wang
- Yucheng Shi
- Zongxia Li
- Junyao Yang
- Zhongzhi Li
- Yue Yu
- Haitao Mi
- Dongruo Zhou
- Leoweiliang
affiliations:
- Tencent HY LLM Frontier
- Indiana University
- University of Maryland, College Park
- University of Georgia
- National University of Singapore
arxiv_id: '2610.27435'
url: https://arxiv.org/abs/2610.27435
pdf_url: https://arxiv.org/pdf/2610.27435
published: '2026-10-19'
collected: '2026-10-21'
category: Agent
direction: Agent 执行脚手架自优化
tags:
- Agent Harness
- Self-Evolution
- Terminal Agents
- Runtime Monitor
- Reliability
- LLM Agents
one_liner: 固定模型权重，通过成功/失败对照轨迹与运行时监控证据迭代改进 agent harness，提升任务可靠性与成功率
practical_value: '- 建立 agent 运行时监控，不只记录模型轨迹，还记录 harness 执行事件（命令执行、反馈、上下文裁剪、完成判定），与任务成败标签关联，定位系统性问题。

  - 选取“同一配置下既有成功又有失败”的任务作为诊断单元，用成功轨迹作免费参考，无需人工标注即可发现可靠性缺口。

  - 维护一份 Harness Handbook，把失败证据映射到源码与行为，便于跨任务复用问题模式；优先优化共享机制而非单点 patch。

  - 引入候选 harness 变更前先做行为校验和重复评测，通过后再迭代；固定模型权重、只改执行层，对生产系统风险更低。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：长程终端 agent 单次能成功但多次运行不稳定，随机错误会沿动作与上下文传播。模型能力具备但执行可靠性不足，harness 控制命令执行、反馈、上下文管理与完成判定，是提升一致性的直接切入点。

**方法关键点**：
- 提出 RiseHarness，在模型权重固定下迭代改进 harness；
- 聚焦“可翻转任务”：同一配置下同时存在成功与失败运行，成功运行提供基准和失败分析参考；
- 运行时监控器同时采集 agent 轨迹与 harness 内部执行痕迹，分析模型动作如何与命令执行、反馈、上下文管理和完成决定交互；
- Harness Handbook 将证据映射到 harness 行为与源码，识别跨任务共享机制中的重复问题；
- 从其他 harness 框架搜索相关实现作为设计参考，适配当前模型与执行协议；
- 候选改动经过行为检查与重复任务评估，有效版本进入下一轮迭代，持续融合不同框架的合适机制。

**关键结果**：在多个模型上评估任务成功率与可靠性；消融实验验证 harness 执行证据与外部调研的贡献；在同模型未见基准上验证迁移性。摘要未给出具体数值，但核心增益来自成功/失败对照执行证据与跨框架机制复用。
