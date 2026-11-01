---
title: 'TextSeal2: Distortion-Free LLM Watermarking with Copula Mixing and Memoryless
  Races'
title_zh: TextSeal2：基于Copula混合与无记忆竞速的无失真LLM水印
authors:
- Tom Sander
- Pierre Fernandez
- Itai Gat
- Haiming Bao
- Jiaxin Shi
- Jason Park
- Valeriu Lacatusu
- Sylvestre-Alvise Rebuffi
- Hongyan Chang
- Hady Elsahar
affiliations:
- Meta Superintelligence Labs
arxiv_id: '2610.40613'
url: https://arxiv.org/abs/2610.40613
pdf_url: https://arxiv.org/pdf/2610.40613
published: '2026-10-29'
collected: '2026-11-01'
category: LLM
direction: LLM水印·投机解码
tags:
- LLM watermarking
- speculative decoding
- Gumbel-max
- Gaussian copula
- distortion-free
one_liner: 合并多密钥为虚拟密钥并结合无记忆指数竞速，使LLM水印在投机解码下保持无失真且检测率提升
practical_value: '- 电商AIGC文案/广告/商品描述等场景可直接叠加无失真水印做内容溯源与反爬，TextSeal2证明水印不影响输出分布和多样性，不会牺牲文案质量。

  - 多业务线共用同一LLM生成推荐理由或广告素材时，可将多个secret keys合并为单个虚拟key，统一检测且不稀释信号，便于集中部署水印验证服务。

  - 若线上生成链路已用speculative decoding加速，TextSeal2的无记忆竞速机制保证加水印不改变acceptance rate、不引入延迟，可直接嵌入现有推理优化，无需改造采样内核。

  - 检测信号可作为训练数据治理的风控输入，例如过滤AI生成的商品评论或UGC内容，防止污染推荐模型训练集。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

动机：LLM水印需在保持输出质量的同时，兼容投机解码等加速策略。TextSeal通过抛硬币路由两个key恢复Gumbel-max多样性，但检测器无法得知所用key，需平均两个key的分数，导致检测信号被稀释。

方法关键点：TextSeal2将两个或多个key合并为一个虚拟key，借助AutoMark的高斯copula与新鲜噪声耦合，避免多key平均造成的检测损失；任意数量的key（包括公开key）均可合并而不降低检测强度。在投机解码下，对draft races的剩余项再执行一次指数竞速，利用指数分布的无记忆性复现block verification，使输出与目标模型完全一致，且不改变acceptance rate。

关键结果：在三个LLM上、相同输出token多样性、FPR=10^-3条件下，100-token答案检测率较TextSeal高8-22个百分点，与textGrain相当但无需post-logits优化；在投机解码下，200-token答案检测率较TextSeal高18个百分点、较textGrain高22个百分点，acceptance rate保持不变。
