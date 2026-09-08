---
title: 'Enoki: Efficient Multi-Level Hallucination Detection'
title_zh: Enoki：高效的多层次幻觉检测
authors:
- Elisei Rykov
- Timur Ionov
- Nikolay Ivanov
- Maksim Savkin
- Maksim Makarenko
- Alexander Panchenko
- Vasily Konovalov
- Julia Belikova
arxiv_id: '2609.00581'
url: https://arxiv.org/abs/2609.00581
pdf_url: https://arxiv.org/pdf/2609.00581
published: '2026-08-31'
collected: '2026-09-08'
category: Eval
direction: 幻觉检测 · 多粒度事实校验
tags:
- hallucination detection
- Open IE
- fact verification
- span localization
- LLM evaluation
one_liner: 提出 Enoki 开放信息抽取框架，借助文本锚定事实验证与投影，同时完成 claim 级验证和 span 级定位，资源更少定位更优
practical_value: '- 借鉴 Enoki 的共享表示：用一次 Open IE 抽取得到文本锚定三元组，同时输出 claim 级事实校验和 span
  级风险片段定位，避免分别部署两套系统，适合电商商品描述、营销文案等生成内容的实时事实性校验。

  - 工程上采用多后端设计，LLM-based、encoder-based、rule-based 抽取器统一接口，便于按场景在准确率与推理成本之间切换：高价值场景用
  LLM 抽取保障精度，低延迟批量场景用 encoder 或规则。

  - 将未支持三元组投影回原 span，可直接用于前端高亮或解释，提升 Agent 输出可解释性与用户信任，例如客服回答中高亮存疑片段。

  - EnokiQA 数据集提供 claim 与 span 对齐标注，可用于微调内部小模型或评测幻觉检测模块，降低自建标注成本。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：LLM 在高风险场景部署需要可靠的事实性保障，但现有幻觉检测通常在单一粒度上操作：claim 级方法提供可解释的事实单元，span 级方法定位未支持文本。桥接两种视图成本高，LLM 重型流水线需要多次分解与验证调用，模块化系统则需要额外的 claim-to-span 对齐。

**方法关键点**：Enoki 是一个开放信息抽取（Open IE）框架，用于多层次幻觉检测。它提取文本锚定的关系事实，与证据进行验证，并将未支持的事实投影回幻觉 span。该共享表示使 claim 级验证与 span 级定位无需单独对齐。Enoki 支持 LLM-based、encoder-based 和 rule-based 三种抽取后端，通过统一接口在准确率与推理成本之间取得平衡。

**关键结果**：实验表明 Enoki 在使用更少资源的情况下与强 claim 级系统保持竞争力，并在细粒度 span 级和实体级定位上取得更优性能。同时发布 EnokiQA 数据集，包含对齐的 claim 级验证与 span 级定位标注。
