---
title: 'LoomVideo: Unifying Multimodal Inputs into Video Generation and Editing'
title_zh: LoomVideo：5B 参数统一多模态视频生成与编辑的高效架构
authors:
- Jianzong Wu
- Hao Lian
- Jiongfan Yang
- Dachao Hao
- Ye Tian
- Yunhai Tong
- Jingyuan Zhu
- Biaolong Chen
- Qiaosong Qi
- Aixi Zhang
affiliations:
- Peking University
- Alibaba Group
arxiv_id: '2606.06042'
url: https://arxiv.org/abs/2606.06042
pdf_url: https://arxiv.org/pdf/2606.06042
published: '2026-06-03'
collected: '2026-06-06'
category: Multimodal
direction: 多模态视频生成与编辑统一架构
tags:
- Video Generation
- Video Editing
- MLLM
- Diffusion Transformer
- Efficient Architecture
- E-commerce
one_liner: 用 MLLM + Deepstack 注入 + 零开销 Scale-and-Add 条件机制，在 5B 规模实现统一视频生成编辑并加速 5.41
  倍
practical_value: '- **用 MLLM 替代 T5 编码多模态输入**：在电商商品视频生成或虚拟试穿中，可直接使用多模态大模型（如 Qwen3-VL）处理交错图文指令，而无需单独设计文本编码器，提升对商品属性、换装等复杂要求遵循能力。

  - **Scale-and-Add 零开销条件注入**：避免在视频编辑时拼接源视频 token 导致序列翻倍、注意力计算平方增长。在需要融合历史帧或源视频的任务中（例如动态商品展示、视频重渲染），可直接将源视频潜变量按时间步缩放后加到目标潜变量，实现极速推理。

  - **Deepstack 多层特征注入**：将 MLLM 每一层隐藏状态经 MLP 投影后作为 DiT 对应层的 cross-attention key/value，实现深层次语义对齐。这种设计可迁移到跨模态推荐或内容生成中，提升多模态条件遵循能力。

  - **三阶段渐进训练 + RL 后训练**：先低分辨率对齐 MLLM，再提分辨率引入重建/编辑，最后加入多参考图等多任务微调，并辅以 RL 优化人类偏好。该管线可借鉴用于训练电商场景的统一生成式模型，从单任务逐步扩展，稳定提升质量。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：统一视频生成与编辑能处理交错多模态输入是前沿趋势，但现有框架依赖 13B 以上大模型，且编辑时拼接源视频 token 导致序列长度翻倍、自注意力计算量变为 4 倍，推理开销极大。该工作旨在构建一个 5B 参数的高效统一架构，同时保持复杂非刚性编辑能力。

**方法关键点**：
1. 用 Qwen3-VL（8B MLLM）替换 T5 文本编码器，并通过 **Deepstack 注入** 将 MLLM 每一层的隐藏状态经共享 MLP 投影后作为 DiT 对应层的交叉注意力 key/value，实现深层语义对齐。
2. 视频编辑采用 **Scale-and-Add 条件机制**：清洁源视频潜变量按当前时间步 t 缩放后直接加到噪声目标潜变量上，零额外 token，避免序列拼接，大幅降低计算量。
3. 多参考图使用 **负时序 RoPE 索引**，对参考图赋予负的时间位置编码 −τ,−2τ,...，与目标视频帧的正索引区分，实现稳健的多图引导。
4. 三阶段训练：Stage 1 低分辨率对齐 MLLM；Stage 2 提分辨率并加入重建与编辑数据；Stage 3 引入全任务（含多参考图编辑）并调整数据采样；最后用 DiffusionNFT 进行 RL 后训练提升人类偏好。
5. 动态批次与多分辨率训练，并采用基于 token 数的动态时间步偏移，适应图像与视频混合。

**关键实验结果**：
- 在 VBench 上平均分 63.15，优于 Wan 2.2 等基线；OpenVE-Bench 编辑综合分 3.05（与 13B 模型竞争）；RefVIE-Bench 得分 3.78，超越所有开源模型；自建 FashionVideoBench 的 6 项电商任务均达最高。
- 推理速度：T2V 生成 132.23s（6.24× 加速），视频编辑 166.30s（5.41× 加速），远优于拼接式模型。
