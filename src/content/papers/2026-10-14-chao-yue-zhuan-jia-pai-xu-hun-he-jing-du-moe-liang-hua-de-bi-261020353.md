---
title: 'Beyond Expert Rankings: Contrast Calibration for Mixed-Precision MoE Quantization'
title_zh: 超越专家排序：混合精度 MoE 量化的对比校准
authors:
- Renjie Xie
- Juncheng Yang
- Aoting Hu
- Yan Liang
- Mingxi Zhang
- Zheheng Hong
- Wei Xu
- Yanzhi Chen
affiliations:
- Nanjing University of Posts and Telecommunications
- Tylogi AI Lab / TAIL
- Southeast University
- Microsoft
- University of Cambridge
arxiv_id: '2610.20353'
url: https://arxiv.org/abs/2610.20353
pdf_url: https://arxiv.org/pdf/2610.20353
published: '2026-10-14'
collected: '2026-10-15'
category: LLM
direction: MoE 混合精度量化与敏感度校准
tags:
- MoE
- Mixed-Precision Quantization
- Contrast Calibration
- PTQ
- LLM
one_liner: NatScale 用对称 KL 目标校准专家敏感度对比度，在固定存储预算下提升 MoE 量化保真度
practical_value: '- 部署 MoE 大模型（如生成式推荐、精排 reranker、Agent 策略模型）做混合精度量化时，不要只看专家重要性排序：用
  power transformation 校准敏感度对比度，可将不同层/模型放在共同信息尺度上，默认 τ=1 nat 是无调参的实用起点。

  - 工程实现上把 joint gate/up/down 误差、结构化先验和校准权重解耦并预缓存，之后扫预算或 τ 只需重跑线性规划分配器，无需额外前向/反向，适合线上反复调整内存配额。

  - 分配单元下探到 expert 内部 projection，而不是整层统一精度，可在同层内差异化 bit-width，压缩比与效果更优；电商推荐模型若含 MoE
  或专家模块可沿用同一思路。

  - 注意 PPL 与 native KLD 可能偏好不同 τ：若目标是输出分布对齐（如广告创意生成、query 改写），优先看 KLD/Top1 而不是 PPL。'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

## 动机
MoE 语言模型每 token 只激活少数专家，但所有专家权重都要存储。混合精度量化能在内存预算内给敏感权重高精度、给鲁棒权重低精度。现有方法主要靠专家重要性排序，但排序本身不能决定存储分配的强度：敏感度向量的对比度（相对分离程度）控制专家如何争夺存储。

## 方法关键点
- **敏感度校准**：计算梯度二阶矩归一化得分 g_i，用 power transformation w_i = g_i^{βτ} 将正得分专家映射到预设的对称 KL 散度 τ（相对于均匀分布）。τ 唯一决定 βτ，保持专家排名不变，默认 τ=1 nat。
- **联合误差估计**：对每个专家的 gate/up/down 三投影同时量化，在固定 replay 输入上计算输出 RMS 误差，再乘以 routing exposure；结合 AlphaQ 结构先验（谱尾指数、参数方差、位宽衰减）。
- **预算分配**：专家成本 d_i = w_i · A_i · E_i，用 LP 松弛和可行舍入在全局字节预算下选择每个专家的配置；候选误差和统计量可预缓存，改预算或 τ 只重跑分配器。

## 关键结果
在 Qwen3.6-35B-A3B、Qwen3.8-Flash-Next、DeepSeek-V4-Flash-0731 三个模型 × 2.0/2.5/3.0 bpw 九种设置上，对比 MxMoE、FRI-MxMoE、AlphaQ、MODE、GEMQ 五个 baseline，NatScale 在所有九种设置达到最低 native-to-quantized KLD 和最高 Top1，PPL 在七种设置最低。Qwen3.8-Flash-Next 中预算下 KLD 从 AlphaQ 的 0.2487 降至 0.1941，Top1 从 82.82% 升至 84.86%。下游任务 AIME 2025、GPQA Diamond、TruthfulQA 也最高，LiveCodeBench 略低于 MODE。

> 最值得记住：专家排序只告诉你谁更重要，对比度才决定它们如何争夺存储。
