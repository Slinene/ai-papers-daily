---
title: What Makes a Good Unmasking Policy? A Controlled Study of Learned Unmasking
  in Diffusion Language Models
title_zh: 什么造就好的去掩码策略？扩散语言模型学习式去掩码的受控研究
authors:
- Jinya Sakurai
- Xun Xu
- Jaehong Yoon
affiliations:
- NTU Singapore
- Institute for Advanced Intelligence and Computing (IAIC), A*STAR
- Centre for Frontier AI Research (CFAR), A*STAR
arxiv_id: '2610.31576'
url: https://arxiv.org/abs/2610.31576
pdf_url: https://arxiv.org/pdf/2610.31576
published: '2026-10-21'
collected: '2026-10-24'
category: LLM
direction: 扩散语言模型高效解码策略
tags:
- diffusion language models
- unmasking policy
- distillation
- efficiency
- LLM inference
- controlled study
one_liner: 系统解耦学习式去掩码策略，提出轨迹收缩目标，856K参数策略在LLaDA-8B上取得最优精度-效率前沿
practical_value: '- 若在搜索补全、推荐理由生成、query 改写等场景尝试 diffusion LM 或并行解码，可用「轨迹收缩目标」替代“与最终输出一致”作监督：只监督不会导致后续偏离参考轨迹的
  commit，避免低 NFE 下过度激进解码。

  - 策略输入不要只用 hidden states 或只用 confidence；二者结合的小型策略（856K 参数）即可达到最优前沿，且约 10% NFE 下降就能抵消
  policy 开销，适合实时推荐/搜索的低延迟约束。

  - 把解码过程视为 teacher，蒸馏出轻量 unmasking policy，能显著提升吞吐；在自回归 LLM 为主的生产环境中，若未来引入 diffusion
  LM 生成结构化输出，可复用这套精度-NFE frontier 和 throughput 评估方式选型。

  - 该策略在 LLaDA-8B 上训练后基本迁移到 Dream-7B-Instruct，说明轻量 policy 有一定跨模型泛化性，可作为多模型共用的推理加速组件。'
score: 6
source: huggingface-daily
depth: abstract
---

动机：masked diffusion language models 并行生成但效率取决于 unmasking policy；已有 learned policies 在监督、输入、容量上各不相同，缺乏系统理解。

方法：将监督策略视为对解码过程的蒸馏，独立考察 teacher 的 committable 标签、策略模仿的状态、策略观察的输入、以及 policy overhead 需多少 NFE 下降才能抵消。发现“预测与最终输出一致”的标签在低 NFE 下过于宽松；hidden states 单独较弱但可补充 confidence；约 10% NFE 下降即可抵消最多 7.5M 参数策略开销。基于此训练 trajectory-contraction targets：只接受停留在参考轨迹上的 commit，输入 confidence + hidden states。

结果：在 LLaDA-8B-Instruct 上，856K 参数策略取得最佳 accuracy-NFE frontier 和 GSM8K 最高吞吐；在 MATH-500 与 HumanEval 中等目标上有竞争力；并基本迁移到 Dream-7B-Instruct。
