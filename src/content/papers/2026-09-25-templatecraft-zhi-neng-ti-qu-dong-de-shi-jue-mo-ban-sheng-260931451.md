---
title: 'TemplateCraft: Agentic Visual Template Generation'
title_zh: TemplateCraft：智能体驱动的视觉模板生成
authors:
- Hongjie Yu
- Zhiyuan Fan
- Yuzhe Zhang
- Jiangcun Du
- Zhicheng Gao
- Yuhong Zhang
- Xiaokai Zhan
- Zongshi Xie
affiliations:
- Peking University
- Kuaishou Technology
arxiv_id: '2609.31451'
url: https://arxiv.org/abs/2609.31451
pdf_url: https://arxiv.org/pdf/2609.31451
published: '2026-09-25'
collected: '2026-09-29'
category: MultiAgent
direction: 多智能体视觉模板生成与反馈修订
tags:
- Multi-Agent
- Template Generation
- Planner-Evaluator
- Long-term Memory
- Visual Generation
- Feedback Loop
one_liner: 多智能体系统将自然语言创意转化为可复用的客户端视觉模板，通过 Planner-Evaluator 反馈回滚与记忆提升生成成功率
practical_value: '- **阶段级回滚机制**：Evaluator 先定位最早需要修改的阶段（plan / material / effect workflow），再定向修订，只重跑下游阶段；在电商素材/广告模板生成流水线中可减少全量重试成本，避免单次失败就丢弃整个流程。

  - **持久资产与用户输入分离**：将 style reference 等持久资产打包进模板，用户只替换输入，显式要求生成并使用持久资产能提升跨输入风格一致性；生成式广告创意/商品模板可复用这一设计，把品牌视觉资产固化到模板内部。

  - **长短期记忆配合小模型**：Evaluator 使用长期记忆跨任务存储错误与修订轨迹，上下文接近阈值时压缩为摘要；这种 Reflexion 式经验复用让较小开源模型在复杂多阶段任务上逼近
  GPT-4o Planner-only，适合生产环境控制推理成本。

  - **模板级评测设计**：TemplateBench 每个任务带 5 个固定测试输入，评估生成成功率、adherence、reusability 和跨输入风格一致性；可借鉴到推荐/创意生成场景，不只评单次生成质量，还要评模板或策略在不同用户输入下的泛化复用。'
score: 8
source: arxiv-cs.MM
depth: full_pdf
---

短视频一键内容创作依赖视觉模板，但把创意想法变成可复用、客户端可执行的模板，需要大量人工做资产准备、工具编排和反复调试。现有 Agent 工作主要面向一次性内容生成或常规视频制作，缺少对可复用模板的正式定义和评估。

TemplateCraft 把模板生成拆成四阶段：template planning、material generation、effect workflow generation、protocol compilation。Planner 依据指令、skill library 和工具约束生成 spec 与 workflow；Executor 实际调用生成工具；Evaluator 根据执行反馈和候选输出做诊断，并将修订路由到最早出错阶段：REVISE_PLAN、REVISE_MATERIAL、REVISE_EFFECT_WORKFLOW 或 FINISH。系统维护任务级 stage memory 和跨任务 long-term memory，长期记忆记录历史错误与修订轨迹，上下文接近阈值时压缩为摘要，让开模型在不更新参数的情况下复用经验。Material 阶段会生成模拟用户输入和 persistent assets，其中 persistent assets 作为风格/运动参考打包进模板，用户部署时只替换输入。

实验基于 TemplateBench：60 个来自 KwaiCut 生产模板的任务（30 图像 + 30 视频），每个任务含创意指令、评分规则和 5 个固定测试输入。对比 Planner-only、Planner-CoT、Planner-Evaluator、UniVA 及直接生成基线 Seed / Wan2.6。在相同 Qwen3-VL 基座下，TemplateCraft 将图像/视频模板生成成功率从 56.7%/30.0% 提升到 66.7%/50.0%，TA 从 0.5168/0.4034 提升到 0.6583/0.6534，并取得更高的 TR 和视频 AQ。消融显示，执行反馈、阶段回滚和长期记忆联合作用，尤其对复杂视频任务收益更大；显式要求 persistent assets 能进一步提高跨输入风格一致性。与 GPT-4o Planner-only 对比，在视频 SRc 和 TA 上匹配或超越，但图像 TA 略低。

最值得记住的是：执行反馈驱动的阶段级回滚 + 长期记忆，能让较小开源模型在复杂多阶段模板生成上显著缩小与强模型的差距，同时提升可复用性。
