---
title: 'SHq: Learnable Grids for LLM Weight Quantization'
title_zh: SHq：面向 LLM 权重量化的可学习网格
authors:
- Michael Helcig
- Earl Killian
- Dan Alistarh
affiliations:
- ETH Zürich
- Rhoa Research
- Institute of Science and Technology Austria (ISTA)
arxiv_id: '2611.02966'
url: https://arxiv.org/abs/2611.02966
pdf_url: https://arxiv.org/pdf/2611.02966
published: '2026-11-02'
collected: '2026-11-03'
category: Other
direction: LLM 权重量化 · 可学习查找表网格
tags:
- LLM quantization
- lookup-table
- block-scaled
- companding grid
- KL divergence
- GPTQ
one_liner: 用两参数 sinh 压缩网格替代固定查找表，端到端 KL 搜索参数，3-4bit 量化误差显著低于 NF/BOF/INT
practical_value: '- 若业务中需以 4-bit/3-bit 低比特部署 LLM（如 query 改写、商品文案生成、广告标题生成、Agent 推理），可将
  SHq 作为 NF4/INT4/NVFP4 的 drop-in 替换：只改 lookup table 内容，不改变存储与解码，实测 KL 更低且下游精度更好。

  - 量化 grid 的选择不应只看权重 MSE 或 reconstruction error，而应在端到端目标（如生成 query 的分布偏移、业务代理指标）上搜索；SHq
  直接以 calibration KL divergence 扫描参数，这个思路可迁移到量化、蒸馏或压缩方案的选择。

  - 在 block-scaled LUT 格式中，E4M3 block scale 的 sign bit 通常闲置；可引入不对称 grid 或 offset，用
  sign bit 在 grid 与 mirror 间切换，零成本增加有效码本大小，对 2-bit/3-bit 极低比特部署尤其有价值。

  - 对 MoE 稀疏大模型（电商/广告推荐中常见）同样有效；联合使用 SHq 与 per-layer bit allocation（如 RCO）可进一步压缩，且
  SHq 在各 bit-width 下保持最低 KL，适合做统一量化格式。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**

Block-scaled lookup-table 低比特量化格式（NF4、BOF4、NVFP4、Rubin 3-bit LUT）虽允许任意 grid，但现有实现都预先固定 grid。固定 grid 有三个问题：最优 grid 随 bit-width 变化（2-bit 最优 BOFS，4/5-bit 最优 NF，6-bit 一半情况最优 INT）；最优 grid 同时依赖 block scale 的编码与搜索方式；grid 通常按 MSE 拟合，但更低 MSE 不一定带来更低模型输出 KL 散度。于是需要一种可调的、面向端到端目标的 grid 家族。

**方法关键点**

- SHq(α, c) 是两参数闭式 grid：在均匀 lattice 上采样 `sinh(αu)`，加偏移 `c`，再进行幅值归一化。α 控制压缩强度，从均匀（INT-like）连续过渡到几何/浮点式（FP-like）；c 打破对称，使 E4M3 block scale 的 sign bit 可以在 grid 与其镜像之间选择，镜像 levels 交错，最多得到 2^{q+1} 个 distinct values，几乎翻倍。
- 只修改 lookup table 内容，不改变存储、解码或硬件算术，任何 block-scaled LUT 格式都可直接替换。
- 参数选择不依赖权重 MSE，而是在 calibration 文本上扫描 (α, c)，以量化模型与 BF16 模型 next-token 分布的 KL divergence 为目标。
- block 内 16 个连续权重共享 signed E4M3 scale，解码为 `w_hat = s · L[index]`；额外引入 per-block scale search（lever），在 0.6–1.4 倍 absmax 范围内搜索最优 scale code 与 sign。

**关键实验**

在 5 个模型（3B–35B，含 MoE Qwen3.6-35B-A3B）上，2–6 bits、RTN 与 GPTQ 两种量化器，SHq 在 50 个 setting 中 45 个取得最低 held-out KL；3/4 bits 全部 20 个 setting 最低，比最佳固定 grid 低 4.0–34.4%。在 4.5 bpw 下，SHq 相比 NVFP4 降低 KL 40.7–67.4%，下游平均精度提高 0.1–0.7 点。消融显示同时具备 spacing 和 offset 参数的家族表现接近 SHq；缺少 offset 的家族 KL 明显更高；移除 sign bit 使 SHq 的 KL 上升 21–38%。

最值得记住的一句话：低比特 LLM 量化中，grid 应作为超参在端到端 KL 目标上搜索，并且可以利用 block scale 的 sign bit 做不对称镜像，以零成本增加有效码本。
