---
title: Analyzing Defensive Misdirection Against Model-Guided Automated Attacks on
  Agentic AI Systems
title_zh: 针对智能体AI自动化攻击的防御性误导分析
authors:
- Reza Soosahabi
- Vivek Namsani
affiliations:
- Keysight Technologies Inc.
arxiv_id: '2606.20470'
url: https://arxiv.org/abs/2606.20470
pdf_url: https://arxiv.org/pdf/2606.20470
published: '2026-06-18'
collected: '2026-06-21'
category: Agent
direction: Agent安全防御 · 误导性反馈
tags:
- Jailbreak Defense
- Misdirection
- Automated Attacks
- Agentic AI
- Prompt Injection
- Adversarial Robustness
one_liner: 提出检测后给出误导性非操作响应，将自动化越狱攻击成功率上界降低两个数量级
practical_value: '- **对话推荐Agent的防注入策略**：当检测到恶意输入时，不要返回统一的拒绝话术（如“我无法回答”），因为这会为自动化攻击提供可预测的反馈信号；改用看似合理但无实际操作的误导性回应，让攻击者误判成功，从而浪费其查询预算。

  - **轻量级误导实现CMPE**：借鉴文中的渐进式上下文误导方法，在对话状态中维护安全的信息片段，检测到恶意意图后逐步递送无关的“安全诱饵”，既保持对话流自然，又避免泄露系统边界。

  - **防御评估指标迁移**：用攻击者的阳性预测值（PPV）替代传统的ASR来评估鲁棒性，更能反映在自动化红队场景下误导策略的有效性，适合在电商搜索Agent上线前做对抗测试。

  - **工程实现建议**：将安全检测与响应生成解耦，检测模块判定恶意度后，将请求转发至专门的“误导生成器”（可用小型微调模型），不增加主流程延迟，对在线服务影响小。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

**动机**：Agentic AI系统频繁使用LLM解释指令、调用工具，使其更易遭受模型引导的自动化越狱攻击。传统检测并阻止（detect-and-block）策略在攻击者拥有大量查询预算时，可预测的拒绝响应会泄露有效反馈，促使攻击成功率（ASR）趋近1。

**方法关键点**：提出检测并误导（detect-and-misdirect）策略——对恶意交互返回受控的非操作响应，故意制造攻击者自动化评判器的误判，从而降低攻击者所选候选的阳性预测值（PPV），理论上将ASR限制在有界范围内。实现了一个轻量级概念验证CMPE（上下文误导渐进式互动），用安全但策略性误导的文本替换可预测的拒绝话术，以此扰乱自动化搜索。

**关键结果**：在多个越狱基准上，CMPE将估计的ASR上界降低了最多两个数量级；在PAIR和GPTFuzz端到端攻击实验中，几乎完全消除了经过验证的攻击成功。
