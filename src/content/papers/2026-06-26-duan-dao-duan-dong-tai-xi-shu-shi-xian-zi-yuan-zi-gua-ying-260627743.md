---
title: End-to-End Dynamic Sparsity for Resource-Adaptive LLM Inference
title_zh: 端到端动态稀疏实现资源自适应大语言模型推理
authors:
- Yuhang Chen
- Jinhao Duan
- Ruichen Zhang
- Mingfu Liang
- Xiaohan Wei
- Yunchen Pu
- Fei Tian
- Chonglin Sun
- Parish Aggarwal
- Frank Shyu
affiliations:
- Meta AI
- University of North Carolina at Chapel Hill
arxiv_id: '2606.27743'
url: https://arxiv.org/abs/2606.27743
pdf_url: https://arxiv.org/pdf/2606.27743
published: '2026-06-26'
collected: '2026-06-29'
category: LLM
direction: LLM 推理动态稀疏化与资源自适应
tags:
- dynamic sparsity
- gating network
- resource-adaptive inference
- layer skipping
- head pruning
- budget-conditioned
one_liner: 通过预算感知的门控网络动态跳过层、剪枝头并缩短推理长度，单模型覆盖完整计算-精度 Pareto 前沿
practical_value: '- **动态资源适配可用于推荐/搜索的 LLM 推理服务**：训练时让模型学会根据实时资源预算动态跳过层或剪枝 head，线上按请求
  SLA 或 GPU 余量自动调整计算量，避免 OOM 或超时。

  - **门控网络设计可直接复用**：轻量 MLP 门控接受隐藏态 + 预算嵌入，配合 LoRA 适应动态裁剪后的分布偏移，工程上易集成到现有 LLM 服务框架。

  - **联合优化目标保证质量不崩塌**：同时使用交叉熵、知识蒸馏和预算匹配损失，在电商多轮对话或广告文案生成中保持回答质量，且可显式控制推理长度。

  - **推理段控制技巧适合 Agent 思考长度管理**：通过引入 `<think></think><answer>` 结构，用门控控制推理 token 长度，在预算紧张时直接截断思考进入回答，可用于
  Agent 自适应降级。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：LLM 部署常假设固定资源，但实际云环境动态波动（spot 实例抢占、多租户负载变化），静态模型要么 OOM 要么浪费计算。已有动态推理方法多依赖输入难度而非实时资源预算，无法满足弹性要求。

**方法**：提出 L2A 框架，在冻结的 LLM 中插入三种可训练门控网络：层跳过门、注意力头剪枝门和推理段转换门（`<think>`→`<answer>`）。门控以隐藏状态和外部标量预算 `b` 为输入，输出 (0,1) 软决策。训练时联合优化：① 下一 token 交叉熵；② 稠密教师 KL 散度蒸馏；③ 实际计算量与目标预算的 L1 惩罚；④ 推理 token 长度损失。门控经温度退火转为硬跳过。预算信号由线上 SLA 截止时间、剩余存活时间等实时量标定。

**结果**：在 Llama-3-8B 上，达到 34% 层稀疏度时 GSM8K 准确率仅比稠密模型低 0.6%（36.5% vs 35.9%），而静态剪枝同等稀疏度下准确率下降 5-10%。动态策略也泛化到未见过的代码和推理任务（HumanEval、BBH）。消融表明蒸馏和预算损失对保持推理质量至关重要。单模型即可沿整个计算-精度 Pareto 前沿自适应运行，无需多模型部署。
