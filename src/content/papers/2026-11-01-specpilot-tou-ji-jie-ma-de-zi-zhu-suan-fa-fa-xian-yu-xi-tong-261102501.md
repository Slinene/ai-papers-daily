---
title: 'SpecPilot: Autonomous Algorithm Discovery and Systems Optimization for Speculative
  Decoding'
title_zh: SpecPilot：投机解码的自主算法发现与系统优化
authors:
- Kunjun Li
- Wenhao Chai
- Yihao Liang
- Yuezhou Hu
- Shuyao Xu
- Yi Pan
- William X. Zheng
- Kannan Ramchandran
- Kurt Keutzer
- Jiantao Jiao
affiliations:
- University of California, Berkeley
- Princeton University
- Stanford University
- NVIDIA
arxiv_id: '2611.02501'
url: https://arxiv.org/abs/2611.02501
pdf_url: https://arxiv.org/pdf/2611.02501
published: '2026-11-01'
collected: '2026-11-04'
category: LLM
direction: 投机解码 · 自主 Agent 优化
tags:
- Speculative Decoding
- Agentic Loop
- LLM Inference
- Cost Model
- Reward Hacking
- Systems Optimization
one_liner: 用自治 Agent 循环自动发现投机解码的算法与系统优化，单请求加速比提升 2.4 倍、批处理提升 2 倍
practical_value: '- 用 cost model 定位部署瓶颈：在电商/推荐 LLM 推理服务中，单请求 vs 批处理、不同 GPU 上的优化重点不同，可先构建理论
  ceiling 模型，自动识别当前系统最大可优化 gap，避免盲目调优。

  - Token forcing 防 reward hacking：在自主优化或自动调参时，逐 token 对比基线输出确保无损，可借鉴到在线模型自动更新、推理参数搜索等场景，防止质量劣化。

  - 批量场景的分级验证与合并机制：论文发现的两级验证和三种 batching 机制可迁移到多租户推荐请求合并处理，降低 per-request overhead，提升吞吐。

  - 12-bit 无损权重格式：如果验证可行，可直接应用于部署中的大模型量化，在保证输出质量前提下节省显存、加速 decoding。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：并行 drafter 使 speculative decoding 每步可生成整块 token，但现有 stock 系统未充分释放潜力。单请求时每步接受 token 少却读取全部目标权重；批处理时 per-request 验证开销使加速比相比 AR 近乎减半；且优化具有部署特异性，无统一方案适用所有 serving regime、drafter、target model 与 GPU。

**方法关键点**：SpecPilot 是一个自治 agentic loop。每轮中 cost model 定位当前系统与理论 ceiling 的最大 gap；并行 agents 探索不同优化方向并集成成功项；token forcing 逐 token 对照 stock 检测 reward hacking；structured memory 将验证过的机制传递到后续轮次和新部署。该循环发现了通用无损 12-bit 权重格式、面向 hybrid recurrent targets 的树验证、两级验证以及三种 batching 机制。

**关键结果**：在 4 个 target models、3 个 drafters、2 个 GPU platforms、5 个 benchmarks 上，无训练、无质量损失，单请求加速比从 stock 的 4.46× 提升至 10.87×，批处理从 1.94× 提升至 3.93×。
