---
title: 'Train Where the Quantized Model Goes: On-Policy Distillation for Low-Bit Reasoning'
title_zh: 量化模型走到哪，就在哪训练：低比特推理的在线策略蒸馏
authors:
- Yuanteng Chen
- Zhilei Liu
- Peisong Wang
- Yuantian Shao
- Chuangyi Li
- Weining Wang
- Shuang Qiu
- Gang Li
- Jing Liu
- Jian Cheng
affiliations:
- Institute of Automation, Chinese Academy of Sciences
- School of Artificial Intelligence, University of Chinese Academy of Sciences
- Zhongguancun Academy
- City University of Hong Kong
- NJUST
arxiv_id: '2609.26708'
url: https://arxiv.org/abs/2609.26708
pdf_url: https://arxiv.org/pdf/2609.26708
published: '2026-09-22'
collected: '2026-09-23'
category: Training
direction: 低比特量化 · 在线策略蒸馏
tags:
- Low-bit Quantization
- On-Policy Distillation
- Quantization-Aware Distillation
- Exposure Bias
- Reasoning
- RLVR
one_liner: 用在线策略蒸馏把教师监督放到低比特量化模型自己的生成轨迹上，将 MATH-500 平均保留率从 35% 恢复到 70%
practical_value: '- 若线上部署低比特 LLM 做 Agent 规划、长推理或长文案生成，QAD 后不要直接上线：补一个少量步数的 on-policy
  蒸馏阶段，用模型自己的 rollout 配合冻结 BF16 teacher 和任务 verifier，能显著减少重复循环和 budget exhaustion。

  - 蒸馏阶段可以非常简单：反向 KL token-level + group-relative advantage，β=1 固定无需调参；每个 step 8 prompts、G=32/64
  rollouts，几十到数百 step 即可，GPU-hours 比 QAD 少 14–23 倍。业务上可低成本验证。

  - 教师选择：1.7B 以上的低比特学生用自身 BF16 副本通常足够，不必上更大教师；只有 0.6B 这类学生本身太弱时才需要更强教师。这能省掉大模型推理成本。

  - 训练/部署一致性很关键：rollout 必须走部署时的量化前向路径（INT8 activations + low-bit weights），才能把量化扰动纳入训练分布；类似在生成式推荐、query
  改写或 Agent 路径采样中，应让训练 rollout 与实际服务链路一致，避免 teacher-forcing 与线上自回归之间的 exposure bias。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**  
极低比特（<3 bit）量化能大幅压缩 LLM，但 QAD 恢复极不均衡：短问答平均保留 86% BF16，MATH-500 只有 35%。长生成会陷入重复循环，耗尽 decoding budget 也无法完成求解。原因是量化放大 exposure bias：QAD 只在固定语料前缀上做 teacher forcing，部署时模型条件在自身被量化扰动的输出上，偏差沿自回归轨迹不断累积。

**方法关键点**  
- 两阶段框架：QAD 先恢复策略可行性，提供稳定低比特初始化；OPD 再用 on-policy 蒸馏恢复长推理轨迹控制。
- OPD 从 QAD checkpoint 开始，学生通过部署时的量化前向路径采样 completion；冻结 BF16 teacher 对学生自己生成的前缀提供 token-level 反向 KL 指导，同时加入任务 verifier 奖励（数学最终答案正确性、代码测试执行）。
- 损失 = policy gradient + β·反向 KL，β=1 固定；group-relative advantage 用同一 prompt 的多个 completion 做相对比较。
- 训练轻量：每 step 8 prompts，G=32/64 rollouts，lr 3e-6，数学阶段 80–140 step，代码阶段 80–150 step。
- 教师选择：≥1.7B 学生用自身 BF16 副本即可；0.6B 需更强 teacher。

**关键结果**  
在 Qwen3-0.6B/1.7B/4B、Falcon3-1B 四模型，2.79/1.88 effective bits 上：
- OPD 将平均 MATH-500 BF16 保留率从 35.3% 提升到 69.7%，GSM8K 从 62.7% 提升到 85.0%，HumanEval 从 66% 提升到 91%，同时 QA9 保留率从 88.1% 升至 92.1%。
- 行为层面：Qwen3-0.6B W2.79 在 MATH-500 上 loop rate 从 70% 降到 17%，budget exhaustion 从 95% 降到 53%。
- 效率：Qwen3-4B W1.88 的 OPD 仅 57 GPU-hours，QAD 为 820；Falcon3-1B W2.79 为 11 vs 253。
- 16 个 matched-budget 对比中 OPD 全部超过 continued teacher-forced QAD，GSM8K 每千步收益最高差 42 倍。

**最值得记住的一句话**  
把教师监督放到量化模型自己的生成轨迹上，是在极低比特下恢复长推理能力的关键。
