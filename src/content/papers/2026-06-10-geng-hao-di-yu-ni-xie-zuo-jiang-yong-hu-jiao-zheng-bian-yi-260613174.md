---
title: 'Getting Better at Working With You: Compiling User Corrections into Runtime
  Enforcement for Coding Agents'
title_zh: 更好地与你协作：将用户矫正编译为编码 Agent 的运行时执行规则
authors:
- Yujun Zhou
- Kehan Guo
- Haomin Zhuang
- Xiangqi Wang
- Yue Huang
- Zhenwen Liang
- Pin-Yu Chen
- Tian Gao
- Nuno Moniz
- Nitesh V. Chawla
affiliations:
- University of Notre Dame
- IBM Research
- Tencent AI Lab
arxiv_id: '2606.13174'
url: https://arxiv.org/abs/2606.13174
pdf_url: https://arxiv.org/pdf/2606.13174
published: '2026-06-10'
collected: '2026-06-13'
category: Agent
direction: Agent 个性化 · 运行时规则编译与强制执行
tags:
- Runtime Enforcement
- Personalization
- Coding Agent
- User Correction
- Access-Compliance Gap
one_liner: 提出 TRACE，把用户矫正编译成运行时强制检查，克服记忆检索却仍违反偏好的“访问‑合规”差距
practical_value: '- **从反馈到硬约束**：在电商或推荐 Agent 中，用户反馈（如“别再推这类商品”）若仅记入 memory，后续仍可能违反。可借鉴
  TRACE 将反馈编译为可执行规则，在排序前、回复生成前用钩子（hook）校验，强制执行，减少用户重复纠正。

  - **规则生命周期管理**：面对持续的用户修正，通过五类动作（new/update/supersede/split/noop）动态维护规则库，避免冲突和退化，适用于个性化策略的增量演化。

  - **记忆与强制互补**：系统可同时保留记忆存储（上下文感知）和规则引擎（强制执行）。对于成本敏感的推荐场景，对关键偏好（如明确过滤条件）施加编译检查，对软性偏好仍用记忆提示，二者非替代关系。

  - **轻量规则提取**：使用小型 LLM 自动从用户反馈中提取原子规则和验证正则（如检测“debug 文件清理”的命令模式），在电商 Agent 中可自动生成“取消订单后禁止推荐同类商品”的触发条件和校验逻辑，降低人工配置成本。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：交互 coding agent 即使通过记忆记住了用户的矫正（如“清理调试文件”），在后续会话中仍频繁违反，迫使用户重复纠正。文章量化了这一“访问‑合规”差距：在真实用户交互构建的诊断基准上，即使偏好被检索并放入上下文，agent 也仅满足不到一半的检查（Mem0 条件下 57.5% 违规率，纯记忆无法实现可靠遵守）。根本原因在于，记忆将矫正保留为自然语言建议，而非执行时必须满足的条件。

**方法关键点**：提出 **TRACE**（Test‑time Rule Acquisition and Compiled Enforcement）作为 coding agent 运行时的即插即用技能层。其流程包括：
1. **矫正信号检测**：用轻量 LLM（Gemma 4 31B）实时扫描会话，判断用户消息是否包含持久偏好信号。
2. **规则原子化**：将矫正提取为原子规则，包含应用条件和验证标准，例如“当任务可能创建临时文件时，完成前清理调试日志”。
3. **规则生命周期管理**：通过五动作决策（new, update, supersede, split, noop）将新规则与用户现有规则库调和，防止冲突并支持增量更新。
4. **编译强制执行**：每条规则编译为三个组件——适用性检查、行为指令、验证器。验证器通过挂钩（tool‑use、文件写入、终端等事件）嵌入 agent 执行流程，不满足条件时中断运行并反馈给 agent 修正，限定重试次数。实验中的 47 条规则全部采用 verify‑retry 模式。

**关键实验**：
- **诊断基准**：基于 19 个真实用户任务、29 项偏好检查，对比 No Rules / All Rules / Mem0 / Relevant Rules / Compiled Rules。编译规则合规率 **70.1%**，远高于 Mem0（42.5%）和 Relevant Rules（54.0%），证实访问≠合规。
- **ClawArena 模拟用户评测**：TRACE 将分布内（ID）违规从 100% 降至 **37.6%**，分布外（OOD）降至 **2.0%**（三款模型零违规），任务通过率与无记忆基线持平；用户干预轮次由 2.0 降至 ID 1.37、OOD 1.02，且不增加运行时延。
- **MemoryArena**：TRACE 实现最高任务通过率（17.3% vs. 最高内存基线 12.2%）和最低违规率（60.5%），证明当约束是任务成功条件的一部分时，编译强制直接转化为性能提升。

**一句话结论**：个性化不应止于记住偏好，而应决定何时必须约束执行并提供运行时强制机制——记忆与强制是互补的底盘，而非替代方案。
