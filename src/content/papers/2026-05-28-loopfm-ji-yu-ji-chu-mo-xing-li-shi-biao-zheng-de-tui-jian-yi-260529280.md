---
title: 'LoopFM: Learning frOm HistOrical RePresentations of Foundation Model for Recommendation'
title_zh: LoopFM：基于基础模型历史表征的推荐知识迁移
authors:
- Shali Jiang
- Hua Zheng
- Boyang Liu
- Laming Chen
- Kenny Lov
- Chuanqi Xu
- Lisang Ding
- Qinghai Zhou
- Can Cui
- Xiaolong Liu
affiliations:
- Meta AI
arxiv_id: '2605.29280'
url: https://arxiv.org/abs/2605.29280
pdf_url: https://arxiv.org/pdf/2605.29280
published: '2026-05-28'
collected: '2026-05-30'
category: RecSys
direction: 知识蒸馏优化 · 历史表示结构化
tags:
- Knowledge Distillation
- Foundation Model
- Embedding Transfer
- Sequential Recommendation
- Compression
- Industrial Recommendation
one_liner: 将大模型历史中间层嵌入压缩并序列化为小模型输入特征，打破标量知识蒸馏的带宽瓶颈。
practical_value: '- **离线生成用户侧序列特征**：将大模型已产生的历史交互 embedding 按键（如 user ID）压缩成时间序列，作为
  lightweight 模型的直接输入，无需实时推理大模型，显著降低在线延迟。

  - **正交填充知识缺口**：LoopFM 序列提供跨域、跨特征交互信息，与标量 KD 互补；在线上可并行部署两条迁移通道，提升整体迁移率（内部实验迁移率翻倍）。

  - **以压缩控制成本，以结构保留时序信号**：用自动编码器 + Matryoshka 维度灵活 + INT4 量化，可实现 4× 存储压缩；序列化方式比简单池化更好（DMIN
  attention 优于 mean-pool），但 sum-pool 也能捕获大部分增益，可按成本选择。

  - **容量差距越大收益越高**：小模型直接学高基数 ID 序列效果差，而 LoopFM 提供的低维、信息浓缩表示使小模型直接受益，这适合电商推荐中的重模型-轻模型架构。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
工业推荐采用重型基础模型 (FM) 和轻型垂域模型 (VM) 两层架构，传统知识蒸馏 (KD) 仅传递 FM 的标量预测值，信息带宽极低。随着 FM 参数达到万亿级别，迁移率 (transfer ratio) 持续恶化——单一标量无法承载丰富的跨域特征和时序模式。

**方法关键点**
- **三阶段模块化流水线**：① 提取 FM 若干中间层激活值拼接为高维嵌入；② 通过自动编码器（可配合 Matryoshka 实现任意维前缀有效）压缩至低维，并做 INT4 量化；③ 按键（如用户 ID）分组，按时间排序形成历史嵌入序列。
- **无需在线 FM 推理**：序列仅使用历史嵌入，VM 侧通过序列编码器（如 DMIN attention 或 sum-pool）消费，架构解耦。
- **理论分析**：将信息增益分解为时序信息 + 跨特征信息 - 压缩损失，并给出迁移率下界，该下界随 FM 特征丰富度单调递增，随压缩质量提升而收紧。

**关键实验**
- 公开数据集：TaobaoAd（22 特征）上，LoopFM+KD 取得 AUC 0.6344（相对基线 0.5886 提升 6.4%），所有六种 VM 架构均获益；KuaiVideo 和 Amazon 分别约 +1.0% 和 +0.5%。
- 工业系统：万亿参数 FM，LoopFM 在已有 KD 基础上将迁移率约翻倍，线上广告转化提升 Y1H1 +0.5%，Y1H2 两次独立上线分别 +1.03% 与 +1.22%。
- 消融：较浅层表示迁移效果更好；序列长度增加单调提升 AUC 且边际递减；嵌入维度与序列编码器宽度需协同扩增；嵌入漂移（频繁更新 FM checkpoint）可能损害一致性。

**核心结论**
LoopFM 提供了一条与标量 KD 正交的高带宽迁移通道，通过历史嵌入结构化，将大模型的知识有效注入小模型，为工业推荐系统的大模型赋能开辟了新路径。
