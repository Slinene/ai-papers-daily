---
title: 'Decision4Rec: A Jev-Inspired Framework of Decision Models on Knowledge and
  Active Graphs for Multi-Agent Recommender Systems'
title_zh: Decision4Rec：基于知识与活跃图谱的多智能体推荐决策模型框架
authors:
- Marco Polignano
- Het Darshan Mehta
- Pasquale Lops
- Ernesto William De Luca
- Giovanni Semeraro
affiliations:
- Università degli studi di Bari Aldo Moro
- Otto-von-Guericke University
- Leibniz Institute for Educational Media | Georg Eckert Institute
arxiv_id: '2610.26035'
url: https://arxiv.org/abs/2610.26035
pdf_url: https://arxiv.org/pdf/2610.26035
published: '2026-10-19'
collected: '2026-10-20'
category: RecSys
direction: 决策模型重排 · 多智能体候选池
tags:
- Decision model
- Multi-agent pool
- Knowledge graph
- LLM reranking
- Recommendation
- Luce model
one_liner: 将决策模型（Jev/Kev）用于推荐重排，结合场景知识图谱语句和多智能体候选池，在稀疏Amazon目录上NDCG@10提升25%-36%。
practical_value: '- 用决策模型（Kev/Jev）替代生成式LLM做重排：直接输出候选概率，确定性单次前向，便于线上校准与风险控制；用Luce模型+两次随机顺序可消除位置偏差。

  - 把场景行为编码为相对尺度语句（top 10%/often）而非原始次数，使同一个rerank模型可跨品类/新店铺复用；知识图谱计数可实时更新，无需重训。

  - 多智能体候选池中始终保留现有精排模型完整top列表，其它来源仅作为特征修正顺序，避免简单rank fusion对原有召回造成负向影响。

  - 训练rerank记录时严格防泄漏：统计特征不能包含target、不补缺失target、target所在的最后一步不能被第一阶段模型训练过；这对构建高质量推荐rerank数据很实用。

  - 训练0.8B开源决策模型即可在多数设置中打平甚至超过商业Jev，性价比高。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
生成式LLM做推荐排序存在候选顺序敏感、输出文本无概率、采样不一致、生成成本高。2026年出现的决策模型（Jev/Kev）对选项直接返回概率、确定性单次前向，天然适合推荐中的比较与重排。但直接用于推荐并不work：发布的Kev-4B重排SASRec top50只是随机水平，需要场景行为、高质量候选和真实选择训练。

## 方法关键点
- 四模块框架：知识图谱将日志写成场景相对尺度语句（如 sold top 10%、follow-up often），无训练；多智能体池收集候选并保留精排模型列表；决策模型用统一typed question接口输出选项概率；Luce选择模型+残差score融合排序。
- 知识图谱语句使用相对尺度而非原始计数，让跨场景复用成为可能；每条行为家族对应一个无训练强基线信号（流行度、趋势、序列规则、共现、内容相似）。
- 多智能体池中，训练好的SASRecF作为agent之一，其它agent提供follow-up、co-purchase、text similarity、recent popularity等列表；残差ranker仅修正顺序并保30，不会破坏原有召回。
- 训练决策模型Kev（0.8B/4B/9B/27B）用LoRA+choice head，训练记录来自三个源域的真实下一次选择；三条防漏规则：统计不含target、不添加缺失target、reranker训练的target不能被第一阶段模型学过的最后一步。
- 推理时同一选择问两次随机顺序，用Luce模型消位置偏差，得到各候选worth；最终与residual ranker分数标准化融合。

## 关键结果
- Decision4Rec-Full(4B) 在 Video Games 和 Musical Instruments 上 NDCG@10 比最佳训练基线高25%和36%；Steam密集场景与基线持平（+1~2%不显著）。
- 增益主要来自multi-agent pool：residual ranker alone 已经+17%/+26%；4B决策模型在池上再加7%/8%（显著）。
- 无训练推荐器的Decision4Rec-KG达到训练基线NDCG@10的81~92%，展示冷启动/新品类潜力。
- 在完全未训练的MovieLens-1M域增益5~7%；训练0.8B开放模型在11/15设置中胜于商业Jev且从不更差。

最值得记住：决策模型+场景相对行为语句+多智能体池，是稀疏目录上比生成式LLM更可靠、更便宜的LLM重排路径。
