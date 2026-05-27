---
title: 'FinHarness: An Inline Lifecycle Safety Harness for Finance LLM Agents'
title_zh: 面向金融LLM代理的内联生命周期安全栅栏
authors:
- Haoxuan Jia
- Yang Liu
- Bin Chong
- Yingguang Yang
- Yancheng Chen
- Jiayu Liang
- Qian Li
- Hanning Lu
- Kefu Xu
- Hao Zheng
affiliations:
- Peking University
- Nanyang Technological University
- Tsinghua University
- University of Science and Technology of China
- University of Illinois Chicago
arxiv_id: '2605.27333'
url: https://arxiv.org/abs/2605.27333
pdf_url: https://arxiv.org/pdf/2605.27333
published: '2026-05-26'
collected: '2026-05-27'
category: Agent
direction: 金融代理安全 · 内联安全栅栏
tags:
- Finance LLM Agent
- Safety Harness
- Prompt Injection
- Tool Monitoring
- Cascade Judge
- Inline Lifecycle
one_liner: 通过查询监控、工具监控与级联法官在代理执行中注入安全证据，在保持业务批准率的同时降低攻击成功率并大幅减少高级模型调用。
practical_value: '- **内联安全监控架构**：在Agent执行循环中嵌入查询监控(Query Monitor)与工具监控(Tool Monitor)，用确定性合规先验对每一步打分，防范中间步骤的提示注入攻击，比边界过滤更可靠。

  - **风险窗口级联路由**：通过累加最近5步风险分数 (W=5, θ=1.0) 决定是否调用高级法官，普通步骤仅用轻量法官 (gpt-4o-mini)，高级调用减少4.7倍，平衡安全与成本。电商对话中高风险操作（如大额下单）可借鉴此路由策略。

  - **证据注入促代理自主**：将触发风险的规则信号（如强制词、数量异常、序列违规）作为结构化证据注入Agent输入，让Agent自主选择拒绝、重规划或升级，而非硬阻断，保持流程灵活且不牺牲业务审批率。

  - **双信号有限记忆回顾**：通过风险显著性和共谋（语义相似+实体重叠+信息提供者）召回最多2个历史步骤，法官上下文长度恒定O(1)，避免长轨迹下成本爆炸，适用于多轮对话状态追踪。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**  
金融LLM代理面临提示注入攻击，攻击常分散在多轮中并隐藏在工具调用之间，现有的边界过滤器无视中间步骤，事后LLM法官介入太晚且成本随轨迹长度线性增长。必须在代理执行循环中嵌入内联安全监控，实时评估每一步并反馈安全信号。

**方法关键点**  
- **查询监控**：对用户输入融合单轮意图（如动词层级、金额大小、风险产品标记）和跨轮漂移（如虚假引用、权限跳跃），计算会话级风险累计，带衰减记忆。 
- **工具监控**：对即将执行的工具调用评估权限层级、危险参数、参数范围异常、业务事实矛盾和序列违规（如未经验证的关键写入）。 
- **级联**：累加最近W=5步风险分数，超过阈值θ=1.0则路由至高级法官（gpt-4o），否则用轻量法官（gpt-4o-mini）；同时通过双信号记忆召回最多2个历史步骤，保证上下文大小恒定。 
- **证据动态注入**：所有触发风险的规则头作为结构化证据插入Agent输入，支持代理自主拒绝、重规划或升级，而非外部粗暴阻断。

**关键实验**  
- 在FINVAULT基准（107良性/107攻击）上，路由版FINHARNESS将攻击成功率(ASR)从38.3%降至15.0%，良性审批率仅微降2pp至39.3%，高级法官调用减少4.7倍。 
- 与GuardAgent/InferAct等外部护栏相比，后者ASR极低但审批率崩溃（8.4%），FINHARNESS在安全与业务间取得更优平衡。 
- 在856条合成攻击集上，主动拦截（硬停+自我拒绝+升级）提升6.7pp，自我拒绝率上升15.7pp，体现证据注入的有效性。

**一句话记住**  
FINHARNESS将安全信号作为证据动态注入代理决策循环，让代理自主权衡安全与业务，兼顾拦截率、审批率与高级模型成本。
