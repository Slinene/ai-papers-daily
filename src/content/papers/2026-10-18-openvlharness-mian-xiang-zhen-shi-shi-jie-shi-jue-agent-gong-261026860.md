---
title: 'OpenVLHarness: Real World Visual Agentic Tool-Use with Multimodal Memory'
title_zh: OpenVLHarness：面向真实世界视觉 Agent 工具使用的多模态记忆
authors:
- Yu Zhou
- Cheng-Fu Yang
- Rui Sun
- Di Wu
- Sibo Peng
- Mingyang Zhang
- Zhen Yang
- Ruiyi Zhang
- Nanyun Peng
- Zhe Gan
affiliations:
- University of California, Los Angeles
- Apple
arxiv_id: '2610.26860'
url: https://arxiv.org/abs/2610.26860
pdf_url: https://arxiv.org/pdf/2610.26860
published: '2026-10-18'
collected: '2026-10-20'
category: Agent
direction: 多模态 Agent 工具调用与记忆增强推理
tags:
- Multimodal LLM
- Tool Use
- Memory
- Agent
- Visual Reasoning
one_liner: 通过能力层与持久多模态记忆统一工具输出，多模态 LLM 在 22 个基准上平均提升 9.7-12.6 分
practical_value: '- 电商多模态购物助手中，可借鉴 capability layer + evidence rendering 将商品搜索、图像识别、价格/库存等异构工具输出统一转成结构化
  observation，减少模型解析成本。

  - persistent multimodal memory 按地址存储商品图、结构化数据、网页引用，支持多轮对话跨步骤引用，避免重复调用工具，适合商品对比、搭配推荐等需要持续上下文的任务。

  - coding interface 对存储数据执行生成式程序，可用于多源数据联合计算，如比价、价格历史分析、风格一致性判断，把多个工具结果组合成可执行逻辑。

  - 成本收益结论：中等推理 effort + 工具记忆比高 effort 纯推理更优且 token 成本低至 37%，提示业务 Agent 优先做工具集成而非一味增加推理预算。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：多模态 LLM 在视觉推理上提升受限于内部推理，22 个基准控制实验显示仅增加推理预算收益有限，需要外部工具获取接地感知、外部知识与数值测量。

方法关键点：OpenVLHarness 由 capability layer 与 persistent multimodal memory 组成。capability layer 组合任务级工具接口与证据渲染，统一异构后端输出并转为模型可读 observation；persistent multimodal memory 把对应图像、结构化数据和 web 引用保存为可寻址 artifacts，贯穿每个 query；coding interface 在存储数据上执行生成程序，组合多个工具结果进行数值计算。该机制支持迭代获取、检查和组合多模态证据。

关键结果：在 22 个基准、8 个开源/闭源骨干上，平均提升 9.7-12.6 分（Qwen3-VL-8B +11.2，Kimi K3 +9.7，GPT-6 Astra +9.9）。用 GPT-6 Luna 中等推理 effort 超过 base model、Codex、Visual Sketchpad 最大 effort 7.7-8.5 分，且模型 token 成本至多 37%。
