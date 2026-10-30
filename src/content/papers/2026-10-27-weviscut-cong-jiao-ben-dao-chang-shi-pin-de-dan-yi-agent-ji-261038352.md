---
title: 'WeVisCut: The Whole Editing Room in One Agent From Narration to Long-Form
  Video'
title_zh: WeVisCut：从脚本到长视频的单一 Agent 编辑系统
authors:
- Chenyu Mu
- Wenming Weng
- Qinrui Wang
- Xingsong Ye
- Hao Yu
- Jun He
- Chong Sun
- Chen Li
- Jing Lyu
- Erkun Yang
affiliations:
- Xidian University
- WeChat Vision, Tencent Inc.
arxiv_id: '2610.38352'
url: https://arxiv.org/abs/2610.38352
pdf_url: https://arxiv.org/pdf/2610.38352
published: '2026-10-27'
collected: '2026-10-30'
category: Agent
direction: 长视频编辑 Agent 策略学习与蒸馏
tags:
- Agent
- Video Editing
- Policy Learning
- Tool Use
- Distillation
- Long-form Video
one_liner: 用离线反推编辑决策训练9B策略，在统一工具环境中逼近Claude Opus 5且token减少33倍
practical_value: '- 从成品反推决策的 inversion + verified replay 管线值得借鉴：在推荐/广告的多步决策场景（如会话式推荐、创意生成）中，可以用线上成功案例反推隐式决策链，并通过回放验证构造高质量监督数据，训练小模型逼近大模型。

  - 状态化 Agent harness（共享生产状态、工具反馈驱动决策与修复）可迁移到电商 Agent 架构，统一维护商品/素材/用户状态，支持多轮工具调用的一致性和自我纠错。

  - 紧凑策略蒸馏思路：9B 模型达到大模型相当效果且 token 减少 33 倍，适合成本敏感的实时推荐/广告文案生成；通过任务特化监督而非通用多阶段工作流，显著降低推理成本。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：长视频从脚本生成需要跨镜头一致且连贯的决策，现有多阶段 agentic 编辑器依赖通用模型，质量与成本权衡不清。  
**方法关键点**：WeVisCut 构建了连接工具执行与策略学习的系统。其 agent harness 维护共享生产状态，使工具反馈指导后续决策和修复。由于成品视频不暴露编辑决策，作者设计四阶段数据管线，结合 editing inversion 和 verified replay，从 3,750 个成品视频恢复编辑意图，生成超 130K 训练样本。用这些监督训练一个 9B 策略，在同一 harness 内协调生产并处理失败；同时提出 100-task 基准和五个指标评估编辑质量与交付可靠性。  
**关键结果**：在共享工具环境下，WeVisCut 显著优于基础模型，与 Claude Opus 5 性能相当，但每个成功输出分钟使用的生成 token 减少近 33 倍；在提出的指标上超过 task-matched 原生编辑器。
