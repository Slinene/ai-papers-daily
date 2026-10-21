---
title: Predicting Privileged Information Effectiveness for On-Policy Self-Distillation
title_zh: 预测策略内自蒸馏中特权信息的有效性
authors:
- Kaijian Zou
- Emiliano Penaloza
- MohammadHossein Rezaei
- Anisha Gunjal
- Mohit Raghavendra
- Lu Wang
- Yunzhong He
- Anas Mahmoud
affiliations:
- University of Michigan – Ann Arbor
- Mila
- Scale AI
arxiv_id: '2610.22512'
url: https://arxiv.org/abs/2610.22512
pdf_url: https://arxiv.org/pdf/2610.22512
published: '2026-10-14'
collected: '2026-10-21'
category: Training
direction: 多轮代理场景下的自蒸馏训练
tags:
- on-policy self-distillation
- privileged information
- KL divergence
- multi-turn agents
- LLM training
- evaluation
one_liner: 系统评估多轮代理场景下16种特权信息配置，提出KL散度指标预测其训练收益
practical_value: '- PI 的内容与生成源比固定设计更重要：优先选择信息密度高、由更强模型生成的轨迹片段作为 PI，尤其在多轮 Agent 对话中可显著提升自蒸馏收益。

  - 训练前用 KL 指标预筛 PI 候选：计算 sampled-token reverse KL (D) 与 error-step KL contrast (Δd^{-}_{err})，比直接看
  PI utility 更能稳定预测训练后性能，可避免信息泄漏导致的误判。

  - 当候选 PI 差异较大时，利用 Δd^{-}_{err} 为每个任务动态选择 PI，比随机选择平均提升更高；适合业务中多任务、多轨迹来源的场景。

  - 自蒸馏目标可与 GRPO 等强化学习目标结合，在有效 PI 下获得比纯 GRPO 更强的性能，适合需要兼顾模仿与探索的电商 Agent 训练。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：On-policy self-distillation (OPSD) 让 LLM 从特权信息 (PI) 中自我改进，无需独立教师模型，但 PI 的内容与构造方式对训练效果的影响缺乏系统理解，尤其在多轮代理场景中，轨迹包含动作、观察与推理，可被转化为多种 PI。

**方法**：在三个多轮代理基准上，系统评估 16 种 PI 配置，覆盖三种不同规模与推理模式的 student 模型。提出两种 KL 散度指标：sampled-token reverse KL (D) 与 error-step KL contrast (Δd^{-}_{err})，用于在训练前评估 PI 的有效性，并与 PI utility 进行对比。

**关键结果**：PI 有效性取决于内容、生成源与学生模型：信息密度高的轨迹和由更强生成器产生的 PI 带来更大增益，但 thinking 模型受益不稳定；KL 指标比 PI utility 更一致地预测训练后性能；按 Δd^{-}_{err} 选择每个任务的 PI 优于随机选择，尤其在 PI 候选差异大时；有效 PI 与 GRPO 结合可超越强 GRPO 基线。
