---
title: 'Flide: Accelerating Decision Inference with Exact State Forking'
title_zh: Flide：通过精确状态分叉加速决策推理
authors:
- Bobo Li
- Jiajia Song
- Hao Fei
- Wynne Hsu
- Mong Li Lee
affiliations:
- National University of Singapore
- University of Oxford
arxiv_id: '2610.42148'
url: https://arxiv.org/abs/2610.42148
pdf_url: https://arxiv.org/pdf/2610.42148
published: '2026-10-30'
collected: '2026-11-02'
category: Agent
direction: Agent 决策推理加速 · 精确状态分叉
tags:
- Decision Models
- Inference Engine
- Prefix Sharing
- State Forking
- Gated DeltaNet
- Agent Systems
one_liner: 提出支持决策模型分支请求的推理引擎，通过扁平化执行和ForkAttention实现精确且高效的批量决策
practical_value: '- 若业务中有大量「同一上下文下对多个候选项打分/判断」的场景（如搜索 query 质量过滤、商品标题合规审查、广告创意审核），可参考
  Flide 将逻辑分支树与物理 token 流解耦的思路，把共享前缀只计算一次，分支部分扁平化执行，避免重复 forward 或 cache 复制。

  - ForkAttention 用 GPU-resident 索引控制注意力掩码，保证每个分支与单独推理数值完全一致；在设计自己的批量推理服务时，可借鉴这种「逻辑分支
  + 物理连续序列 + 掩码隔离」模式，在标准 attention 和 Gated DeltaNet 层上均可实现，适合混合架构模型。

  - 对于多轮 agent 交互中逐步扩展历史（如用户不断追问、筛选条件动态增加），可利用其 checkpoint 机制从已保存状态恢复，只计算新增部分，显著降低长会话延迟，这对电商导购、客服
  agent 等场景很有价值。

  - 如果业务对决策概率的精确性有要求（如风控、A/B 测试），需避免标准批量推理导致的概率偏移，Flide 的「精确算术等价」设计提供了可复用的工程原则：把分支拓扑放入
  GPU 元数据，配合预录制执行图，兼顾吞吐与一致性。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：决策模型（如 Jev）在 LLM agent 系统中用于快速、轻量的分类推理，但现有面向生成的推理引擎（vLLM、SGLang）处理「同一前缀下多个分支问题」时，要么大量重复计算前缀，要么因批处理拼接导致输出概率失真，无法满足决策场景对低延迟和数值精确性的双重需求。

**方法关键点**：Flide 将决策请求的逻辑树结构与物理执行解耦，把多个分支问题组织进一条扁平 token 流。核心是 ForkAttention，通过 GPU-resident 索引管理分支间的依赖关系，在标准 attention 和循环 Gated DeltaNet 层上保证每个 query 分支与单独 forward 在精确算术下完全一致。分支拓扑直接由 GPU 元数据表达，可支撑混合请求和预录制执行图，并支持从 checkpoint 恢复扩展的 agent 历史。

**关键结果**：在公开混合模型和决策模型上的评测显示，Flide 回答 query 的速度比 vLLM 和 SGLang 快最高 9.5 倍，同时在 total variation distance 上最接近 float32 参考结果。
