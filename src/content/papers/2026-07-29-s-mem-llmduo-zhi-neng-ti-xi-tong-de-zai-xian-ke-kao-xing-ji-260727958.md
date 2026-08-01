---
title: 'Σ-Mem: An Online Reliability Memory for LLM-based Multi-Agent Systems'
title_zh: Σ-Mem：LLM多智能体系统的在线可靠性记忆
authors:
- Peilin Feng
- Suorong Yang
- Soujanya Poria
affiliations:
- Nanyang Technological University
arxiv_id: '2607.27958'
url: https://arxiv.org/abs/2607.27958
pdf_url: https://arxiv.org/pdf/2607.27958
published: '2026-07-29'
collected: '2026-08-01'
category: MultiAgent
direction: 多智体可靠性记忆与自适应协调
tags:
- MultiAgent
- Reliability Memory
- LLM Steering
- Online Learning
- Weyl's Inequality
one_liner: 提出在线维护 peer 能力与关系的可靠性记忆，通过残差引导、路由与投票复用，无需重训模型
practical_value: '- **可靠性记忆即服务**：可对电商搜索/推荐中的多个 LLM agent（如意图解析、商品理解、排序）分别维护能力矩阵，根据历史正确反馈动态调整其在集成投票或路由中的权重，无需反复微调中心模型。

  - **稳定在线更新**：使用衰减对称矩阵 + Weyl 不等式保证单事件扰动有界，使长期可靠性能持续累积，避免噪声突发扭转信任。适用于广告竞价策略或推荐多路召回融合中的在线信誉更新。

  - **无应答也能路由**：直接读取记忆得分 $s_{p,t}= \phi(x_t)^\top M_p \phi(x_t)$ 即可选 peer，决策时不依赖 agent
  输出，可复用于多路召回合并前的最优召回器选择，降低中心模型推理成本。

  - **关系证据补充**：记录 peer 之间的正确性共现关系，可识别共谋偏见或相关性错误，适用于推荐系统多模型融合时判断一致性是否真正可靠。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
多智能体系统中，中心模型无法直接验证所有 peer 的答案，当多个 peer 给出相同但错误的答案时，仅凭内容记忆无法区分真实一致性还是共谋偏见。现存记忆系统只记录交互内容（“发生了什么”），缺少对“谁可靠、何时可靠”的建模。

**方法**
- **双重成分**：每个 peer 维护一个对称能力矩阵 $M_p \in \mathbb{R}^{r \times r}$（历史能力证据）以及一个全局关系矩阵 $G \in \mathbb{R}^{P \times P}$（peer 正确性共现关系）。
- **稳定更新**：事件后以 $M_p \leftarrow \gamma M_p + \eta c_{p,t} \phi(x_t)\phi(x_t)^\top$ 更新，利用 Weyl 不等式保证单次扰动有界，持久信号累积，噪声衰减。关系矩阵类似用中心化正确性向量外积更新。
- **决策读写**：① 残差引导：将 $M_p$ 读出的方向通过可学习投影注入中心模型上层残差流，影响注意力，计算 Yes/No 似然差作为效用 $U_{p,t}$，联合 $G$ 做后验推断选 peer。② 直接路由：只用 $s_{p,t}=\phi(x_t)^\top M_p \phi(x_t)$ 选最高分 peer，不看回答。③ 可靠性加权投票：以 $s_{p,t}$ 为权重聚合回答。

**关键结果**
- 在 Qwen 0.6B~9B 五个中心模型上，混合反事实攻击下：CF@90 可靠 peer 翻转时，Σ-Mem 将弱基座(0.6B)准确率从 46.22% 提至 71.10%。
- 用 3 peer 训练，测试时扩展到 4/5 peer（含未见模型），泛化良好；跨 OOD 任务（PIQA, MMLU, BBH 等）30 例中 27 例提升，BBH 增益尤其明显。
- 同一记忆支持无中心模型的直接路由和加权投票，整体准确率 60.67%~60.99%，超过多数投票(59.12%)和最佳固定 peer(57.52%)。随反馈率从 5% 到 100%，性能单调提升，记忆能可靠累积有用信号。
