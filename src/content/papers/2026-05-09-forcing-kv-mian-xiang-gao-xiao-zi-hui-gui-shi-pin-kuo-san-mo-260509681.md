---
title: 'Forcing-KV: Hybrid KV Cache Compression for Efficient Autoregressive Video
  Diffusion Models'
title_zh: 'Forcing-KV: 面向高效自回归视频扩散模型的混合 KV 缓存压缩'
authors:
- Yicheng Ji
- Zhizhou Zhong
- Jun Zhang
- Qin Yang
- XiTai Jin
- Ying Qin
- Wenhan Luo
- Shuiyang Mao
- Wei Liu
- Huan Li
affiliations:
- ZJU
- Video Rebirth
- HKUST
- BJTU
arxiv_id: '2605.09681'
url: https://arxiv.org/abs/2605.09681
pdf_url: https://arxiv.org/pdf/2605.09681
published: '2026-05-09'
collected: '2026-05-16'
category: Multimodal
tags:
- Video Diffusion
- KV Cache
- Compression
- Autoregressive
- Attention Heads
- Efficiency
one_liner: 发现自回归视频扩散模型注意力头分为静态和动态两类，提出混合 KV 缓存压缩，结合静态结构剪枝与动态相似性剪枝，实现最高 2.82× 加速和 30%
  显存减少
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：自回归视频扩散模型（如 Self Forcing、LongLive）在流式生成长视频时，历史帧的 KV 缓存导致注意力计算和显存开销急剧增长，成为实时、高分辨率部署的瓶颈。现有压缩方法（如 Dummy Forcing）忽视注意力头的功能异质性，盲目丢弃历史上下文，造成块间跳变和动态性退化。

**方法关键点**：
- **头部功能发现**：通过大量实证，将注意力头分为两类——**静态头**重点关注当前块与最近过渡锚帧，维持块内保真度和跨块连续性；**动态头**以固定间隔关注历史帧的相同空间区域，捕捉运动与主体一致性。该划分跨样本、去噪步和模型稳定。
- **离线头部分析**：基于注意力质量计算（当前块 + 过渡帧占比），一次性将头部分类，无需在线开销。
- **静态结构剪枝**：为静态头恒久保留过渡锚帧和当前块，丢弃远处冗余帧，大幅减少注意力计算。
- **动态相似性剪枝**：将每帧划分为若干段，计算相邻帧段间余弦相似度，根据压缩比保留低相似度（高变化）段，剔除静止或冗余背景区域。仅用首个 Transformer 块的键状态计算相似度以降低额外代价。
- **混合压缩框架**：解耦静态模式与动态上下文利用，在保持关键信息的同时压缩率远超统一窗口方法。

**关键实验**：
- 模型：Self Forcing、LongLive；扩展至 Krea-Realtime-14B。
- 基准：VBench（5 秒）、VBench-Long（30/60 秒）、用户调研。
- 对比：完整 KV、StreamingLLM、Dummy Forcing。
- 结果：480P 下 LongLive 加速 1.30×（~27% KV 参与计算），Self Forcing 加速 1.50×（~46% KV 参与计算）；1080P 下最高 2.82× 加速；缓存显存减少约 30%；VBench 总分不降（80.43 vs. 80.23），块间断指标从 3.6 降至 2.5，用户调研中动态性评分大幅领先 Dummy Forcing（52.8% vs. 5.0%）。消融实验证实混合策略和分段相似性剪枝的必要性。

**核心洞见**：自回归视频扩散模型的注意力头存在明确的功能分工——静态头靠过渡锚帧保障画质连续，动态头依赖稀疏帧间对应维持运动一致性，针对性地压缩各自的冗余上下文是突破缓存瓶颈的关键。
