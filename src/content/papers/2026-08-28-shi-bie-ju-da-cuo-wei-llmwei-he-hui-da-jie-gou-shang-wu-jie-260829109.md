---
title: 'Recognition-Refusal Misalignment in LLMs: Why Models Answer Structurally Unanswerable
  Questions'
title_zh: 识别-拒答错位：LLM为何回答结构上无解问题
authors:
- Yucheng Du
- Xiyang Hu
affiliations:
- University of Southern California
- Arizona State University
arxiv_id: '2608.29109'
url: https://arxiv.org/abs/2608.29109
pdf_url: https://arxiv.org/pdf/2608.29109
published: '2026-08-28'
collected: '2026-09-10'
category: LLM
direction: LLM 拒答路由与可辨识性
tags:
- LLM
- refusal
- steering
- linear representation
- safety
- unanswerable questions
one_liner: 结构无解问题中LLM已有可线性读取的不可答表征，但与安全拒答通路近正交，导致路由失败
practical_value: '- 在推荐/Agent 工具链中，可对“结构上不可执行/无有效答案”的用户请求做线性探针或残差流方向检测，生成前拦截，避免错误推荐或错误
  API 调用。

  - 别假设安全对齐的拒答能力会自动迁移到“无效问题”；应单独构建无效意图/工具不可执行分类器，或补训练目标使识别方向与拒答行为方向对齐。

  - 推理时 steering 可以在不改参数的情况下提升拒答/澄清能力，适合快速上线和 A/B；对电商问答中“无此商品属性、日期无效”等场景可尝试。

  - 预训练已具备不可答表征，说明修复成本可以较低：轻量 LoRA/linear adapter 对齐识别方向与行为方向可能足够。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：LLM 常对结构上无解问题（如 cot(-540°)、(1).startswith("1")）生成答案而非拒答；需要判断是模型没有识别出“无有效答案”，还是识别后没有路由到拒答。

方法：在 1.7B-70B 的指令微调模型上，用隐藏态线性方向分离可答与不可答的数学/代码提示；将该方向与安全拒答方向、行为定义的无效感知方向比较；并在生成时沿识别方向做 steering 干预。

结果：单一线性方向 AUC 0.939，说明生成前已编码不可答信号；但该方向与安全拒答方向近乎正交（cos 0.087），与行为方向仅部分对齐（cos 0.40）；steering 可剂量依赖地使“undefined/cannot compute”输出提升 33-52pp，随机方向无效；base/instruct 对比显示低余弦几何在预训练末端已存在。因此失败主要是 routing failure 而非 encoding failure。
