---
title: 'MAS-Guard: Unified Guardrails from Individual Agents to Multi-Agent LLM Systems'
title_zh: MAS-Guard：从单智能体到多智能体LLM系统的统一护栏
authors:
- Mohammad Kachuee
- Phu Mon Htut
- Sheng Li
- Nikolaos Pappas
- Miguel Ballesteros Martinez
- Yassine Benajiba
- Sujith Ravi
- Dan Roth
affiliations:
- Oracle AI
arxiv_id: '2610.28397'
url: https://arxiv.org/abs/2610.28397
pdf_url: https://arxiv.org/pdf/2610.28397
published: '2026-10-20'
collected: '2026-10-21'
category: MultiAgent
direction: 多智能体系统安全护栏
tags:
- Multi-Agent
- Guardrails
- Prompt Injection
- LLM Safety
- Agentic AI
one_liner: 统一运行时护栏框架，结合本地A-Guard与系统级Charter/Control Plane，ASR降低71.5-86.3%同时保持效用
practical_value: '- **分离护栏模型与执行业务的Agent模型**：用独立的轻量模型（如Gemma-4-26B-A4B-IT）做安全检查，避免与业务Agent模型耦合，便于统一升级和审计；在电商推荐/广告Agent中可复用此模式，将安全/合规检查从生成链路剥离。

  - **确定性检查优先，语义检查兜底**：对路由、消息格式、能力范围等能用代码确定的规则（如禁止SQL agent直接调邮件服务）先用确定性检查拦截，语义分类器只处理模糊内容；这能大幅降低推理开销和误报，适合高并发线上系统。

  - **统一的干预决策空间（ALLOW/REFLECT/CONFIRM/BLOCK）**：所有local和system guardrail输出同一套决策动作，聚合规则固定为“最严格优先”，避免额外模型仲裁层；在电商多Agent流程中可直接借鉴，用于工具调用、跨Agent消息、用户输入等事件。

  - **对无法instrument的第三方Agent做边界防护**：即使某些Agent是黑盒，只要orchestration层可控，就能在其输入输出边界部署Charter合规检查；这适用于与外部供应商Agent、联盟广告API等交互的场景，保护数据不外泄。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

## 动机
多智能体LLM系统将任务分解给多个角色Agent协作，但分布式权威、异构角色和可能被攻陷的参与者使安全防护更加困难。现有防御各自为战，覆盖局部执行、系统级交互和干预机制时碎片化严重，缺乏统一框架。特别是实际部署中往往混合可instrument的Agent和仅暴露请求-响应接口的opaque Agent，需要跨边界一致的护栏。

## 方法关键点
MAS-Guard提出两层护栏：
- **本地Agent Guardrail (A-Guard)**：集成在可instrument Agent的执行循环中，针对用户输入、工具调用、工具结果等事件应用任务专用专家（如Prompt Injection检测、敏感工具调用检测）。专家使用独立于业务Agent的模型（Gemma-4-26B-A4B-IT）进行判断，并通过自动提示优化（APO）迭代改进。
- **系统级护栏**：开发者定义**Agent Charter**（角色、I/O契约、能力范围）和**Control Plane**（路由策略、消息格式、主题策略等），通过确定性检查（如禁止某路由）和语义检查（如角色违规、内容泄露）共同约束跨Agent交互。
- **统一干预空间**：所有护栏输出归约到ALLOW、REFLECT、CONFIRM、BLOCK四类决策，聚合时采用最严格优先（BLOCK>CONFIRM>REFLECT>ALLOW），避免额外模型决策层。

## 关键实验
在ACIArena、TAMAS、AgentLeak、OmniLeak、OverThink、ASB六个基准上，用GPT-5.6-Terra、Muse-Glimmer-30B、Grok-4.3三种Agent模型评估，对比Sandwich、Delimiter、ACI-Sentinel、LlamaFirewall、ToolSafe、AgentDoG、AgentDoG-1.5、FIDES等八种防御。MAS-Guard将总体攻击成功率（ASR）从27.1%-30.9%降至4.2%-8.8%，相对降低71.5%-86.3%，同时满足良性任务效用参考标准。消融显示A-Guard对单Agent漏洞（ASB、OverThink）贡献最大，语义检查对多Agent注入和隐私泄露（ACIArena、AgentLeak）有互补增益。

## 最值得记住的一句话
将安全护栏与业务Agent模型解耦，并用“确定性结构检查+语义合规检查”双层机制在orchestration层统一拦截，可在不牺牲任务效用的前提下大幅降低多智能体系统的攻击成功率。
