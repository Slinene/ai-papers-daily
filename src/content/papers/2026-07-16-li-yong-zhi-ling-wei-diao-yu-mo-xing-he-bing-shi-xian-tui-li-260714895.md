---
title: Leveraging Instruction Tuning and Merging for Reasoning Model Adaptation
title_zh: 利用指令微调与模型合并实现推理模型低成本领域适应
authors:
- Yu-Du Feng
- Niels Mündler-Sasahara
- Mark Vero
- Martin Vechev
affiliations:
- ETH Zurich
arxiv_id: '2607.14895'
url: https://arxiv.org/abs/2607.14895
pdf_url: https://arxiv.org/pdf/2607.14895
published: '2026-07-16'
collected: '2026-07-17'
category: LLM
direction: 推理模型适应 · 指令微调+合并
tags:
- instruction tuning
- model merging
- reasoning models
- domain adaptation
- cost-effective
one_liner: 先指令微调再与原始推理模型合并，低成本提升在难验证领域的性能
practical_value: '- 若拥有特定领域的高质量SFT数据（如电商搜索意图、商品摘要），可对推理模型进行无推理痕迹的指令微调，再与原模型合并，以极低成本（<3美元）提升该领域效果，同时保留推理能力。

  - 模型合并技巧可作为一种轻量领域适应方案，避免灾难性遗忘，适合在资源有限时快速迭代测试。

  - 对于缺乏可靠自动评估的生成式推荐或Agent任务，可考虑用人类标注数据微调再合并，绕开难以设计的奖励函数。

  - 方法简单稳健，适合嵌入现有LLM微调流水线，作为RLVR训练前的快速实验步骤。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：推理语言模型（RLM）在数学、编程等有可靠验证器的领域表现突出，但在文本摘要等难以自动验证的领域提升困难。这些领域存在大量人工编写的高质量监督数据却未被有效利用。

**方法**：提出两阶段轻量适应方案：①对RLM进行经典指令微调，仅使用目标领域的输入-输出对，不包含推理链；②将微调后模型与原始RLM进行线性合并，恢复推理行为并保持通用能力。

**结果**：在编程（可验证）和文本摘要（难验证）任务上均取得性能提升，同时在其他领域保持原有推理水平。整个适应流程成本低于3美元，性价比极高。
