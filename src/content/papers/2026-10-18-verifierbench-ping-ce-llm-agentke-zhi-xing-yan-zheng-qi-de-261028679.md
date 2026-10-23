---
title: 'VerifierBench: Benchmarking the Generation of Executable Verifiers for LLM
  Agents'
title_zh: VerifierBench：评测LLM Agent可执行验证器生成的基准
authors:
- Jianing Yin
- Ziyi Chen
- Hao Wang
- Yiyou Sun
- Zijian Jin
- Dawn Song
- Daoan Zhang
affiliations:
- University of Pennsylvania
- University of Illinois at Urbana-Champaign
- University of California, Berkeley
- New York University
- University of Rochester
arxiv_id: '2610.28679'
url: https://arxiv.org/abs/2610.28679
pdf_url: https://arxiv.org/pdf/2610.28679
published: '2026-10-18'
collected: '2026-10-23'
category: Eval
direction: Agent 验证器生成评测与审计
tags:
- verifier generation
- LLM agents
- benchmark
- executable verifiers
- self-improvement
- evaluation
one_liner: 构建VerifierBench与V4V审计，揭示LLM生成的验证器普遍过严，多数假拒源于不接受任何有效解
practical_value: '- 在自生式训练数据过滤或 RL reward 场景下，别只看“拒绝无效样本”的准确率：VerifierBench 显示模型很容易生成过严验证器，看似强实则大量误拒有效解。上线前应显式统计
  balanced accuracy，并专门补充 alternative valid solutions 来暴露假拒绝。

  - 生成可执行验证器时，自测集不能只用与生成器同分布的负样本/正样本；要加入格式变体、工具调用顺序变体、等价代码改动等，因为案例表明验证器常写入无关的格式、工具或代码假设。

  - 可借鉴 V4V 的六项审计思想：在 pipeline 中对验证器自动做 checklist——是否至少有一个已知正确解通过？是否对多个允许解不误拒？是否只依据任务指令而非隐含假设？

  - 如果把 LLM 当作文本/策略评判器（例如筛选广告文案、推荐理由），需注意“拒绝负例强、接受正例弱”可能反映模型保守；可通过阈值校准或多验证器投票降低过度严格带来的数据丢弃风险。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**  
LLM agents 在完成任务和过滤合成训练数据时需要一个可靠验证器，但自动生成的验证器本身可能不可靠，在递归自改进（RSI）中会持续放大错误。现有评测缺少对验证器生成质量的系统基准。

**方法关键点**  
论文构建 VerifierBench：222 个任务，来自六个 agent benchmark，覆盖工具调用、状态类和代码验证三种类型；内置 4,993 个隐藏测试用例，包含 alternative valid solutions 和 attacks。提出 Verifier4Verifier (V4V) 六项审计，筛查源验证器和测试套件。在统一 agent harness 中评测 19 个模型。

**关键结果**  
标准化 balanced accuracy 从 10.6 到 62.1。生成的验证器拒绝无效解比接受有效解更可靠；但这掩盖了过度严格：多数假拒绝来自验证器不接受任何该任务的测试解。案例研究显示验证器对解格式、工具使用、代码改动做了无根据假设，从而排除有效解。这些错误之所以在自测中留存，是因为代理测试的解与验证器共享错误假设，或提交验证器时未确认任何正确解通过。结论建议同时测试验证器接受正确解，以及接受任务允许的其他解。
