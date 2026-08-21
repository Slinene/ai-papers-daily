---
title: Temporal Multi-Signal Fusion for Token-Level Hallucination Detection
title_zh: 时序多信号融合的Token级幻觉检测
authors:
- Igor Itkin
affiliations:
- Independent Researcher
arxiv_id: '2608.18115'
url: https://arxiv.org/abs/2608.18115
pdf_url: https://arxiv.org/pdf/2608.18115
published: '2026-06-29'
collected: '2026-08-21'
category: Eval
direction: LLM 幻觉检测 · 多信号时序融合
tags:
- hallucination detection
- RAG
- BiGRU
- multi-signal fusion
- token-level
- RAGTruth
one_liner: 用 BiGRU 序列标注融合文本统计、NLI 蕴含与 LM surprisal，在 RAGTruth 上幻觉检测 AUC 达 0.840，比独立基线高
  11 点
practical_value: '- 在电商 RAG 或 Agent 生成商品描述、推荐理由、客服回答时，可加一个轻量 Token 级幻觉检测器：只用生成文本 +
  外部信号（文本统计、NLI entailment、LM surprisal），不需要模型内部 logits，适合闭源 LLM（如 GPT-4、Kimi）接入。

  - 把幻觉检测从独立 token 分类改为序列标注：用 BiGRU 对 token 序列建模，证据能从高置信位置传播到邻近模糊 token，明显优于逐 token
  独立打分。业务上可对生成的推荐文案逐 span 判断可信度，而不是只给句子级分数。

  - 特征集可复用：文本统计 + NLI entailment + LM surprisal 的 33 维特征，实现简单、成本低，可快速在自有 RAG 场景验证。作者发现架构（BiGRU/Mamba/Attention）不是瓶颈，特征集才是天花板（AUC
  ≈0.845），提醒我们优先投入特征工程。

  - 跨模型泛化好：在未见过的生成模型上 AUC 损失 <4%，意味着训练一个检测器可以覆盖多个上游 LLM，适合业务中多模型并存的场景，减少重复标注。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**  
现有 token 级幻觉检测通常只用单一信号对每个 token 独立评分，当生成模型对错误内容高度自信时容易失效。幻觉往往不是孤立 token，而是连续 span，需要利用上下文时序信息。  

**方法关键点**  
将幻觉检测定义为序列标注任务：每个 token 对应一个 33 维特征向量，融合文本统计特征、NLI 蕴含分数、LM surprisal，不依赖模型内部状态。用 BiGRU 对 token 特征序列建模，输出 token 级幻觉概率。仅需生成文本和外部信号，适用于闭源模型。  

**关键结果数字**  
在 RAGTruth 数据集上，BiGRU 检测器 AUC 达到 0.840（10 个随机种子平均），比独立逻辑回归基线提升 11 个点（Wilcoxon signed-rank p=0.002）。受控分解实验显示，大部分增益来自时序顺序建模而非模型容量。进一步实验发现，BiGRU、Mamba、Attention 架构的 AUC 天花板都在 0.845 附近，说明瓶颈在特征集而非模型结构。在未见过的生成模型上测试，AUC 仅下降不到 4%，跨模型泛化能力强。
