---
title: 'AngelSpec: Towards Real-World High Performance Inference with Speculative
  Decoding'
title_zh: 'AngelSpec: 面向真实负载的推测解码训练与部署框架'
authors:
- Hong Liu
- Rui Cen
- Junhan Shi
- Guangshuo Qin
- Jiebin Zhang
- Tianyu Liu
- Runzhi Fan
- Guoliang Zhao
- Ruobing Xie
- Kai Zhang
affiliations:
- Tencent Inc.
arxiv_id: '2607.25852'
url: https://arxiv.org/abs/2607.25852
pdf_url: https://arxiv.org/pdf/2607.25852
published: '2026-07-28'
collected: '2026-07-29'
category: LLM
direction: 推测解码 · 多策略协同与自适应验证
tags:
- Speculative Decoding
- Multi-Token Prediction
- Block Diffusion
- LLM Inference
- Adaptive Verification
- AngelSpec
one_liner: 针对负载异构，专业化MTP与块扩散drafter，配合自适应验证深度，在Hy3-21B上实现1.98–2.40倍加速
practical_value: '- 若业务LLM服务需加速（如推荐解释生成、query改写），可借鉴“工作负载特化”思想：为闲聊等高熵场景训练MTP drafter；为代码生成等低熵场景训练块扩散drafter，提升接受率。

  - D-cut的自适应验证深度策略可迁移至Agent多步推理：根据请求置信度与系统负载动态决定LLM生成步数，平衡响应时间与质量，避免固定budget浪费。

  - 训练技巧：Training-Time Test（TTT）和基于总变差距离（TV loss）的损失函数可有效缓解drafter分布偏移，对低延迟场景（如在线推荐）有直接应用价值，可复用其接受率对齐训练范式。

  - AngelSpec开源训练框架支持多drafter联合训练与评估，降低企业自研推测解码方案的门槛，适合多领域LLM应用的快速实验。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**：真实世界LLM服务面临高度异构的负载——开放聊天熵高，代码与数学推理则存在长程可预测段。单一推测解码drafter无法在所有场景最优，需要从训练、架构与运行时联合优化。

**方法**：
1. **特化训练**：为对话数据训练轻量MTP drafter，为代码/数学数据训练块扩散drafter DFly；MTP采用共享参数的多深度TTT自回归rollout，并用TV‑based损失（LK冷启动 + end‑to‑end TV）显式优化接受率。
2. **DFly架构**：混合目标条件骨干（融合DFlash的全局投影与DFlare的层特定目标视图），增加前任条件自回归头（隐藏校正），在保持块级并行的同时引入块内依赖，提升长块接受质量。
3. **D‑cut自适应验证**：将目标模型验证视为批次共享资源；基于前缀置信度估计各请求预期收益，结合离线的运行时成本表，动态选择全局验证深度（0.25–1.0倍块长），在高并发下裁剪低效用后缀，平衡吞吐与延迟。

**关键结果**：在Hy3‑A21B上，DFly平均接受长度较MTP提升59.7%，较DFlash提升29.8%。搭配D‑cut后，在真实生产流量（404B MoE，TP=8）中，并发64下吞吐较纯DFly提升15.7%，较自回归解码加速1.98–2.40×，且在各并发级别平均吞吐最高。消融表明混合条件骨干+隐藏校正头的组合贡献最大，域数据扩展进一步巩固代码/数学优势。
