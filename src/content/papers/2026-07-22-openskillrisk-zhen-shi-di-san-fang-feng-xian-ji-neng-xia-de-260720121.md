---
title: 'OpenSkillRisk: Benchmarking Agent Safety When Using Real-World Risky Third-Party
  Skills'
title_zh: OpenSkillRisk：真实第三方风险技能下的智能体安全基准
authors:
- Qiyuan Liu
- Tingfeng Hui
- Kun Zhan
- Kaike Zhang
- Ning Miao
affiliations:
- City University of Hong Kong
- Beijing University of Posts and Telecommunications
- Li Auto Inc.
arxiv_id: '2607.20121'
url: https://arxiv.org/abs/2607.20121
pdf_url: https://arxiv.org/pdf/2607.20121
published: '2026-07-22'
collected: '2026-07-23'
category: Agent
direction: LLM Agent 安全基准评测
tags:
- Agent Safety
- Benchmark
- Third-Party Skills
- Risk Assessment
- LLM Evaluation
one_liner: 构建含263个真实风险技能的基准，揭示LLM智能体在规避第三方工具风险时的不足
practical_value: '- 在构建面向电商场景的客服Agent或推荐助手时，若需集成第三方工具或自定义技能，可借鉴OpenSkillRisk的分类体系（七类威胁）进行安全风险预审，避免部署后出现有害行为。

  - 重点关注“上下文敏感风险”和“系统级风险”，这类风险在当前最安全的配置下仍有17%的执行率，需在代码审查和沙箱测试中额外设计针对性的检测用例。

  - 分析三种典型失败模式：未识别风险、识别后未阻止、执行超出用户意图。可在Agent框架中引入“风险识别→人工确认→执行”的防御回路，或通过提示工程强化LLM对恶意指令的警觉性。

  - 若自研Agent平台支持外部开发者上传技能（类似插件市场），可参考该基准构建自动化安全扫描流水线，将技能描述与沙箱执行结果结合进行风险评估。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：LLM智能体在开放环境中常调用第三方技能，但这些技能可能隐含仅在执行时才暴露的安全风险，现有基准对此类真实风险的覆盖不足。

**方法**：构建OpenSkillRisk基准，从公共技能市场收集263个风险技能，按威胁类型分为七类，为每个技能配标准化用户任务及沙箱环境。在三个CLI智能体框架（Cognee、CrewAI、LangChain）和13个主流LLM上执行受控评估，诊断智能体的安全行为模式。

**关键结果**：所有系统均无法可靠处理风险技能，最安全配置下仍有约17%的案例执行了不安全动作；上下文相关风险和系统级风险尤其难以规避。行为分析揭示三种重复失败模式：未识别风险、识别后未及时干预即执行、超出用户意图范围执行技能指令。
