---
title: Multi-Block Diffusion Language Models
title_zh: 多块扩散语言模型
authors:
- Yijie Jin
- Jiajun Xu
- Yuxuan Liu
- Chenkai Xu
- Yi Tu
- Jiajun Li
- Dandan Tu
- Xiaohui Yan
- Kai Yu
- Pengfei Liu
affiliations:
- Shanghai Jiao Tong University
- Xi'an Jiao Tong University
- Huawei
arxiv_id: '2606.29215'
url: https://arxiv.org/abs/2606.29215
pdf_url: https://arxiv.org/pdf/2606.29215
published: '2026-06-29'
collected: '2026-07-02'
category: LLM
direction: 扩散语言模型 · 多块并行解码
tags:
- Diffusion Language Models
- Multi-Block Decoding
- Teacher Forcing
- Block Buffer
- KV caching
- Parallel Decoding
one_liner: 通过多块教师强制训练和块缓冲解码，将块扩散语言模型扩展至多块并行生成，实现近两倍加速且精度不降
practical_value: '- 若在推荐系统中用扩散模型生成文案、推荐理由等长文本，可借鉴多块并行解码思路，将生成过程拆分为固定大小的噪声块组，提升并行度，降低推理延迟。

  - 块缓冲（Block Buffer）机制通过保持 KV cache 静态形状和前缀复用，能直接迁移到在线 LLM 服务的缓存管理，减少显存波动，适合高并发场景。

  - 多块教师强制（MultiTF）提供了一种低成本后训练方案：在已有 BD-LM 基础上，只需构造带噪声的连续块与干净前缀的混合训练数据，就可以让模型适配更高效的解码策略，适合快速迭代。

  - 实验中的 TPF 指标可作为工程权衡的参考：在精度允许范围内（如 1% 准确率损失），可将每步生成令牌数提升近 3 倍，有利于在成本与效果间做配置化调优。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：块扩散语言模型（BD-LM）通过 KV 缓存和可变长生成提升了扩散模型的推理效率，但其训练采用教师强制，模型仅观察单个噪声块；而多块并行（MultiBD）解码要求模型同时处理一组不同噪声水平的连续块，存在训练-推理不匹配。

**方法**：提出 **Multi-Block Teacher Forcing (MultiTF)**，在干净前缀条件下训练有界的噪声块组，并采用随机噪声调度来模拟推理时的异构噪声模式，以此后训练 BD-LM 得到 MBD-LM。同时设计 **Block Buffer** 解码算法：固定输入形状以保持静态 KV 缓存，复用前缀缓存，将多块并行转换为实际墙钟加速。

**结果**：MBD-LLaDA2-Mini 将每前向传递令牌数（TPF）从 3.47 提高到 6.19，平均准确率从 79.95% 升到 81.03%；融合 DMax 后，TPF 达 9.34，代码/数学基准准确率仅下降 1.02%。
