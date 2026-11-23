---
title: 'cmHC: Balancing Stream Mixing in Hyper-Connections via Geometric Contraction'
title_zh: cmHC：通过几何收缩平衡超连接中的流混合
authors:
- Haowei He
- Ziwen Zhao
- Chenshuo Pan
- Gang Lin
- Zhihao Yang
- Chao Wang
- Xinzhang Liu
- Kaidong Yu
- Han Gao
- Dongfang Li
affiliations:
- Xingchen AGI Lab, China Telecom
- The Hong Kong University of Science and Technology (Guangzhou)
- Harbin Institute of Technology (Shenzhen)
- Huawei Technologies Co., Ltd.
arxiv_id: '2611.27193'
url: https://arxiv.org/abs/2611.27193
pdf_url: https://arxiv.org/pdf/2611.27193
published: '2026-11-19'
collected: '2026-11-23'
category: Training
direction: 大模型训练 · Hyper-Connections
tags:
- Hyper-Connections
- Birkhoff Polytope
- Residual Streams
- Pretraining
- MoE
- Training Stability
one_liner: cmHC 通过收缩 Birkhoff 多胞形内部来平衡多流残差混合，提升 LLM/MoE 预训练稳定性与扩展性
practical_value: '- 自研/继续预训练电商搜索、广告文案或 Agent 底座大模型时，可把 cmHC 作为 Hyper-Connections 的直接替代：无需新增参数，论文在
  dense 和 MoE 多规模上验证有效，能降低浅层流混合退化风险。

  - 对推荐/广告里的 MoE 特征交互或大模型 MoE，同样可测试 cmHC 的稳定性收益；尤其关注浅层适度收缩，避免流过度同质化。

  - 借鉴其“混合矩阵几何位置”诊断思路：在多流/多专家模块中统计混合矩阵到 Birkhoff 顶点/重心的距离，判断是否退化为独立流或均匀混合，作为特征融合模块调优依据。

  - 如果有 Ascend NPU 训练/推理需求，可参考其 hyper-connection 融合算子设计，降低执行延迟（论文达 44.8%）；否则该项主要是底层训练架构贡献。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：Hyper-Connections 扩展残差连接为多流混合，但 mHC 将混合矩阵约束到 Birkhoff 多胞形后，存在混合不足（矩阵靠近顶点，流近似独立）与混合过度（矩阵集中在均匀重心，流趋同）的权衡，影响深层网络预训练稳定性。

**方法关键点**：提出 cmHC，在 Birkhoff 多胞形上做几何收缩，迫使混合矩阵深入内部，既避免欠混合又保留流可分性；该方法无新增参数，并证明流混合下界；浅层采用适度收缩防止过混合，保障梯度传播。同时为 Ascend NPU 开发融合算子。

**关键结果**：在 dense 与 MoE 模型的多参数规模实验验证有效性和可扩展性；融合算子使 hyper-connection 执行延迟最高降低 44.8%。
