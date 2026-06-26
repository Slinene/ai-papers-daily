---
title: 'TOPS: First-Principles Visual Token Pruning via Constructing Token Optimal
  Preservation Sets for Efficient MLLM Inference'
title_zh: 基于第一性原理的视觉 Token 最优保留集剪枝，实现高效多模态大模型推理
authors:
- Tinghao Wang
- Yichen Guo
- Rui Huang
- Zheng Lu
- Qizhe Zhang
- Chenxi Li
- Yuan Zhang
- Jiajun Cao
- Zhirong Shen
- Yaosong Du
affiliations:
- Peking University
- University of Electronic Science and Technology of China
- Nanyang Technological University
- Beijing Academy of Artificial Intelligence
arxiv_id: '2606.27161'
url: https://arxiv.org/abs/2606.27161
pdf_url: https://arxiv.org/pdf/2606.27161
published: '2026-06-25'
collected: '2026-06-26'
category: Multimodal
direction: 多模态大模型高效推理 · 视觉 token 剪枝
tags:
- token pruning
- MLLM efficiency
- information theory
- training-free
- visual tokens
- plug-and-play
one_liner: 提出任务相关性、信息覆盖与语义多样性三原则的免训练剪枝模块 TOPS，可大幅削减视觉 token 且保性能
practical_value: '- 若业务中多模态推荐系统处理商品图片，可直接嵌入 TOPS 模块，在几乎不损失准确率的前提下大幅减少视觉 token 计算量，降低推理延迟与成本。

  - 三原则（任务相关性、信息覆盖、语义多样性）可迁移至长文本或混合模态输入，例如在 Agent 检索增强场景中，对用户行为序列、文档内容进行关键 token 筛选，节省
  LLM 的 KV cache 并提高效率。

  - 免训练、模型无关的剪枝方案适合快速实验与部署，无需修改模型结构或重新训练，可针对不同 MLLM 骨干即插即用，降低工程接入门槛。

  - 剪枝后性能不降反升的观察（缓解幻觉）可为轻量化多模态模型设计提供思路，未来在端侧推荐或实时交互 Agent 中有潜在价值。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

动机：多模态大模型（MLLM）推理时视觉 token 数量庞大，导致计算开销过高。现有剪枝方法依赖单一准则（如注意力得分或多样性），缺乏对剪枝内在目标的统一原则性定义。

方法：从第一性原理出发，将视觉 token 剪枝形式化为构建 Token 最优保留集（Token Optimal Preservation Sets），通过信息论分析提炼出三个基本原则：**任务相关性（Task Relevance）**、**信息覆盖性（Information Coverage）** 和 **语义多样性（Semantic Diversity）**。基于此提出 TOPS 模块，分阶段筛选：先计算 token 与指令的关联度，再通过最大覆盖保证信息完整，最后引入多样性避免冗余。TOPS 免训练、模型无关，可直接插入各类 MLLM。

结果：在 7 种 MLLM 骨干、14 个基准上，TOPS 在不同剪枝比例下均优于先前方法。在 LLaVA-NeXT 上，移除 77.8% 视觉 token 后，7B 模型的性能保持 100.0%，13B 模型甚至达到 100.6%，表明剪枝冗余 token 有时能缓解幻觉，为轻量化 MLLM 设计提供启示。
