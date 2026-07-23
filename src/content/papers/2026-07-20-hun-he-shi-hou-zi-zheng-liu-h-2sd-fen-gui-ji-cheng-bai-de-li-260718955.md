---
title: 'H^2SD: Hybrid Hindsight Self-Distillation'
title_zh: 混合事后自蒸馏H^2SD：分轨迹成败的推理增强训练
authors:
- Qiye Cai
- Yichuan Ma
- Linyang Li
- Peiji Li
- Yongkang Chen
- Qipeng Guo
- Yicheng Zou
- Tao Gui
- Xiaocheng Feng
- Bing Qin
affiliations:
- Shanghai Artificial Intelligence Laboratory
- Harbin Institute of Technology
- Fudan University
- The Chinese University of Hong Kong
arxiv_id: '2607.18955'
url: https://arxiv.org/abs/2607.18955
pdf_url: https://arxiv.org/pdf/2607.18955
published: '2026-07-20'
collected: '2026-07-23'
category: Training
direction: LLM 推理训练 · 事后自蒸馏
tags:
- RLVR
- Self-Distillation
- Credit Assignment
- Reasoning
- Hindsight
- GRPO
one_liner: 提出H^2SD，根据轨迹成败分别用重述增强和参考提示进行教师信号调制与蒸馏，提升推理训练稳定性和效果
practical_value: '- 训练LLM Agent时，区分成功与失败轨迹：对成功响应只做重述增强，用重评估概率调制更新幅度，避免扰乱正确行为；对失败响应引入事后参考提示和逆向KL蒸馏，提供明确纠正信号

  - 在商品推荐对话、多轮推理等场景，可利用用户反馈（如点击/转化）作为轨迹正确性标签，分别应用不同的教师蒸馏策略，克服稀疏奖励下的token级信用分配问题

  - 混合教师上下文构建方式无需额外强教师模型，仅需事后正确答案（如验证器确认的结果），降低工程依赖，适合轻量级业务fine-tuning

  - 重述指令（rephrasing）可凸显关键推理步骤，类似推荐解释生成中可对高质量解释进行改写增强，抑制冗余，提升生成效率与稳定性'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：RLVR（如GRPO）只能提供轨迹级标量奖励，token级监督稀疏。现有自蒸馏（OPSD）用特权信息构造教师但直接匹配分布易致不稳定，RLSD仅调制幅度却无法纠正错误轨迹。**方法**：提出H^2SD，根据轨迹正确性差异性地使用教师信号。成功轨迹：用已验证的学生响应和重述指令作为特权上下文，教师重新计算原响应token概率，仅调制更新幅度，强化关键步骤，不改变奖励确定的优化方向。失败轨迹：用包含关键步骤和验证答案的参考提示作为教师输入，最小化学生到教师的逆向KL散度，注入纠正性指导。**关键结果**：在多个推理基准上，H^2SD全面优于RLVR、OPSD和RLSD等基线；消融验证了基于正确性的路由和重述指令是关键增益来源；训练过程更稳定，在准确率和生成效率间取得良好平衡。
