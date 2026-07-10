---
title: 'Jet-Long: Efficient Long-Context Extension with Dynamic Bifocal RoPE'
title_zh: 'Jet-Long: 动态双焦 RoPE 的高效长上下文扩展'
authors:
- Haozhan Tang
- Zerui Wang
- Yuxian Gu
- Song Han
- Han Cai
affiliations:
- NVIDIA
arxiv_id: '2607.07740'
url: https://arxiv.org/abs/2607.07740
pdf_url: https://arxiv.org/pdf/2607.07740
published: '2026-07-07'
collected: '2026-07-10'
category: LLM
direction: 零样本长上下文扩展 · 动态 RoPE 分组
tags:
- RoPE
- Context Extension
- Zero-shot
- FlashAttention
- Long Context
- Inference Efficiency
one_liner: 一种无需微调的零样本长上下文扩展方法，通过动态调整远程窗口分组因子保持位置在分布内，并利用容斥注意力合并实现几乎无开销的推理
practical_value: '- **零样本扩展部署**：可将任意开放权重 RoPE LLM 的上下文窗口无损扩展 4 倍以上（如 32K→128K），无需长上下文微调，适合快速上线长上下文应用（RAG、Agent
  轨迹、长文档理解）。

  - **双窗口架构**：本地窗口（w0=2048）完全保留原始 RoPE，远程窗口动态调整分组大小 G=max(1, ceil(L/w_pretrained))，在短输入时退化为基模型，长输入时最小化位置压缩，避免短上下文性能退化。

  - **工程实现借鉴**：通过“校正旋转”在 query/key 上施加位置偏移 Δ，实现远程窗口注意力，保持 KV 缓存不变；预填充阶段用三次 FlashAttention
  的容斥合并（inclusion–exclusion merge）融合为单个 CuTe 内核，达到 1.28–1.39× FA2 吞吐，生成开销 ≤4%，可直接集成到线上推理服务。

  - **超参数鲁棒**：唯一超参数 w0 在 512~4096 间几乎无波动（RULER 波动 <2pp），无需按部署场景调参，降低维护成本。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：LLM 在 RAG、代码仓库理解、多轮 Agent 等场景中经常遇到远超预训练窗口（4K–32K）的输入，零样本上下文扩展是开放权重模型的主流方案。现有方法或固定一个缩放因子，在短上下文牺牲保真度，在长上下文外推崩溃。Jet-Long 提出动态双焦 RoPE，使远程窗口的缩放因子随序列长度自适应，彻底分离短长上下文优化。

**方法关键点**：
- **双窗口分解**：本地窗口 w0 保留原始 RoPE，远程窗口通过动态分组大小 G = max(1, ⌈L / w_pretrained⌉) 进行位置降采样，确保所有远程旋转角度落在训练分布内。
- **离散位置别名**：远程映射 f(x) = ⌊x/G⌋，直接将位置投射到模型已见过的离散网格，优于频率插值，避免 OOD 旋转。
- **KV 缓存不变**：通过在线校正旋转（Δq, Δk）从原始缓存键值中直接重构远程视角，无需重写缓存，支持流式生成。
- **容斥合并预填充**：利用三次 FlashAttention（A: 滑动窗口本地，B: 全局远程，C: 滑动窗口远程）的容斥组合实现精确的距离路由，融合为单个 CuTe 内核，预填充速度达 1.28–1.39× FA2，生成仅增加 ≤4% 开销。

**关键结果**：在 Qwen3-1.7B/4B/8B 上，上下文从 32K 扩展到 128K，Jet-Long 在 RULER 上超越最强基线 4.79/2.18/2.03 pp，HELMET-RAG 及 PG-19 困惑度均最优；方法无缝复用至混合注意力架构 Jet-Nemotron；本地窗口大小 w0 在 512–4096 内稳定（RULER 波动 <2pp）。
