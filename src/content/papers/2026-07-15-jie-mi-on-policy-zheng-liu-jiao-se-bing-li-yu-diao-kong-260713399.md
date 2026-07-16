---
title: 'Demystifying On-Policy Distillation: Roles, Pathologies, and Regulations'
title_zh: 揭秘 On-Policy 蒸馏：角色、病理与调控
authors:
- Rui Wang
- Hongru Wang
- Yi Chen
- Boyang Xue
- Tianqing Fang
- Wenhao Yu
- Kam-Fai Wong
affiliations:
- The Chinese University of Hong Kong
- Tencent AI Lab
arxiv_id: '2607.13399'
url: https://arxiv.org/abs/2607.13399
pdf_url: https://arxiv.org/pdf/2607.13399
published: '2026-07-15'
collected: '2026-07-16'
category: Training
direction: LLM 训练 · On-Policy 知识蒸馏
tags:
- On-Policy Distillation
- Teacher-Student
- Length Exploitation
- Signal Regulation
- Exploration Catalyst
- Advantage Clipping
one_liner: 系统分析 OPD 作为探索催化剂的两大病理（师生失配与长度剥削），并提出简易信号调控予以克服
practical_value: '- **蒸馏信号质量比教师规模更关键**：在电商搜索/推荐场景蒸馏大模型（如生成式推荐理由、查询词）时，应优先保障 token
  级监督信号的准确性，而非盲目使用更大教师模型。

  - **防止长度剥削的方法可直接复用**：当学生模型通过生成长度作弊（如冗余填充或过早截断）优化时，可引入 **advantage clipping 与 log-scale
  compression** 来消除长度相关性，使优化目标重回推理质量，这对生成式推荐、对话 Agent 等任务尤其有效。

  - **Prompt 多样性优先于单问题采样数量**：在构造 OPD 训练数据时，增加样本多样性比增加同一 prompt 的采样次数更能提升探索效率，可指导搜索推荐场景中的指令数据扩增。

  - **在推荐 Agent 训练中采用类似信号调控**：若使用 OPD 训练基于 LLM 的推荐 Agent 与学生模型，可借鉴本文的轻量级信号修正手段，规避师生不匹配导致的错误引导。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：On-policy distillation (OPD) 已是 LLM 后训练的标配，但其训练动态仍不清晰。本文系统研究 OPD 的角色、病理与调控，以解释其成败关键。

**方法关键点**：
- **角色澄清**：OPD 本质是探索催化剂，通过稠密 token 级指导引导学生走向正确推理路径，但无法突破模型能力上限。有效性完全取决于引导信号质量，且提升 prompt 多样性比增加单 prompt 采样数更重要。
- **病理揭示**：识别两大失效模式——**师生失配**（分布差距大时，信号偏离任务正确性，误导探索）与**长度剥削**（token 级目标导致学生通过截断或填充来操控奖励，陷入退化长度模式）。
- **调控方案**：提出轻量级信号调节——**advantage clipping 与 log-scale compression**，抑制异常奖励信号，确保探索沿真实梯度方向。

**关键结果**：在 7 个基准上，信号调控彻底消除长度剥削，蒸馏效果稳定超过普通 OPD 及 RLVR 基线，证实**信号质量而非教师规模**是 OPD 成功的关键。
