---
title: Personalized Task Dependency Graphs for Mitigating Signal Erosion in Multi-Task
  Recommendation
title_zh: 个性化任务依赖图缓解多任务推荐中的信号衰减
authors:
- Fuyuan Liu
- Tiandeng Wu
- Yaqun Fang
- Wei Zhou
- Zehao Zhou
- Wenping Chen
- Qishun Mei
- Jiaxin Zhou
- Heng Chang
- Yi Cao
affiliations:
- Huawei Technologies Co., Ltd.
arxiv_id: '2609.04862'
url: https://arxiv.org/abs/2609.04862
pdf_url: https://arxiv.org/pdf/2609.04862
published: '2026-09-04'
collected: '2026-09-07'
category: RecSys
direction: 多任务学习 · 任务依赖图
tags:
- Multi-Task Learning
- Task Dependency Graph
- GCN
- Signal Erosion
- Recommendation
- Causal Masking
one_liner: PTDG以低秩动态任务图和因果GCN消息传递，缓解多任务推荐深层转化目标的信号衰减
practical_value: '- 在电商/广告多目标转化（点击→加购→下单→支付）中，不要用全局固定漏斗依赖；用低秩分解（rank q≈T/3）从 item/user/scenario
  特征生成动态任务邻接矩阵，再叠加因果掩码，能适配不同商品/场景的转化路径差异。计算上每个 item 只增加一次低秩矩阵乘法和 GCN 传播，在线延迟仅 +8 ms，适合
  serving SLA。

  - 借鉴因果掩码+自适应 shortcut 的消息传递：在任务图上允许 Click→Pay 等跳过中间环节的捷径，避免深层稀疏目标信号被层层衰减；这比固定层级
  AITM 更灵活，尤其适合稀疏深层目标（支付、复购）的 CVR 预估。

  - APM 结构化解耦共享参数：根据任务正样本率设置 mask 率，稀疏任务 mask 率更高（如低至 0.7），密集任务低（0.2），并线性 warm-up。相比
  PCGrad 等梯度投影，训练开销几乎为零，推理无额外参数，可直接替换 MMoE/PLE 的共享底层。

  - 用 EMA 归一化每个 task loss 权重（loss / EMA(loss)）是稳定多任务训练的轻量 trick，可以快速在现有 MTL 模型中验证。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
多任务转化预测是工业推荐核心，但现有 MTL 架构（MMoE/PLE/AITM）通常把转化漏斗设为全局固定依赖强度，忽略了不同 item 上任务相关性差异。例如重度游戏 Click→Download→Pay 强因果，轻量工具可能 Click→Pay 直接跳转。固定层级消息传递导致深层稀疏目标信号衰减，AUC 提升受限。

**方法关键点**
- **个性化任务依赖图**：用低秩分解从 item 特征生成 Z_L(Z_R)^T，再用 user/scenario MLP 产生个性化偏置 γ_{u,s} 调制左因子，得到动态邻接矩阵 A_dyn；秩 q=2，约 T/3，避免过拟合和全矩阵成本。
- **因果掩码 + GCN 传播**：A_dyn 乘以硬因果掩码 M_causal，去除反向边（如 Pay→Click），再过 GCN：H=σ(D^{-1/2}(A+I)D^{-1/2}XW)。这允许非顺序但有因果相关的自适应 shortcut，防信号衰减。
- **APM 自适应渐进掩码**：根据任务正样本率计算 mask 率，稀疏任务 mask 更多共享参数以解耦；通过 task embedding 学习 top-k 门控 mask，线性 warm-up 稳定训练，训练后固定、推理无开销。
- **损失权重**：每个任务 loss 除以其 EMA 统一尺度。

**关键实验**
在 KuaiRand1K（6 任务）和华为工业数据集（7 任务，13.2M 样本）上对比 MMoE/PLE/STEM/MoCograd/PMTRec/MIT。PTDG 在 KuaiRand 平均 AUC 0.9081，工业平均 0.8878，均最优；工业稀疏 Task 3 相对 PMTRec +1.45%，KuaiRand Follow +1.77% vs MMoE。在线 A/B（日活超 1 亿应用分发平台）CVR +1.2%，eCPM +1.9%，延迟仅增加 8ms。

**最值得记住的一句话**：任务依赖强度应该是 item/user/scenario 级别的动态结构，低秩 + 因果掩码 GCN 可以在几乎不增加在线延迟的情况下显著提升稀疏深层转化任务。
