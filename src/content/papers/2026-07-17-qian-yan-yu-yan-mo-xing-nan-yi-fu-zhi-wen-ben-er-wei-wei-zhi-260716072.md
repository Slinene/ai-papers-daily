---
title: 'Frontier Language Models Struggle to Copy: Text Can Be Better Viewed in 2D'
title_zh: 前沿语言模型难以复制文本：二维位置编码或更优
authors:
- Haodong Wen
- Yiran Zhang
- Yingfa Chen
- Kaifeng Lyu
affiliations:
- Tsinghua University
arxiv_id: '2607.16072'
url: https://arxiv.org/abs/2607.16072
pdf_url: https://arxiv.org/pdf/2607.16072
published: '2026-07-17'
collected: '2026-07-20'
category: LLM
direction: 位置编码改进 · 复制保真度
tags:
- 2D-RoPE
- Positional Encoding
- Copy Task
- Length Generalization
- Transformer
one_liner: 提出2D-RoPE将文本组织为二维网格，大幅提升LLM复制任务的长度泛化能力
practical_value: '- 在需要高精度复制长文本的电商/广告场景（如生成商品描述、广告文案、搜索查询改写），可尝试用2D-RoPE微调或从零训练，缓解模型输出错漏、幻觉问题。

  - 基于LLM的Agent常需记忆并精确复制对话历史或工具输出中的关键信息，2D-RoPE可增强位置感知，提升指令遵循与信息保真度。

  - 当业务中涉及结构化数据转换（如JSON、列表生成），模型常忽略细节或格式错误，2D-RoPE的网格复制机制可提升格式遵循能力。

  - 若将LLM用于推荐理由生成，需准确复现用户历史中的物品名、属性，2D-RoPE有望提高复制的精确率，但需在具体任务上验证。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：即使GPT-4等前沿模型，在简单复制任务（如重复二进制串、转换Python列表）上仍频繁失败，根源在于Transformer的位置编码偏向通过局部上下文匹配走捷径，而非精确定位源位置。这制约了LLM在需要精确复制的场景中的可靠性。

**方法关键点**：
- 提出2D-RoPE，将一维文本序列折叠成二维网格，每个token获得行、列两个位置ID，分别用RoPE编码。此时复制任务退化为在固定列偏移处取输入token，模型只需学习“同一列偏移”的注意力模式，极大简化了任务。
- 具体实现：沿行方向折叠，列数作为超参数；注意力计算时同时使用行、列编码，模型可自然关注同列位置的token。

**关键结果**：
- 合成实验：4层Transformer+2D-RoPE在复制长达4000个token的二进制串时达到100%准确率，而标准RoPE在训练外长度上完全失效；2D-RoPE成功泛化到训练长度数百倍的输入。
- 大规模验证：在DCLM数据集上用1.4B参数训练语言模型，2D-RoPE在复制任务上的困惑度显著低于RoPE基线，且对语言建模困惑度无明显负面影响，表明二维视角可能带来通用建模收益。
