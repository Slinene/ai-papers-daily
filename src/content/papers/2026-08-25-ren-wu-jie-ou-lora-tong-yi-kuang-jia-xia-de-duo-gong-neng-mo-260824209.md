---
title: Task-disentangled Low-Rank Adaptation for Versatile Audio-visual Multi-modal
  Learning Tasks within a Unified Framework
title_zh: 任务解耦 LoRA：统一框架下的多功能音视频多模态学习
authors:
- Hanyu Xuan
- Mengqi Zhang
- Junjun Mao
- Fei Wang
- Kun Li
- Guanghui Yue
- Zhiliang Wu
- Hehe Fan
arxiv_id: '2608.24209'
url: https://arxiv.org/abs/2608.24209
pdf_url: https://arxiv.org/pdf/2608.24209
published: '2026-08-25'
collected: '2026-08-30'
category: Multimodal
direction: 多模态多任务学习 · 任务解耦 LoRA
tags:
- Audio-Visual Learning
- Multi-task Learning
- LoRA
- Task Disentanglement
- Unified Framework
one_liner: 用任务解耦 LoRA 在统一 LLM 框架中整合通用知识、任务特定模式与跨任务协作，缓解多任务干扰。
practical_value: '- 在多目标/多场景推荐与搜索统一模型中，可借鉴“通用 LoRA 底座 + 任务调制矩阵”的架构：共享低秩空间保留通用表征，任务特定矩阵做轻量解耦，比完全共享或独立微调更抗干扰，也便于快速接入新任务。

  - 跨任务协作专家通过可学习门控显式建模任务间相关性，适合电商 CTR、CVR、GMV 等多目标联合优化，减少负迁移；可优先对相关性强的任务组开启协作路径。

  - 以 LLM/LoRA 参数高效适配多模态输入，适合商品图、文案、短视频素材统一编码；按任务插入不同调制层即可扩展类目识别、属性抽取、卖点生成等，不必为每个任务完整微调大模型。

  - 若业务要建设多模态统一理解底座，可参考“模型侧与任务侧双重显式协作”思路，避免 naive joint training 带来的互相干扰。'
score: 6
source: arxiv-cs.MM
depth: abstract
---

动机：现有音视频多模态学习大多按单任务分别训练，与人类统一的感知能力相悖；而直接多任务联合训练又会因任务间关系复杂而互相干扰。

方法关键点：以 LLM 为统一底座，设计任务解耦 LoRA 机制，包含三部分：任务通用低秩矩阵捕捉通用音视频知识；任务特定调制矩阵负责解耦不同任务的特有模式；跨任务协作专家通过可学习门控挖掘任务间相关性。整体从模型侧和任务侧同时引入显式协作，实现多个 AVMML 任务在同一框架内训练。

关键结果：在多个 AVMML 任务上超过现有统一音视频模型，并在部分任务上超过多数单任务专用模型。
