---
title: 'MemoryAthena: Adaptive Routing over Latent and Generated Memories'
title_zh: MemoryAthena：潜在记忆与生成记忆的自适应路由
authors:
- Mingyuan Li
- Guangsheng Yu
- Juyuan Zhang
- Xu Wang
- Zhibo Man
- Haonan Zhang
- Shaoxiong Ji
affiliations:
- ELLIS Institute of Finland
- University of Turku
- University of Technology Sydney
- University of Science and Technology of China
- Shanghai Jiao Tong University
arxiv_id: '2609.25853'
url: https://arxiv.org/abs/2609.25853
pdf_url: https://arxiv.org/pdf/2609.25853
published: '2026-09-21'
collected: '2026-09-25'
category: RAG
direction: 记忆增强 LLM · 检索与生成记忆自适应路由
tags:
- memory-augmented LLM
- adaptive routing
- retrieval vs generation
- learned memory
- lightweight routing head
one_liner: 冻结骨干下训练轻量因果路由头，以 Engram 检索为锚对生成记忆做有界插值干预，QA/NLP 多任务平均提升
practical_value: '- 在 RAG / 记忆增强推荐或 Agent 系统中，可把直接检索结果作为 anchor，生成式候选只做有界插值；当路由判断收益为负或不显著时回退到检索结果。这种“拒绝即恢复
  baseline”的设计适合线上安全上线，避免生成内容污染原始记忆。

  - 冻结大模型主干，仅训练轻量因果路由头，用反事实未来 token 似然优势作为监督信号。业务上可对用户/商品记忆的多路候选（如 item embedding、LLM
  生成的用户兴趣 summary、序列隐状态）训练一个小 router 决定选用或融合，无需微调主模型。

  - GE 和 GH 的分离值得借鉴：一路从检索到的线索生成，一路直接从模型 contextual state 生成。推荐场景可分别对应“基于召回的候选生成”与“基于用户序列隐状态的候选生成”，并让
  router 在两者之间选择或插值。

  - 论文中的 oracle 互补分析提示：多路记忆虽然真实路由头不能完全释放上限，但可离线构造 gold-label oracle 评估各路潜在价值，再决定是否投入训练更复杂的
  router。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：学习式记忆通常只做检索读取，但有用表示能否被生成？生成记忆在不同上下文可能互补也可能干扰，因此需要学习何时、哪条路径、多强地干预。

**方法关键点**：MemoryAthena 设三条通路：直接 Engram 检索 E、从检索线索生成 GE、不查表从主干因果状态生成 GH。冻结主干、记忆、生成器与 reader，仅训练轻量因果路由头；用 GE/GH 相对 E 的反事实未来 token 似然优势做监督。推理时，被接受候选通过有界插值修改 E 残差，拒绝则完全恢复 E。

**关键结果**：QA 五任务平均 37.65→39.28，通用 NLP 六任务平均 76.73→79.13；记忆侧参数约 201M（不含冻结主干）。E/GE/GH 跨任务与输入互补，生成记忆适合作为检索的选择性校正。
