---
title: No Resource, No Benchmarks, No Problem? Evaluating and Improving LLMs for Code
  Generation in No-Resource Languages
title_zh: 零资源语言LLM代码生成：评估与改进策略
authors:
- Alessandro Giagnorio
- Alberto Martin-Lopez
- Gabriele Bavota
arxiv_id: '2606.16827'
url: https://arxiv.org/abs/2606.16827
pdf_url: https://arxiv.org/pdf/2606.16827
published: '2026-06-14'
collected: '2026-06-20'
category: LLM
direction: LLM 适配零资源代码生成
tags:
- code generation
- no-resource language
- weight diff transfer
- instruction tuning
- benchmark
one_liner: 针对零资源编程语言，通过权重差异迁移法在基础模型上注入指令跟随能力，实现低成本专用代码模型部署
practical_value: '- 若业务中存在专有查询语言或领域特定语言（如内部配置DSL、搜索表达式），可以借鉴“基础模型继续预训练+权重差异迁移”的方式，低成本适配LLM，无需昂贵的指令微调

  - 在对指令跟随要求高的场景（如Agent任务规划、推荐理由生成），避免直接在指令模型上做进一步预训练，以防损害其指令能力，而是采用先预训练再注入指令能力的两阶段策略

  - 构建内部低资源语言基准时，可复用论文的基准构建思路：从有限代码库中提取函数签名、文档字符串和测试用例，自动化生成评测集

  - 该方法模型与数据均轻量，适合资源受限的团队，可用于快速验证新语言或新领域的LLM生成效果'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**  
工业界常出现自研或领域特定语言，这些语言在LLM训练数据中几乎为零（no-resource）。商业工具如GitHub Copilot无法支持，企业必须自建代码推荐器。现有研究多关注高资源语言或训练数据较多的低资源语言，而零资源场景缺乏基准和有效方法。  
**方法**  
1. 基于两种新设计的编程语言（训练数据极少）构建三个代码生成基准。  
2. 实验多种策略：少样本提示、在少量数据上继续预训练或微调。  
3. 发现继续预训练对零资源语言性能提升最大，但直接对指令微调后的模型继续预训练会破坏其指令跟随能力。  
4. 提出两阶段方案：（1）从基础模型开始，用少量目标语言代码继续预训练；（2）从某个指令模型提取指令跟随能力的“权重差异”（W = θ_instruct - θ_base），并将其叠加到上述目标语言预训练后的模型上，从而恢复指令跟随能力。  
**结果**  
在三个基准上，该方法（基础模型+语言预训练+权重差异转移）取得了最佳性能，显著超越其他方案，且避免了昂贵的指令微调成本。该方案使企业能够以低成本部署针对专有语言的专用指令模型，同时保持模型对自然语言指令的高遵循度。
