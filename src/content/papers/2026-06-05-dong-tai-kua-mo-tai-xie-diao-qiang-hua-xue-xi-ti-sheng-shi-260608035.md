---
title: 'DyCo-RL: Dynamic Cross-Modal Coordination for Visual Reasoning'
title_zh: 动态跨模态协调强化学习提升视觉推理
authors:
- Hangui Lin
- Yan Shu
- Zhengyang Liang
- Chi Liu
- Xiangrui Liu
- Minghao Qin
- Teng Long
- Zheng Liu
- Nicu Sebe
affiliations:
- University of Trento
- BAAI
- Singapore Management University
- IQuest Research
arxiv_id: '2606.08035'
url: https://arxiv.org/abs/2606.08035
pdf_url: https://arxiv.org/pdf/2606.08035
published: '2026-06-05'
collected: '2026-06-13'
category: Multimodal
direction: 多模态大模型视觉推理训练优化
tags:
- RLVR
- Visual Reasoning
- MLLMs
- Cross-modal Coordination
- Fisher-Rao Geodesic
one_liner: 通过对齐token功能角色与实际注意力分配，改进RLVR中的跨模态协调
practical_value: '- 多模态电商/推荐系统（如商品图文联合推理）可借鉴 token 功能角色划分思想，显式建模视觉感知与文本推理步骤的交替，减少幻觉或不一致。

  - 在强化学习训练中，可引入基于注意力对齐的中间过程信号作为辅助奖励或重要性权重，而不仅依赖最终结果奖励，有助于提升生成序列的合理性。

  - Fisher-Rao geodesic 距离可用于分析序列生成时模态内的注意力转移模式，作为一种新的可解释性工具，诊断多模态 Agent 的信息流问题。

  - 对多模态 Agent 的 CoT 推理设计，可显式区分“提取视觉证据”步与“文本上下文推理”步，并加入对齐约束，提高决策准确性。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有 RLVR 方法训练多模态大模型（MLLM）进行视觉推理时，仅优化最终答案正确性，忽略了生成过程中动态跨模态协调。作者通过 token 级分析发现，CoT 推理中模型常未能正确交替执行“提取视觉证据”与“合成文本上下文”，这种协调失效与推理错误有因果关联。

**方法**：提出 DyCo-RL，将动态跨模态协调融入 RLVR 优化。首先，利用 Fisher-Rao geodesic 距离度量同一模态内相邻 token 的注意力偏移，据此为每个 token 分配视觉倾向或文本倾向的功能角色。然后，计算 token 实际注意力分配与其指定角色的对齐分数。最后，将该对齐分数作为优势重加权的引导项，在策略梯度中调整 token 更新幅度，使优化过程更关注协调良好的 token。

**结果**：在 Qwen2.5-VL-3B/7B 上，将 DyCo-RL 应用于 GRPO、DAPO、Dr.GRPO 和 DeepEn-Thinker 四种主流 RLVR 算法，在 7 个视觉中心与数学推理基准上均取得一致性提升，证明了方法的算法无关性和有效性。
