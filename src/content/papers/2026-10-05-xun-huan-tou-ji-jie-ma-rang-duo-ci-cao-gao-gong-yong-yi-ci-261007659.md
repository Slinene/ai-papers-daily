---
title: 'DLoop: Looped Speculative Decoding'
title_zh: 循环投机解码：让多次草稿共用一次验证
authors:
- Geonmo Gu
- Byeongho Heo
- HeeJae Jun
- Yoohoon Kang
- Sangmin Lee
- Sangdoo Yun
- Dongyoon Han
affiliations:
- NAVER AI Lab
- NAVER AI Search Platform
- Korea University
arxiv_id: '2610.07659'
url: https://arxiv.org/abs/2610.07659
pdf_url: https://arxiv.org/pdf/2610.07659
published: '2026-10-05'
collected: '2026-10-08'
category: LLM
direction: LLM 推理加速 · 投机解码
tags:
- Speculative Decoding
- LLM Inference
- Draft Model
- Loop-aware Training
- Confidence Gate
- EAGLE
one_liner: DLoop 让一次验证覆盖多个草稿阶段，通过置信度门控与 loop-aware 训练，在多种投机解码上把 wall-clock speedup
  提升 5–41%
practical_value: '- 如果线上 LLM 链路（query 改写、商品/广告文案生成、推荐理由生成）采用 speculative decoding，可在
  drafter 后加置信度门控：对每个 draft block 累加 log probs，与阈值比较决定是否再 draft 一轮；不增加模型和模块，只增加少量
  draft forward cost，能减少 target model 验证次数，尤其适合草稿接受率高的结构化/模板化输出。

  - 对已有的 EAGLE/MTP 自回归 drafter 或 DFlash/Domino/DSpark 并行 drafter，可以按 DLoop 做 loop-aware
  微调：训练时用 draft model 自己的 hidden states 多轮 unroll，损失只加在最远端 block，N 取 3；不改变架构，可在既有
  draft weights 上继续训练，显著提升长草稿链上的可靠性。

  - 门控阈值 g 比较鲁棒，论文统一用 -0.5 或 -0.75；在业务数据上小规模扫描即可，不必训练额外 head。该方法也可与 tree verification
  叠加：若已有 tree 推理加速，可沿最高分路径继续延长，进一步减少验证次数。

  - 注意并发 serving 下增益会随 batch 负载上升而衰减；建议在低并发、长尾或单请求延迟敏感的场景使用，或结合动态批调度/regrouping 优化。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
标准 speculative decoding 每轮 drafting 后必须做一次 target model 验证，即使 draft 模型产生的所有 token 都会被接受。论文观察到，在 EAGLE-3、DFlash、Domino、DSpark 等 draft model 上，数学/代码/对话任务中大量 drafting stages 被完全接受，而 target model 的验证 forward 占解码时间主导。验证延迟对 token 数增长不敏感，因此把这些被浪费的验证合并成一次，有机会进一步提速。

**方法关键点**
- **Confidence-gated drafting loop**：每轮 drafting 后，把一个 block 内所有 draft token 的 log-prob 求和作为置信度分数，与阈值 g 比较；高于阈值则继续下一轮 drafting，否则把累积的所有 draft tokens 一次性交给 target model 验证。接受规则不变，解码保持 lossless。
- **适用于并行与自回归 drafter**：循环重复的是整个 drafting stage，不改变 drafter 生成 token 的方式；附加 drafting 阶段用 draft model 自身的 hidden states 替代尚未验证位置的 target hidden states。
- **Loop-aware training**：训练时展开多轮 drafting，用 ground-truth token 替换 draft token 输入，但 hidden state 链使用 drafter 自己的输出；损失只取第一轮和最后一轮的 cross-entropy，`L = 1/2(L(1)+L(S))`，N=3。不增加参数、不增加 target model forward。
- 门控只需要求和与比较，没有额外模块。

**关键实验与结果**
在 EAGLE-3、DFlash、Domino、DSpark 以及 Qwen3.5-9B/Gemma-4-12B 的 MTP 模块上，用 Qwen3-4B/8B 作 target model，基准覆盖 GSM8K、MATH-500、AIME25、HumanEval、MBPP、LiveCodeBench、MT-Bench、Alpaca。DLoop 让平均 acceptance length 提升 12–102%，wall-clock speedup 提升 5–41%；其中 DSpark 提升最大。与 tree verification 组合后，DFlash+DDTree 平均 speedup 从 5.79× 到 6.48×，DSpark+DARTree 从 4.22× 到 5.15×。Ablation 显示 loop 与 loop-aware training 单独使用收益有限，二者结合后增益超过简单相加。在 SGLang 并发 serving 下，低并发吞吐提升明显，高并发收益衰减。

**最值得记住的一句话**：用 draft model 的额外 forward 换 target model 的验证 forward，并让验证覆盖多个草稿阶段，是投机解码中一种简单且可叠加的加速方式。
