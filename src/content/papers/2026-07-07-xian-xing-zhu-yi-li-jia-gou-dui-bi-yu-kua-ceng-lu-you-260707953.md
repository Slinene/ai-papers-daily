---
title: 'Linear Attention Architectures: Mechanisms, Trade-offs, and Cross-Layer Routing'
title_zh: 线性注意力架构对比与跨层路由
authors:
- Tommaso Cerruti
- Tim Rieder
- George Rowlands
- Lingfeng Jin
- Imanol Schlag
affiliations:
- ETH Zurich, D-INFK
- ETH AI Center, ETH Zurich
arxiv_id: '2607.07953'
url: https://arxiv.org/abs/2607.07953
pdf_url: https://arxiv.org/pdf/2607.07953
published: '2026-07-07'
collected: '2026-07-11'
category: Training
direction: 线性注意力架构对比与跨层路由
tags:
- linear-attention
- DeltaNet
- cross-layer routing
- training efficiency
- long-context
- language model
one_liner: 比较四种递归线性注意力并提跨层值路由，Kimi Delta Attention+Muon损失最低
practical_value: '- 推荐模型处理长用户行为序列时，可用 Gated DeltaNet 等线性注意力替换标准注意力，降低计算复杂度，支持更长序列建模，提升训练吞吐。

  - 跨层值路由（CLVR）提供廉价的信息跨层传递方式，可借鉴至深度推荐模型（如多塔、DeepFM）中，将底层值张量路由到高层，增强信息流动。

  - 优化器选择：Muon 在相同架构下比 AdamW 验证损失更低，若任务侧重点效果可尝试 Muon（注意稳定性）。

  - 混合堆栈（部分标准注意力+部分线性注意力）平衡效果与效率，适合推荐序列编码器，上游用标准注意力捕获近期行为，下游用线性注意力处理长历史。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：标准自注意力在长序列上计算开销二次增长，限制大模型训练与推理。线性注意力通过递归绕过注意力矩阵，但各类变体（DeltaNet、Gated DeltaNet、Kimi Delta Attention、Gated DeltaNet-2）设计差异大，缺乏系统对比。同时，多层网络中记忆更新可能存在冗余，跨层路由有望提升效率。

**方法**：将四种最新线性注意力统一到递归记忆框架，从表达力、记忆衰减、写入/擦除控制、训练吞吐等维度对比。在350M参数、15B token规模下，系统评估优化器（AdamW vs Muon）、纯/混合架构、序列长扩展性，并对1.3B、3B模型缩放。提出两种跨层路由：基于Delta规则的写误差路由和写值路由CLVR。

**结果**：纯Kimi Delta Attention + Muon获最低验证损失；纯Gated DeltaNet + AdamW训练吞吐最高；混合堆栈一般改善损失但降低吞吐；Muon一致优于AdamW。跨层误差路由无效，但CLVR在DeltaNet/Gated DeltaNet上均降低验证损失，验证其轻量有效性。
