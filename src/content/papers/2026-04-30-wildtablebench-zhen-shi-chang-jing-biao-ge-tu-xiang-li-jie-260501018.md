---
title: 'WildTableBench: Benchmarking Multimodal Foundation Models on Table Understanding
  In the Wild'
title_zh: WildTableBench：真实场景表格图像理解基准
authors:
- Junzhe Huang
- Xiaoxiao Sun
- Yan Yang
- Yuxuan Hou
- Ruotian Zhang
- Sirui Li
- Hehe Fan
- Serena Yeung-Levy
- Xin Yu
arxiv_id: '2605.01018'
url: https://arxiv.org/abs/2605.01018
pdf_url: https://arxiv.org/pdf/2605.01018
published: '2026-04-30'
collected: '2026-05-17'
category: Eval
direction: 多模态表格理解评估基准
tags:
- Multimodal
- Table Understanding
- Benchmark
- Visual QA
- Real-world Images
- Structural Reasoning
one_liner: 首个针对自然场景表格图像的问答基准，暴露多模态模型在结构感知与数值推理上的严重缺陷
practical_value: '- 电商客服/运营中常需解析用户上传的汇款单、报价表等复杂表格图像，WildTableBench 的诊断分析（如合并单元格、嵌套结构导致的感知失败）直接提示出需要增强的视觉结构解析模块。

  - 可借鉴其标注的 17 种子问题类型（如跨行/跨列表格查询、算术推理）设计内部评估集，针对性评估自研多模态模型在真实表格 QA 上的鲁棒性，避免仅用纯文本或干净渲染表格评估导致的虚假信心。

  - 模型对比结果显示，即使是 GPT-4o 等最强闭源模型在数值推理上仍有明显短板，业务落地时建议结合显式 OCR 结果与结构化解析做后处理（如先转 Markdown
  再查询），而非直接依赖端到端问答。

  - 基准基于高信息密度表格（平均 15.7 行 × 6.2 列），对电商场景中常见的商品规格表、财务报表截图极具代表性，可直接作为领域微调数据的风格参考。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**
当前表格理解评测多基于结构化文本表格或干净渲染图像，忽略了真实场景中表格图像布局多样、背景复杂、领域广泛的特点。为此，提出 WildTableBench——首个针对自然场景表格图像的问答基准。

**方法关键点**
从在线论坛和网站收集 402 张高信息密度表格图像（平均 15.7 行 × 6.2 列），涵盖金融、科技等 7 个领域。人工标注并验证 928 个问题，划分为 5 大类 17 子类，包括结构定位、数值推理、跨单元格查询等。基于此基准，对 21 个前沿闭/开源多模态基础模型进行全面评估与诊断分析。

**关键结果**
仅一个模型（GPT-4o）超过 50% 准确率，其余模型在 4.1%–49.9% 之间。分析揭示模型在复杂结构感知（如合并、嵌套表头）和多步数值推理上存在系统性缺陷，尤其在需要空间定位的问题上表现极差。这些发现为表格图像理解指出了明确的改进方向。
