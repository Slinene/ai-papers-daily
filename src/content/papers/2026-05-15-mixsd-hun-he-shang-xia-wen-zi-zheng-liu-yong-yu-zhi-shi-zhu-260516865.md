---
title: 'MixSD: Mixed Contextual Self-Distillation for Knowledge Injection'
title_zh: MixSD：混合上下文自蒸馏用于知识注入
authors:
- Jiarui Liu
- Lechen Zhang
- Yongjin Yang
- Yinghui He
- Yingheng Wang
- Weihao Xuan
- Zhijing Jin
- Mona Diab
affiliations:
- Carnegie Mellon University
- University of Toronto
- University of Illinois Urbana-Champaign
- Princeton University
- Cornell University
arxiv_id: '2605.16865'
url: https://arxiv.org/abs/2605.16865
pdf_url: https://arxiv.org/pdf/2605.16865
published: '2026-05-15'
collected: '2026-05-20'
category: Training
direction: 知识注入 · 混合自蒸馏 · 分布对齐
tags:
- knowledge injection
- catastrophic forgetting
- self-distillation
- distribution alignment
- fine-tuning
one_liner: 提出MIXSD，通过混合基础模型自身专家与朴素条件采样构建分布对齐监督，大幅减轻知识注入时的灾难性遗忘。
practical_value: '- **用模型自身的语境采样作为监督信号**：在注入新知识时，不直接使用人工书写的目标文本，而是用基础模型在“看到事实”与“未看到事实”两种条件分布下采样的token混合生成训练目标，使监督更贴近模型原有分布，减少分布偏移带来的遗忘。

  - **通过混合率 `λ` 灵活控制注入与保留的平衡**：λ=0.3–0.5 通常可保持注入准确率的同时大幅提升通用能力保留；在电商/Agent 场景下，可将该超参数作为调节“领域知识吸收
  vs 通用能力保持”的杠杆，无需复杂正则化。

  - **替代昂贵的 on‑policy 自蒸馏**：MIXSD 仅需一次离线生成混合 rollouts，训练成本与 SFT 相近，却显著优于 OPSD 等 on‑policy
  方法，适合工业级知识注入流程。

  - **用 Fisher 对齐比率诊断遗忘风险**：发现参数更新方向（而非幅度）与遗忘强相关，可在微调过程中监控该指标，提前预警能力退化；对于 Agent 多步推理能力保持尤其重要。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
supervised 微调（SFT）是注入新知识的主流手段，但常导致灾难性遗忘，损害模型的推理、指令遵循等预训练能力。作者认为根源在于 SFT 目标序列由外部编写，偏离模型自身的自回归分布，迫使模型模仿低概率 token 路径，从而在 Fisher 信息敏感的“高危方向”上更新参数，破坏原有行为。现有方法（正则化、on‑policy 自蒸馏）未能直接解决这一分布不匹配。

**方法**  
提出 **MIXSD**，无需外部教师，完全利用基础模型自身构建监督。对每条知识注入数据，在每一步解码时，从两个条件分布中采样：
- **专家条件**：在输入中添加事实上下文，使生成 token 倾向表达正确信息；
- **朴素条件**：仅用原始提示，反映模型先验。  
以概率 `1-λ` 选择专家 token，以概率 `λ` 选择朴素 token，拼接成完整的目标序列，然后按标准 NLL 损失微调。混合率 `λ` 控制分布对齐强度：`λ=0` 等同于纯专家监督，`λ` 越大越接近基座分布。该方法只需一次离线生成混合 rollouts，训练开销与 SFT 相当。

**关键结果**  
在两个自制数据集（KGFACT 事实回忆、KGFUNC 算术函数学习）及 SimpleQA 知识编辑上，用 Qwen3‑1.7B/4B/8B 评估。
- 标准 SFT 注入准确率高（近 100%）但遗忘严重，保留性指标平均仅 1%–43%。  
- MIXSD（λ=0.3~0.5）保持注入准确率（>90%）同时保留大部分预训练能力（如 8B 模型 λ=0.3 时训练准确率 99%，平均通用能力保留达 70%）。  
- SFT 产生大量错误类型（实体泄露、模板崩溃），MIXSD 错误分布与基座模型相似。  
- Fisher 对齐比例与遗忘的相关系数高达 0.82，证实更新方向是关键。  

**核心见解**  
“让监督信号扎根于模型自身的生成分布，即可在学到新事实的同时保住旧能力——简单分布对齐远比复杂防遗忘机制有效。”
