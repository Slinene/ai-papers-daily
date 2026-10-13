---
title: 'Encore: Few-Shot Agentic Discovery of Manipulation Strategies'
title_zh: Encore：从少量演示中发现操控策略的 Agent 框架
authors:
- Yifan Kang
- Zihan Wang
- Zhiwen Fan
- Bangya Liu
affiliations:
- Massachusetts Institute of Technology
- 22077AI Open Source Foundation
- Texas A&M University
- University of Wisconsin–Madison
arxiv_id: '2609.37359'
url: https://arxiv.org/abs/2609.37359
pdf_url: https://arxiv.org/pdf/2609.37359
published: '2026-09-29'
collected: '2026-10-13'
category: Agent
direction: Agent 从少量演示中提取策略并编程执行
tags:
- Few-shot
- Coding Agent
- Policy Discovery
- Demonstration Pack
- Robot Manipulation
one_liner: 把少量演示作为证据包供编程 Agent 研读并迭代改写策略，冻结后评估不暴露成功信号
practical_value: '- 可借鉴「演示即证据」的思路：在电商 Query 改写、广告文案生成或推荐策略决策中，将少量高质量成交/高点击样本的结构化轨迹（关键行为事件、状态变化）作为
  prompt 上下文，让 LLM 从中归纳策略，而不是重新训练或微调。

  - 固定感知/动作 API 的抽象很有用：给 Agent 暴露一组受限的领域函数（如召回、过滤、排序、出价），让 Agent 组合生成可执行策略程序，比自由文本输出更可控、可上线。

  - 开发期允许少量 rollout 调试迭代，但最终 sealed evaluation 不反馈成功信号，可以防 Agent 过拟合评估指标或奖励黑客；迁移到线上测试时，冻结策略后用无偏指标评估。

  - 确定性信息蒸馏：把演示/日志压缩为多视角关键帧、事件片段等结构化 pack，能降低 LLM 读取长流程的负担；在用户行为序列建模中，可提取关键行为事件、商品切换等作为总结性证据输入。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：机器人任务通常用一句话描述，缺少抓取方式、接触顺序、目标状态等实现细节，仅凭指令的 Agent 必须靠试错搜索。已有 coding agent 能编写、运行和调试程序，但难以从零发现操控策略。

**方法关键点**：ENCORE 将少量演示作为证据而非训练数据。确定性 builder 把每个演示蒸馏成一个 pack，包含多视角关键帧、夹爪事件、帧条和完整轨迹。coding agent 研究该 pack，基于固定的感知与动作 API 编写策略程序，在少量 development rollouts 上迭代 refine，最后冻结并在 sealed evaluation 中评估，全程不暴露成功信号。

**关键结果**：在 LIBERO-PRO 上，有演示时首个程序已在半数扰动任务中成功，1 个任务无演示成功；冻结程序以 96.3% 胜过同语言模型的最强先前 agentic 系统（89.3%）。在 RoboDojo 指令未说明目标的任务中，无演示时没有程序成功。真实双手机器人上，用 5 个演示学会立方体交接与杯子翻转。
