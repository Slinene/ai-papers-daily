---
title: 'Measuring Language Transfer in Robot Policies: Adding Greek to a Cosmos3 Vision-Language-Action
  Policy'
title_zh: 测量机器人策略中的语言迁移：为 Cosmos3 视觉-语言-动作模型添加希腊语
authors:
- Ayoub Kirouane
- Georgios Giaples
- Christos Petrocheilos
affiliations:
- Sophea AI, KIEFER SA, Athens, Greece
arxiv_id: '2609.07470'
url: https://arxiv.org/abs/2609.07470
pdf_url: https://arxiv.org/pdf/2609.07470
published: '2026-09-06'
collected: '2026-09-10'
category: Eval
direction: 低资源语言迁移评估与对照实验
tags:
- Language Transfer
- Vision-Language-Action
- Evaluation
- Low-resource
- Multilingual
- Seed Variance
one_liner: 机器改写指令为 Cosmos3 VLA 添加希腊语，揭示五类误导性评估，证明双语训练与多种子对照的必要性
practical_value: '- 评估低资源语言或新场景能力时，先构建“故意错误指令/随机输入”等保证 null 基线，避免单一指标假阳性；做多语言 query
  理解、商品文案生成或多语种 Agent 时，用乱序或错误语言作为底线对照。

  - 多种子重复实验是必须的：低资源语言效果随随机种子波动可高达 31.6 点，线上小流量或多轮实验才能区分配方差异；报告应给出跨种子方差而非单次对比。

  - 双语混合训练比纯目标语言训练更稳：在电商多语言场景，英文+小语种联合微调通常优于只用小语种数据，且无需改架构。

  - 对机器翻译或模板生成的数据有严重过拟合风险：同一指令提供多种措辞（如 7 种 paraphrase）可显著降低对特定翻译风格的过拟合；做多语言 prompt/文案生成时增加措辞多样性。'
score: 6
source: huggingface-daily
depth: abstract
---

动机：机器人基础模型几乎只用英语训练和评估，多数语言没有演示语料；为低资源语言做本地化时，难点不是翻译而是可靠测量，常见指标会给出虚假成功信号。

方法关键点：在开源 Cosmos3 VLA 策略上，仅用机器改写英文指令为希腊语（带术语表），不改变架构。设计判别式 90 任务套件，每臂 3 个种子，并引入故意错误指令作为控制下限；比较英语-only、希腊语-only、双语训练、多语言文本塔、热启动与解冻文本塔等配置。同时测试颜色直方图、单目标基准、训练损失等常见但可能误导的指标。

关键结果：颜色直方图在纯噪声生成上翻倍；单目标基准正确希腊语 84.6% vs 错误指令 82.6%；训练损失差异在 1.4% 内但希腊语能力相差 7.2 倍；种子波动高达 31.6 点。对照实验显示：无希腊语演示的多语言文本塔停留在错误指令下限；纯希腊语训练超过控制至多 2.7 点；双语训练稳定超过控制 6.7-7.1 点，达到英语性能约 2/5。策略过拟合翻译措辞，训练 7 种措辞可将惩罚减半；从语言适应世界模型热启动或解冻文本塔均降低性能。
