---
title: 'Represented but misread: Post-training changes how language models read out
  what they represent'
title_zh: 后训练改变读出而非表征：语言模型如何误读其所表征的信息
authors:
- Jochen Laubrock
affiliations:
- University of Potsdam
arxiv_id: '2611.26584'
url: https://arxiv.org/abs/2611.26584
pdf_url: https://arxiv.org/pdf/2611.26584
published: '2026-11-19'
collected: '2026-11-21'
category: Training
direction: LLM后训练读出机制与探针诊断
tags:
- post-training
- linear probing
- signal detection theory
- SFT
- DPO
- AI detection
one_liner: 用探针和信号检测论揭示后训练主要改变模型如何读出表征而非表征本身，且小训练信号可定向修复
practical_value: '- 用线性探针对比模型自身输出，可审计模型是否“心里明白但嘴上说错”：在生成式推荐、对话Agent或风控中，若探针显示特征已编码但模型答案未利用，说明可通过微调或prompt释放该能力，避免盲目增加参数或数据。

  - 小训练信号即可定向修复读出：研究发现仅2000条正确标注的作者判断数据就能改善特定语料上的答案，说明业务中针对特定任务（如真假识别、内容安全）只需少量高质量标注微调，就能纠正LLM的行为，成本可控。

  - 关注内部状态的读出位置：文本结束后的token位置比文本本身位置更能传递后训练变化，早期层参与读出改变。在复用隐藏态做下游分类或检索增强时，应选择合适的层和位置，而非简单取最后一个token，可提升下游任务效果。

  - 后训练可能降低某些敏感度：例如AI生成文本检测能力在后训练后平均Δd''=-0.34，风控团队在微调通用模型后需用探针监控此类能力是否退化，必要时加入针对性数据保持。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：理解后训练（SFT/DPO）是改变模型表征还是读出机制，对控制LLM行为、避免能力退化至关重要。

**方法关键点**：在6个开源base和post-trained模型上，对比线性探针与模型自身答案，用信号检测论分析敏感度d'和先验使用。任务包括德文文本人类/AI作者判断、否定陈述真假判断。结合阶段检查点、模型缝合、训练干预实验定位变化来源。

**关键结果数字**：
- 人类/AI作者判断：探针和词n-gram分类器能很好区分，但模型答案差且经常反向；后训练平均降低答案敏感度Δd'=-0.34（跨模型家族），-0.29（跨提示）。
- 先验使用：base模型对先验变化调整不足，多数post-trained模型过度调整。
- 两点检查点显示变化发生在SFT阶段；早期层关键；从中间深度起，文本之后位置的内部状态而非文本本身位置传递变化。
- 否定陈述真假：探针解码接近上限，但几个base模型答案未使用该信息，后训练修复；修复位于语句之后位置。
- 训练研究：加入2000条正确标注新闻作者判断即可改善报纸和教科书语料上的答案，但在聊天语料上反转。

结论：后训练改变的是如何从表征读出判断，小训练信号即可定向设置读出方向。
