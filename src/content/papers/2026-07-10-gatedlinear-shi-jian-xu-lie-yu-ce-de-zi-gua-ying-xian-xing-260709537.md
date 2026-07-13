---
title: 'GatedLinear: Adaptive Routing of Complementary Linear Bases for Time Series
  Forecasting'
title_zh: GatedLinear：时间序列预测的自适应线性基路由框架
authors:
- Qitai Tan
- Ruiwen Gu
- Yilin Su
- Mo Li
- Xu Lin
- Xiao-Ping Zhang
affiliations:
- Shenzhen International Graduate School, Tsinghua University
arxiv_id: '2607.09537'
url: https://arxiv.org/abs/2607.09537
pdf_url: https://arxiv.org/pdf/2607.09537
published: '2026-07-10'
collected: '2026-07-13'
category: Other
direction: 时间序列预测 · 自适应路由线性基
tags:
- time-series-forecasting
- linear-models
- mixture-of-experts
- gated-routing
- lightweight
- interpretability
one_liner: 用三因子融合门将互补线性基动态路由到异质时序模式上，轻量且可解释
practical_value: '- 推荐系统中，不同用户群或物品生命周期可能呈现平滑趋势、突变或周期性，可借鉴三基分解思想，用多个线性专家捕捉不同模式，并通过轻量门控动态融合，替代单一路径。

  - 门控的因子化解耦设计（通道特异性、预测步偏移、相位偏置）可迁移到多场景、多步长的推荐或广告预估中，实现细粒度、可解释的融合权重分配。

  - 轻量参数规模（相较复杂基础模型）适合在线服务延迟敏感、资源受限的工业场景，例如实时流量预测、广告出价调整等。

  - 可解释路由模式可直接输出每个专家在各维度上的贡献，为模型诊断和场景分析提供依据，类似推荐中分析不同策略对不同人群的有效性。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：真实时间序列常同时包含平滑趋势、非平稳漂移和严格相位对齐的周期性，单一计算机制（如自注意力）难以兼得，且深层模型参数冗余。

**方法**：提出 GatedLinear，将预测视为在三种互补线性基之间的自适应路由：(1) 全局趋势-季节性基捕捉长程平滑投影，(2) 差分增量基处理非平稳漂移，(3) 相位对齐循环基实现显式周期性复用。核心创新是 Tri-Factorized Fusion Gate，将路由决策解耦为三个因子：通道特异性偏好、预测步相关偏移、已知未来时间标记导出的相位索引偏置，实现逐点细粒度软融合，无需堆叠重计算模块。

**结果**：在标准基准上达到与复杂基础模型持平甚至更优的精度，参数规模显著更小，且路由模式具备直接可解释性。
