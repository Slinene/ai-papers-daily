---
title: Behavior Leverage Imbalance in Multi-Teacher On-Policy Distillation
title_zh: 多教师在线蒸馏中的行为杠杆不平衡与Soft Clamp校准
authors:
- Jiabin Shen
- Guang Chen
- Chengjun Mao
affiliations:
- Ant Group
arxiv_id: '2607.07050'
url: https://arxiv.org/abs/2607.07050
pdf_url: https://arxiv.org/pdf/2607.07050
published: '2026-07-08'
collected: '2026-07-09'
category: Agent
direction: 多教师在线蒸馏 · 工具调用校准
tags:
- Multi-Teacher Distillation
- On-Policy Distillation
- Tool-Use Calibration
- Behavior Imbalance
- Token-Level Divergence
- Agent
one_liner: 指出多教师在线蒸馏中局部高杠杆 token 信号会导致工具过呼叫等行为偏移，提出 Soft Clamp 动态压缩极端 token 级散度来校准
practical_value: '- **诊断视角迁移**：不要只看全局 loss 或 token 暴露量，要监控**决策边界 token**（如 `<tool_call>`
  的教师-学生概率差），这个“行为杠杆”能早期预警生成模式漂移。在电商推荐 Agent 或搜索多步推理中，可对关键动作 token（“下单”“点击”“调用函数名”）进行类似监控。

  - **Soft Clamp 轻量校准**：无需改动路由或增加模型，对每个 token 的 JS 散度做 batch 内动态阈值压缩：\(d''_i = d_i
  \cdot C / \text{stopgrad}(d_i)\)，超过阈值只截断前向值但保留梯度。这个方法可嵌入现有 GKD 训练流程，应对多教师蒸馏中某一类行为过拟合的问题（如过度推荐、频繁改写
  query）。

  - **多教师蒸馏的风险评估**：当不同教师负责不同行为模式（如工具调用 vs. 直接回答、生成 vs. 改写）时，即使数据量和散度平衡，也会因模式入口 token
  的高杠杆产生行为偏移。在设计推荐系统的多教师对齐（例如点击率教师 vs. 停留时长教师）时，需检查关键决策 token 的局部信号强度。

  - **格式锚定**：结构化输出（如 XML 工具调用、推荐列表格式）容易发生模式漂移，加入少量监督 loss（如 `sft alpha=0.3`）作为格式锚定可保持输出可解析，这一
  trick 可直接用于生成式推荐中的 Semantic ID 序列格式约束。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**
在 Agent 工具调用场景中，多教师在线蒸馏（MOPD）天然适合让一个教师专长工具调用，另一教师专长直接回答，学生从自身生成分布学习。但实验发现，即便全局损失和 token 暴露量显示工具教师与回答教师的贡献平衡，模型仍会系统性偏向工具过呼叫（over-calling）：应该直接回答的样本上也开始调用工具。这种偏移无法用样本数、总散度解释，本质是**行为杠杆不平衡**——模式入口 token（如 `<tool_call>`、函数名）对全局生成模式有不成比例的控制力，局部微小信号即可改变整个轨迹。

**方法关键点**
- **行为杠杆诊断**：不对全序列做平均，而是监控响应样本上 `<tool_call>`  token 的学生概率、教师-学生概率差（signed pressure）等决策边界指标，这些指标与最终过呼叫率高度一致。
- **Soft Clamp 校准**：对每个 token 的 JS 散度 \(d_i\)，在 batch 内设动态阈值 \(C = k \cdot \text{mean}(d_i)\)（\(k=3.0\)）。若 \(d_i > C\)，则前向值截断为 \(C\)，但梯度乘以 \(C/d_i\)，从而压缩极端信号的训练冲击同时保留学习梯度。
- **对比基线**：Hard Clip（直接截断）、Global Reweight（按 batch 相对散度重加权）。
- **格式锚定**：所有蒸馏变体均混入少量监督损失（权重 0.3）作为格式锚，防止结构化工具调用模式漂移。

**关键实验与结果**
- **数据集**：APIGen-MT（领域内决策）、BFCL（函数调用质量与拒绝无关）、BFCL 多轮循环诊断、When2Call（外域决策）。
- **模型与训练**：基座 Qwen3.5-9B，两个教师同初始化分别训练，GKD 学生采用 0.8/0.5 的 rollout 混合和 β。
- **主要数字**：
  - Vanilla GKD 将 APIGen 过呼叫从 4.9%（Base SFT）拉高到 13.7%，虽提升呼叫召回（91.4%），但 Soft Clamp 将过呼叫压至 9.0%，同时保持决策准确率 89.2%。
  - BFCL 多轮循环中，Vanilla GKD 每轮平均调用 1.494 次、Loop@3 14.8%，Soft Clamp 降至 1.268 次、Loop@3 10.1%，最终答案率从 89.6% 升至 94.1%。
  - When2Call 表明 GKD 变体未能提升全部外域决策，Soft Clamp 仅校准行为偏差而非通用解决。

**核心洞察**
多教师在线蒸馏不应只关注教师信号的“总量”，还需监控信号作用在哪些 token 上——尤其是能改变生成模式的高杠杆位置，局部校准即可有效抑制行为偏移。
