---
title: 'MoE$^2$-LoRA: When MoE Models Meet MoE-style Low-Rank Adaptation'
title_zh: MoE²-LoRA：为MoE模型设计的MoE风格低秩适配
authors:
- Qingyu Yang
- Haonan He
- Minglei Li
- Jingqi Ye
- Tao Chen
- Lei Bai
- Peng Ye
affiliations:
- Shanghai Artificial Intelligence Laboratory
- KTH Royal Institute of Technology
- University of Science and Technology of China
- Fudan University
- The Chinese University of Hong Kong
arxiv_id: '2607.21978'
url: https://arxiv.org/abs/2607.21978
pdf_url: https://arxiv.org/pdf/2607.21978
published: '2026-07-24'
collected: '2026-07-27'
category: Training
direction: MoE模型参数高效微调
tags:
- MoE
- LoRA
- PEFT
- Routing
- Parameter Sharing
- Adapter
one_liner: 首次用MoE路由思想做LoRA微调，复用预训练路由器激活动态选择全局共享的LoRA专家
practical_value: '- 若内部用MoE架构LLM做推荐/对话任务（如query改写、商品描述生成），MoE²-LoRA提供了一种高效微调方案：引入全局共享LoRA专家池，既减少参数量又保持多任务适配能力。

  - 路由条件投影（RCP）复用预训练路由器激活，可借鉴到多兴趣推荐模型中，用已有用户意图路由为不同兴趣头动态选择低秩适配器，避免静态分配。

  - 全局专家池的层间共享机制简化了部署：只需维护一套适配器权重，节省存储和推理时IO；适合边缘设备或需要频繁更新的推荐模型。

  - 实验显示该方法在多种MoE骨干上稳健提升，说明即使推荐系统的底层LLM结构变化，该方法也能迁移复用，减少适配成本。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

动机：现有MoE模型的参数高效微调（PEFT）方法要么忽略预训练路由器先验（统一适配器），导致效率低和遗忘风险；要么静态选择专家，限制每个token的容量和跨专家特征学习。为此，作者提出将MoE的动态路由思想引入LoRA。

方法关键点：
- **双通道路由条件投影（RCP）**：重用基础MoE路由器的激活值，经双通道投影生成LoRA专家的选择权重，实现动态、token级的适配器路由，同时保留预训练专家的特化先验。
- **全局LoRA专家池**：在所有Transformer层之间共享同一组LoRA专家，使适配器能跨层复用，涌现出层间亲和性，并自然平衡专家利用率。
- 训练时只更新RCP模块和全局LoRA池的权重，冻结原始模型参数，参数量极低。

结果：在多个MoE骨干（不同模型大小、专家粒度）上评测，下游任务准确率均达到SOTA，同时保持甚至提升通用能力，验证了方法的有效性与泛化性。
