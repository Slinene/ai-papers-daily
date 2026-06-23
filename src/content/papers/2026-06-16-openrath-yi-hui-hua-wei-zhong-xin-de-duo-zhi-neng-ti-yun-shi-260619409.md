---
title: 'OpenRath: Session-Centered Runtime State for Agent Systems'
title_zh: OpenRath：以会话为中心的多智能体运行时状态管理
authors:
- Fukang Wen
- Zhijie Wang
- Ruilin Xu
arxiv_id: '2606.19409'
url: https://arxiv.org/abs/2606.19409
pdf_url: https://arxiv.org/pdf/2606.19409
published: '2026-06-16'
collected: '2026-06-23'
category: MultiAgent
direction: 多智能体运行时状态抽象
tags:
- Agent Runtime
- Session State
- Multi-Agent Systems
- OpenRath
- Runtime Abstraction
- Agentic Workflow
one_liner: 提出 Session 作为一等运行时值，统一多智能体系统的状态、分支与审计
practical_value: '- **复杂 Agent 工作流的状态审计与复现**：在电商推荐的多步 Agent 决策（如用户意图理解→多路召回→融合排序）中，可将
  Session 作为贯穿全流程的一等对象，统一记录工具调用、沙箱操作、内存事件和上下文压缩证据，便于事后复现线上异常或离线评估策略分支。

  - **显式分支与合并支持策略探索**：推荐 Agent 经常需要并行探索多种召回理由或排序策略，当前依赖外部编排或硬编码，OpenRath 的 fork /
  merge 操作可直接内嵌到运行时，让 Agent 自行分支验证再择优合并，降低工程复杂度。

  - **Selector 路由控制流**：将控制流决策抽象为 Selector，Agent 可依据 Session 状态动态选择下一步动作（如调用哪个子 Agent
  或工具），这对构建自适应推荐流水线（例如根据用户行为密度切换简单规则与 LLM 推理）有直接参考价值。

  - **后端无关与可组合设计**：Session 抽象屏蔽了底层存储、沙箱与 LLM 提供商的差异，便于在离线实验与线上部署之间迁移，同时 Workflow 的第一类定义能简化多团队协作开发推荐系统的
  Agent 组件。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现代 Agent 系统常面临运行时状态碎片化——对话脚本、工具副作用、内存事件、工作区位置、分支来源和重放证据分散记录，难以审计与复现。这在多智能体、多会话的复杂场景中尤为突出。

**方法**：OpenRath 借鉴 PyTorch 将张量作为核心抽象的思路，提出 **Session** 作为一等运行时值。Session 贯穿 Agent 与 Workflow 的传递，统一承载对话块、沙箱位置、谱系元数据、token 用量、待办工作与工具证据，并原生支持分支、检查点、回放、后端感知与组合。在 Session 之上，定义了 Sandbox、Tool、Agent、Memory、Workflow 和 Selector 等抽象，其中 Selector 将控制流转化为运行时路由决策。fork/merge/replay 成为显式的运行时操作，不再依赖外部追踪重建状态。

**结果**：论文提供了编程模型、架构与审计里程碑，但当前仅验证了可控的运行时属性，未进行广泛量化对比。核心贡献在于将 Session 确立为可审计组合的一等值，后续工作将评估在线质量与内存效果。
