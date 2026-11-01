---
title: 'Instruction Capacity: Behavior and Degradation of Language Models under Controlled
  Load'
title_zh: 指令容量：受控负载下语言模型的行为与退化
authors:
- Hennadii Kutomanov
affiliations:
- Independent researcher
arxiv_id: '2610.36095'
url: https://arxiv.org/abs/2610.36095
pdf_url: https://arxiv.org/pdf/2610.36095
published: '2026-10-25'
collected: '2026-11-01'
category: Eval
direction: 指令跟随能力评测 · 容量度量
tags:
- instruction following
- evaluation
- capacity
- load
- GPT-4o mini
- statistical modeling
one_liner: 用原子替换规则构建负载度量，测出 GPT-4o mini 在 95% 正确率下约 37-38 条规则的指令容量
practical_value: '- 在电商 Agent 或生成式推荐 prompt 中，多约束（类目、价格、品牌、排序、输出格式）本质是规则负载，可借鉴本工作的「原子规则替换」思想，用离线评测标出模型在指定正确率下的规则容量，作为
  prompt 复杂度预算上限。

  - 论文给出负载因素（文本长度、词位置、替换密度、规则数、规则编号）与正确率之间平滑可拟合的规律，工程上可建立类似回归曲线，在规则数量增加时预测掉落，提前做 prompt
  拆分或分段生成。

  - 方法提供开源数据和 passport，可直接改造为业务 prompt 指令负载回归测试，监控不同模型版本/微调后的容量退化，辅助选择基座或 LoRA 融合策略。'
score: 6
source: huggingface-daily
depth: abstract
---

动机：LLM 遵循复杂指令能力有限，随负载增加会丢规则、混对应关系，但缺少以负载为单位、带不确定性的容量度量。

方法关键点：设计一种测量工具，负载由原子规则构成——规则将文本中单 token 词替换为无语义符号，规则相互独立，每个替换结果可计算。每次词出现作为一个 Bernoulli trial，记录答案位置和规则编号。统计模型测量正确替换概率随文本长度、词位置、替换密度、规则数量和规则编号的变化，拟合平滑规律并恢复不依赖编码的参考水平，从而输出指令容量（在给定正确替换比例下能持有的规则数）及其不确定性。

关键结果：对 GPT-4o mini 进行 2958 次请求、642,430 次试验，得到各负载因素和答案崩溃的规律；在 95% 正确替换比例下，指令容量约为 37-38 条规则；在全替换密度下约为 18-19 条规则。测量代码、数据和 passport 开放，passport 数值均可从发布数据点复现。
