---
title: 'MemPilot: Orchestrating On-Demand Multimodal Memory Curation for LLM Agents'
title_zh: MemPilot：按需多模态记忆编排的 LLM Agent 框架
authors:
- Haozhen Zhang
- Haodong Yue
- Quanyu Long
- Jianzhu Bao
- Qingyuan Liu
- Tao Feng
- Bohan Liu
- Weida Liang
- Wenya Wang
affiliations:
- Nanyang Technological University
- Tsinghua University
- University of Illinois Urbana-Champaign
arxiv_id: '2610.06830'
url: https://arxiv.org/abs/2610.06830
pdf_url: https://arxiv.org/pdf/2610.06830
published: '2026-10-05'
collected: '2026-10-06'
category: Agent
direction: Agent 多模态记忆按需编排与模型路由
tags:
- Agent Memory
- Multimodal
- RL
- LLM Routing
- GRPO
- Cost-Latency Trade-off
one_liner: 用 RL 多步策略按需编排记忆检索与异质 LLM/VLM 策展，实现质量-成本-延迟可控折衷
practical_value: '- 借鉴双视图记忆：保留 query-agnostic 压缩记忆库用于低成本检索，同时保留原始多模态历史用于按需精调，避免离线压缩丢细节；电商
  Agent 里可以兼容现有长会话记忆系统，不推翻重建。

  - 将「是否调用视觉/大模型」设为策略动作，把模型池中的 LLM/VLM 按成本和延迟画像暴露给 orchestrator，让 RL 学会按 query 难度和预算动态路由；推荐/搜索
  Agent 里可把通用问答降级到小模型，把商品图片理解、多轮用户偏好抽取路由到 VLM。

  - 用 objective-wise advantage decoupling 做多目标 RL：质量、成本、延迟分别组内归一化再按偏好加权，比合并 reward
  更稳定；业务中若要同时优化转化率、token 成本和响应耗时，可复用该 trick。

  - 延迟不用墙钟时间，改用固定系数仿射估计（fixed overhead + per-token input/output + per-image），避免 API
  波动影响训练；线上部署时也可用此 proxy 做策略训练或仿真。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**：现有 agent memory 大多是 query-agnostic 构建，既浪费预处理成本，又会丢掉未来 query 可能需要的细节；最近运行时自适应方法通常结构僵化、只优化部分目标或固定后端，缺少性能-成本-延迟的细粒度可控。MemPilot 面向多模态交互历史，把记忆策展建模为可按偏好动态编排的序列决策问题。

**方法关键点**：
- 双视图记忆：保留 query-agnostic 记忆库 M（可由任意现有记忆系统初始化）与原始多模态历史 H（按 256 token chunks 分段），分别支持高效访问和按需精调。
- 多步 orchestrator policy：每步选择 Retrieve 或 Curate；Curate 因子化解耦为 retrieval query、evidence count k、curation instruction、模型选择 m、visual access v 五个控制维度。
- 异质模型池：orchestrator 本身仅处理文本，把具体策展任务委托给外部 LLM/VLM，按 query 难度和资源偏好动态选择模型，支持是否传入图像。
- 训练用 GRPO：奖励包含质量 Q、货币成本 C、延迟 L；objective-wise advantage decoupling 对三个目标分别组内归一化后再按偏好加权，避免信号混淆；prefix-based marginal utility 在每个策展阶段后截断生成 probe answer，估计该阶段的边际质量提升，从而给 stage tokens 精细 credit。
- 延迟用固定系数仿射 proxy 估计，训练稳定。

**关键结果**：在 Mem-Gallery、WorldMemArena、H2HMem 上训练，并以 MemEye、MemLens 作为 OOD 测试。MemPilot-Perf 在所有 5 个 benchmark 上取得最高的 LLM-judge 分数，例如 Mem-Gallery 65.82 vs A-Mem 51.45；MemPilot-Bal 在更低成本下保持竞争力，MemPilot-Cost 进一步把成本压到很低（Mem-Gallery 8.2e-3）。偏好扫描显示其 Pareto frontier 比 LightMem、BudgetMem、OmniSimpleMem 等 trade-off-aware baseline 更宽。消融中，去掉 LLM/VLM delegation 平均 judge 从 37.40 骤降到 14.58；去掉 prefix-based marginal utility、objective-wise decoupling 或 retrieval-instruction decoupling 也都造成显著退化。

**最值得记住的一句话**：把离线记忆与原始历史分存，让 RL policy 按偏好在线决定 retrieve or curate 以及模型/视觉资源分配，比固定 pipeline 或预算档位更灵活地实现性能-成本-延迟 trade-off。
