---
title: Plan or Retrieve First? A Scale Study of Tool Discovery Architectures
title_zh: 先规划还是先检索？大规模工具发现架构对比研究
authors:
- Mingfei Zhang
- Amit Surana
- Ziauddin Majid
- Chenxi Wang
- Michael Xu
affiliations:
- Apple
arxiv_id: '2610.19068'
url: https://arxiv.org/abs/2610.19068
pdf_url: https://arxiv.org/pdf/2610.19068
published: '2026-10-13'
collected: '2026-10-15'
category: Agent
direction: Agent 工具发现架构对比与自适应路由
tags:
- Tool Discovery
- LLM Agent
- Retrieval Architecture
- Plan-then-Retrieve
- ToolBench
- Adaptive Routing
one_liner: 在50k API规模下系统对比Retrieve-then-Plan与Plan-then-Retrieve，发现单工具查询RtP占优、多工具查询PtR占优的复杂度交叉
practical_value: '- 复杂度自适应路由：用RtP的top-1检索相似度作为零成本路由信号，高相似度（查询直接包含API名/品牌名）走RtP，低相似度（抽象多步骤意图）走PtR，可节省约36%的discovery调用开销且无检索质量损失。

  - 多意图查询分解：在电商/Agent场景中，对于“连衣裙+高跟鞋+包包”这类多面意图query，可以让LLM先生成多个Abstract Tool Stubs（或子意图桩），每个桩独立检索再合并，优于单embedding直接检索。

  - Stub hallucination双刃剑管理：简单query包含明确的专有名词或品牌时，不要抽象成generic stub，否则丢失强匹配信号；复杂query则可以利用stub的分解能力。工程上可对stub生成加入专有名词保留策略。

  - 检索是Agent行为的上界：实验显示planner轨迹保真度≥96%，即planner几乎只从检索结果中选择tools，所以优化检索架构比优化planner
  prompt更关键。在大规模工具注册表下应优先投入检索质量。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
工具增强的LLM agent需要从数十万API注册表中发现相关工具，但上下文窗口有限，无法注入全部定义。主流Retrieve-then-Plan（RtP）直接嵌入用户查询检索相似工具，假设语义差距小；但复杂多步意图时单embedding难以捕捉多面需求。Plan-then-Retrieve（PtR）让LLM先生成Abstract Tool Stubs（假设的函数签名）再作为检索query，但缺乏在工业规模下的系统性对比。

## 方法关键点
- 两个架构共享相同基础设施：GTE-base embeddings、FAISS flat索引、Gemini 2.5 Flash planner，唯一变量是检索范式。
- RtP：嵌入原始query，检索top-k API。
- PtR：LLM先零样本生成多个hypothesized tool stubs（JSON格式，含tool_name和reasoning），每个stub独立嵌入检索，合并top-k结果去重后交给planner。
- 评估在ToolBench（46,984个API，50个类别）的G1（单工具，n=200）、G2（类别内多工具，n=200）、G3（跨类别多工具，n=100）三个子集，指标为recall、precision、pass rate。

## 关键实验与结果
- 复杂度交叉：G1上RtP recall 0.372 vs PtR 0.289；G2上PtR recall 0.188 vs RtP 0.143；G3上PtR方向性优势但部分差异不显著。交叉在k=1到20所有检索预算、1k到47k注册表规模、Gemini 2.5 Flash与gpt-oss-120b两个模型家族上均成立。
- 架构分歧：工具选择分歧度从1k注册表的88%升至47k的98%，表明架构选择是结构性属性，规模越大越重要。
- 轨迹保真度≥96%：planner几乎总是从检索集合中选择工具，检索成为瓶颈，架构选择直接决定下游行为。
- 成本分析：PtR的discovery call增加约75-104% token开销，在G1上损害（-0.072 recall），G2上获益（+0.042 recall）。复杂度自适应路由可节省约36%的discovery开销且无检索质量损失。
- Stub hallucination机制：stub唯一性达79-99%，且正确/错误匹配的cosine相似度几乎相同（0.874 vs 0.872），说明嵌入空间无法区分好坏；但多stub覆盖补偿了单个stub失配。

**最值得记住的一句话**：工具发现架构的选择取决于查询复杂度，单工具查询直接检索更优，多工具查询先规划生成工具桩再检索更优，且该结论在工业规模下稳定。
