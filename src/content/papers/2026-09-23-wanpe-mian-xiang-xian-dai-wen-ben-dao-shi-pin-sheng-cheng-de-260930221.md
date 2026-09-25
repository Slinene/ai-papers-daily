---
title: 'WanPE: Towards Cinematic Prompt Enhancement for Modern Text-to-Video Generation'
title_zh: WanPE：面向现代文本到视频生成的电影级提示增强
authors:
- Yubo Zhu
- Yawen Shao
- Ziyun Dai
- Zixun Fang
- Kai Zhu
- Siyang Sun
- Haolan Xue
- Chuxin Wang
- Tingyu Weng
- Jingming Luo
affiliations:
- Nanjing University
- Wan Team, Alibaba Group
- University of Science and Technology of China
- Fudan University
- Tsinghua University
arxiv_id: '2609.30221'
url: https://arxiv.org/abs/2609.30221
pdf_url: https://arxiv.org/pdf/2609.30221
published: '2026-09-23'
collected: '2026-09-25'
category: LLM
direction: LLM 提示词增强 · 视频生成
tags:
- prompt enhancement
- text-to-video
- GRPO
- semantic consistency
- evaluation
one_liner: 397B 提示增强模型，通过视频反向构建与语义一致性 GRPO，大幅提升长视频生成的人类偏好
practical_value: '- 电商视频广告/商品短视频：可借鉴“反向构建”思路，从高点击、高转化的广告成片或商品视频反推分镜脚本文案，训练 LLM 提示规划器；避免依赖人工正向写
  prompt 模板。

  - 在 RLHF/GRPO 优化生成式推荐或 query 改写模型时，引入“语义一致性奖励”：用 embedding 相似度或判别器约束生成结果与用户原始意图的距离，防止多步生成漂移，适合多轮对话式推荐、Agent
  工具调用。

  - 构建评测集时按“时长/意图粒度”分层，并采用盲选成对比较，能更稳定地测量 prompt 增强等文本生成模块的业务收益；比只看 BLEU/ROUGE 更贴近人类偏好。

  - 若业务中要生成多镜头脚本（如广告创意、短视频脚本），可显式建模 shot-level plan；一次规划生成多个镜头，保持角色/商品外观、品牌信息一致性，而不是逐镜头独立生成。'
score: 6
source: huggingface-daily
depth: abstract
---

动机：现代 T2V 生成器可生成 30 秒多镜头视频，文本 prompt 成为“导演计划”，但用户 prompt 往往过于简单，缺乏镜头、运镜、灯光等电影级规划；现有提示增强多采用前向改写，易偏离用户意图、跨镜头不一致。

方法：WanPE 是 397B 参数提示增强模型，基于 1.05M 真实视频构建视频 grounding 反向构建训练：从视频内容反推电影级分镜 prompt，再输入生成器。采用 Semantic-Consistency GRPO (SC-GRPO)，在 GRPO 中引入语义一致性约束，保证多镜头及长时间下用户需求不漂移。评测基准 WanPEval 覆盖 5-30 秒、不同意图粒度，约 11K 盲评。

结果：配合 Wan3.0 生成器，WanPE-397B 在 5-15 秒人类偏好比原始提示提升 10.66-18.84 分，30 秒提升 50.86 分；消融证明反向构建优于前向改写，SC-GRPO 跨模型尺度保持语义一致性。在 5-15 秒全面领先商用方案，30 秒与 Seedance 2.5 竞争。
