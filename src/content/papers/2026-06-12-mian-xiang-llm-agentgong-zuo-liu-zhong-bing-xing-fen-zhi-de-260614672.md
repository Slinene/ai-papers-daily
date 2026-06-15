---
title: Towards Direct Latent-Space Synthesis for Parallel Branches in LLM-Agent Workflows
title_zh: 面向LLM-Agent工作流中并行分支的直接隐空间合成
authors:
- Shikun Liu
- Mufei Li
- Dongqi Fu
- Haoyu Wang
- Yinglong Xia
- Hong Li
- Hong Yan
- Pan Li
affiliations:
- Georgia Institute of Technology
- Meta
arxiv_id: '2606.14672'
url: https://arxiv.org/abs/2606.14672
pdf_url: https://arxiv.org/pdf/2606.14672
published: '2026-06-12'
collected: '2026-06-15'
category: MultiAgent
direction: Multi-Agent 并行合成 · KV cache 复用
tags:
- LLM-Agent
- Multi-Agent
- KV cache
- Latent Communication
- Synthesis
- Parallel Workflow
one_liner: 让合成器直接消费并行Worker的KV cache，通过两阶段训练和cache映射实现高效高质量的并行分支汇总
practical_value: '- **用KV cache替代文本串联进行Agent间通信**：在并行子Agent完成推理后，直接复用其KV cache，避免重新编码文本前缀，大幅降低TTFT。对电商客服、多工具调用等并行任务可显著提升响应速度。

  - **两阶段训练策略值得借鉴**：先通过大规模并行上下文对话数据做通用适应（Track 1），再通过蒸馏文本合成轨迹获得推理能力（Track 2），最后合并checkpoint而非顺序微调，能避免遗忘并平衡泛化与推理。这在需要同时处理简单汇总和复杂判断的推荐/问答系统中可复用。

  - **可学习的Cache Mapper + LoRA组合**：使用MLP根据分支数、长度生成仿射校准系数，配合LoRA适配，让模型适应非顺序的cache输入。工程上成本低，可作为即插即用模块接入现有的并行Multi-Agent流程。

  - **轨迹信息选择对效率敏感**：实验表明只传worker的final output能实现最佳准确率-延迟折衷，传完整轨迹虽准确率高但开销大。在电商推荐Agent中，可优先压缩子Agent输出为简洁摘要再合成，避免完整交互历史的重传。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**  
LLM Agent工作流中常见的并行分支后合成（如多方案生成、多工具调用）通常需要将各分支的文本输出串接后重新编码供合成器使用，这既丢失了原有的DAG结构，又产生重复的prefill计算。随着Agent系统越来越倾向非顺序执行，直接复用worker的KV cache进行合成成为自然的加速方向，但多分支cache的并行输入与模型默认的顺序上下文接口不兼容。  
**方法**  
- **Parallel-Synthesis框架**：对worker输出的KV cache进行位置重编码（统一对齐到分支点后），再通过可学习的**Cache Mapper**（MLP根据分支长度和数量预测逐层仿射参数）校准，最后配合**合成器LoRA**从非顺序cache生成回复。  
- **两轨训练与合并**：Track1使用大规模对话数据和并行工具调用、多文档QA等构造“并行上下文”进行通用适应；Track2从BrowseComp等数据中蒸馏文本合成轨迹，强化复杂推理的合成能力。两轨独立训练后通过权重平均合并，避免顺序微调导致的能力覆盖。  
**关键实验**  
在数学、科学QA、代码、GAIA和MARBLE数据库诊断共9个数据集上，Parallel-Synthesis在7个上匹配或超过文本串联合成（仅GAIA Level 2、3和MBPP-Plus略低），同时将Time-to-First-Token降低2.5–11倍。消融表明合并训练优于单轨或顺序训练，Cache Mapper与LoRA协同作用突出。  
**核心结论**  
直接利用并行KV cache进行合成是可行且高效的，通过针对性训练能让模型学会从隐状态聚合多路信息，尤其擅长推理密集型任务；这为构建原生支持DAG执行的Agent系统提供了新接口。
