---
title: Modeling Preference Dependencies with Directed Acyclic Graphs for Narrative-Driven
  Recommendation
title_zh: 叙事驱动推荐中基于有向无环图的偏好依赖建模
authors:
- Mingzhe Lu
- Jian Qin
- Ruize Qin
- Jinhao Liu
- Yunpeng Li
- Hang Su
affiliations:
- Institute of Information Engineering, Chinese Academy of Sciences, Beijing, China
- School of Cyber Security, University of Chinese Academy of Sciences, Beijing, China
- Faculty of Engineering and IT, The University of Melbourne, Melbourne, Australia
- Independent Researcher
arxiv_id: '2610.37280'
url: https://arxiv.org/abs/2610.37280
pdf_url: https://arxiv.org/pdf/2610.37280
published: '2026-10-27'
collected: '2026-10-28'
category: RecSys
direction: 叙事驱动推荐 · 偏好依赖DAG
tags:
- Narrative-Driven Recommendation
- Preference Dependency Graph
- LLM Agent
- Open-Web Retrieval
- Topological Ranking
one_liner: 提出PDG-F框架，将用户叙述解析为偏好依赖DAG，指导分路径检索与拓扑排序，显著提升开放域推荐召回上限与精度
practical_value: '- 将复杂用户需求拆成偏好依赖DAG，显式建模“哪些条件是修饰哪些基础偏好”，避免扁平关键词匹配导致虚假相关；可迁移到电商长尾query理解、复杂筛选条件结构化。

  - 以依赖边为单位改写检索query，分路径召回候选后再做拓扑传导打分，比单次检索或listwise rerank更能扩候选池与提升召回天花板；适合需要开放域检索、大候选池的推荐/搜索场景。

  - 拓扑路径评分+对数压缩聚合是确定性打分，不依赖RankGPT等提示词排序，可规避上下文窗口限制、位置偏差和推理延迟，工程上可复制为低延迟重排模块。

  - 先扩候选池召回、再优化排序：论文显示候选池扩大后pool recall近翻倍甚至三倍，但ranking gap仍是主要瓶颈；业务上若NDCG提升困难，优先补召回而非只调排序模型。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
叙事驱动推荐中，用户的多维偏好往往相互修饰限定，例如“奇幻+浪漫作为副线，且浪漫应通过对话、幽默与处理分歧展开，而非性场面”。把叙述当作扁平关键词或独立属性匹配，容易把《指环王》这类表面包含奇幻、浪漫、幽默但幽默属于友情的片子误判为相关，而《哈尔的移动城堡》才真正满足“浪漫通过日常拌嘴展开”的限定。现有方法缺乏对偏好间修饰依赖结构的显式建模。

**方法关键点**  
- 构建偏好依赖图（PDG）：PDG-A从叙述中提取偏好原子，按“解释视角—具体实例”两层展开为节点；判断节点对之间的限定关系生成有向边；检测并解除有向环，再做传递约减，得到DAG。
- 拓扑上下文细化：按拓扑顺序为每个节点生成具体偏好描述，融入祖先节点的偏好上下文，使上游偏好逐步限定下游偏好。
- 有向路径检索：对每条依赖边（包括虚拟ROOT边）改写为搜索query，经Serper API获取URL，按节点抓取网页、分块，并在每个节点下提取候选item及证据，保留支持/矛盾描述。
- 拓扑路径排序：对每个候选-偏好描述对打0–4分（矛盾到复述），沿DAG递归计算路径分数（折扣因子0.7），跨节点聚合后用对数压缩得到最终分。

**关键实验**  
三个数据集：Reddit MovieSuggestions（英文电影）、自建Book（英文30查询）、Anime（中文30查询，来源小红书/知乎），评测P@10、R@10、NDCG@10。对比Qwen-3.8-27B、MiniMax-M3、DeepSeek-V4-Pro、Perplexity AI、GPT-6-Astra、OCG-Agent等。PDG-F(+Year)在三个数据集所有指标均最优：Movie P@10 0.3650、NDCG@10 0.4511；Book P@10 0.4233、NDCG@10 0.5101；Anime P@10 0.2467、NDCG@10 0.3085。候选池平均大小从OCG-Agent的约17–23扩到251–687，pool recall在三个域分别从0.2102→0.4858、0.2854→0.5481、0.1672→0.4734。Recall@10已超过OCG-Agent的完整候选池召回上限。

**最值得记住的一句话**  
显式建模偏好间的修饰依赖DAG，并让同一结构同时驱动检索与排序，是叙事驱动推荐突破候选池天花板的关键。
