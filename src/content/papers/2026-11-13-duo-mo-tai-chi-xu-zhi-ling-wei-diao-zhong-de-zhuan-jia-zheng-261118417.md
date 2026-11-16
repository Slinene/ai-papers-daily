---
title: 'CoPre-MoE: Consolidating and Preserving MoE for Multimodal Continual Instruction
  Tuning'
title_zh: 多模态持续指令微调中的专家整合与保持 MoE 方法
authors:
- Tao Hu
- Ling-Xiang Zhang
- Da-Wei Zhou
affiliations:
- School of Artificial Intelligence, Nanjing University
- State Key Laboratory for Novel Software Technology, Nanjing University
arxiv_id: '2611.18417'
url: https://arxiv.org/abs/2611.18417
pdf_url: https://arxiv.org/pdf/2611.18417
published: '2026-11-13'
collected: '2026-11-16'
category: Training
direction: 多模态持续学习 · MoE 参数压缩
tags:
- MoE
- Continual Learning
- Multimodal
- Parameter Efficiency
- Catastrophic Forgetting
one_liner: 提出 CoPre-MoE，通过共享-私有专家池整合冗余并冻结历史路由键，在抑制遗忘同时大幅降低多模态持续学习参数开销
practical_value: '- 多场景推荐/搜索模型持续迭代时，可借鉴共享-私有专家池设计：将跨业务通用能力（如用户意图理解、图文匹配）沉淀到固定容量通用专家池，场景特有专家用低秩分解（共享投影基+紧凑核心）控制参数量。

  - 路由侧用可学习 retrieval key 代替普通 softmax 门控：新增任务/场景时冻结历史专家对应的 key，并对新 key 加正交惩罚，避免新旧任务路由混淆，缓解旧场景效果回退。

  - 定期评估专家间功能重叠（例如用交叉替换验证），主动合并冗余专家，能在不损失精度前提下减少 MoE 层参数和推理计算量，适合长期在线学习系统。

  - 推理无需任务 ID，动态路由自动组合通用与私有专家，便于部署到统一线上服务，无需请求侧传入场景标签。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：多模态大语言模型（MLLM）持续指令微调要求顺序学习新任务且避免灾难性遗忘。现有基于 MoE 的方法为每个任务分配独立专家，虽隔离了参数更新，但随任务增多出现跨任务功能冗余（如 ScienceQA 与 TextVQA 都需要定位图像区域），且参数量线性增长，推理开销变大。

**方法关键点**：CoPre-MoE 提出“先学习后压缩”的范式。对每个新任务先训练 task-specific MoE；随后通过功能重叠评估，将跨任务冗余专家合并到一个固定容量的通用专家池（shared pool），剩余专家分解为共享投影基 + 紧凑任务特定核心，存入私有专家池（private pool），显著降低参数增长。路由端为每个专家设置可学习 retrieval key，历史 key 冻结，新 key 施加正交正则，防止与旧任务冲突；推理时根据输入动态组合两个池，无需测试任务标签。

**关键结果**：在 UCIT 等多模态持续学习基准上，CoPre-MoE 在保持或超越现有方法精度的同时，大幅削减了参数增量，缓解了遗忘；图1显示跨任务专家替换实验证明冗余普遍存在，验证了合并策略的合理性。
