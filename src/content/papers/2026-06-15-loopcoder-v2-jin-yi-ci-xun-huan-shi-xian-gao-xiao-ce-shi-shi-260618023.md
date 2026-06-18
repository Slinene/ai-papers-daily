---
title: 'LoopCoder-v2: Only Loop Once for Efficient Test-Time Computation Scaling'
title_zh: LoopCoder-v2：仅一次循环实现高效测试时计算扩展
authors:
- Jian Yang
- Shawn Guo
- Wei Zhang
- Tianyu Zheng
- Yaxin Du
- Haau-Sing Li
- Jiajun Wu
- Yue Song
- Yan Xing
- Qingsong Cai
affiliations:
- Beihang University
- IQuest Research
- Langboat
- Renmin University of China
arxiv_id: '2606.18023'
url: https://arxiv.org/abs/2606.18023
pdf_url: https://arxiv.org/pdf/2606.18023
published: '2026-06-15'
collected: '2026-06-18'
category: LLM
direction: 并行循环Transformer · 增益-成本权衡
tags:
- Looped Transformer
- Test-Time Compute
- Non-Monotonic Scaling
- Code Generation
- SWE-bench
- Gain-Cost Trade-off
one_liner: 并行循环Transformer仅循环两次即达最优，平衡表征增益与位置偏移代价
practical_value: '- 在Agent/工具调用场景中，可借鉴并行循环Transformer设计，通过共享KV缓存的滑动窗口注意力与跨循环位置偏移，在不显著增加显存的前提下实现测试时计算扩展。

  - 循环次数并非越多越好：实验发现2次循环是最优的，再增加循环收益递减甚至退化；在推荐/搜索Agent的迭代推理中，建议通过诊断（表征多样性、更新幅度）确定最佳推理轮次，避免盲目堆叠。

  - 跨循环位置偏移引入的边界失配是固定代价，当表征精炼增益缩小时会成为主导；在设计迭代式推荐模型（如循环精炼用户/物品表示）时，需权衡每次迭代的增益与固定结构偏差。

  - 若要将循环机制用于电商生成式推荐或搜索，可尝试用一个共享的Transformer块多次循环生成候选物品的Semantic ID，并监控循环间的表征振荡，在2次循环附近寻找性能甜区。'
score: 6
source: huggingface-daily
depth: abstract
---

动机：Looped Transformer通过重复使用同一Transformer模块实现测试时计算扩展，但顺序循环会带来延迟和KV缓存随循环次数线性增长。并行循环Transformer（PLT）通过跨循环位置偏移（CLP）和共享KV的门控滑动窗口注意力缓解了此问题，使循环次数成为可选的超参数。本文从增益-成本视角研究PLT的循环次数选择：额外循环可能精炼表征，但CLP在每个循环边界引入位置失配代价。

方法：从头训练一组7B参数的PLT编码模型LoopCoder-v2，使用不同循环次数，在18T token上预训练后进行一致的指令微调。核心设计是同一参数模块循环多次，并用CLP区分循环位置，同时通过共享KV缓存降低显存。

结果：双循环变体在代码生成、推理、Agent软件工程及工具使用基准上全面优于无循环基线，SWE-bench Verified从43.0升至64.4，Multi-SWE从14.0升至31.0。但三循环及以上变体性能退化，呈现明显的非单调循环次数效应。诊断分析显示，第二次循环贡献了主要的生产性精炼，后续循环产生震荡更新且表征多样性降低。由于CLP引起的失配代价基本固定，而精炼增益随循环次数递减，偏移代价逐渐占主导，导致收益饱和于两次循环。该增益-成本权衡为PLT的循环次数选择提供了理论解释。
