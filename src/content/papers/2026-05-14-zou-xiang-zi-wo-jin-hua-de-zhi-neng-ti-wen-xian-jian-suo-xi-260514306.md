---
title: Towards Self-Evolving Agentic Literature Retrieval
title_zh: 走向自我进化的智能体文献检索系统
authors:
- Yuwen Du
- Tian Jin
- Jing Kang
- Xianghe Pang
- Jingyi Chai
- Tingjia Miao
- Fenyi Liu
- WenHao Wang
- Sikai Yao
- Yuzhi Zhang
affiliations:
- Shanghai Jiao Tong University
- SciLand
- Zhejiang University
arxiv_id: '2605.14306'
url: https://arxiv.org/abs/2605.14306
pdf_url: https://arxiv.org/pdf/2605.14306
published: '2026-05-14'
collected: '2026-05-16'
category: Agent
tags:
- LLM
- Agent
- Literature Retrieval
- Hallucination
- Benchmark
- Self-Evolving
one_liner: 提出PaSaMaster，以自演进检索、幻觉消除排名和规划-检索分离，在1%成本下超越GPT-5.2，实现零源幻觉
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：科学文献检索面临双重困境：传统关键词系统无法理解复杂学术意图，生成式大模型虽能理解但成本高且易产生幻觉（虚构论文）。现有范式或牺牲意图理解保证源真实，或改善语义理解却失去可靠性。亟需一种既能深度理解研究意图、又能确保每篇返回文献可验证、且经济高效的方法。

**方法关键点**：
- **自演进检索**：将文献检索从一次性查询-文档匹配转变为迭代过程。Navigator代理根据查询生成检索策略和验证清单，Librarian群并行检索、评分，然后Navigator基于排名证据识别覆盖缺口、优化意图，进入下一轮检索，实现认知更新。
- **幻觉消除的意图-论文相关性排序**：不从参数记忆生成论文列表，而是从验证过的语料库（1.6亿篇论文的结构化元数据、摘要、全文块三层仓库）检索，并用基于证据块的支持进行相关性评分。训练轻量Scorer模型，对每篇论文按检查点打分并给出证据，最终得分结合平均检查点分数和校准概率，再经列表重排序。
- **成本高效的规划-检索分离**：前端LLM仅用于意图理解和策略细化，大规模检索与证据验证交由定制语料和轻量模型，工具集分为检索（语义直接检索、引文网络扩展、网页到仓库验证）和阅读（元数据查找、摘要阅读、证据块定位），避免昂贵全文阅读。
- **PaSaMaster-Bench**：首个面向复杂意图的多学科文献检索基准，包含244个任务、38个学科，每个任务有专家标注的多约束查询、检查清单和真实论文集，严格评估意图理解而非关键词匹配。

**关键实验**：在PaSaMaster-Bench上对比了词汇检索（Google Scholar）、语义检索（OpenScholar、Bohrium）、生成式LLM（GPT-5.2、Gemini-3.1-pro、DeepSeek-v3.2等）和固定流水线智能体检索（Google Scholar Labs）。PaSaMaster取得F1@20=21.69，比最强基线Google Scholar Labs（18.87）提高14.9%，比词汇检索F1提升15.6倍，比GPT-5.2（16.69）高30.0%，且零幻觉、成本仅$0.05/查询（GPT-5.2为$6.06，仅其1%）。生成式LLM幻觉率最高达37.79%。

**一句话**：文献检索的未来不在于生成更多论文，而在于让系统学会自我进化地理解研究意图，并在真实证据上排序——这能同时实现准确性、可靠性和经济性。
