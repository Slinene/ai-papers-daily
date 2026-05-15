---
title: 'BEAM: Binary Expert Activation Masking for Dynamic Routing in MoE'
title_zh: BEAM：通过二值掩码实现MoE动态专家路由
authors:
- Juntong Wu
- Jialiang Cheng
- Qishen Yin
- Yue Dai
- Yuliang Yan
- Fuyu Lv
- Ou Dan
- Li Yuan
affiliations:
- Alibaba Group
- Peking University
arxiv_id: '2605.14438'
url: https://arxiv.org/abs/2605.14438
pdf_url: https://arxiv.org/pdf/2605.14438
published: '2026-05-13'
collected: '2026-05-15'
category: LLM
tags:
- MoE
- Dynamic Routing
- Sparsity
- Inference Acceleration
- Binary Mask
- LLM
one_liner: 提出BEAM，学习二值掩码实现token自适应专家稀疏激活，保留98%性能，MoE层FLOPs减85%，解码加速达2.5倍
score: 9
source: huggingface-daily
depth: full_pdf
---

## 动机

Mixture-of-Experts (MoE) 通过固定 Top-K 路由为每个 token 激活相同数量的专家，导致简单 token 进行冗余计算，限制推理速度。现有动态路由方法要么需要修改架构并 costly retrain，要么在高稀疏度下因训练-推理不匹配而性能剧烈下降；静态剪枝或合并专家则无法适应 token 级难度变化。因此需要一个即插即用、能在保持模型能力的同时实现极端稀疏加速推理的方案。

## 方法关键点

- **二值掩码路由器**：在原 Top-K 路由基础上，增加一个轻量可学习的 mask router `Wm`，对输入 token 生成原始掩码 `σ(xWm)`，通过阈值 0.5 二值化为掩码 `m ∈ {0,1}^N`，与 Top-K 权重 `g` 逐元素相乘得到最终路由权重 `ĝ = g ⊙ m`，实现选择性去激活冗余专家。
- **解耦设计**：主路由器负责专家选择和负载均衡，掩码路由器仅控制激活数量，消除优化目标冲突，使模型能表达 Top-K 集合内更丰富的激活模式。
- **端到端训练**：采用 Straight-Through Estimator (STE) 绕过二值化不可微问题；引入 L1 正则损失 `Lreg = (1/K)∑_{i∈TK} |ˆmi|`，推动掩码稀疏；整体目标 `L = L_lm + αL_bal + βL_reg`，通过 β 平滑控制稀疏度-准确率权衡。
- **即插即用的部署**：将 BEAM 集成到 vLLM 推理框架，仅需少量 CUDA kernel 修改（掩码路由将-1写入专家ID，对齐时跳过-1入口），保持与现有优化兼容，无需改变模型结构。

## 关键结果

- 在 Qwen1.5-MoE-A2.7B、DeepSeekV2-Lite、Qwen3-30B-A3B 三个 MoE 模型上评估，涵盖推理、知识、常识等 8 个 benchmarks。
- **极端稀疏**：BEAM 在仅激活 0.11–0.56 个专家（原 K=4/6/8）时，仍保留原模型 85%–95% 性能，远超 Top-K Pruning/Reduced、MoE-Dynamic 和 AdaMoE。
- **加速效果**：MoE 层 FLOPs 减少达 85%（无共享专家模型），解码 TPOT 最高加速 2.5 倍，吞吐量提升 1.4 倍。
- **β 参数**：单一正则系数即可灵活控制稀疏度，无需手动调节阈值。
- 分析表明 BEAM 能根据 token 语义丰富度、层深和作用域自适应分配计算，且保持专家负载均衡。

**最值得记住的一句话**：BEAM 通过解耦路由与稀疏控制，以即插即用的方式使 MoE 模型实现 token 级自适应专家激活，既保留超过 98% 的性能，又显著降低计算量并加速推理。
