---
title: 'PaDoc: Layout-Grounded Parallel Decoding for Document Parsing'
title_zh: PaDoc：布局引导的并行解码文档解析
authors:
- Hao Yu
- Jiabo Zhan
- Kang Liu
- Linnan Zhao
- Dongxu Yue
- Rui Chen
- Jinglin Wang
- Chong Sun
- Chen Li
- Jing Lyu
affiliations:
- Tsinghua University
- Wechat Vision, Tencent
arxiv_id: '2608.06146'
url: https://arxiv.org/abs/2608.06146
pdf_url: https://arxiv.org/pdf/2608.06146
published: '2026-08-05'
collected: '2026-08-08'
category: Multimodal
direction: 多模态文档解析 · 并行解码加速
tags:
- Document Parsing
- Parallel Decoding
- Layout Grounding
- vLLM
- MLLM
- Prefix-conditioned Factorization
one_liner: 将文档布局建模为分支结构，通过前缀条件分解实现并行解码，将自回归深度缩减至最长分支，突破速度瓶颈
practical_value: '- 生成式推荐需同时产多条文案/建议时，可借鉴分支并行解码：在共享用户/上下文表示上并发生成多序列，降低端到端延迟。

  - 训练阶段使用打包变长祖先注意力（Packed Variable-Length Ancestor Attention）保持多分支可见性，该技巧可迁移到部分自回归多序列生成模型的训练。

  - 推理部署上，借助 vLLM 共享前缀缓存和并发请求能力优化批量生成：重用长期兴趣等公共前缀，减少重复计算，提升吞吐并降低 P95 延迟。

  - 电商详情页解析等离线图文理解任务，PaDoc 的并行解码可大幅提升单卡吞吐，适合大批量商品图片结构化处理，可集成至内容审核、智能排版等流程。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：端到端文档解析器将页面序列化为一个自回归序列，解码长度随总内容线性增长；而两阶段裁剪方案虽有区域并行性，却引入重复视觉前向与上下文碎片。**方法**：PaDoc 将预测布局视作分支结构，基于区域充分性假设推导出前缀条件分解，使布局流与各区域内容分支并行推进，解码深度降至最长分支路径。在单一 MLLM 内，通过打包变长祖先注意力在标准 next-token 训练下保留完整可见性；推理时使用掩码并行解码创建分支，vLLM 后端将这些分支作为并发请求处理，并重用驻留在缓存中的共享前缀。**结果**：OmniDocBench Full 上布局 F1 达 91.1，端到端总分 94.24，文本编辑得分 0.038，公式 CDM 95.59；在 384 页子集、单 A800 GPU 上，五种并发级别下均为最快端到端解析器，有效页吞吐提升 67.4–118%，P95 延迟降低 39.2–54.9%（对比同 backbone 顺序 SFT 基线）。
