---
title: 'Acceptance Is Not Speed: Length Inflation in Training-Free Lossy Speculative
  Decoding'
title_zh: 接受不等于速度：训练自由有损推测解码中的长度膨胀
authors:
- Chiatzen Wang
- Bill Xu
- Haochen Gu
- Hongyang Zhang
affiliations:
- University of Waterloo
arxiv_id: '2610.23818'
url: https://arxiv.org/abs/2610.23818
pdf_url: https://arxiv.org/pdf/2610.23818
published: '2026-10-16'
collected: '2026-10-19'
category: Other
direction: LLM 推理 · 推测解码效率评估
tags:
- speculative decoding
- length inflation
- LLM inference
- evaluation
- lossy verification
- reasoning
one_liner: 发现 relaxed 推测解码的接受 token 数增加会伴随生成长度膨胀和推理延长，使指标失真，应报告完成长度和验证轮数
practical_value: '- 线上若用 LLM 生成推荐理由、搜索 query 改写、Agent 规划，并用 speculative decoding 加速，不要只报
  accepted tokens per round；必须在墙钟时间前先验证是否出现输出长度膨胀，否则吞吐指标会虚高。

  - 对预算受限的 Agent 任务（如多步工具调用、长推理链），lossy 验证可能接受低目标模型概率 token，导致推理啰嗦、max_tokens 耗尽而拿不到最终答案；建议优先使用
  lossless 或对 token 概率设置更高门槛。

  - 评估解码加速方案时，增加 completion length 和 verifier rounds 指标，并与线上真实延迟打点结合；可加长度惩罚、max_new_tokens
  约束或后处理截断来控制膨胀。

  - 若用于生成式商品文案、推送标题等，lossy 加速可能让输出变冗长，影响点击和转化；建议离线对比输出长度分布和任务指标，避免仅看 accept rate。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

动机：speculative decoding 常用每轮接受的 draft token 数衡量加速，在 lossless 验证下该指标可靠。但 relaxed（lossy）验证会接受原本会拒绝的 token，可能改变目标模型输出分布，使 accepted tokens per round 失真。

方法：对 12 组 target-drafter pairs，评估现有训练自由 relaxed verification 规则，与 lossless 在相同 prompt 上对比 completion length、verifier rounds、wall-clock time 和任务准确率。

关键结果：在最宽松设置下，relaxed 平均每轮接受 1.34× 的 token，但完成长度变为 1.54×；被 relaxed 额外接受的 token 往往目标模型概率低，导致推理链变长；部分规则虽减少 verifier rounds，但准确率大幅下降；进一步分析发现，持续推理会耗尽预算，使模型来不及给出最终答案。结论：accepted tokens per round 单独不能衡量实际解码速度，评估 relaxed speculative decoding 必须同时报告 completion length 和 verifier rounds。
