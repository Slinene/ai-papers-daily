---
title: Think Again or Think Longer? Selective Verification for Budget-Aware Reasoning
title_zh: 选择性验证：预算感知的推理分配方法
authors:
- Sajib Acharjee Dip
- Dawei Zhou
- Liqing Zhang
affiliations:
- Department of Computer Science, Virginia Tech
- Fralin Biomedical Research Institute, Virginia Tech
- FBRI Cancer Research Center, Washington, DC
arxiv_id: '2606.19808'
url: https://arxiv.org/abs/2606.19808
pdf_url: https://arxiv.org/pdf/2606.19808
published: '2026-06-17'
collected: '2026-06-19'
category: Reasoning
direction: 推理时计算资源分配优化
tags:
- Selective Verification
- Budget-Aware Reasoning
- Test-time Compute
- Gating
- Verification Allocation
one_liner: SEVRA用门控机制选择性触发验证，在提升准确率的同时大幅削减后生成token开销
practical_value: '- **选择性验证降低服务成本**：在推荐Agent或RAG管线中，对LLM生成的解释、候选理由进行二次验证会增加延迟和费用，可训练轻量门控模型（基于初始输出的隐含状态或置信度特征）决定是否触发验证，避免全量验证，参考SEVRA将验证token减少26.8%~91.2%的收益。

  - **优先扩展初始推理预算**：实验表明延长初始生成（如增加token限制）往往比事后验证更高效，在推荐场景中，若已为LLM分配推理预算，应优先投入在首次生成更长、更细致的推理链，而非立即增加验证步骤。

  - **门控模型可跨任务迁移**：SEVRA的门控策略从数学任务直接迁移到常识推理无需重训，仍能保持高精度且大幅减少验证调用，暗示在领域迁移时，基于求解器状态的“可恢复性”特征具通用性，可尝试复用于搜索词推荐、文案生成等不同任务的验证控制。

  - **显式控制有害翻转**：对于高敏感场景（如电商价格推荐、法律合规审查），SEVRA将有危害性答案翻转率从2.2%降至1.0%，这种“先判定再验证”的思路可用于拦截LLM在二次推理时可能引入的错误修改，提升输出稳定性。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：推理时追加验证并非总是划算——它可能修复错误，但也可能浪费算力在已正确解答上，甚至将正确答案改错。因此需要一种部署层面的分配策略，动态决定何时触发验证。

**方法**：提出SEVRA（Selective Verification for Reasoning Allocation），在服务层冻结求解器（如Qwen3-4B），记录初始解答状态（如推理路径、置信度信号），训练一个可恢复性感知的门控模型，判断是否调用验证器进行修正。该门控仅在需要时引入额外推理，避免全量验证。

**关键结果**：
- MATH500: 选择性验证准确率76.3% > 全验证75.5%，同时减少26.8%后生成token，有害翻转率从2.2%降至1.0%。但单纯延长初始生成预算（8192 token）可得76.0%准确率且总token更少，揭示初始预算调优优先于验证。
- GSM8K: 选择性策略仅验证3.0%样本，准确率从93.4%提升至94.5%，验证token减少91.2%。
- CommonsenseQA: 全验证反而损害性能；Self-Consistency@5可提升准确率但token成本增约5倍。
- 部署规则：先尽可能分配初始推理预算，再在需要显式检查、审计或回归风险控制时启用选择性恢复。
