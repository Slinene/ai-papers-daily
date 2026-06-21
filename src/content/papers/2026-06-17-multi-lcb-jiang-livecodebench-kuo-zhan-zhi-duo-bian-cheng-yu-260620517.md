---
title: 'Multi-LCB: Extending LiveCodeBench to Multiple Programming Languages'
title_zh: Multi-LCB：将 LiveCodeBench 扩展至多编程语言的代码生成评估基准
authors:
- Maria Ivanova
- Pavel Zadorozhny
- Rodion Levichev
- Ivan Petrov
- Adamenko Pavel
- Ivan Lopatin
- Alexey Kutalev
- Dmitrii Babaev
affiliations:
- GigaCode
- Yandex School of Data Analysis, Applied AI Institute
arxiv_id: '2606.20517'
url: https://arxiv.org/abs/2606.20517
pdf_url: https://arxiv.org/pdf/2606.20517
published: '2026-06-17'
collected: '2026-06-21'
category: Other
direction: 多语言代码评估基准构建
tags:
- Code Generation
- Multilingual
- Benchmark
- LLM Evaluation
- Contamination
- Overfitting
one_liner: 将 LiveCodeBench 扩展到 12 种编程语言，揭示 LLM 跨语言代码生成的过拟合与污染问题
practical_value: '- **多语言任务等价转换方法**：通过翻译 Python 任务到其他语言并保持评估协议一致，可借鉴用于构建多语言推荐系统的等价测试集，例如将用户查询或物品描述转为多种语言，验证跨语言推荐的一致性。

  - **模型过拟合检测**：对比模型在 Python 与其他语言的性能差异，发现 Python 过度拟合；在推荐系统中，可通过类似手法分析模型是否过度依赖特定模态或高频特征，识别训练数据偏置。

  - **污染感知评估设计**：使用时间戳过滤任务，避免训练集污染，该机制可直接用于推荐基准的版本管理，确保评测的公平性和时效性。

  - **多语言性能差距分析**：暴露的多语言性能鸿沟提示在训练多模态 / 多语言推荐模型时，需平衡各语言的数据配比，并在评估中纳入多语言维度以指导模型优化。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：LiveCodeBench (LCB) 已成为评估 LLM 代码生成能力的主流基准，但仅支持 Python，无法反映模型在真实软件工程中处理多语言的需求。

**方法关键点**：提出 Multi-LCB，将 LCB 的 Python 竞赛编程任务通过语言翻译与等价性验证转为其他 11 种编程语言的任务，保留原始 LCB 的污染控制（按发布时间过滤）和测试框架。同时兼容 LCB 的未来更新，实现自动扩展。

**关键结果数字**：评估 24 个指令与推理型 LLM 后，发现：① 所有模型在非 Python 语言上平均 pass@1 下降 15-30%，暴露严重的 Python 过度拟合；② 部分模型在特定语言（如 C++）出现异常高分，揭示语言特定数据污染；③ 小模型（<7B）在多语言任务上退化尤为明显，与 Python 性能的 Spearman 相关性仅 0.67，表明 Python 能力无法线性外推至多语言。
