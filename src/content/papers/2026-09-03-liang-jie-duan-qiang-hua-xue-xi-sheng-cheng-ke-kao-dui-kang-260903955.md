---
title: Two-Stage Reinforcement Learning for Sound and Adversarial Test Generation
  in Code LLMs
title_zh: 两阶段强化学习生成可靠对抗测试用例提升代码 LLM
authors:
- Jiacheng Xu
- Wentao Zhang
- Zhiyi Lyu
- Fuxiang Zhang
- Chaojie Wang
- Yang Liu
- Bo An
affiliations:
- Nanyang Technological University, Singapore
- Skywork AI
arxiv_id: '2609.03955'
url: https://arxiv.org/abs/2609.03955
pdf_url: https://arxiv.org/pdf/2609.03955
published: '2026-09-03'
collected: '2026-09-06'
category: Training
direction: 代码 LLM 测试生成 · 对抗 RL
tags:
- RL
- Code Generation
- Test Generation
- Adversarial RL
- LLM
one_liner: 提出两阶段 RL 测试生成框架 TCS，先学可靠测试再对抗生成反例，提升代码生成 pass@1 与答案选择
practical_value: '- 若业务任务具备可自动验证的 reward（如商品属性合法性、SQL 可执行、Promo 规则检查、点击/转化模拟器），可借鉴
  TCS 两阶段生成器：Stage 1 贴近参考解/规则生成合法样本，Stage 2 针对线上模型常见失败模式生成反例，用于训练更鲁棒的排序/生成模型或筛选候选。

  - 将测试生成器作为可学习的 critic：在电商 Agent 或推荐 query/文案生成中，训练一个判别器为候选输出打分，替代或辅助人工评审；用当前策略的失败样本构造滚动缓冲，持续挖掘
  hard negatives，提升候选筛选的区分能力。

  - 推理时选择：生成多个候选推荐理由/搜索 query/广告标题，用学到的检查器自动过滤不合格输出，降低低质量内容上线风险；类似无参考评估，适合在线管道。

  - 注意领域差异：代码执行反馈明确且低成本，电商反馈（点击/转化）噪声大、延迟高，需用离线模拟器或业务规则先构造可信 reward，不宜直接照搬对抗 RL 的完全在线迭代。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：代码生成 RL 依赖可执行测试反馈，但测试用例既要 sound（与参考解一致）又要 discriminative（能发现问题），人工构造稀缺。将测试生成视为对抗 RL 问题：测试生成器应随 solver 当前失败模式生成反例。

**方法**：提出 Test Cases Scaling (TCS)，两阶段 RL 训练测试生成器，两个阶段都从滚动策略对齐缓冲采样。Stage 1 生成与参考解一致的测试，保证 soundness；Stage 2 将缓冲限制为当前失败模式，学习反例测试，提升区分度。测试生成器与代码 solver 形成对抗迭代。

**结果**：在 TACO 与 LiveCodeBench 上，TCS 提升 pass@1 与基于生成测试的推理时答案选择；其测试生成器也能作为通用选择器，用于筛选其他 LLM 输出。
