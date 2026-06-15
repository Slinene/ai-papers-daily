---
title: 'tap: A File-Based Protocol for Heterogeneous LLM Agent Collaboration'
title_zh: tap：异构LLM Agent基于文件系统的协作协议
authors:
- Minseo Kim
affiliations:
- HUA Labs
arxiv_id: '2606.14445'
url: https://arxiv.org/abs/2606.14445
pdf_url: https://arxiv.org/pdf/2606.14445
published: '2026-06-12'
collected: '2026-06-15'
category: Agent
direction: 多智能体协作 · 文件通信协议
tags:
- multi-agent
- file-based protocol
- heterogeneous agents
- code review
- self-applied operation
one_liner: 通过文件优先级设计结合实时通知，实现Claude与Codex在同一仓库无共享内存的长期开发与审查。
practical_value: '- **消息持久化与审计**：在推荐Agent流水线（如生成式检索->精排->文案生成）中，可以模仿tap将中间消息（检索结果、特征拼接、决策理由）以文件形式落盘，既做审计又能用于失败重试，避免仅依赖内部状态。

  - **异构模型配对产生多样性**：实验发现不同模型（Claude/Codex）配对审查时检出缺陷率更高（69.8% vs 53.1%），这启示在多智能体推荐评估中，混合不同供应商的LLM作为“评审”可能减少群体思维，尤其适用于敏感规则审核、安全校验等任务。

  - **无共享运行时的编排**：通过独立git worktree和文件隔离，Agent无需共享内存或统一API网关，可直接用于现有微服务环境——每个推荐模块（召回、排序、解释生成）由不同厂商模型驱动，通过文件交换输出继续迭代。

  - **自应用迭代机制**：tap自身用自己开发，问题直接通过审查->mission->修复循环改进协议，这种“用Agent改进Agent系统”的模式能迁移到推荐引擎自动调参或策略进化，前提是操作日志与复盘记录结构化可回放。'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

**动机**  
现有LLM多智能体开发系统（ChatDev、MetaGPT、AutoGen）通常假设所有Agent在同一模型家族、同一运行时或中央对话服务中运行，导致错误趋同、审查盲区。直接在异构环境（不同模型、不同执行环境）中协作需要一种不依赖共享内存与通用通信通道的轻量协议。

**方法关键点**  
- **文件优先级消息存储**：Agent调用`tap_reply`时，先将含YAML元数据的Markdown消息写入`inbox/`目录，作为原始消息记录；实时通知路径（Tier 2）仅作为加速，不替代文件本体。  
- **双通道通信**：Tier 1 文件检查（MCP工具直接读文件），Tier 2 实时推送（Claude用MCP Channel，Codex用WebSocket）。即使实时通知丢失，文件仍可重读，消息不丢失。  
- **环境定制配置**：`tap add`命令自动适配Claude的`.mcp.json`、Codex的`config.toml`等不同配置格式，统一过程而不强制统一API。  
- **工作区隔离**：每个Agent使用独立git worktree，用`instanceId`分隔PID、日志与状态文件，支持并行运行。  
- **恢复设计**：写入文件后才尝试发送实时通知，接收方不信任通知载荷，直接重读`inbox/`文件处理，将通信失败转化为延迟而非消息丢失。

**实验结果**  
在为期27天、37代的自我应用（tap开发并审查tap自身）中，产生209个相关PR、717个工件。375个审查工件分析显示：异构模型配对（Claude审查Codex或反之）记载至少一处缺陷或修改请求的比例为69.8%，同构配对为53.1%。24个安全相关案例中有6个潜在运行时漏洞（如execSync注入）由跨模型审查发现。协议运行中暴露了路径前缀、日志冲突、命名碰撞等问题，通过文件记录->审查->修复循环在迭代中修正。
