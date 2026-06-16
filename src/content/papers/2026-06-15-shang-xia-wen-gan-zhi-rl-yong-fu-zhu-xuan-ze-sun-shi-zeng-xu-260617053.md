---
title: Context-Aware RL for Agentic and Multimodal LLMs
title_zh: 上下文感知RL：用辅助选择损失增强长序列与多模态证据接地
authors:
- Peiyang Xu
- Bangzheng Li
- Sijia Liu
- Karthik R. Narasimhan
- Pramod Viswanath
- Prateek Mittal
- Xingyu Fu
affiliations:
- Princeton University
- UC Davis
arxiv_id: '2606.17053'
url: https://arxiv.org/abs/2606.17053
pdf_url: https://arxiv.org/pdf/2606.17053
published: '2026-06-15'
collected: '2026-06-16'
category: Training
direction: 上下文感知强化学习 · 多模态与Agent
tags:
- Context-Aware RL
- GRPO
- Contrastive Context
- Agentic
- Multimodal
- Grounding
one_liner: 在 GRPO 中增加对比上下文选择辅助损失，显著提升 Agent 与多模态 LLM 的证据接地能力
practical_value: '- **辅助上下文选择损失**：在现有 RL（如 GRPO）训练中，同时训练一条「给定 query-answer，从一对相似但结论相反的上下文中选出支持该答案的正确上下文」的辅助任务，可作为轻量插件提升模型对关键证据的敏感度。

  - **构造对比上下文对的工程方法**：Agent 场景用轨迹过滤（同仓库、同文件、同函数、不同 issue + 答案掩码）构造 1k 高质量对，多模态用生成编辑+相似检索构造
  7k 对，避免人工标注。业务中可类似挖掘正负用户行为序列、对比商品图文等。

  - **避免将对比数据简单用于 SFT 或混入 RL 奖励**：实验表明，用对比数据做 SFT 会严重破坏长序列策略（编码 Agent 任务 resolve rate
  从 28% 跌至 1.3%），单纯作为二元奖励加入 RL 几乎无效；只有设计为辅助 logit 级损失并配合 GRPO 的 clip/KL 约束，才能稳定获益。

  - **长序列推荐/Agent 的场景直接复用**：在用户长行为序列、商品描述、多模态推荐中，可通过构造「仅关键一步不同」的正负上下文对，用相同辅助损失强化模型抓取关键信息，提升长程一致性和抗噪声能力。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

## 动机
LLM 在长上下文（如 Agent 多轮轨迹）和多模态（图像细节）中常出现**上下文不感知**：关键证据明明在上下文中，却未能被模型抓取并用于决策。本文先用一个简单的对比上下文探测任务验证开源模型接近随机选择，与强闭源模型差距达 40 点，说明证据接地是普遍短板。

## 方法
提出 **CONTEXTRL**，在 GRPO 基础上增加一个**对比上下文选择辅助损失**。

### 1. 构造对比上下文对
- **Agent 轨迹对**：从 SWE‑smith 的 66k 轨迹中，通过「同仓库、同 commit、同文件、同函数、不同 issue」等严格级联过滤，并用 `<PATCH_MASKED>` 掩盖编辑指令，保留思考/工具输出，经 GPT‑5.4 验证和人工复审，获得 1k 高质量对。  
- **多模态图像对**：自然图像用生成编辑（指令生成→图像合成→人工/自动审核，过滤编辑痕迹和整体偏移），结构化图像用相似度检索（Qwen3‑VL‑Embedding，余弦≥0.85），合计 7k 对。

### 2. 辅助损失设计
给定 `(Q, A, C⁺, C⁻)`，将正负上下文作为选项 A/B 随机化，用 teacher forcing 计算模型在两个选项 token 上的 logits 差，经裁剪后做 sigmoid 交叉熵，鼓励模型选择支持答案的正确上下文。

### 3. 联合训练
`L = L_GRPO + λ·L_CA`，λ 取 0.001–0.005。

## 关键实验
- **Agent 评估**：在 SWE‑Bench Verified/Lite 等 5 个基准上，Qwen3‑8B 平均 +1.5%，Klear‑AgentForge‑8B 平均 +3.2%，NIAH 长上下文检索从下降转为超越基准。  
- **多模态评估**：12 个 VQA 基准，Qwen2.5‑VL‑7B 平均 +2.0%，Qwen3‑VL‑8B 平均 +1.6%，所有子类别一致提升。  
- **消融对比**：同样对比数据用于 SFT 或混入 RL 奖励（DA‑SFT / DA‑RL）几乎不带来提升，甚至导致长序列任务崩溃（Agent resolve rate 直接掉至 0–1.3%）。只有辅助损失形式能稳定转化对比数据为性能增益。

## 核心结论
**“对比数据本身不是关键，如何将上下文选择信号融入训练才是。”** CONTEXTRL 提供了一种极简、模态无关的辅助训练方式，可广泛用于提升模型在长上下文与多模态场景中的证据接地能力。
