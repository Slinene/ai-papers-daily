---
title: LLM agent safety, multi-turn red-teaming, jailbreak benchmarks, adversarial
  robustness, safety-critical systems
title_zh: NRT-Bench：安全关键控制室中LLM操作员代理的多轮红队测试基准
authors:
- Hanwool Lee
- Dasol Choi
- Bokyeong Kim
- Seung Geun Kim
- Haon Park
affiliations:
- AIM Intelligence
- KAERI
arxiv_id: '2606.20408'
url: https://arxiv.org/abs/2606.20408
pdf_url: https://arxiv.org/pdf/2606.20408
published: '2026-06-18'
collected: '2026-06-22'
category: Agent
direction: Agent安全 · 多轮红队测试
tags:
- LLM agent safety
- multi-turn red-teaming
- jailbreak benchmarks
- adversarial robustness
- safety-critical systems
one_liner: 构建多轮红队基准，揭示LLM代理在自适应攻击下高度脆弱，且模型间漏洞互不重叠。
practical_value: '- 对推荐/对话Agent做安全评估时，可借鉴**多轮自适应攻击模拟**，而非单次注入，更贴近真实用户恶意交互。

  - 防御措施可能**互相抵消甚至反效果**：在客服Agent中叠加安全模块前，务必针对具体模型做A/B测试，不能通用假设有效。

  - **客观危害指标**（如业务指标下降、用户流失）比LLM-Judge文本判断更可靠，可用于推荐系统的安全离线评估。

  - 多个模型漏洞几乎互斥，提示在Agent链中**组合不同LLM**可能提升鲁棒性，但需避免单点被突破。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

**动机**：LLM代理被越来越多地用于安全关键系统，但在持续、自适应的多轮对抗压力下的鲁棒性仍不清楚。现有评估大多限于单轮或依赖LLM判断安全，缺乏对物理/系统级危害的客观衡量。

**方法**：提出NRT-Bench，模拟核电站控制室，五个LLM操作员维护六项关键安全功能（CSFs）。攻击者通过四条通道注入消息，每轮根据反馈调整策略，目标导致任一CSF丢失。危害定义为系统客观状态（CSF丢失即停止），而非文本判断。评估四个前沿模型，采用固定攻击配对重放协议。

**关键结果**：自适应多轮攻击使8.7%~12.1%的会话导致安全功能丢失。模型看似鲁棒性相近，但失败会话几乎不重叠：149次攻击中，无一同时击败所有模型，而三分之一至少击败一个，表明漏洞近乎互斥。添加防御的效果高度依赖模型：同一防护栈或安全顾问代理可能降低一个模型的攻击成功率，却提高另一个模型的成功率。
