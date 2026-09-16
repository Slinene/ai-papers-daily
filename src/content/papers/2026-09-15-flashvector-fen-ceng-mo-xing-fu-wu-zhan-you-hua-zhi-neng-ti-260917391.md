---
title: 'FlashVector: Agent for Hierarchical Model Serving Stack Optimization'
title_zh: FlashVector：分层模型服务栈优化智能体
authors:
- Qi Wu
- Lohan Lemire
- Kai Meng
- Zhongmou Cai
- Raphael Bargues
- Petr Zhitnikov
- Zeyuan Cao
- Yao Wang
- Shujun Bian
- Wei Chen
affiliations:
- Stanford University
- Unity Vector AI Team
arxiv_id: '2609.17391'
url: https://arxiv.org/abs/2609.17391
pdf_url: https://arxiv.org/pdf/2609.17391
published: '2026-09-15'
collected: '2026-09-16'
category: Agent
direction: Agent 驱动的服务栈自动调优
tags:
- Agent
- Model Serving
- Inference Optimization
- GPU Kernel
- Feature Store
- Autotuning
one_liner: 将 LLM 驱动的 GPU kernel 优化范式推广到模型服务器、特征处理与运行时配置的全栈自动调优
practical_value: '- 将服务栈各层抽象为统一的 Profile-Diagnose-Optimize-Verify 循环，每层只需提供领域化的 profiling
  工具（GPU 用 Nsight，CPU 服务用 eBPF）和知识库，即可复用同一套 agent 框架优化 CUDA、C++、Python 等异构代码，避免为每个组件单独建系统。

  - 优化验收必须通过生产流量回放 + 全栈负载测试，且收益超过测量噪声 floor（基线 ±6%，可重复采样收紧到 2.1%）；对浮点重排等改动设置预测输出偏差阈值，防止精度回退。这套验证机制可直接迁移到模型/服务的上线把关。

  - 维护一个持续更新的优化知识库（业务逻辑、模型结构、组件架构、优化 cookbook），每次运行后只做 in-place refine 而不是累积全部历史，能有效控制上下文窗口增长、减少
  LLM 幻觉，适合长期运行的优化 agent。

  - 代码优化和参数搜索可以用同一 loop：在 SLO 约束下用真实请求回放搜索 batch size、实例数等配置，并通过 shadow canary 放量验证；模型每次重训或服务更新后自动触发新一轮，可以避免配置漂移导致的成本回升。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

## 动机
模型服务是生产推荐系统最大的成本项之一。优化需要跨 GPU kernels、ML framework、模型服务器、在线特征处理等多层技术栈，每层依赖不同的领域知识，人力难以覆盖；同时模型持续重训、流量变化和硬件更新使手动优化快速失效。虽然已有 GPU kernel agent 在单 kernel 优化上达到人类专家水平，但其他层的自动化优化仍接近空白。

## 方法关键点
- **层 agent 抽象**：每层实现同一个 Profile-Diagnose-Optimize-Verify 循环，但各自使用领域化工具：GPU kernels 用 Nsight Systems/Compute，模型服务器用 eBPF，特征处理用 Python/C++ profiler；优化结果通过 Refine 阶段写回知识库。
- **优化局部、验证全局**：每层独立提出候选优化，但必须通过生产流量回放和全栈负载测试确认端到端收益超过测量噪声（基线 ±6%，可收紧至 2.1%）；同时按改动类型校验预测正确性：确定性重写要求逐元素相等，浮点重排要求误差 <10^-3 且异常值 <0.1%。
- **持续优化循环**：自动触发于模型发布或配置过期，每次从历史接受/拒绝记录开始，运行结束后更新知识库，使优化不随模型重训或基础设施升级而衰减。
- **知识库管理**：包含业务逻辑、模型服务器架构、特征存储、模型实现、硬件指南和人工优化 cookbook；通过 in-place refine 限制上下文增长，缓解 LLM 幻觉和遗忘。

## 关键结果
部署在 Unity Vector 广告平台的生产模型上：模型服务器吞吐最高提升 2×、延迟加速最高 1.98×；特征存储吞吐提升 1.6×。典型案例如下：
- 模型服务器（Triton）输入反序列化瓶颈从 Python 重写为 C++，单步加速 30×；
- 多任务推荐模型：fused attention 将 attention 延迟从 996.5µs 降至 279.8µs（3.56×）；embedding 层分解使 GPU kernel 时间减少 33.4%，前向延迟降低 30.1%；
- 在线特征预处理：用 Cython 替代 pandas/numpy 热点，单调用加速 4.4–350×，整 pod 吞吐从 940 RPS 提升至约 1500 RPS（1.6×）；
- 运行时参数自动搜索：在固定 SLO 下，通过调整 instance count 和 dynamic batch size，吞吐最高提升 2×。

## 最值得记住的一句话
一个统一的 profile-diagnose-optimize-verify 闭环 + 生产流量回放验证，可以让 LLM agent 从单 kernel 优化无缝推广到异构多语言服务栈，并持续跑在生产环境中。
