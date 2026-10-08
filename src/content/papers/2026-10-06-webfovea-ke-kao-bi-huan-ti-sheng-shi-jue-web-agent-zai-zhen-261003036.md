---
title: 'WebFovea: When the Model Is Right but the Click Is Wrong -- Reliable Round
  Trips for Vision-Based Web Agents on Live Websites'
title_zh: WebFovea：可靠闭环提升视觉 Web Agent 在真实网站上的表现
authors:
- Jiangang Han
affiliations:
- Independent Researcher
arxiv_id: '2610.03036'
url: https://arxiv.org/abs/2610.03036
pdf_url: https://arxiv.org/pdf/2610.03036
published: '2026-10-06'
collected: '2026-10-08'
category: Agent
direction: Web Agent 可靠执行与工程硬化
tags:
- Web Agent
- Harness Reliability
- Multimodal LLM
- Browser Automation
- Failure Analysis
one_liner: 通过硬化解析、执行、观测、信息呈现四阶段，同一模型成绩从31.0升至57.0
practical_value: '- 把 agent 环路拆成 parse → execute → observe → prompt 四阶段，分别监控和加固；业务里常只调模型，但瓶颈常在
  harness，同一模型换 harness 可大幅提分。

  - 真实网页自动化要处理坐标缩放（论文中曾所有点击落在 3/4 坐标处）、iframe、原生下拉框和文本框的静默失败；建议统一坐标空间并加执行后状态校验，必要时降级为
  DOM/JS 操作。

  - 对 LLM 输出做严格 schema 校验和清洗，防止 chat-template 自生成 token 污染动作序列；记录失败样本用于回归。

  - 设置 guardrails 管理预算和规则约束，避免 Agent 越界或浪费步骤；可将不同步骤路由到不同模型平衡成本与效果。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：WebRetriever Challenge 2026 Protocol III 要求从真实网站入口自主操作并返回可验证答案。模型能力必要但不充分，失败常发生在模型与页面之间的 harness 层。

方法关键点：WebFovea 将每步动作视为四阶段往返：模型回复解析为动作、动作在页面生效、结果准确回报、模型获得所需信息。针对四阶段硬化：修正坐标空间不匹配（曾使每次点击落在目标坐标的 3/4 处）；处理原生下拉框、iframe、文本框中的静默失败；清理自生成 chat-template token 对 4.9% 任务集的污染；增加 guardrails 约束规则与预算。

关键结果：同一模型四次提交，官方隐藏集得分从 31.0 升至 57.0，最终排名第 2（满分 100）。提升主要来自 harness 改动而非模型更换，且提供负结果与失败分析。
