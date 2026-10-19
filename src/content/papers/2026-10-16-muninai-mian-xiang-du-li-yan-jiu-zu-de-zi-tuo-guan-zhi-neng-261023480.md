---
title: 'MuninAI: A Self-Hosted Agentic Framework for Independent Research Groups'
title_zh: MuninAI：面向独立研究组的自托管智能体文献问答框架
authors:
- Markus Fischer
- Jens Meiler
- Matthias Elgeti
affiliations:
- Institute for Drug Discovery, Leipzig University Medical School
- Institute for Medical Physics and Biophysics, Leipzig University Medical School
- Integrative Center for Bioinformatics, Leipzig University
- Center for Scalable Data Analytics and Artificial Intelligence (ScaDS.AI)
- School of Embedded Composite Artificial Intelligence (SECAI)
arxiv_id: '2610.23480'
url: https://arxiv.org/abs/2610.23480
pdf_url: https://arxiv.org/pdf/2610.23480
published: '2026-10-16'
collected: '2026-10-19'
category: Agent
direction: Agent 科学文献问答 · RAG 工具编排
tags:
- Agent Harness
- RAG
- Open-weight LLM
- Citation Graph
- Self-hosted
- Evaluation Suite
one_liner: 开源自托管 Agent 框架将开放权重模型与检索、阅读、计算工具编排，使文献问答准确率翻倍且几乎不产生幻觉
practical_value: '- 工具编排优先于换模型：在商品知识库问答、广告素材核查、客服辅助等场景，先设计 reading/search/computation
  工具与 agent harness，而不是直接换更大模型；评测时固定 backbone，对比 naive RAG 与 harness 的差距。

  - 引入 citation/relation graph：将商品关系、内容引用、品牌-属性等构建成可检索的 graph，供 agent 多跳导航；要求每个答案声明可溯源，降低生成式推荐中的虚构商品
  ID 或属性风险。

  - 主动弃权机制：当知识库缺少对应商品、属性、政策时让系统返回“未知/不提供”，避免生成式推荐编造价格、卖点或库存；可设置证据缺失阈值来触发弃权。

  - 自托管与单卡基线：对未公开的选品、竞价、用户数据，可选用开源 20B 级模型本地部署；发布一键评测脚本，在自己的语料和模型上重跑，作为上线门槛。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

动机：研究组需要让 LLM 基于自己的文献库回答问题，但托管服务会接触未发表工作，自托管部署又无法访问语料。Munin 是一个开源自托管科学助手框架，索引小组语料和引用图，并用 agent harness 包装任意开放权重模型，提供专门的阅读、搜索和计算工具。

方法关键点：核心不是特定模型，而是 harness 的工具编排与状态机；通过引用图增强检索，支持多跳导航和证据溯源；当语料缺失答案时可主动弃权；评测套件随软件发布，一条命令即可在自有语料和模型上重跑。

关键结果：在 199 对文献问题上，harness 使基础模型准确率从 0.387 提升到 0.874（+0.487，95% CI [0.407, 0.568]）；naive retrieve-then-answer 在所有 backbone 上均低于无辅助模型；约两倍答案主张可追溯到模型自己读取的段落；移除源论文后，Qwen backbone 约九成、gpt-oss-20b 八成正确问题会弃权；300 个虚构引用中未产生任何虚构本地引用。该模式在三个 backbone（两个开发者）上成立，包括单张消费级 GPU 可跑的 20B 模型；断网条件下 Qwen backbone 仍超过 PaperQA2。
