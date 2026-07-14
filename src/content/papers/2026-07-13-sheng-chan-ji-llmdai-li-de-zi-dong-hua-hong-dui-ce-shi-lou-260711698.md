---
title: 'Agent Hacks Agent: Autoresearch for Production-Agent Red-Teaming'
title_zh: 生产级LLM代理的自动化红队测试：漏洞概念图发现与复用
authors:
- Xutao Mao
- Xiang Zheng
- Cong Wang
affiliations:
- City University of Hong Kong
arxiv_id: '2607.11698'
url: https://arxiv.org/abs/2607.11698
pdf_url: https://arxiv.org/pdf/2607.11698
published: '2026-07-13'
collected: '2026-07-14'
category: Agent
direction: 代理安全 · 自动化红队测试
tags:
- Red-teaming
- Agent safety
- Vulnerability concept graph
- Auto-research
- Falsifiable loop
- Production agents
one_liner: 提出AHA框架，通过假设-伪造-验证循环自动发现代理漏洞，构建跨模型可复用的漏洞概念图
practical_value: '- **代理安全审计可迁移**：对于电商/推荐系统中集成LLM代理（如自动化竞品分析、客服回复生成），可借鉴VCG思路构建安全知识库，持续记录攻击面与使能条件，方便后续系统升级后快速复测。

  - **假设驱动的红队测试降低人工成本**：无需手工编写大量攻击样本，AHA的假设-伪造-验证循环可自动化探索未知漏洞，工程上可用类似沙盒环境对推荐Agent的prompt界面、API调用链路进行持续安全扫描。

  - **跨模型可复用性验证**：观察到漏洞核心在不同模型间重复出现，启示我们：为Gemma、Llama等设计的防护方案在迁移至内部微调模型时仍可能有效，可优先针对VCG中的使能条件设计防御。

  - **场景与通道迁移能力**：VCG从直接攻击（如提示注入）迁移到间接攻击（如通过外部文档污染）有效，意味着推荐系统的多路召回或用户画像注入点可复用同一套漏洞假设进行测试，提升安全覆盖效率。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：生产级LLM代理（如Claude Code、Codex）直接操作文件、命令和状态，安全失败即真实动作，但现有红队工具仅记录攻击成功表面，未捕获导致不安全轨迹的“使能条件”，导致审计、修补和跨版本复用困难。

**方法**：提出AHA，一个可证伪的发现循环：由研究代理生成漏洞假设（如“提示注入可绕过文件读取限制”），构造对应的伪造测试（falsifier），在沙盒中实例化合法攻击并执行，观察代理轨迹后反思是否支持假设，若被证据规则确认则提升为漏洞概念图（VCG）节点。每个概念包含攻击面、使能条件、伪造器、迁移预测及证据，形成结构化、可审计的安全知识图。

**结果**：在Claude Code和Codex上测试三个直接/间接攻击场景，VCG发现的核心漏洞跨模型、跨代理反复出现；冻结的VCG无需进一步搜索，在相同单次攻击协议下攻击成功率比最强冻结基线高14.2个百分点；VCG概念可跨场景及跨攻击通道迁移。
