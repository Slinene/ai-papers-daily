---
title: 'The Other Half of the Memory Wall: Serving 35B MoEs from SSD with Trained
  Routing Prediction'
title_zh: 内存墙的另一半：用训练的路由预测从 SSD 服务 35B MoE
authors:
- Yu Lin
- Yiming Wang
- Runyuan Cai
- Hanze Liu
- Xiaodong Zeng
affiliations:
- AutoArk
arxiv_id: '2609.18063'
url: https://arxiv.org/abs/2609.18063
pdf_url: https://arxiv.org/pdf/2609.18063
published: '2026-09-15'
collected: '2026-09-18'
category: LLM
direction: LLM 推理优化 · SSD offloading
tags:
- MoE
- Offloading
- Inference
- Routing Prediction
- LoRA
- Memory Wall
one_liner: Edge0 用下一层路由预测实现 SSD 流式加载专家权重，在单 24GB 卡上以 20 tok/s 服务 35B MoE，质量接近 fp16
  教师
practical_value: '- 在资源受限的单卡环境部署 LLM 推荐/Agent 时，可采用 SSD offload + 路由预测预取：只加载预测命中的专家，用下一
  token 的路由预测提前发起 I/O，隐藏磁盘延迟，降低峰值显存。

  - 量化部署大模型时，可用未合并的 recovery LoRA 在量化后的 student path 上训练，补偿 int4 量化与路由替换带来的质量损失，推理时只增加极小的
  adapter 计算，适合线上低时延场景。

  - 路由预测思想可迁移到 Agent 多步推理或生成式推荐流水线：预测下一步需要的模型/数据组件并提前加载，减少串行等待，提升吞吐。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：MoE 推理在消费级硬件受权重内存限制，35B 模型 4-bit 约 19.5GB，稀疏激活减少计算但不减少常驻权重。单纯 SSD offloading 无效，因为下一层专家必须等上一层输出才能确定，读取无法提前隐藏于计算。

**方法关键点**：Edge0 引入 per-layer prerouter，在 token t 预测下一层 t+1 的路由，并将该预测直接作为路由使用，使得预取的专家集与实际路由一致，不丢弃任何专家。同时用未合并的 recovery LoRA 在量化后的 student path 上训练，弥补 int4 量化和路由替换造成的质量损失。

**关键结果**：单 24GB 机器上，Edge0 以约 20 tok/s 服务 35B MoE，峰值活跃内存仅 3GiB；在五个公开基准上平均只比 fp16 教师低几个点，8B 模型同样运行在相同框架，框架、checkpoint、adapter 全部开源。
