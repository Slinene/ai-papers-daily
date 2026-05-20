---
title: 'AgentKernelArena: Generalization-Aware Benchmarking of GPU Kernel Optimization
  Agents'
title_zh: AgentKernelArena：面向泛化性的GPU内核优化代理基准测试
authors:
- Sharareh Younesian
- Wenwen Ouyang
- Sina Rafati
- Mehdi Rezagholizadeh
- Sharon Zhou
- Ji Liu
- Yue Liu
- Yuchen Yang
- Hao Li
- Ziqiong Liu
affiliations:
- AMD
arxiv_id: '2605.16819'
url: https://arxiv.org/abs/2605.16819
pdf_url: https://arxiv.org/pdf/2605.16819
published: '2026-05-15'
collected: '2026-05-20'
category: Eval
direction: GPU内核优化代理评估基准
tags:
- GPU Kernel
- Agent Benchmark
- Generalization
- Code Generation
- HIP
- Triton
one_liner: 首个覆盖HIP/Triton/PyTorch-to-HIP的智能体GPU内核优化评估基准，引入未见配置泛化测试。
practical_value: '- **Agent迭代优化流程的量化评估**：借鉴其编译、正确性、性能三道门控检查的设计，可为推荐系统中代码生成Agent（如特征工程脚本优化、数据处理pipeline生成）构建类似的闭环评测，确保输出代码在真实环境中可用且高效。

  - **泛化测试避免过拟合**：论文揭示从零生成的kernel容易硬编码特定输入形状，在未见配置下正确性大幅下降。在电商场景中，若用Agent生成模型训练或推理代码，应增加不同batch
  size、序列长度等配置的泛化测试，避免隐式过拟合。

  - **隔离执行与集中评分**：其模块化工作区隔离执行、集中打分的框架可复用于多Agent系统的性能基准测试，尤其适合评估代码优化类Agent的鲁棒性和速度提升。

  - **对推荐场景的直接价值有限**：工作聚焦底层GPU kernel优化，与业务层的生成式推荐、多智能体协作关联较弱，主要提供评估方法论参考。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有GPU kernel优化基准只评估单次LLM调用，忽略完整的智能体迭代调试流程，且未包含kernel-to-kernel优化任务和输入配置泛化测试。这导致对AI编程代理的实际能力评估不足。

**方法**：提出AgentKernelArena，包含196个任务，覆盖HIP-to-HIP优化、Triton-to-Triton优化、PyTorch-to-HIP翻译三类场景。每个任务在隔离工作区中运行完整agent工作流，经过编译、正确性、性能三重门控检查，并采用集中评分机制。关键创新是未见配置泛化协议：要求agent在固定输入shapes上优化，但最终用从未见过的输入尺寸测试优化后kernel的正确性与加速比。

**关键结果**：对Cursor Agent、Claude Code、Codex Agent等生产级代理的评测显示，多数类别达到近乎完美的编译率和较高正确率。最强配置在PyTorch-to-HIP任务上平均加速6.89倍，HIP-to-HIP达6.69倍，Triton-to-Triton为2.13倍。泛化测试表明，HIP和Triton的优化能较好迁移到新输入形状，而PyTorch-to-HIP的正确性显著下降，说明从零生成kernel的agent容易硬编码shape相关假设。该基准为agentic GPU kernel优化提供了标准化评估框架。
