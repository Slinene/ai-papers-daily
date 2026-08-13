---
title: 'Information Abundance Paradox: Long-Context Training Undermines Parametric
  Knowledge'
title_zh: 信息丰度悖论：长上下文训练削弱参数化知识
authors:
- Arda Uzunoglu
- Benjamin van Durme
- Daniel Khashabi
affiliations:
- Johns Hopkins University
arxiv_id: '2608.12218'
url: https://arxiv.org/abs/2608.12218
pdf_url: https://arxiv.org/pdf/2608.12218
published: '2026-08-12'
collected: '2026-08-13'
category: Training
direction: 长上下文训练中参数化与上下文化的权衡
tags:
- long-context
- parametric knowledge
- context addiction
- gradient allocation
- LLM pretraining
- SFT
one_liner: 提出信息丰度悖论：训练上下文越丰富，模型越依赖上下文而非参数知识，导致长上下文训练并非中性增益
practical_value: '- 在电商搜索/推荐中用 LLM 建模用户行为序列时，盲目拉长训练上下文可能让模型过度依赖近期上下文，削弱对长期兴趣的参数化表达；建议通过无上下文/冲突上下文测试评估模型鲁棒性，找到最优上下文窗口而非一律用最大长度。

  - 微调推荐/Agent 模型时，若训练集中大量提供高质量候选上下文（如检索文档、相似商品），模型容易“上瘾”于上下文。可在微调时混合一定比例无上下文或含噪声上下文的样本，迫使模型同时保留参数知识。

  - LoRA 适配器放置位置可以调节学习模式：希望模型更多依赖参数知识（如长期用户画像）则倾向于只更新 FFN 层；希望模型更好利用上下文（如对话历史）则更新
  Attention 层。可根据业务需求选择模块化微调策略。

  - 在 RAG 或长上下文生成式推荐中，性能可能随上下文长度呈倒 U 型；建议在验证集上搜索最优上下文长度，并监控模型在上下文缺失或误导时的衰减程度，避免部署后出现脆弱性。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**
LLM 大量使用长上下文（文档、代码库、交互历史），业界默认更长的训练上下文只会带来好处。然而，Phi-3 128K 变体相对 4K 变体在 MMLU/BBH/MCQA 上普遍下降（如 3.8B zero-shot MMLU 下降 3.5%），OLMo 3 65K 相对 8K 也有类似现象。这表明长上下文训练可能并非中性数据通道，而是改变了模型的学习模式。

**方法关键点**
- 提出**信息丰度悖论**：当训练上下文中任务相关信息丰富时，模型会降低在参数中编码该信息的动力，转向直接利用上下文，导致测试时对上下文依赖增强（context addiction）。
- 预训练实验：Llama-2 架构，10B tokens 来自 Project Gutenberg 长文档，固定 token 预算与优化步数，上下文窗口从 512 到 32768 变化，模型规模 20M/55M/259M/750M。评估零样本语言建模、SuperGLUE、闭卷 MCQA。
- 监督微调实验：Qwen3 0.6B-14B，LoRA 微调 MMLU-Pro 四个领域，固定上下文长度 n=8 文档，改变目标域文档数 k=0/4/8，测试支持/冲突/无上下文三种条件。
- 机制分析：合成任务（位运算、字符串、模10算术、凯撒密码），比较训练梯度范数；计算 FFN/SA 梯度比；模块限制微调（仅更新 FFN 或 SA）；测试时注意力分配。

**关键实验结果**
- 预训练中 SuperGLUE 和 MCQA 性能随上下文窗口呈倒 U 型，峰值约 2048 tokens；语言建模损失 U 型，峰值约 8192 tokens。扩大模型规模不改变趋势。
- SFT 中，k=8 相比 k=0 提升有支持上下文时的准确率，但无上下文准确率明显下降，且更易受冲突上下文误导（例如 Qwen3-4B 无上下文从约 51.7% 降至约 48.8%）。
- 机制上，长上下文训练使 FFN/SA 梯度比下降，注意力更集中于上下文 token；FFN-only 微调提升参数鲁棒性，SA-only 微调增强上下文依赖。

**最值得记住的一句话**：长上下文训练不是中性的数据通道，信息丰富的上下文会削弱参数化知识，导致模型在上下文缺失或误导时表现变差。
