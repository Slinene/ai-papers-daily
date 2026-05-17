---
title: 'Falkor-IRAC: Graph-Constrained Generation for Verified Legal Reasoning in
  Indian Judicial AI'
title_zh: Falkor-IRAC：基于图约束生成的印度司法AI推理验证框架
authors:
- Joy Bose
arxiv_id: '2605.14665'
url: https://arxiv.org/abs/2605.14665
pdf_url: https://arxiv.org/pdf/2605.14665
published: '2026-05-14'
collected: '2026-05-17'
category: Reasoning
direction: 图约束生成 · 法律推理验证
tags:
- Graph-Constrained Generation
- Legal Reasoning
- Knowledge Graph
- Verifier Agent
- FalkorDB
- IRAC
one_liner: 用IRAC知识图谱约束LLM生成，通过可证伪验证器确保法律推理的引用真实与逻辑自洽
practical_value: '- **可证伪验证器（Verifier Agent）模式**：生成后由独立代理在图谱中回溯验证路径，可部署于对话推荐系统，对生成的解释或商品推荐理由进行事实核验，杜绝虚假属性拼接。

  - **知识图谱约束生成**：将领域知识结构化为节点与关系（类似商品-属性-规则图谱），生成时必须匹配图谱中的有效路径，避免LLM自由发挥产生不合规内容，适用于电商合规文案或营销话术生成。

  - **冲突检测作为一级输出**：推荐系统可借鉴，当多路召回或多目标融合产生矛盾（如“高性价比”与“高端定价”同时出现）时主动暴露，而非强行择优，提升透明度。

  - **图原生评估指标**：引用接地准确率、路径有效率等指标可迁移至推荐解释评估，衡量解释与知识库的符合程度，替代传统NLP指标，更贴合业务对可信解释的要求。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：法律推理依赖结构化符号推理（先例、法条、程序状态），当前基于向量的RAG无法可靠表示此类约束，频繁产生幻觉引用与推理链断裂，在印度等案件高负荷地区造成实质司法损害。
**核心方法**：提出Falkor-IRAC框架，将最高法院及高等法院判决自动解析为IRAC（问题、规则、分析、结论）知识图谱，节点包含程序状态转移、先例关联和法条引用，存储于图数据库FalkorDB以供低延迟遍历。生成时，LLM输出需经过Verifier Agent的可证伪验证——仅当能在图谱中找到从问题到结论的有效支持路径时才被接受；系统同时显式输出教义冲突，而非静默消解。
**关键结果**：在51个最高法院判决构成的验证集上，Verifier Agent正确验证了全部已提交查询的引用真实性，并正确拒绝了所有伪造引用；定义并应用了引用接地准确率、路径有效率、幻觉先例率等图原生指标，论证其比BLEU/ROUGE更适合法律推理评估。当前在CPU环境存在超时问题，后续将借助GPU加速并与纯向量RAG基线对比。
