---
title: On the Practice of Scaling Search Conversion Rate Prediction
title_zh: 电商搜索转化率预测模型的规模化实践
authors:
- James Pak
- Jyun-Yu Jiang
- Fan Zhang
- Sen Wang
- Taekmin Kim
- Henry Tsai
- Vijay Rajaram
- Juexin Lin
- Mohitdeep Singh
- Alessandro Magnani
affiliations:
- Coupang
arxiv_id: '2605.29232'
url: https://arxiv.org/abs/2605.29232
pdf_url: https://arxiv.org/pdf/2605.29232
published: '2026-05-28'
collected: '2026-05-30'
category: RecSys
direction: 搜索转化率预测 · 模型缩放与推理优化
tags:
- CVR prediction
- model scaling
- MaskNet
- embedding scaling
- inference optimization
- search ranking
one_liner: 系统研究搜索CVR模型在骨干、嵌入、数据三个维度的独立可加和缩放规律，并实现线上 +2.6% 转化提升
practical_value: '- **优先选用 MaskNet 配合交叉宽度缩放**：相比 DCNv2 和序列模型，MaskNet 在相同 FLOPs 下具有更高的特征交叉效率，且内存占用更友好，适合在搜索
  CVR 这类强调显式高阶交互的任务中构建 Pareto-optimal 骨干。

  - **独立缩放实验可加速迭代**：骨干、嵌入维度和训练数据量对离线 mAP 的提升效应接近线性可加，因此可以分别在子数据集上独立调参（如先在小数据上做架构搜索），再将组合方案直接迁移到全量数据训练，大幅降低探索成本。

  - **数据缩放遵循对数线性，新特征不必全量回填**：训练时长增加带来的收益递减明显，且近期 300 天行为序列就足够支撑个性化嵌入效果，历史特征缺失用 “unseen”
  占位不会明显损伤指标，从而可以只对高价值特征做近期回填。

  - **推理优化让大模型延迟持平**：采用 CPU 特征预处理与 GPU 骨干推理分离、客户端预分组 + 服务端动态批处理的混合方案，可在 8 倍推理 FLOPs
  下将 P99 延迟从 82ms 降至 32ms，峰值吞吐提升 4.4 倍，避免因延迟约束放弃大模型。

  - **热启动训练策略显著缩短迭代周期**：利用固定维度隐层作为输入投影，使得特征增减时只需重新初始化输入映射层，其余参数全部 warm-start，可将训练时间从冷启动的
  +264% 压缩到仅 +36%，适合高频模型更新。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：在电商搜索高流量环境下，CVR 预测模型的规模化面临质量、训练成本与推理延迟的三角制约。现有缩放研究多聚焦推荐场景，且对搜索 CVR 中异构特征、大规模嵌入表及多维度缩放效应的理解不够系统。

**方法关键点**
- **三维缩放框架**：将模型放大分解为骨干计算量、嵌入参数量、训练数据量三个可独立控制的维度。
- **骨干评估**：对比 DCNv2、MaskNet、Transformer、RankMixer 及其 DHEN 集成，发现 MaskNet 通过交叉宽度放大（projected cross-input dimension）能更高效地捕捉高阶特征交互，且在同等 FLOPs 下内存占用远低于序列模型（Transformer/RankMixer），避免 OOM。
- **嵌入缩放**：增大 item 嵌入维度比增加词汇量（通过 hash modulo）更有效，两个方向收益可加和；query/text 嵌入缩放收益有限，原因在于文本 token 的通用语义难以通过维度提升获得额外表征能力。
- **数据缩放**：训练时长增加遵循对数线性收益规律，利用“unseen”占位符处理历史缺失特征不会明显损害效果，验证了近期数据对新特征回填的足够性。
- **训练/推理加速**：设计固定维度的输入投影层，实现特征变更时只需重初始化映射层其余参数全部 warm-start，大幅缩短迭代周期；推理端采用 CPU 预处理 + GPU 骨干分离以及客户端预组批 + 服务端动态批处理，峰值吞吐提升 4.4 倍，P99 延迟下降 62%。

**关键实验与结果**
- 数据集：电商平台超过一年的真实搜索交互日志。
- 评估指标：未来七天购买的 mAP（近似 MRR），与线上 A/B 搜索转化率一致。
- 主要数字：MaskNet 交叉宽度从 512 扩至 4096 带来 +0.64% mAP 且训练吞吐仅下降约 27%；嵌入维度翻倍比词汇量放大 10 倍更有效；数据从 35 天增至 300 天呈对数线性；三维叠加合计 +0.74% 离线 mAP；线上 8 倍 FLOPs 模型推出后搜索转化率提升 +2.6%，延迟与基线持平。
