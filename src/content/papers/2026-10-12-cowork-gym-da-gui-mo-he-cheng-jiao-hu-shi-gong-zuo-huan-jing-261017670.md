---
title: 'Cowork-Gym: Synthesizing Interactive Work Environments at Scale'
title_zh: Cowork-Gym：大规模合成交互式工作环境
authors:
- Anni Zou
- Cheng Chen
- Jiaji Deng
- Weikang Zhou
- Xinji Mai
- Yue Wu
- Jianing Lin
- Lipeng Xie
- Lixiong Qin
- Qingyue Zhao
affiliations:
- Alibaba Token Foundry
arxiv_id: '2610.17670'
url: https://arxiv.org/abs/2610.17670
pdf_url: https://arxiv.org/pdf/2610.17670
published: '2026-10-12'
collected: '2026-10-17'
category: Training
direction: Agent 环境合成与后训练
tags:
- Cowork agents
- environment synthesis
- post-training
- on-policy distillation
- user simulator
one_liner: 用构建-执行-修订循环合成64.9K个Cowork环境，后训练小模型在多个Agent基准上大幅超越基座
practical_value: '- **用执行反馈自动修复生成环境**：在电商/Agent场景中构建训练数据时，可引入 build-execute-revise
  循环，把任务目标的可行性、工具可执行性、用户行为一致性和成功标准都纳入自动校验，避免人工审核，提高数据质量和规模。

  - **有状态用户模拟器设计**：模拟用户不只输出对话，还直接编辑共享工作区（如购物车、订单、商品列表），这让 Agent 训练更接近真实多轮交互。推荐系统对话模拟或电商客服
  Agent 训练可借鉴此模式。

  - **多阶段后训练配方**：SFT + RL + on-policy distillation 的组合让 9B 小模型在 Agent 基准上平均提升 8.7
  点，对于业务中缺乏大模型成本的团队，可参考此低成本训练方案提升自研小模型能力。

  - **环境多样性与场景覆盖**：14 个场景、64.9K 任务规模证明合成数据在覆盖长尾工作流上的价值，类似思路可用于生成大量电商用户任务流（如比价、凑单、多条件筛选）来训练
  Agent。'
score: 7
source: huggingface-daily
depth: abstract
---

## 动机
Cowork Agent 需要处理工具、文件依赖和用户动态修改共享工作区的需求，但现有环境往往无法保持任务目标、可执行资源、用户行为和成功标准之间的一致性，难以大规模训练和评估。

## 方法关键点
- 提出 Cowork-Gym 框架，通过 build–execute–revise 循环合成环境：先用构建器生成任务，再实际执行获取证据，结合审查反馈验证并修复环境，确保一致性与可执行性。
- 设计有状态用户模拟器，不通过固定脚本而是以对话和直接编辑共享工作区的方式对 Agent 行为做出反应，更贴近真实 Cowork 动态。
- 合成 64.9K 个环境，覆盖 14 个应用场景；用这些环境对 9B、27B、35B-A3B Qwen 模型进行后训练，包含 SFT、RL 和 on-policy distillation。

## 关键结果
- 在六个 Agent 基准上，后训练模型比基座平均提升 8.7、6.4、4.1 个点。
- Ours-27B 在总榜排名第二，在 PawBench 和 ClawEval 上平均得分最高，超过总参数量超 100B 的对比模型。
