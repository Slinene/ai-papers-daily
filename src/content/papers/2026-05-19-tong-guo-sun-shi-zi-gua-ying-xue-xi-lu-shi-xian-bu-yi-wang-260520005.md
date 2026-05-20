---
title: Fine-Tuning Without Forgetting via Loss-Adaptive Learning Rates
title_zh: 通过损失自适应学习率实现不遗忘的微调
authors:
- Parjanya Prajakta Prashant
- Jiongli Zhu
- Aldan Creo
- Babak Salimi
affiliations:
- University of California San Diego
arxiv_id: '2605.20005'
url: https://arxiv.org/abs/2605.20005
pdf_url: https://arxiv.org/pdf/2605.20005
published: '2026-05-19'
collected: '2026-05-20'
category: Training
direction: 损失自适应学习率缓解微调遗忘
tags:
- Catastrophic Forgetting
- Learning Rate Schedule
- Fine-tuning
- LLM
- Loss-Adaptive
- Knowledge Acquisition
one_liner: 提出与训练损失平方根成反比的学习率调度，在保持新任务性能的同时，平均减少93%的灾难性遗忘。
practical_value: '- 在电商客服或推荐解释的LLM微调中，可直接用FINCH代替常规余弦调度，无需修改目标函数或准备回放数据，即可保持模型在通用对话、推理等能力上的性能。

  - 做新知识注入（如新品信息、新政策）时，FINCH能大幅减轻幻觉率上升和校准退化，比单纯的小学习率或LoRA更优。

  - 方法实现简单：只需在训练循环中维护损失指数滑动平均，并据此计算每步学习率，与AdamW兼容，引入超参数少（仅ηbase和ηmax），适合快速工程落地。

  - 对于需要持续微调但预训练数据不可访问的场景（如多轮对齐优化），FINCH提供了一种廉价的数据遗忘控制手段，可避免模型在反复更新中能力坍塌。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**：微调大模型（LLM）会显著损害预训练获得的通用能力（灾难性遗忘），而常见缓解方法（如回放预训练数据、降低高损失样本权重）在知识获取或低资源语言适应等任务上会牺牲新任务的学习效果，因为这些任务中“难”的token正是需要被学习的内容。

**方法关键点**
- 理论分析表明，每步遗忘量被学习率与当前mini-batch损失平方根的乘积所决定：ΔL_old ≤ C1 η √L_batch + C2 η² L_batch。
- 据此设计FINCH调度：η_i = κ / √(L_Bi + ε)，使高损失batch使用小学习率，损失下降后自动放大学习率，从而保持每步遗忘的上界恒定。
- 实际实现中，用指数移动平均平滑瞬时损失(L̄_i = α L̄_{i-1} + (1-α) L_Bi, α=0.9)，并设置学习率上限η_max=5e-5。
- 整个过程完全不改变微调损失函数或样本权重，保证模型仍能从所有token中充分学习。

**关键结果**
- 在Qwen3-4B和Llama-3-8B上的知识获取、科学推理、低资源语言适应三个场景中，FINCH相比标准SFT平均遗忘减少93%（六项实验累计旧任务性能退化从61.9点降至3.9点）。
- 知识获取任务上，FINCH达到83.3%的新任务准确率（SFT为83.5%），而平均旧任务退化从-9.6升至+0.1；同时，TruthfulQA退化从-13.9降至-2.6，HaluEval从-9.8升至+3.3，置信校准Brier退化从14.7降至9.1。
- 在所有评估设置中，FINCH均位于新任务性能-遗忘量的Pareto前沿，优于所有基线方法。

**一句话**：将学习率设为当前batch损失平方根的倒数，就能在不牺牲新任务学习的前提下，把遗忘控制在极低水平。
