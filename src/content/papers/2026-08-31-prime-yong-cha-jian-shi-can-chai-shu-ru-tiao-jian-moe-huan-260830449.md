---
title: 'PRIME: Mitigating Subgroup Optimization Competition in Shared CTR Top Networks
  with Plug-in Residual Input-Conditioned Mixture of Expert'
title_zh: PRIME：用插件式残差输入条件 MoE 缓解共享 CTR Top 网络中的子群优化竞争
authors:
- Heng Yao
- Siyun Hou
- Tianying Liu
- Yulou Shu
- Yong He
- Chuan Yuan
- Kaibin Qiu
- Guowei Chen
- Jiayu Zhao
- Chao Yu
affiliations:
- Ant Group
- Henan Polytechnic University
- Independent Researcher
- Alibaba Inc.
arxiv_id: '2608.30449'
url: https://arxiv.org/abs/2608.30449
pdf_url: https://arxiv.org/pdf/2608.30449
published: '2026-08-31'
collected: '2026-09-01'
category: RecSys
direction: CTR 预测 · 条件 MoE 残差插件
tags:
- CTR prediction
- Mixture of Experts
- Low-Rank Residual
- Gradient Competition
- Load Balancing
one_liner: 提出 Dense 锚定的低秩残差输入条件 MoE 插件，以零残差初始化保持原模型不变，缓解共享 Top-NN 子群梯度竞争并提升 CTR 精度
practical_value: '- 用「锚定原预测 + 零残差初始化」给线上 CTR 模型加条件分支：训练起点与原模型完全一致，避免直接替换 Dense 路径带来的函数突变和上线风险，适合对已有精排模型做渐进式安全升级。

  - 条件路由必须放在决策相关表征上：如果子群体差异在特征交叉后才出现，用 pre-cross embedding 路由会失效；建议按业务场景选择路由输入层（如中间
  cross 层），并在不同骨架上做消融验证。

  - 低秩专家 rank q=16 + 多 bag 平均（G=4）在很小参数/推理开销下获得中位数 AUC 提升；可作为多场景、多广告位精排模型的轻量条件化方案，避免复制完整
  MLP。

  - 负载均衡用 EMA 更新 router bias，不加 auxiliary loss，消除平衡系数调参和对主目标的干扰；该做法可直接复用到多目标/多场景 MoE。

  - 用业务语义分组（站点、设备、时段）对比随机组梯度 cosine，可先诊断共享层是否存在子群竞争，再决定是否需要条件化改造。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
CTR 模型的特征交互结构不断演进，但 top 网络仍是所有样本共享的 MLP。异构用户、物品、上下文子群体更新同一组参数，弱对齐的梯度使共享更新成为折中。论文在 Avazu 上对 DNN、AutoInt、FiBiNET、DCNv2 做诊断：按 site_category、app_category、device_type、hour 构造语义子群，其 Top-NN 梯度 cosine similarity 比同规模和 label 比例的随机组低 0.23–0.37，证明存在语义子群优化竞争，单纯加宽 MLP 无法解决参数共享粒度问题。

## 方法关键点
- **Dense 锚定残差**：原模型输出概率 p_d 作为锚点，新增分支学习输入条件 logit residual，最终 p = 0.5 p_d + 0.5 p_s。
- **低秩专家**：从 embedding 层取 z 并 LayerNorm；G=4 个 expert bags，每 bag M=8 个 rank-q（q=16）专家，专家输出为 uᵀ SiLU(V z̃)+b，参数规模 O(qd)，避免复制完整 Top-NN。
- **输入条件路由**：每个 bag 有独立 router，softmax 权重由 z̃ 线性映射 + 负载 bias 决定；多 bag 平均得到 p_s。
- **函数保持初始化**：u 和 b 初始化为 0，保证训练起点 p = p_d，与原模型完全等价。
- **Auxiliary-loss-free 负载均衡**：不把 load balance loss 加进 CTR 目标，仅用 EMA 路由负载更新 bias，避免额外 loss 系数调参。

## 关键结果
在 Avazu 和 Criteo 的 13 种 CTR 架构、5 个配对 seed 上：Avazu macro-average AUC 0.7588→0.7611，LogLoss 0.3701→0.3689，median paired ΔAUC +0.0022；Criteo median ΔAUC +0.0066、LogLoss +0.0081。11/13 架构 mean AUC 提升。对比 APG，在 FiBiNET/DCNv2 上 10 个 seed AUC 全胜，参数更少、延迟更低。语义子群竞争 gap 从 0.3016 降到 0.1981，降幅 34.3%。参数/MAC-matched 非条件残差和 uniform/permuted routing 均明显低于 PRIME，证明增收益来自输入条件组织而非容量扩张。

**最值得记住的一句话**：不要靠加宽共享 MLP，而是用输入条件低秩残差把“公共预测”和“子群修正”解耦，同时保持原函数起点和决策路径表征一致。
