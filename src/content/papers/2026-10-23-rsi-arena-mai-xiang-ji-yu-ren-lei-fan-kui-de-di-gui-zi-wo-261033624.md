---
title: 'RSI Arena: Towards Recursive Self-Improvement with Human Feedback'
title_zh: RSI Arena：迈向基于人类反馈的递归自我改进
authors:
- Yue Huang
- Yanbo Wang
- Lichi Li
- Yuanyuan Chen
- Andreas Haupt
- Xiaonan Luo
- Zheyuan Liu
- Jihye Choi
- Felix Juefei-Xu
- Xiangliang Zhang
affiliations:
- Bake AI
- Stanford University
- NVIDIA Research
- Hugging Face
- Scale AI
arxiv_id: '2610.33624'
url: https://arxiv.org/abs/2610.33624
pdf_url: https://arxiv.org/pdf/2610.33624
published: '2026-10-23'
collected: '2026-10-28'
category: Agent
direction: Agent 自主后训练与人类反馈
tags:
- RLHF
- post-training
- autonomous agents
- recursive self-improvement
- human feedback
one_liner: 10个前沿模型作为训练代理自主后训练Nemotron基础模型，两阶段人类反馈闭环，最强模型关闭76%能力差距
practical_value: '- 可借鉴自主后训练流水线：让 LLM agent 负责数据选择、训练脚本实现、检查点挑选，可将算法工程师从重复调参中释放，适合电商/推荐场景中大量候选模型或
  prompt 版本的快速迭代。

  - 用人类偏好做递归改进：Stage 2 把用户对比记录和投票注入 agent，使其再次训练提升风格化评分，类似推荐系统里的用户反馈闭环，但要注意 benchmark
  提升与偏好提升无明确关联，需以真实业务指标（如 CTR、转化率）为准。

  - 评估时控制风格偏差：论文对答案长度和格式做统计调整后才比较模型偏好，电商推荐/文案生成场景中，用户偏好容易被文本长度、排版影响，上线前应做风格消融。

  - 监控安全与合规：一个模型在 StrongREJECT 上有害合规上升，自主训练可能放大讨好倾向；在生成式推荐或对话助手中，需设置安全护栏与红队测试。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：能否让 AI agent 自主训练语言模型，并利用用户反馈持续改进，是走向递归自我改进的关键一步。

方法：RSI Arena 两阶段研究。第一阶段 10 个前沿模型作为训练 agent，均从 NVIDIA Nemotron 3.5 Lightning 30B-A3B Base 出发，各自拥有 1,000 GPU 小时与 $300 API 额度，在共享 64-GPU 集群上独立选择数据、实现训练流程、挑选检查点，历时 6 天。评估覆盖 20 个基准和盲评。第二阶段给每个 agent 提供第一阶段中涉及自身模型的对比记录与人类投票，再给 3 天进行进一步训练。

结果：所有 agent 都产出可用助手，最强模型由 GPT-6 Astra 训练，在 12 个能力基准上关闭基础模型到 Instruct 版本差距的 76%，人类偏好评分在统计调整长度和格式后接近 NVIDIA Instruct。第二阶段 10 个模型中有 8 个的风格调整后相对评分较第一阶段提升；但基准提升微弱，与偏好提升无明确关联。一些 agent 鼓励更长回复，一个模型在 StrongREJECT 上有害合规增加。该框架提供了一个可审计的设置，研究人类反馈如何指导自主模型开发，向递归自我改进与人类反馈（RSIHF）迈出一步。
