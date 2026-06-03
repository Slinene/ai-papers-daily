---
title: 'Agent libOS: A Library-OS-Inspired Runtime for Long-Running, Capability-Controlled
  LLM Agents'
title_zh: Agent libOS：面向长期运行能力受控LLM Agent的类库操作系统运行时
authors:
- Yingqi Zhang
affiliations:
- Tsinghua University
arxiv_id: '2606.03895'
url: https://arxiv.org/abs/2606.03895
pdf_url: https://arxiv.org/pdf/2606.03895
published: '2026-06-02'
collected: '2026-06-03'
category: Agent
direction: Agent运行时架构 · 能力安全控制
tags:
- LLM Agent
- Capability System
- Runtime
- Security
- OS Metaphor
one_liner: 将LLM Agent抽象为操作系统进程，把安全边界从工具包装下沉到运行时原语，实现按能力授权、阻塞等待与审计
practical_value: '- **工具与权限分离**：将模型可见的工具 Schema 与真实资源授权解耦，避免因 prompt injection 或输出注入导致越权操作，对构建电商客服、推荐系统
  Agent 等需要安全控制的应用有直接参考价值

  - **进程模型管理 Agent 生命周期**：用 fork/spawn/exec/wait 等语义管理子任务和人工审批等阻塞操作，可以轻松实现推荐 Agent
  的暂停、恢复、任务分派与状态隔离

  - **类型化对象内存**：用带权限和来源的类型化对象图替代原始对话文本，有利于记忆管理、上下文裁剪和知识复用，适用于需要维护用户画像和对话状态的推荐 / 查询推荐
  Agent

  - **JIT 生成工具沙箱化**：通过 Deno 的无权限运行和 syscall 代理机制安全执行 Agent 生成的 TypeScript 工具，可为企业环境下的动态工具扩展提供工程范本'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

**动机**：LLM Agent 正从请求-响应的对话助手进化为长期运行的软件角色，需要维护状态、等待外部事件、获取并衰减权限、产生可审计的副作用。当前框架普遍采用“对话循环 + 工具注册表”的模式，将模型可见的工具 Schema 和对宿主资源的访问权限混在一起，导致 prompt 注入、权限提升、审计困难等安全风险。

**方法关键点**：
- **AgentProcess 抽象**：将每个 Agent 视为一个进程，拥有身份、父子关系、状态、工具表、对象内存视图和能力集合，生命周期由运行时调度。
- **“工具作为 libc，原语作为权限边界”设计原则**：模型可见的工具是浅层包装，所有文件、对象、shell、人工审批、时钟等操作都必须在运行时原语层面通过能力检查。工具可见性不蕴含资源授权。
- **能力系统和人工审批队列**：资源（对象、命名空间、路径、shell 策略等）通过能力（capability）授予，支持 always_allow、ask_each_time 等策略。人工审批建模为阻塞原语，由调度器恢复等待动作，不是 callback 或 prompt 钩子。
- **类型化对象内存**：代替原始聊天记录，存储有类型、来源、权限、可变性标记的对象，模型只能通过物化器获得上下文片段，无法直接读写。
- **JIT 工具沙箱**：Agent 可提议生成 TypeScript 工具，经静态校验后在 Deno 的无权限子进程中运行，只通过受控的 syscall 会话与宿主动态通信，无法绕过能力检查。
- **可注入资源提供者层**：文件系统、时钟/睡眠、shell 执行等均通过提供者接口接入，便于替换或审计。

**关键结果**：原型实现 123 个回归测试，验证了工具表隔离、工作区包含、fork 衰减、命名空间隔离、异步 sleep 交错、人工审批阻塞恢复、shell 策略匹配、JIT syscall 隔离等安全属性。确定性演示脚本无模型完成创建进程、fork、权限拒绝、人工批准、修补文件等完整流程。论文强调架构层面的安全保证而非基准测试提升。
