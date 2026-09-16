---
title: 'Decoy Direction Optimization: A Post-Hoc Defense Against LLM Abliteration'
title_zh: 诱饵方向优化：针对 LLM 消融攻击的事后防御
authors:
- Aashiq Muhamed
- Mona T. Diab
- Virginia Smith
affiliations:
- Carnegie Mellon University
arxiv_id: '2609.16204'
url: https://arxiv.org/abs/2609.16204
pdf_url: https://arxiv.org/pdf/2609.16204
published: '2026-09-13'
collected: '2026-09-16'
category: LLM
direction: LLM 安全 · 权重编辑防御
tags:
- LLM Safety
- Weight Editing
- Refusal Feature Ablation
- Post-Hoc Defense
- Adversarial Robustness
one_liner: 注入高幅非线性诱饵方向扰乱攻击者的消融估计器，低成本后处理防御 RFA
practical_value: '- 若业务部署开源 LLM 做客服/内容审核，担心白盒消融攻击移除安全护栏，可用 DDO 做一次性后处理权重编辑，免去每个新 checkpoint
  全量安全微调，优化成本低 30–450 倍。

  - 借鉴思路：不隐藏真实拒绝特征，主动注入高幅非线性“诱饵”方向，让攻击者的对比估计失效并消融到无害正交特征，适合保护模型核心能力不被逆向抽取或探测。

  - 工程实现只修改 MLP 神经元权重，不改变推理架构、不引入额外 KV cache 或算子，便于接入现有推理管线，风险低。

  - 对推荐/Agent 场景，若部署专有策略模型，可利用“注入伪特征”增加黑盒探测成本，类似对抗防御思路保护知识产权。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：开放权重 LLM 的安全护栏容易被 Refusal Feature Ablation (RFA) 这类白盒攻击移除，攻击者通过对比估计找出线性拒绝方向并投影掉，通常能保持模型能力同时绕过安全约束；传统防御需要为每个新 checkpoint 做昂贵的微调。

**方法关键点**：提出 Decoy Direction Optimization (DDO)，一种无需微调的事后权重编辑防御。基于机制洞察：RFA 攻击依赖对比估计定位拒绝方向。DDO 不隐藏真实拒绝回路，而是主动在 MLP 神经元注入高幅、非线性诱饵信号，污染攻击者的估计器，使其消融到无害正交特征，真实安全机制保持不变。推导谱界形式化该效果。

**关键结果**：在 6 个模型家族上，标准 RFA 攻击下 ASR 低于 10%；Llama-3-8B-Instruct 上，自适应多阶段攻击最差 ASR 为 65%，与训练防御的 58% 可比；将 Heretic 权重级攻击 ASR 从 88.7% 降至 18%；每个配置的优化成本比训练型防御低 30–450 倍。
