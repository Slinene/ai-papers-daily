---
title: 'LatentLoop: Scaling Looped MoE Models with Asymmetric Compute Allocation'
title_zh: LatentLoop：非对称计算分配的循环 MoE 模型规模化
authors:
- Zefeng He
- Yunkai Chai
- Xiaoyang Chen
- Tong Zhu
- Zongliang Wu
- Yun Luo
- Yafu Li
- Yu Cheng
affiliations:
- SJTU
- Shanghai AI Lab
- USTC
- CUHK
- NTU
arxiv_id: '2610.19975'
url: https://arxiv.org/abs/2610.19975
pdf_url: https://arxiv.org/pdf/2610.19975
published: '2026-10-13'
collected: '2026-10-15'
category: Training
direction: 循环 MoE 训练 · 非对称计算分配
tags:
- Looped MoE
- Asymmetric Compute
- MoE
- Transformer
- Compute Allocation
- Scaling
one_liner: 提出 LatentLoop，压缩首轮循环序列、保留次轮全分辨率，将省下算力重分配给隐藏宽度，在相同预算下降低 NLL 并提升下游基准
practical_value: '- 在用户行为序列建模中，可借鉴 LatentLoop 的非对称计算分配：对长序列第一轮使用压缩表示（如 latent 投影或
  token 合并），第二轮保留全分辨率，并将节省的 FLOPs 转向加宽 hidden size，而非直接降低延迟；这可在相同推理预算下提升模型质量。

  - 用可学习残差系数诊断循环 Transformer 各次访问的贡献，识别可压缩的浅层/首轮访问，指导剪枝或低精度量化；固定系数实验结论“首轮可压缩、次轮不可压缩”可作为先验。

  - 在 MoE 推荐/广告模型中，专家 FFN 权重可跨不同序列分辨率共享，但 attention 参数应独立，以适应压缩后序列与全分辨率序列的差异；这比全共享更细粒度，利于多尺度特征融合。

  - 面向资源受限的线上推理，可先对输入序列做低秩/降采样压缩并分配给第一层，保留关键的后期层高分辨率，配合专家共享减少参数和 FLOPs；这比均匀缩放更有效，有潜力用于生成式推荐的大模型加速。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：循环 MoE 通过共享层与稀疏专家增加有效深度，但每次循环仍消耗计算，等算力预算下收益不明确。已有工作显示共享参数的不同循环访问作用不同。残差系数实验发现首次访问的 scale 更小，固定系数下降低首访问权重不损或提升性能，而降低第二次访问则显著损伤，表明计算分配存在不对称性。

**方法关键点**：提出 LatentLoop，将第一次循环访问的序列压缩到更低分辨率，第二次保留全分辨率，把节省的 FLOPs 重新用于增大 hidden size；引入可学习系数控制首访问对全序列的更新强度；MoE 权重跨访问共享，但注意力参数独立，以适配不同序列分辨率。

**关键结果**：在 15 个配置（1.3B-7B 参数，最大预算 >10^21 FLOPs）上验证 NLL 一致下降。在拟合 NLL=1.988 处，预测相对 vanilla MoE 节省 19.0% 算力，相对 looped baseline 节省 7.9%；九个基准在 0-shot 和 5-shot 下平均分全面提升。
