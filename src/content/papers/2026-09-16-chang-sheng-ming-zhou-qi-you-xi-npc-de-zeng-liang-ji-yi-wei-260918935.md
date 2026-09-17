---
title: 'Long-Lived Characters, Local Inference: Incremental Memory Maintenance for
  Game NPCs'
title_zh: 长生命周期游戏 NPC 的增量记忆维护
authors:
- Zimu Xu
affiliations:
- University of Bern
arxiv_id: '2609.18935'
url: https://arxiv.org/abs/2609.18935
pdf_url: https://arxiv.org/pdf/2609.18935
published: '2026-09-16'
collected: '2026-09-17'
category: LLM
direction: LLM 推理 · 增量记忆维护
tags:
- incremental memory
- KV cache
- NPC
- LLM inference
- recurrent-attention
- agent memory
one_liner: 提出 LLM 运行时增量更新记忆的机制，避免重算长前缀并保持语义绑定
practical_value: '- 在电商对话 Agent 或推荐助手中，当用户画像、订单状态等关键信息发生增量变化时，可以采用类似“移除被取代 KV 条目 +
  在真实序列尾部追加更新”的策略，避免每次重新编码全部历史，显著降低本地部署的推理延迟和计算成本。

  - 记忆更新应放在序列尾部而非原位覆盖：实验表明 true-tail updates 能避免 slot-preserving 方法出现的“双减法”类状态错误，这对需要精确状态追踪的电商规则系统（如库存、优惠券核销）尤其重要。

  - 评估记忆维护系统时不能只看注意力分布相似度：论文发现注意力接近性无法解释语义差异，因此电商 Agent 的长期记忆评估应以下游任务准确率（如订单修改后的库存判断）为准。

  - 混合循环-注意力架构（如 Qwen）在长上下文场景中能平衡效率与效果，可作为需要长期用户上下文记忆的生成式推荐 Agent 的候选基座。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：本地部署的 LLM 游戏 NPC 每次修改少量记忆都需要重读整个生命历史，因为修改会使长前缀的 KV cache 失效，准备成本与前景对话和其他角色维护竞争。当对话连接游戏规则系统（如物品归属、转移是否已发生）时，记忆错误会直接破坏确定性规则。

**方法关键点**：在量化 Qwen 混合循环-注意力模型上研究增量记忆维护。运行时移除被取代的注意力 KV 条目，在真实序列尾部计算替换记录，保留持续循环状态和未改变的 KV。通过多更新对话重放、固定输入位置消融和注意力诊断进行实验。

**关键结果**：独立块组合削弱查询条件记忆选择，但无均匀块初始注意力崩溃。True-tail 更新在八轮脚本维护中保留重要当前状态和历史绑定；一个放置案例三次重建恢复完整补充量，而保留槽位的替代方案重复双减法错误。注意力分布接近性不能解释这些语义差异。结论：角色推理状态应视为维护的历史依赖资源，而非最新记忆文本的一次性编码。
