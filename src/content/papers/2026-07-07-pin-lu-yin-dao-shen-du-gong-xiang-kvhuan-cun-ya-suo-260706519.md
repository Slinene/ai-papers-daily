---
title: 'FreqDepthKV: Frequency-Guided Depth Sharing for Robust KV Cache Compression
  in Long-Context LLM Inference'
title_zh: 频率引导深度共享KV缓存压缩
authors:
- Anna Córdoba
- Adam Puente Tercero
- Nerea Angulo Hijo
- Mar Linares Tercero
- Julia Barrientos
- Ainhoa Miranda
- Jesús Olivera
affiliations:
- Instituto de Investigación en Visión Artificial
arxiv_id: '2607.06519'
url: https://arxiv.org/abs/2607.06519
pdf_url: https://arxiv.org/pdf/2607.06519
published: '2026-07-07'
collected: '2026-07-08'
category: LLM
direction: 长上下文LLM推理 · KV缓存压缩
tags:
- KV cache compression
- long-context inference
- depth sharing
- frequency decomposition
- adaptive policy
- inference-time adaptation
one_liner: 推理时不需重训，通过频率分解与自适应模式分配压缩KV缓存，在长上下文任务中精度接近全缓存且实现3.9倍压缩
practical_value: '- 对于利用长用户历史序列的推荐系统，可直接应用该技术压缩KV缓存，显著降低在线推理的显存和延迟

  - 自适应分配压缩模式（共享深度/残差/精确）的思路可迁移到多任务推荐中的特征缓存管理，动态调整不同任务对历史状态的依赖

  - 无需额外训练，适合快速集成到现有推理引擎，降低长上下文LLM在搜索、广告等场景的部署成本

  - 低频分量共享策略可启发跨层特征融合设计，通过频域分解减少冗余缓存，提升工程效率'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：长上下文LLM推理中，KV缓存的内存和带宽开销随上下文线性增长，成为瓶颈；现有压缩方法（驱逐、量化等）易丢失层特异性证据，损害检索与多步推理所需的细粒度信息。  
**方法关键**：将相邻层的KV状态分解为共享的低频深度分量和稀疏的高频残差；引入轻量在线探针，根据各注意力头对重建敏感度的贡献，动态将其分配到共享深度、残差深度或精确缓存三种模式，无需额外训练即可自适应提示结构。  
**结果**：在32k预填充窗口的长上下文问答、Needle检索、摘要和代码生成等基准上，FreqDepthKV 达到 58.3 EM、63.0 F1、32.5 ROUGE-L、48.1 pass@1，精度贴近全缓存，同时解码吞吐提升至 70.4 tokens/s，首token延迟降至2.06秒，峰值KV内存仅6.2 GB，实现3.9倍有效压缩比。
