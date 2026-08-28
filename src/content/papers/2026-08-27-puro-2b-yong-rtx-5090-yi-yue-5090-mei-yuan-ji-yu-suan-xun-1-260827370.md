---
title: 'Puro-2B: Poor Lab''s Qwen2-1.5B Trained on RTX 5090 within $5090'
title_zh: PuRo-2B：用 RTX 5090 以约 5090 美元级预算训练 Qwen2-1.5B
authors:
- Kairong Luo
- Jiarui Cui
- Yaorui Yin
- Shengqi Chen
- Yiming Yang
- Linxiang Gao
- Yanmohan Wang
- Mingzhe Zhang
- Kaiyue Wen
- Kaifeng Lyu
affiliations:
- Tsinghua University
- Pengcheng Laboratory
arxiv_id: '2608.27370'
url: https://arxiv.org/abs/2608.27370
pdf_url: https://arxiv.org/pdf/2608.27370
published: '2026-08-27'
collected: '2026-08-28'
category: Training
direction: 低成本 LLM 预训练 recipe
tags:
- low-cost pretraining
- FP8
- MuonH
- curriculum model averaging
- open-recipe
- RTX 5090
one_liner: 开源低成本预训练 recipe：RTX 5090 + FP8 + MuonH + 课程平均，约 $6.9K 训出接近 Qwen2.5-1.5B
  的 2B 模型
practical_value: '- 低成本训练 domain-specific 小模型：RTX 5090 的 BF16/FP8 每美元算力约为 H200 的 2.7
  倍，业务侧可评估消费级 GPU 集群做 LLM 训练/微调，而不必只租 A100/H200；但需注意驱动改 P2P/GDR、InfiniBand 组网等工程风险。

  - FP8 混合精度可从随机初始化开始，不需要 BF16 warm-up：参考 blockwise scaling（激活 1D 128，权重 2D 128x128），敏感状态保持
  BF16/FP32，预期吞吐提升 1.3-1.4x 且质量损失很小，适合训练中小规模排序/召回或生成式推荐模型。

  - MuonH 优化器对 attention/MLP 矩阵做 fixed-radius 投影，显式控制 effective LR，比普通 Muon 更稳；在总
  token 预算不固定、需要持续训练时，WSD + 较长线性 decay 比短 decay 更划算，可迁移到训练中小型 Transformer。

  - 数据课程与 checkpoint averaging：按源内质量分排序 chunk 的 coarse curriculum + 末尾常数 LR checkpoint
  averaging，不需要全局质量分就能提升下游任务；对多源推荐/搜索语料，可用 proxy 小模型评估各数据源的下游收益，指导 mixture 权重，显著降低数据筛选成本。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**：LLM 预训练成本长期高企，即使开源权重和 recipe，复现小型模型也常需数十万至百万美元，小型实验室难以参与。PuRo-2B 试图用一套可复现、可负担的 recipe，把 2B 参数、1.4T token 级预训练拉到消费级 GPU 和数千美元预算内。

**方法关键点**：
- 硬件选 RTX 5090：算力单价约为 H200 的 2.7 倍；通过修改驱动启用 P2P/GDR，配合 400G InfiniBand 组网，使 72% 计算走 FP8 时仍达到约 73% MFU。
- 系统基于 Megatron Core + Transformer Engine：只用 DP+PP，不用 TP；按拓扑放置 PP group，调整 MBS 到 GEMM 的 roofline knee，给 LM head 所在 stage 少分 Transformer 层。
- FP8 blockwise 混合精度：从随机初始化开始，Transformer 线性层 GEMM 用 E4M3，激活按 128 分组、权重按 128x128 分块量化，敏感状态保持 BF16/FP32；FP8 加速 1.36x，质量损失仅约 2% BF16 等价。
- MuonH 优化器：对 attention/MLP 等近似 scale-invariant 矩阵施加 Hyperball 约束，显式控制 effective LR；其余参数用 AdamW。LR schedule 用 Phase1 power + Phase2 长线性 decay，WSD sweep 显示大 peak 或长 horizon 都需要更长 decay。
- Curriculum Model Averaging (CMA)：Phase2 按源内质量分 chunk 从低到高排序，末尾 29B token 保持常数 LR 继续训练，平均最后 6 个 checkpoint。
- 数据 recipe：只用公开数据源，用 Kaiyuan-SpaRK 去重；通过 proxy 小模型评估每个候选源/slice 的多基准能力，指导 mixture 和过滤阈值，不做全局质量分。

**关键实验与结果**：在 15 个数学、代码、推理、知识 benchmark 上对比 Qwen2-1.5B、Qwen2.5-1.5B、Gemma-2-2B、Llama-3.2-3B、SmolLM3-3B 等。最佳 PuRo-2B 总 GPU-hours 22,514，成本约 $6.9K，超过 Qwen2-1.5B，接近 Qwen2.5-1.5B。另有 uniform Phase2 版本约 $4.4K 即可超过 Qwen2-1.5B。Puro Cost Scaling Law 拟合 cost-performance，显示 $4.4K 可达到 Qwen2-1.5B 平均分 55.14。下游 SFT 测试中，curriculum 初始化在 GSM8K 和 broad instruction tuning 上持续优于 uniform。

**最值得记住的一句话**：不到 5 千美元级的复现预算就能从零训出接近 Qwen2.5-1.5B 的 2B 模型，核心是把有效学习率、FP8、课程平均和消费级硬件作为联合系统一起设计，而不是单点叠加。
