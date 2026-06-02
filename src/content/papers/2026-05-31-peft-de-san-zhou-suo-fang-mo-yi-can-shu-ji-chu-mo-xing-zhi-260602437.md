---
title: 'On the Scaling of PEFT: Towards Million Personal Models of Trillion Parameters'
title_zh: PEFT 的三轴缩放：万亿参数基础模型支撑百万持久个性化模型
authors:
- Mind Lab
- Song Cao
- Vic Cao
- Kaijie Chen
- Bunny Fan
- Hera Feng
- Huan Feng
- Arthur Fu
- Jun Gao
- Hongquan Gu
affiliations:
- Mind Lab
arxiv_id: '2606.02437'
url: https://arxiv.org/abs/2606.02437
pdf_url: https://arxiv.org/pdf/2606.02437
published: '2026-05-31'
collected: '2026-06-02'
category: Training
direction: PEFT 缩放 · 个性化模型 · LoRA RL
tags:
- LoRA
- PEFT
- Scaling
- Personalization
- RL
- MoE
one_liner: 通过 Scale Up（强先验）、Scale Down（小型稳定适配器）与 Scale Out（适配器种群）三轴协同，让 LoRA 在万亿 MoE
  上实现低成本、可持续的个性化 RL 更新与集体智能。
practical_value: '- **用户级 LoRA 适配器**：电商推荐或 Agent 系统可对每个用户或 Agent 实例维护一个 LoRA adapter，仅更新
  <1% 参数即可捕获长期偏好、技能或工具使用习惯，成本远低于完整模型微调。

  - **RL 训练的稳定初始化**：在 RLHF 或 RLVR 场景中，极低秩 adapter (rank=1) 的初始化不能简单复用 SFT 下的 SVD 初始化，应使用控制初始更新幅度的
  RL-native 方法（如 OLoRA-tail），避免策略漂移导致 KL 崩溃。

  - **多 Adapter 投票提升决策质量**：当存在多个来自不同用户或 Agent 的 adapter 时，可借鉴论文中基于多样性的大数投票机制，聚合多个适配策略输出，在推理阶段获得集体智能收益（AIME24
  准确率从单模型 36.4% 提升到 198 模型的 48.7%）。

  - **训练–推理一致性**：大规模 MoE 部署个性化模型时，路由差异会导致训练策略与线上策略不一致，采用 Router Replay R3 等技术记录并回放路由决策，可保证
  RL 更新的有效性。'
score: 10
source: huggingface-daily
depth: full_pdf
---

**动机**：前沿基础模型能力与日俱增，但打造一个能持久记忆个人偏好、技能与行为的个性化助手仍然困难。传统上下文检索和提示无法完全满足“持久状态”的需求。该工作将 PEFT（尤其是 LoRA）视作一种紧凑的“本地自适应状态”，让每个用户或 Agent 实例仅需更新极少参数，就能在共享先验上积累经验，从而支持百万级持久个性化模型。

**方法关键点**：
- **三轴缩放框架**：Scale Up（强化共享基础模型能力，使微小更新高杠杆）、Scale Down（将适配器缩至极低秩且保持稳定性，降低边际成本）、Scale Out（支撑大量适配器共存，实现群体智能）。
- **Trillion MoE + LoRA RL**：在 1T 参数 MoE 模型上应用 LoRA 进行 GRPO 式在线 RL，通过混合并行和路由协同设计，将计算/通信开销降至全参数 RL 的约 10%。
- **Router Replay R3**：针对 MoE 中训练–推理路由分歧导致的策略不一致，记录推理侧路由并在训练时重放，保证了 on-policy RL 的正确性。
- **低秩稳定性与初始化**：对 Qwen3-8B 进行 216 次 PPO 扫描，发现 rank=16–32 是实用甜蜜点；rank=1 时 best-run 仍可达标，但平均可靠性暴跌。提出 RL-native 初始化（OLoRA-tail），避免 SVD 初始化带来的过大更新幅度导致策略漂移。
- **Context Learning 写策略**：将上下文交互压缩为适配器更新，让个性化状态写入适配器。

**关键实验**：
- 在 Kimi K2 (1T MoE) 上，LoRA RL 将 GPU 需求降至全参数训练的 ~10%，训练曲线平滑且泛化能力无退化。
- Qwen3-8B PPO 扫描：rank=16/32 平均增益最高；低秩 (rank=1) 的 best-run 与中秩持平，但 mean-run 显著下降，且对 batch size 和随机种子极其敏感。
- Router Replay R3 使训练-推理概率差异和 KL 散度接近零，梯度更稳定，最终数学验证准确率更高。
- 多样化 LoRA 适配器的多数投票将 AIME24 准确率从单实例的 0.3644 提升至 0.4867 (k=198)，验证了群体智能。

**核心启示**：PEFT 不止是微调省钱方案，更是让大规模个性化模型与群体智能可行的缩放法则——共享一个强大的先验，让轻量适配器承载行为状态，通过种群多样性解锁新兴能力。
