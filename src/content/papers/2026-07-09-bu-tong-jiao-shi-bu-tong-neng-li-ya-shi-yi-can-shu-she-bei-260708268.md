---
title: 'Different Teachers, Different Capabilities: Sub-1B On-Device Distillation
  for Structured Text Enrichment'
title_zh: 不同教师不同能力：亚十亿参数设备端蒸馏结构化文本富集
authors:
- Vinay Kumar Chaganti
arxiv_id: '2607.08268'
url: https://arxiv.org/abs/2607.08268
pdf_url: https://arxiv.org/pdf/2607.08268
published: '2026-07-09'
collected: '2026-07-10'
category: Other
direction: 知识蒸馏 · 小模型结构化抽取
tags:
- knowledge distillation
- small language models
- structured generation
- reasoning distillation
- on-device deployment
- text summarization
one_liner: 揭示推理教师、指令教师、管道教师蒸馏小模型时传递不同能力，形成设备端结构化提取的任务级路由策略。
practical_value: '- 电商商品描述/标签生成场景可用大模型推理教师蒸馏到<1B端侧模型，大幅降低延迟（论文中从39秒降到0.8秒），适合高吞吐在线结构化提取。

  - QLoRA微调0.6B小模型仅需有限资源即可复现，蒸馏时保留教师推理能力的关键是教师需具备推理特性，而非仅规模放大。

  - 不同教师传递不同能力：推理教师转移写作质量，管道教师转移标签多样性，指令教师更忠实；可据此构建“字段级路由器”，对关键字段（如标题摘要）用推理蒸馏模型，对需要忠实性的字段用指令蒸馏模型。

  - 采用三位法官盲评的无参考评估方式，结合约束解码作为基线，可作为业务中自动化评估生成质量的参考方案。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

动机：大规模结构化文本提取（如新闻摘要+分类）若直接调用大模型，每项物品都需支付高昂延迟，蒸馏到端侧小模型可大幅提速降本。

方法：将8B推理教师（deepseek-r1:8b）蒸馏为0.6B学生（Qwen3-0.6B + QLoRA，三个种子），并设置两个教师对照组（同规模非推理教师、更大的管理管道）。任务将新闻文章映射到包含短摘要和五个分类标签的JSON。评估采用盲审、无参考、三位LLM法官打分，同时对比 few-shot 提示和约束解码基线。

关键结果：学生平均延迟0.8秒（教师39秒）；摘要质量追回了基线与教师差距的58%，比约束解码高+16.8分，比 few-shot 提示高+4.9分。同规模非推理教师训练的学生与未微调基座无差别，说明摘要提升源于教师的推理特性。不同教师传递不同能力：推理教师传递写作质量，管道教师传递标签多样性；在22篇短/信息稀少的测试子集上，指令教师的学生更忠实（74分 vs 55分），推理系学生更容易虚构。最终提供按字段路由的部署方案。
