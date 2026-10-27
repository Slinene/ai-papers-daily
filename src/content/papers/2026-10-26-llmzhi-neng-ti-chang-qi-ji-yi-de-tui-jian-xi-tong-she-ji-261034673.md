---
title: 'Agent Memory as Recommendation: Recommender-System Design for Long-Term Memory
  of LLM Agents'
title_zh: LLM智能体长期记忆的推荐系统设计
authors:
- Xinyu Zhang
- Weiwei Sun
affiliations:
- Fudan University
arxiv_id: '2610.34673'
url: https://arxiv.org/abs/2610.34673
pdf_url: https://arxiv.org/pdf/2610.34673
published: '2026-10-26'
collected: '2026-10-27'
category: Agent
direction: Agent长期记忆 · slate推荐级联
tags:
- Agent Memory
- Slate Recommendation
- Learning to Rank
- Candidate Generation
- Context Selection
- Cost-Efficient
one_liner: 把Agent记忆选择形式化为预算约束下的slate推荐，零LLM调用匹配64次重排且服务成本降3.2倍
practical_value: '- 把记忆/上下文选择形式化为预算slate推荐：召回+学习排序+固定预算填充，可迁移到电商Agent客服、导购的多轮历史筛选，或搜索广告的query上下文优选；比动态截断更稳。

  - 零LLM调用链路可落地：BM25+dense embedding双通道召回，RRF融合top128，LightGBM LambdaRank用10个轻量特征（相似度、排名、位置、长度、共享key等）排序，再按token预算贪心填充，写时无LLM成本，适合高QPS生产环境。

  - 用stage factorization定位瓶颈：Acc = ai + (ac-ai)*r_pool*r_rank，先看候选池覆盖率，再看排序是否把证据放进budget；这能避免盲目换模型，直接发现是召回还是排序导致证据丢失。

  - 固定预算填充优于per-query cutoff：当reward沿排序不下降时，任何cutoff都包含于fill，所以Adaptive-k类动态截断只会降低覆盖率；若存在低质量文档的负外部性，才需要set-level模型，否则别用动态截断。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
LLM Agent在多会话服务中，每个请求都要从庞大且持续增长的长期记忆里选出少量进入有限上下文窗口。这个选择直接决定回答正确性：上下文漏掉证据turn，准确率下降37-64个点。该问题有三个与推荐系统相同的性质：大规模目录、每请求成本预算、价值在整张slate上评估。论文将其形式化为预算约束下的slate推荐，把记忆构建、召回、排序、上下文组装统一到一个设计空间。

## 方法关键点
- **形式化**：请求=用户，存储turn=item，上下文窗口=slate，token预算=约束；目标最大化judge接受概率。
- **设计空间**：memory construction → candidate generation → ranking → context assembly四级联；每个系统是该空间中的一个点。
- **关键结论**：
  - Stage factorization: Acc = ai + (ac-ai)·r_pool·r_rank；性能瓶颈可被定位。
  - 在证据独立且reward不随填充下降时，item-wise ranking归约为0-1背包，最优slate按证据概率排序后填满预算。
  - 固定预算填充包含任何可fit的前缀cutoff，因此优于动态截断。
- **AgentMemRec**：零LLM调用。候选生成用BM25+bge-m3余弦双通道，RRF融合top128；排序用LightGBM LambdaRank，10个特征（5相关性+5 turn上下文），标签是gold证据turn；slate构造按token增量贪心填充到2700 tokens。

## 关键结果
- LongMemEval-S（κ≥2，n=209）：AgentMemRec准确率80.7（Qwen）/89.4（DeepSeek），比Adaptive-k、DynamicRAG、HippoRAG2、A-Mem、T-Mem高10.4-31.2点；比64次LLM调用的reranker（Ref）成本低3.2倍，准确率持平。
- LongMemEval-M：70.0/81.3，比baselines高10.6-33.3点。
- LoCoMo：77.0，与T-Mem复现77.4持平，超过Mem0、Zep、MemOS，写时零LLM调用。
- slate完整性0.94，远高于HippoRAG2/A-Mem的0.50；候选池覆盖率0.981，排序后完整性0.959。

## 最值得记住的一句话
把记忆选择当推荐级联：先用宽候选池和轻量学习排序保证证据覆盖，再用固定预算填充，就能以零LLM调用达到甚至超过重型LLM记忆系统的效果。
