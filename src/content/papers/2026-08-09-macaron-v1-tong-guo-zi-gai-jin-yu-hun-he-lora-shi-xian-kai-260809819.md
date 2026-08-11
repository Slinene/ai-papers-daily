---
title: 'Macaron-V1: Towards Open Continual Learning with Self-Improvement and Mixture-of-LoRA'
title_zh: Macaron-V1：通过自改进与混合 LoRA 实现开放持续学习
authors:
- Mind Lab
- Vin Bo
- Asher Cai
- Jingwei Cao
- Song Cao
- Vic Cao
- Amelia Chen
- Andrew Chen
- Kaijie Chen
- Cleon Cheng
affiliations:
- Mind Lab
arxiv_id: '2608.09819'
url: https://arxiv.org/abs/2608.09819
pdf_url: https://arxiv.org/pdf/2608.09819
published: '2026-08-09'
collected: '2026-08-11'
category: Agent
direction: Agent 持续学习与适配器组合
tags:
- LoRA
- MoL
- self-improvement
- continual learning
- agent
- RL
one_liner: 提出冻结基座 + 可组合 LoRA 专家的 MoL 架构与递归自改进循环，实现代理模型部署后持续适应与协作
practical_value: '- **多域任务路由架构**：将不同业务域（如对话、推荐、搜索）建模为独立 LoRA 适配器，冻结共享基座，通过 Proxy 按请求路由，避免任务干扰且支持独立更新，类似推荐系统中多目标
  MoE 的路由分离。

  - **版本化 harness 协议**：HCP 将 prompt、工具、技能、环境等配置统一为 TOML 工件，可作为推荐 Agent 中工具与指令的线上可
  audit 配置层，便于 A/B 测试和回滚。

  - **长上下文执行与 KV 复用**：通过可拼接的 own-view 实现跨适配器 prefix cache 命中，值得在多轮会话、长用户行为序列的 LLM
  推理中借鉴，降低延迟。

  - **递归自改进循环**：从生产日志挖掘失败任务 → harness 配置搜索 → LoRA 更新，可复用至搜索推荐 Agent 的持续优化，逐步扩展能力边界。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
传统后训练将模型锁定在训练快照，难以适应新知识、工具和用户需求。真正需要体验智能：从实际环境持续学习并改进。Macaron-V1 通过适应（递归迭代）和协作（专家组合）两个维度构建开放持续学习系统。

**方法关键点**
- **Mixture of LoRA (MoL)**：冻结 744B GLM-5.2 基座，训练 4 个 LoRA 专家（Chat/Agent/Coding/GenUI），由 L0 适配器做路由决策，Proxy 执行 route-answer-summary 三跳循环。每个适配器拥有独立会话视图，交叉适配器通过 192 token 摘要传递上下文。
- **Model-Harness Co-design**：将 harness 提升为一级优化目标。UI4A 提供组件原生生成式 UI；REPL 代理 harness 支持可执行组合与验证重用；HCP 协议版本化配置（prompt、工具、技能等），使训练与部署接口一致。
- **递归自改进 (RSI)**：MindForge 框架实现任务发现 → 轨迹扩展 → 配置搜索与适配器更新闭环。当前只评估配置搜索阶段：固定模型中通过 harness 搜索覆盖全部 122 个基础失败任务。
- **基础设施**：MinT 管理模型/适配器版本线；LongStraw 优化长上下文推理；稀疏 MoE/DSA 基座稳定性修复。

**关键实验**
- 路由准确率：Venti 99.12%（6448 样本），Tall 99.04%，跨基座稳定。路由+摘要延迟约占总延迟 32%。
- 任务质量：Vita 交付测试中，路由与单适配器直接回答质量无统计差异（0.632 vs 0.636）。
- 参数效率：MoL 存储量约为复制基座方案的 26%，节省 74%。
- UI4A：输出 token 较原生 HTML 减少 45%（~672 vs 1224），首屏渲染可加速约 6 倍。
- 长上下文：8 GPU 下 900K token 首字延迟从 107.1s 降至 49.2s。

**最值得记住的一句话**：MoL 通过冻结基座、组合可插拔 LoRA 专家和 Proxy 路由，将代理能力模块化并支持持续学习，而 harness 的显式协议让模型-环境界面可版本化迭代。
