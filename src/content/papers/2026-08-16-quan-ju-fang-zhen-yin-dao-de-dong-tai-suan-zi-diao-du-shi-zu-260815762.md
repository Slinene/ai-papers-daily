---
title: Global Simulation-Guided Dynamic Operator Scheduling for Efficient Multi-Tenant
  Model Serving
title_zh: 全局仿真引导的动态算子调度实现高效多租户模型服务
authors:
- Weinan Liu
- Zeyuan Ding
- Dian Ding
- Chengcheng Wan
- Lu Tang
- Guangtao Xue
- Jiwu Shu
- Yiming Zhang
affiliations:
- Xiamen University
- Shanghai Jiao Tong University
- East China Normal University
- Tsinghua University
arxiv_id: '2608.15762'
url: https://arxiv.org/abs/2608.15762
pdf_url: https://arxiv.org/pdf/2608.15762
published: '2026-08-16'
collected: '2026-08-18'
category: Other
direction: 多租户 LLM 推理的算子级动态调度
tags:
- Operator Scheduling
- GPU Utilization
- Multi-Tenant Serving
- LLM Inference
- Simulation-guided
- PyTorch Backend
one_liner: 提出 SliceScheduler，利用全局映射图和模拟器进行算子级动态调度，提升多租户 LLM 推理吞吐 1.10-2.29 倍
practical_value: '- 在部署 LLM-based 推荐/搜索服务时，容器粒度调度会浪费 GPU 碎片时间，可借鉴 SliceScheduler 将调度单位从容器细化到算子，利用短时空闲
  slice 提升吞吐。

  - 引入全局映射图（GMG）统一描述算子依赖、tensor 形状、资源映射和状态，方便实时全局视角做决策；自己的推理平台可以维护类似有向图，结合模拟器做 what-if
  预测。

  - 设计增量式模拟调度：生成候选 placement 后用模拟器评估内存和延迟，选择最优不违反 SLA 的方案，避免实际试错成本；可用于多模型混部或流量突增场景。

  - 实现为 PyTorch backend，说明算子级调度可以透明集成到现有训练/推理栈，业务侧无需大幅改动模型代码。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：容器粒度调度在 GPU 上留下大量短时空闲片段，重新分配容器开销大，无法利用细粒度机会；算子级调度需要实时处理依赖、内存安全、集群动态，具有挑战。

**方法**：提出 SliceScheduler，包含四个组件：全局映射图 GMG（统一抽象捕获算子依赖、tensor 形状、资源映射和执行状态）；基于 GMG 的全局模拟器（预测候选放置下的算子执行和内存演化）；增量模拟调度模块（选择放置利用碎片空闲 slice，避免内存违规并保持 SLA）；算子执行器（在 GPU 上落地调度决策，协调计算和跨加速器传输）。实现为 PyTorch backend。

**结果**：用生产 trace 回放评估，相比现有方法 token 吞吐提升 1.10-2.29 倍，SLA 违规维持在 9% 以内，证明算子级调度是提升多租户 LLM serving GPU 利用率的实用有效方法。
