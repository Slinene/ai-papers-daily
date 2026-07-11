---
title: 'CineMobile: On-Device Image-to-Video Diffusion for Cinematic Camera Motion
  Generation'
title_zh: 移动端电影运镜生成扩散模型 CineMobile
authors:
- Xuyao Huang
- Zelai Deng
- Xu Wang
- Xizhong Xiao
- Zhijie Deng
affiliations:
- Shanghai Jiao Tong University
- Nankai University
- Transsion
arxiv_id: '2607.03803'
url: https://arxiv.org/abs/2607.03803
pdf_url: https://arxiv.org/pdf/2607.03803
published: '2026-07-03'
collected: '2026-07-11'
category: Other
direction: 移动端高效视频生成
tags:
- video generation
- diffusion model
- model compression
- mobile deployment
- distillation
- quantization
one_liner: 通过剪枝-蒸馏-量化三阶段优化，将大型视频扩散模型压缩至移动端，实现40倍加速的电影运镜生成
practical_value: '主要是视觉生成领域的模型压缩贡献，对推荐/广告/Agent 系统的直接业务可借鉴点有限。

  - 蒸馏引导的结构化剪枝策略可迁移至推荐模型压缩：先用蒸馏让剪枝后模型快速恢复能力，再联合微调。

  - 强化学习与扩散蒸馏结合的少步生成方法，可为搜索推荐系统中使用扩散模型做生成式推荐（如 GenRec）时降低推理步数提供思路。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：移动端图像到视频创作需要电影级运镜效果（如子弹时间、滑动变焦），但大型 Diffusion Transformer (DiT) 计算量大，难以在手机端高效运行。

**方法**：提出 CineMobile，采用三步优化：
1. **蒸馏引导剪枝**：从 Wan2.1 架构出发，利用蒸馏信号指导结构化剪枝，得到紧凑但保留运镜能力的模型；
2. **扩散蒸馏 + 强化学习**：将压缩模型优化为 4 步生成器，大幅减少去噪迭代次数；
3. **混合训练后量化**：对权重进行混合精度量化，将模型体积压至 1 GB 以下。

**结果**：相比 Wan2.1-14B 教师模型，生成速度提升 40 倍，保持可比画质。在 NVIDIA H200 上每步去噪仅 0.6 秒，在联发科天玑 8400 移动平台 20 秒生成 49 帧 480p 视频，峰值内存占用 1.8 GB。
