---
title: 'Dual Exam: Controlled Evaluation of Multimodal Agents and World Models'
title_zh: 双考：多模态智能体与世界模型的受控评估
authors:
- Zhefan Rao
- Meng Chu
- Xuan Zhang
- Jingfan Chen
- Guohao Cai
- Runyi Li
- Shiyi Du
- Ning Lu
- Xu Huang
- Zhixuan Chen
affiliations:
- 香港科技大学
- 新加坡国立大学
- 香港理工大学
- 东京大学
- 卡内基梅隆大学
arxiv_id: '2610.31066'
url: https://arxiv.org/abs/2610.31066
pdf_url: https://arxiv.org/pdf/2610.31066
published: '2026-10-21'
collected: '2026-10-26'
category: Eval
direction: 多模态 Agent 与世界模型评估
tags:
- Multimodal Agents
- World Models
- Evaluation
- Benchmark
- Controlled Evaluation
one_liner: 提出 Dual Exam 框架，分别评估多模态 Agent 与世界模型，发现两者任务表现不均且耦合成功率低
practical_value: '- 将 Agent 的动作选择与状态演化分开评估：在电商对话推荐、广告策略自动出价等场景中，先用固定环境响应测 Agent 决策，再固定动作序列测
  World Model 预测，可解耦定位问题。

  - 构建任务相关状态保持的专项 check：论文揭示 Agent 常丢失任务相关状态，实际推荐/搜索多轮对话中可加入状态保持测试用例，防止遗忘用户偏好、已选商品等关键上下文。

  - 对于用 World Model 模拟用户反馈/市场响应的团队，需独立验证其 action-conditioned 预测准确率，不能仅靠端到端耦合成功率；150
  例耦合实验零成功说明耦合评估会掩盖组件缺陷。

  - 评测集设计采用“固定环境响应/固定动作干预”对照，可迁移到线上 Agent 评测系统，区分策略错误和模型预测错误，降低归因成本。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：World Models 通过模拟经验支持 Multimodal Agents，而 Agent 轨迹可反哺 World Model 改进。但耦合成功率无法区分动作选择错误和状态演化错误，导致故障诊断困难。

**方法关键点**：设计 Dual Exam 评估框架，将两组件解耦：Agent 轨道在固定环境响应机制下评估动作选择，覆盖 1,088 个条目、15 个报告类别、10 个配置；World Model 轨道在固定动作干预下评估状态演化，包含 400 个案例、8 个场景，其中 15 个配置全覆盖，1 个覆盖 6 个场景。另进行 150 个案例的耦合试点，观察单配对端到端成功率。

**关键结果数字**：GPT 6 Astra 在 case-weighted Agent Index 上领先（31.3），GPT-Image-2 在全覆盖 World Model Overall 上领先（21.7）；两者任务和指标不同，不可直接比较。150 案例耦合试点中任务成功数为零，凸显组件级诊断的必要性。结果揭示任务表现不均和无法保持任务相关状态的普遍问题，但分数对预测耦合成功或持续互学习的价值尚未确立。
