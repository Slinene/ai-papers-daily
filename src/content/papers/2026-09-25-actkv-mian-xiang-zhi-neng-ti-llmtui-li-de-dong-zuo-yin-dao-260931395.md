---
title: 'ActKV: Efficient LLM Agents through Action-Guided KV Cache Management'
title_zh: ActKV：面向智能体LLM推理的动作引导KV缓存管理
authors:
- Zihan Wang
- Cheng Tang
- Lei Gong
- Chao Wang
- Wenqi Lou
- Teng Wang
- Xuehai Zhou
affiliations:
- University of Science and Technology of China
- Suzhou Institute for Advanced Research, University of Science and Technology of
  China
arxiv_id: '2609.31395'
url: https://arxiv.org/abs/2609.31395
pdf_url: https://arxiv.org/pdf/2609.31395
published: '2026-09-25'
collected: '2026-09-28'
category: Agent
direction: Agent KV缓存压缩与推理优化
tags:
- KV cache
- LLM Agents
- Inference optimization
- Memory management
- Action-oriented
- Compression
one_liner: 提出首个面向Agentic LLM推理的KV缓存压缩框架，以动作生成贡献度为准则压缩缓存
practical_value: '- **动作导向的KV淘汰策略**：在电商导购、购物助手等Agent推理循环中，可优先保留对后续动作（如商品检索、推荐API调用、订单操作）生成贡献大的KV条目，而非全局文本质量，降低缓存占用且不损失任务成功率。

  - **置信度驱动的自适应预算分配**：利用LLM生成动作时的内在置信度（如token概率）动态调整KV缓存预算，适配不同任务阶段对动作关键记忆的波动需求，可集成到现有Agent
  serving框架中提升长时多轮交互的吞吐。

  - **页式压缩管理与定制内核**：将缓存压缩抽象为淘汰、预算分配、页管理三个原语，并配合定制CUDA kernel实现实际吞吐提升，适合高并发场景下Agent推理服务的工程化落地。

  - **评估指标转向动作质量**：业务中应关注最终动作成功率和任务完成度，而非仅看文本生成困惑度或BLEU，ActKV的实验设计可借鉴到Agent/推荐对话系统的离线评测中。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：Agentic LLM推理在多轮“观察-推理-动作”循环中会积累长KV缓存，造成显存瓶颈和吞吐下降。现有压缩方法侧重整体输出质量，忽视动作在驱动任务进展中的不对称重要性。

**方法关键点**：ActKV是首个针对Agentic LLM推理的KV缓存压缩框架。核心思想是建立以“对动作生成的贡献”为准则的压缩标准，优先保证动作质量。具体包含三部分：
- **动作导向的KV淘汰**：利用稳定的动作访问模式，保留对未来动作生成关键的KV条目，在压缩下仍能可靠推进任务。
- **置信度驱动的自适应预算分配**：基于LLM生成动作的内在置信度动态调整缓存预算，适应不同阶段对关键记忆的需求变化。
- **页式压缩管理**：将压缩标准化为三个原语（淘汰、预算分配、页管理）并定制内核，实现实际吞吐提升，兼容paged memory。

**关键结果**：在长轨迹任务上，ActKV仅用FullKV峰值缓存内存的25.98%，平均保留98.53%的FullKV准确率；token吞吐达FullKV的3.97倍，任务吞吐达3.58倍，达到SOTA性能。
