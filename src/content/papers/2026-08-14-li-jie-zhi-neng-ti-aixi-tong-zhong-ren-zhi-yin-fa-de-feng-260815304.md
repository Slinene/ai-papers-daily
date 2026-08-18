---
title: Understanding Cognition-Induced Risks in Agentic AI Systems
title_zh: 理解智能体AI系统中认知引发的风险
authors:
- Guanchu Wang
- Qinuo Li
- Mengnan Du
- Xia Hu
- Bowen Zhou
affiliations:
- Shanghai Artificial Intelligence Laboratory
- The Chinese University of Hong Kong, Shenzhen
- Tsinghua University
arxiv_id: '2608.15304'
url: https://arxiv.org/abs/2608.15304
pdf_url: https://arxiv.org/pdf/2608.15304
published: '2026-08-14'
collected: '2026-08-18'
category: Agent
direction: Agent 认知风险分层与治理策略
tags:
- Agentic AI
- Cognitive Risks
- Human Agency
- Safety
- Controllability
- LLM Agents
one_liner: 按物理、社会、自我指涉三层次认知框架，系统分析LLM智能体对人类能动性与控制权的风险及缓解策略
practical_value: '- 在电商Agent（自动选品、生成广告文案、push消息推送）上线前，可按三层认知框架设计审计清单：物理层检查工具调用与API权限，社会层审查对用户意图的操纵与隐私风险，自我指涉层防止目标漂移或自修改配置，逐层分级放行。

  - 将“人类能动性、自主性、控制能力”作为核心指标纳入Agent评估集与在线监控；对涉及用户情绪或社会影响的推荐文案、自动客服等场景，强制保留人类审批节点。

  - 对具备长期记忆或自我修正能力的推荐Agent，设置自我指涉风险检查点：定期比对当前目标与原始业务目标，避免过度个性化导致的信息茧房或目标篡改。

  - 架构上采用“最小权限+风险隔离”：Agent调用外部数据和服务时，按认知层级分配权限——物理层只给只读API，社会层需人工确认，自我指涉层禁止自动改写自身prompt或工具配置。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：前沿LLM Agent从任务执行扩展到办公、金融、创意研究等认知与社交工作流，其类人认知能力带来对人类社会的系统性影响，但既有风险分析多局限于任务边界，未充分覆盖认知扩展引发的能动性与控制问题。

方法关键点：提出按认知范围划分的三层风险框架：物理认知层关注Agent与物理世界及工具交互的失控风险；社会认知层关注对社会舆论、人类意图操纵、隐私侵蚀等影响；自我指涉认知层关注Agent对自身目标、记忆、自我改进的失控。每层分别对应分析对人类能动性、自主性、控制能力的侵蚀路径。最后给出缓解策略，包括提升可解释性、人机协同决策、限制自我修改权限、按认知层级动态评估与管控等。

关键结果数字：该文为IEEE主题文章，未包含量化实验或基准测试，主要贡献为风险分类学与治理框架。
