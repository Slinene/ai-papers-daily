---
title: 'Forgetting That Sticks: Quantization-Permanent Unlearning via Circuit Attribution'
title_zh: 量化永久遗忘：通过电路归因实现抗压缩的机器遗忘
authors:
- Saisab Sadhu
- Pratinav Seth
- Vinay Kumar Sankarapu
affiliations:
- Lexsi Labs
arxiv_id: '2605.15138'
url: https://arxiv.org/abs/2605.15138
pdf_url: https://arxiv.org/pdf/2605.15138
published: '2026-05-14'
collected: '2026-05-16'
category: LLM
tags:
- Machine Unlearning
- Quantization
- Circuit Attribution
- LLM
- Safety
one_liner: 提出 MANSU 框架，利用电路归因与量级底线保证 4-bit 量化后遗忘不逆转
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**：现有机器遗忘评估仅在全精度下测量行为抑制，而实际部署的 LLM 均经过 4-bit 量化。近期研究发现 PTQ 可逆转遗忘，本工作证明这不是调参问题，而是梯度更新幅值普遍低于 NF4 量化 bin 宽度导致的系统性双故障：梯度类方法遗忘显著但压缩后失效，偏好优化类方法抗量化但几乎不改变模型。两者均源于更新分散在全部参数，每参数变化量远小于量化 bin，无法跨越量化边界。

**方法关键点**：
- **Phase 1 定位**：用 EAP-IG 因果归因识别遗忘集知识的最小 MLP 电路 C（仅约 3% 参数）。
- **Phase 2 投影**：在 C 内将梯度投影到保留集 Fisher 零空间，得到比全局投影更紧的保留界（定理 1）。
- **Phase 3 量级底线**：对 C 内更新施加逐参数量级底线 δᵢ（≥ NF4 bin 宽度），不足者缩放至 δᵢ，保证量化后必跨越 bin 边界（引理 1）。
- **训练目标**：遗忘集负对数似然 + 保留集 KL 散度（冻结参考模型）+ Fisher 掩码约束。
- **新指标 CAD**：在遗忘前后重跑电路归因，计算归因质量崩塌程度，区分结构性擦除与行为抑制。

**关键实验**：
- 模型：Llama-3.1-8B-Instruct、Qwen-3-8B；数据集：WMDP-bio/chem/cyber、MUSE（Harry Potter）。
- 对比基线：全局 GA、Surgical GA、NPO、SimNPO、GU+SimNPO、LUNAR。
- 主要结果：MANSU 在 WMDP-bio 上遗忘准确率 0.430，NF4 后 0.390（ΔPTQ=−0.040，即量化放大擦除），MMLU 0.573（下降仅 0.030），CAD 1.143（接近完全结构崩塌）。全局 GA 的 BF16 遗忘 0.260 但 NF4 反弹至 0.310（ΔPTQ=+0.050），MMLU 塌至 0.235；SimNPO 保留量化但 MMLU 跌至 0.295。在所有 94 次非 MANSU 实验中，梯度法均出现正 PTQ gap，偏好法遗忘深度仅 1.6 个百分点。Ablation 证实：去掉量级底线则 ΔPTQ 回升至 −0.008，随机电路使 CAD 从 1.143 跌至 0.743，全局投影+底线则 ΔPTQ 转正。

**值得记住的一句话**：如果模型在全精度下通过了遗忘评估，那么它在部署前的标准 4-bit 量化后还能通过吗？答案是否定的——遗忘必须从设计上保证量化持久性。
