---
title: 'ReFreeKV: Towards Threshold-Free KV Cache Compression'
title_zh: ReFreeKV：迈向无阈值 KV 缓存压缩
authors:
- Xuanfan Ni
- Liyan Xu
- Chenyang Lyu
- Longyue Wang
- Mo Yu
- Lemao Liu
- Fandong Meng
- Jie Zhou
- Piji Li
affiliations:
- Nanjing University of Aeronautics and Astronautics
- WeChat AI, Tencent
- Fudan University
- Independent Researcher
arxiv_id: '2502.16886'
url: https://arxiv.org/abs/2502.16886
pdf_url: https://arxiv.org/pdf/2502.16886
published: '2026-06-25'
collected: '2026-07-01'
category: LLM
direction: LLM 推理优化 · KV缓存压缩
tags:
- KV Cache
- Compression
- Threshold-Free
- Inference Efficiency
- Adaptive Budget
one_liner: 提出首个无阈值 KV 缓存压缩方法，自适应分配预算，无需预设阈值即可保持全缓存性能
practical_value: '- 长上下文推理优化：在电商、广告场景中，用户行为序列、商品描述等长文本输入可利用该自适应 KV 缓存压缩，降低线上推理内存与延迟，无需为不同输入单独调阈值。

  - 多轮 Agent 对话管理：Agent 系统常需维持长对话历史，ReFreeKV 的无阈值特性可动态保留关键 KV 对，避免对话状态因缓存裁剪过度而丢失重要信息，提升多轮交互稳定性。

  - 避免输入敏感调参：业务中处理多样化的查询（搜索词、聊天消息）时，传统缓存压缩需凭经验设定预算，此方法可自动调整，减少工程维护成本。

  - 模型部署降本：在 LLM 推荐、检索增强生成等场景下，直接复用该方法实现近乎无性能损失的 KV 缓存压缩，节省 GPU 显存，支持更大 batch size
  或更长上下文，直接降低服务成本。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有 LLM 推理中的 KV 缓存裁剪方法大多依赖输入/领域特定的预算阈值，才能实现最优无损压缩。在真实开放域场景中，输入多样、长度与难度各异，难以预先选用合适的阈值，导致性能显著退化。该工作指出，输入敏感的阈值依赖是 KV 压缩技术实用化的根本限制。

**方法**：提出一种“无阈值”目标，要求压缩方法无需预设阈值，即可自适应调整各层与各头的 KV 预算，同时维持全缓存时的性能。基于该目标，推荐并实现了首个具体方法 ReFreeKV，通过动态评估注意力重要性并保留关键 KV 对，在推断中实现鲁棒的预算分配。

**结果**：在 13 个涵盖不同上下文长度、任务类型和模型规模的数据集上进行广泛实验，ReFreeKV 在无阈值限制下达到与全缓存相当的效果，并在相同压缩率下显著优于需要手动预设阈值的基线方法；此外，其自适应特性带来了更稳定的跨场景表现。
