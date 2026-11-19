---
title: 'PIPETTE: Prompt Injection Purple-Teaming for Robust LLM Agents'
title_zh: PIPETTE：面向鲁棒 LLM 智能体的提示注入紫队框架
authors:
- Lipeng He
- Yihan Wang
- Jiawen Zhang
- N. Asokan
affiliations:
- University of Waterloo
- Zhejiang University
- KTH Royal Institute of Technology
arxiv_id: '2611.24362'
url: https://arxiv.org/abs/2611.24362
pdf_url: https://arxiv.org/pdf/2611.24362
published: '2026-11-17'
collected: '2026-11-19'
category: Agent
direction: LLM Agent 提示注入紫队对抗训练
tags:
- Prompt Injection
- Purple-Teaming
- Adversarial Training
- LLM Agents
- Dictionary Learning
one_liner: PIPETTE用字典学习奖励抑制红队模式坍塌，以on-policy对抗训练提升LLM Agent抗提示注入鲁棒性
practical_value: '- 在电商/Agent 场景，商品详情、评论、消息、工具输出等不可信文本都是 indirect prompt injection
  面；可参考 PIPETTE 的 on-policy 对抗训练，将攻击样本与正常任务混合微调，避免只学会拒绝导致用户体验下降。

  - 内部红队不要只盯 ASR：直接用现有 RL 方法容易模式坍塌。引入基于字典学习的多样性 reward，能发现更多样的注入策略，适合构造更全面的安全回归集。

  - 防御评估需增加 adaptive attacker 测试，不能只看静态攻击；否则上线后可能被绕过。可把红队-防御做成持续紫队流水线，新攻击每轮进入训练。

  - 对低风险场景，若训练成本受限，至少应做输入过滤和 instruction hierarchy；PIPETTE 的静态近零 ASR 可作为强防御参考，但其主要收益在高风险
  Agent 产品。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**
LLM agent 处理不可信外部数据时易受间接提示注入（IPI）攻击。现有 RL 红队方法（RL-Hammer、PISmith）虽能达到高 ASR，但存在模式坍塌，反复发现相似攻击，导致后续对抗训练带来的鲁棒性提升有限。

**方法**
PIPETTE 是统一紫队框架，将红队发现转化为防御收益。红队侧引入基于字典学习的奖励，鼓励覆盖更广攻击策略；防御侧采用面向 IPI 的 on-policy 对抗训练，使 agent 在抵抗攻击的同时完成正常用户任务。

**结果**
在 AgentDojo 与 ASB 基准上，PIPETTE 训练的 defender 对静态攻击实现近零 ASR，并能抵御强自适应攻击；良性任务 utility 与未防御基线接近。
