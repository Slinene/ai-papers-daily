---
title: 'X-AgentRed: Red-Teaming Personal Agents in Evolving Multi-Service Ecosystems'
title_zh: X-AgentRed：针对多服务生态下个人代理的自演化红队框架
authors:
- Yeonsung Jung
- Zhiyuan Wang
- Zifan Wang
- Vítor Albiero
- Benjamin Newman
- Edoardo Debenedetti
- Ivan Evtimov
- Ninareh Mehrabi
affiliations:
- Meta Reality Labs Research
- Meta Superintelligence Labs
- Meta
- FAIR at Meta
arxiv_id: '2610.13886'
url: https://arxiv.org/abs/2610.13886
pdf_url: https://arxiv.org/pdf/2610.13886
published: '2026-10-09'
collected: '2026-10-13'
category: Agent
direction: Agent 安全红队 · 工具依赖图
tags:
- red-teaming
- personal agents
- tool dependency graph
- execution feedback
- multi-service
- safety
one_liner: 构建工具依赖图并利用执行反馈迭代扩展，系统性发现跨服务有害工具调用路径，显著超越STAC
practical_value: '- 可借鉴工具依赖图构建：梳理电商 Agent 中所有服务工具的 effects（如优惠券领取、订单取消）、harms（资金损失、隐私泄露）与
  preconditions，得到有向图，用于测试组合错误，尤其跨服务如搜索推荐 + 购物车 + 支付。

  - 执行反馈闭环：把尝试执行失败的路径反馈给红队生成器，替换等效工具或细化前置条件，更有效地暴露长尾安全漏洞，适合集成到 Agent CI 红队流程。

  - 用图采样 recipe 而非直接 LLM 生成，能避免模型对常见工具组合的偏好偏差，提升对隐蔽组合的覆盖；电商广告场景可用来检测跨工具异常链路（如优惠券叠加导致价格错误）。

  - 该方法不依赖具体模型，与 STAC 对比提升 1.77x 有害路径率和 2.99x 工具覆盖率，可作为思路引入多服务 Agent 上线前安全评估。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

动机：个人代理连接多个服务，执行工具链可能产生组合有害结果，现有红队方法依赖 LLM 生成路径，受训练先验限制，对不常见工具组合探索不足。

方法：X-AgentRed 通过分析每个工具的效果、潜在危害和执行前置条件，构建有向依赖图；从图中采样 recipe，实例化为真实场景；利用执行反馈进行自演化：对成功产生危害的路径做工具替换以多样化，对失败路径细化阻塞步骤的前置条件以实现进一步执行。

结果：在四个前沿 agentic 模型上，有害路径率平均为 STAC 的 1.77 倍，工具覆盖率平均为其 2.99 倍。
