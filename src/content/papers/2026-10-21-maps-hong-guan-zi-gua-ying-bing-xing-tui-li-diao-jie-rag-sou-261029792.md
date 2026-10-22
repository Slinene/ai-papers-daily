---
title: 'MAPS: Macro-Adaptive Parallel Reasoning for Regulating Search Momentum in
  Retrieval-Augmented Generation'
title_zh: MAPS：宏观自适应并行推理调节 RAG 搜索动量
authors:
- Xinze Li
- Dingwen Zhang
- Zhenghao Liu
- Yukun Yan
- Shuo Wang
- Yu Gu
- Ge Yu
- Maosong Sun
affiliations:
- Northeastern University, Shenyang, China
- Tsinghua University, Beijing, China
arxiv_id: '2610.29792'
url: https://arxiv.org/abs/2610.29792
pdf_url: https://arxiv.org/pdf/2610.29792
published: '2026-10-21'
collected: '2026-10-22'
category: RAG
direction: 迭代式 RAG · 搜索动量调节
tags:
- RAG
- Search Momentum
- Parallel Reasoning
- Query Intent Drift
- Multi-hop QA
one_liner: 提出 search momentum 量化迭代 RAG 中的查询意图漂移，并用轨迹解耦与并行多方向检索缓解漂移
practical_value: '- 用 search momentum 做在线 query 漂移监控：在多轮搜索/Agent 中，记录每步生成 query 的
  embedding 位移并加权累积，当 momentum 与原始 query 余弦相似度持续下降时触发校准（重写 query、并行探索或回退原始意图），适合电商搜索
  query 改写、对话式推荐中的信息收集。

  - 状态管理上把“已获取的知识”和“历史查询轨迹”解耦：只保留知识观察和压缩后的推理状态，不把历史 query 序列塞进 prompt，可避免中间错误查询累积污染后续召回。工程上可用一个
  summarizer 将检索到的商品/文档证据压缩成结构化状态，而不是保留完整对话历史。

  - 并行生成多个互补检索方向：在 query/关键词扩展时，先让 LLM 提出 N 个互补方向（如类目、属性、风格、价格带），再分别生成 query 并行检索并合并召回结果。这比单纯并行生成多个
  query 更可控，消融显示 direction proposal 贡献约 4 个百分点。

  - 自适应终止：MAPS 对简单 query 更早终止，复杂 query 多轮继续检索且不丢准确，可用一个 lightweight 判断器基于已收集证据是否足够来决定停止，减少不必要的检索轮次。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**  
迭代式 RAG 虽能逐步生成子查询获取外部知识，但容易产生冗余查询、长链、多样性不足，尤其查询意图会随历史轨迹漂移。论文用 search momentum 刻画这种漂移，发现后续子查询越来越沿着既有检索方向走而非纠正，导致偏离原始信息需求。

**方法关键点**  
- 定义 search momentum 为子查询嵌入位移的指数加权累积，β_t 控制历史影响；拟合 β_t 预测下一步偏离，发现 β 和方向对齐随步数递增，说明漂移会自增强。
- MAPS 框架两个核心：①推理解耦：不保留历史 reasoning trace 和子查询序列，只保留知识观察集 O_{t-1} 和压缩的 refined reasoning state r̃_t，降低历史检索倾向对后续 query 生成的影响；②并行推理：每步先用 M_Intent 识别 N 个互补检索方向，再生成对应子查询，各检索 top-K 后合并证据，由 M_Refine 更新知识观察和推理状态。
- 终止条件：知识足够或达到最大步数，最后基于原始 query、知识集和精炼状态生成答案。

**关键实验与结果**  
在 NQ、PopQA、2WikiQA、HotpotQA、MuSiQue、GPQA 六基准上，用 Qwen3-32B 和 Qwen3.6-35B-A3B 两个 backbone，以 Cover-EM 评估。MAPS 平均分分别达 56.0 和 63.1，比最强 baseline ParallelSearch 高 6.8 和 5.8 个百分点；比 Search-o1 高约 9 个百分点以上。消融显示去掉检索方向、并行推理或解耦都会明显下降，其中去掉 retrieval direction 平均掉约 4 个百分点。分析显示 MAPS 能更早终止简单 query、复杂 query 多轮仍保持高准确，子查询与原文/证据相似度更稳定。

**最值得记住的一句话**  
不要把完整历史 query 轨迹塞给后续生成；保留已获取证据与压缩状态，并用并行多方向检索替代单链探索，可显著降低 query 意图漂移。
