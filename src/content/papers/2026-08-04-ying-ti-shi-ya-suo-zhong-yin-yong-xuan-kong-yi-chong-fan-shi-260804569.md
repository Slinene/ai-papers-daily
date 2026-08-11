---
title: 'Relevant but Incomplete: Referential Dangling as a Paradigm-Level Failure
  Mode in Hard Prompt Compression'
title_zh: 硬提示压缩中引用悬空：一种范式级失败模式
authors:
- Zhengpei Hu
- Kai Li
- Dapeng Fu
- Xuechao Zou
- Yuanhao Tang
- Yue Li
- Tengfei Cao
- Jianqiang Huang
affiliations:
- Qinghai University
- Tsinghua University
- Ant Group Security and Intelligence Laboratory (SIL)
arxiv_id: '2608.04569'
url: https://arxiv.org/abs/2608.04569
pdf_url: https://arxiv.org/pdf/2608.04569
published: '2026-08-04'
collected: '2026-08-11'
category: LLM
direction: LLM Prompt 压缩 · 引用完整性
tags:
- Prompt Compression
- Referential Dangling
- Multi-hop QA
- Context Pruning
- Dependency Preservation
one_liner: 独立评分式硬压缩常割裂依赖对，导致答案片段存在但推理链断裂，多跳QA中广泛发生且可恢复
practical_value: '- 在电商/推荐场景压缩用户行为序列、商品描述或对话历史时，独立评分方法易丢掉关键桥接事实，应引入共指或依存约束，保证“保留的片段能被正确解读”。

  - 对 Agent 多步推理的长上下文输入，压缩必须保留推理链上的完整证据，而非仅保留答案相关片段，否则下游模型（哪怕 GPT‑5.5）也无法弥补断裂。

  - 提出的自动恢复 pipeline 可低成本复用：训练一个小分类器判断被删句是否为保留句的必需支持，仅需增加 0.01 压缩比就能修复部分断裂，适合作为压缩后处理微调步骤。

  - 评估上下文压缩方案时，除压缩率与端到端准确率外，增加内容词覆盖或句间依赖保留指标，可尽早发现引用悬空问题。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
硬提示压缩通过独立评分选取高重要性 token/句子/块来压缩长上下文，但独立选择会割裂证据链：保留的文本片段可能依赖于已删除的前文定义或桥接事实，导致“引用悬空”。在多跳问答（QA）中，答案字符串虽然仍留在压缩后上下文中，但推理所需的中间链条已不完整。该问题是否在主流压缩器中普遍存在、能否通过同预算重选修复、以及是否可自动检测，此前未系统研究。

**方法关键点**  
- 形式化“引用悬空”：保留的任务相关句缺失任意一个最小充分支持集。证明加性评分目标无法保证支持集完整（命题1）。  
- 定义方向性内容词重叠度指标，衡量桥接例子中答案段是否保留而定义段缺失。  
- 对六种硬压缩器（基于嵌入、句法、自信息、分类器、困惑度、注意力）在 HotpotQA 桥接集上统一诊断。  
- 固定预算重选实验：将缺失的支持段落重新插入，并删除同数量非支撑段落。  
- 自动恢复训练：用 BERT 分类器判断被删句是否为保留句的必要解释，推理时重插高分候选句。

**关键实验结果**  
- 在压缩比 0.30 下，Beaver 在三个多跳 QA 数据集上让 34%~54% 的桥接例子的答案路径不完整。六种压缩器的悬空率从 32%（Beaver）到 60%（LongLLMLingua）不等。LongBench-v2 单文档 QA 中，每篇文档都至少出现一处悬空引用。  
- 固定预算重插缺失支持段使 Qwen3‑8B 准确率提升 29~34 个百分点（p<10⁻⁴），恢复至少 88% 的完整证据精度，且上下文更短。更强模型（GPT‑5.5、GLM‑5.2）也无法消化此损失：MuSiQue 上 GPT‑5.5 完整证据比悬空高 8.8 点。  
- 自动恢复分类器仅增加 0.01 压缩比，在 HotpotQA 上提升 Qwen3‑8B 准确率 4.7 点（p=0.022）。  

**核心结论**  
硬压缩不仅要优化相关性，还必须保证引用完整性。加性评分结构从根本上缺乏联合依赖保留机制，而依赖感知重选择可在不牺牲压缩比的前提下大幅恢复精度。
