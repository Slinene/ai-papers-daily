---
title: Parallel Language Models via Variational Decoding
title_zh: 基于变分解码的并行语言模型
authors:
- Felix Draxler
- Robin C. Geyer
- Daniel Geyfman
- Farrin Marouf Sofian
- Justus Will
- Philipp Hildebrandt
- Giosue Migliorini
- Prakhar Srivastava
- Gagan Sai Trinadh Duggaraju Peddiraju
- Kushagra Pandey
affiliations:
- University of California, Irvine
- ETH Zurich
- Charité Berlin
- Hasso Plattner Institute
arxiv_id: '2610.26693'
url: https://arxiv.org/abs/2610.26693
pdf_url: https://arxiv.org/pdf/2610.26693
published: '2026-10-19'
collected: '2026-10-20'
category: LLM
direction: 并行解码 · 变分推断 · LLM 推理加速
tags:
- parallel decoding
- variational inference
- LLM inference
- multi-token prediction
- scaling laws
- speculative decoding
one_liner: 用潜变量路由 token 间依赖，单次前向生成多个一致 token，实现接近自回归质量的 2.3-5.7 倍推理加速
practical_value: '- **在线 LLM 服务加速**：如果业务中大量调用 LLM 做搜索 query 改写、导购 Agent、商品文案生成，可尝试把现有
  AR 模型改造成 PLM 风格的 block-parallel decoder；通过 β 调节质量/吞吐，SFT 时只对 response token 计算损失，保留
  prompt 作为 context，直接复用到指令跟随与对话场景。

  - **辅助变量 / Semantic ID 设计**：Geometry-aware auxiliaries 使用 embedding 空间的加权 V oronoi
  划分而非词表顺序，对生成式推荐中的 Semantic ID 构建有直接启发：用 item embedding 聚类/划分 codebook，比随机 ID 更保留语义，也能提高解码确定性。

  - **偏好对齐可复用**：PLM 的 DPO 用 response-restricted composite score 并做 length normalization，同时优化
  AR encoder 与 parallel decoder；在电商 Agent 的 RLHF / DPO 流程中可以借鉴，避免并行解码分支在偏好优化后掉点。

  - **工程验证点**：relaxed speculative acceptance 相比严格 speculative decoding 接受率平均提升 46.5%，质量损失小；若迁移到
  vLLM 服务，建议先在小参数模型上验证 2-5× QPS 提升，确认长 context、beam search 与自定义 attention mask 的兼容性。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**：自回归 LLM 每次 forward 只输出一个 token，推理延迟高；离散扩散等方法需要多步去噪，训练成本高且单步难以协调 token 间依赖。PLM 的目标是用单一训练目标直接训练并行生成模型，在接近自回归质量的前提下提高吞吐。

**方法关键点**：
- 引入逐 token 潜变量 u_i，decoder 通过 u≤i 并行解码；ELBO 分解为 AR encoder 损失 + parallel decoder 损失。
- 辅助变量设计：使用固定 512 个 embedding 空间单位向量，通过加权 V oronoi 划分将 token embedding 与 auxiliary 关联，保证 aux 先验质量匹配 AR 概率；对 top-128 外的 token 使用 mask auxiliary。
- 训练：encoder/decoder 权重共享；block 大小 K=16，stride s=βK 控制 encoder-decoder 配比；representation alignment loss 加速收敛。
- 推理：Quadratic Decoding 一次调用产生多个候选，encoder 验证并用 relaxed acceptance 提高接受率。

**关键结果**：
- 预训练 80M-3B，25B-300B tokens；PLM 的 NLL 接近同规模 AR，重建 token 数 R 随规模幂律上升，β 控制质量-速度 trade-off。
- 在 speed vs quality Pareto 上优于公开 AR 模型和离散扩散/少步扩散模型；1.3B 后训练在 GSM8K、MATH-500、HumanEval、IFEval 匹配或超过同规模 AR，Q/s 加速 2.3-5.7×。
- 3B PLM-β=1 后训练在多数 benchmark 优于所有 1.3B 变体。

**最值得记住的一句话**：PLM 证明并行生成可以由单一训练目标直接训练到自回归质量，且 parallelism 随模型规模增大。
