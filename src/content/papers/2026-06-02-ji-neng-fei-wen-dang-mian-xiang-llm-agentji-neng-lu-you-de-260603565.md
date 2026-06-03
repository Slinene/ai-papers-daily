---
title: 'Skill Is Not Document: A Query-Conditional Benchmark and Two-Stage Retriever
  for LLM Agent Skill Routing'
title_zh: 技能非文档：面向LLM Agent技能路由的查询条件基准与两阶段检索器
authors:
- Zifei Wang
- Wei Wen
- Qiang Ji
- Ruizhi Qiao
- Xing Sun
affiliations:
- Tencent IMA Product Center
- Tencent Youtu Lab
arxiv_id: '2606.03565'
url: https://arxiv.org/abs/2606.03565
pdf_url: https://arxiv.org/pdf/2606.03565
published: '2026-06-02'
collected: '2026-06-03'
category: Agent
direction: Agent 技能检索与路由优化
tags:
- skill routing
- LLM agent
- retrieval
- skill compatibility
- dataset
- cross-encoder
one_liner: 提出保留LLM拒绝信号作为技能兼容性负监督，构建中英双语技能检索基准R3-Skill，并设计两阶段检索器精排利用该信号
practical_value: '- 构建Agent技能库时，不能简单当作文档检索，必须考虑技能间兼容性，应将前期LLM判断为“不可组合”的样本保留为负监督，用于训练精排模型。

  - 推荐采用两阶段检索：粗排用双编码器快速召回，精排用交叉编码器，并将兼容性负信号编码为分级标签（如 label=1），通过 listwise 损失优化排序。

  - 新增 Set-Compat 指标衡量检索集合的协同可用性，比单独的 recall/NDCG 更能反映 Agent 后续调用的真实成功率。

  - 双编码器阶段注入兼容性负样本效果甚微（被梯度稀释），兼容性监督应集中放在交叉编码器精排阶段，这是架构选择的实践结论。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

- **动机**：LLM Agent 通过组合多个技能完成复杂任务，技能检索是其前端关键环节。传统技能检索沿用文档检索假设（独立相关性），忽略技能间能否协同工作（skill compatibility）。现有数据合成流程丢弃了LLM判定“不可组合”的样本，丧失了兼容性负监督信号。
- **方法要点**：  
  - 提出 R3-Skill 数据集：收集95K+技能，去重得10,246个，经KMeans聚类为8个超域和40个子域；利用近邻硬约束采样生成技能组合，用LLM判断可执行性（WRITE/SKIP），保留SKIP样本并归类为8种拒绝原因。最终含41,592条accept query和32,828条reject注解，覆盖4条语言方向。  
  - 两阶段检索系统：R3-Embedding（基于Qwen3-Embedding-0.6B的bi-encoder）用InfoNCE进行粗召回；R3-Reranker（基于Qwen3-Reranker-0.6B的cross-encoder）接收embedding top-20，并引入SKIP伙伴作为兼容性分级标签（label=1），用listwise CE优化排序。  
  - 梯度分析表明SKIP信号在双编码器端因“双边平衡”效应被稀释，在交叉编码器端才有效释放。
- **关键实验**：在R3-Skill测试集上，R3-Embedding + R3-Reranker 达到 Hit@1=0.7714、NDCG@10=0.8327、Set-Compat=0.3525，其中 Set-Compat 比纯嵌入阶段提升+13.07pp。在SkillRet公开基准上同样取得竞争性成绩。消融实验确认兼容性信号仅对 cross-encoder 有效。
- **核心结论**：技能检索的联合正确性由独立相关性与查询条件下的兼容性共同决定，LLM拒绝信号可转化为有效的兼容性负监督，并仅在 cross-encoder 阶段发挥作用。
