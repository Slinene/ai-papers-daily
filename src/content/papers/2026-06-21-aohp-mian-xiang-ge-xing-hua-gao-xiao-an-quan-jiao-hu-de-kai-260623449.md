---
title: 'AOHP: An Open-Source OS-Level Agent Harness for Personalized, Efficient and
  Secure Interaction'
title_zh: AOHP：面向个性化、高效、安全交互的开源OS级代理框架
authors:
- Shanhui Zhao
- Jiacheng Liu
- Guohong Liu
- Jichao Yan
- Jialei Ye
- Yuhao Yang
- Hao Wen
- Shizuo Tian
- Yizhen Yuan
- Yuxuan Chen
affiliations:
- Tsinghua University
- Peking University
- The University of Hong Kong
arxiv_id: '2606.23449'
url: https://arxiv.org/abs/2606.23449
pdf_url: https://arxiv.org/pdf/2606.23449
published: '2026-06-21'
collected: '2026-06-24'
category: Agent
direction: OS级代理原生支持
tags:
- OS-level Agent
- Android
- Personalization
- Efficiency
- Security
- Open-Source
one_liner: 将AI代理视为一等OS角色，通过个性化服务组合、高效接口与安全信息流，提升任务完成率21.12%，降低51.55% token成本
practical_value: '- **移动端Agent架构设计**：将Agent作为OS一等公民的思路可直接用于电商/购物助手App，实现跨应用（如搜索、商品详情、支付）的无缝服务组合，提升用户转化。

  - **降低LLM调用成本**：高效代理接口通过系统级能力暴露减少对LLM的频繁调用，在需要多步推理的推荐场景（如对比商品、下单建议）中可显著节省token消耗。

  - **敏感数据安全控制**：细粒度信息流隔离机制适用于处理用户支付、地址等隐私数据，在推荐系统集成支付或用户画像查询时可借鉴其权限分级策略。

  - **真实环境评测基准**：开源的AOHP平台可作为移动端Agent能力评测的测试床，用于验证搜索推荐Agent在Android系统中的实际表现与安全合规性。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有消费级操作系统（如Android）以应用为中心，缺乏对AI Agent的原生支持，导致执行开销大、安全风险高，阻碍了Agent的广泛部署。随着Agent从单一对话界面走向系统级任务编排，业界急需一个开放的OS级Agent研究平台。

**方法**：基于Android开源项目（AOSP）构建AOHP，将Agent设计为OS的一等角色。核心包括三个机制：(1) **个性化服务组合**：根据用户上下文动态链接多个应用能力，实现跨应用的无缝任务流；(2) **高效Agent接口**：提供标准化的系统服务访问接口，大幅减少Agent对LLM的反复询问，降低token消耗与延迟；(3) **安全信息流**：引入基于标签的访问控制，确保Agent操作始终符合用户隐私策略，防止敏感数据泄漏。

**结果**：在覆盖OS核心能力的挑战性任务上，相比传统应用内Agent方案，AOHP实现任务完成率提升21.12%，执行成本（token消耗）降低51.55%，安全策略合规性也显著优于基线。
