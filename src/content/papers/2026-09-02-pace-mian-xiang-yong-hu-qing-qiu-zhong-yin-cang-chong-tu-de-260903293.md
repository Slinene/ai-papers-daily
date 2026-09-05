---
title: 'PACE: Towards Surfacing Hidden Conflicts in User Requests'
title_zh: PACE：面向用户请求中隐藏冲突的识别与证据检索框架
authors:
- Yoojin Kim
- Jihyoung Jang
- Hyounghun Kim
affiliations:
- Department of Computer Science and Engineering, POSTECH
- Graduate School of Artificial Intelligence, POSTECH
arxiv_id: '2609.03293'
url: https://arxiv.org/abs/2609.03293
pdf_url: https://arxiv.org/pdf/2609.03293
published: '2026-09-02'
collected: '2026-09-05'
category: MultiAgent
direction: 多智能体协作检索与冲突感知推理
tags:
- multi-agent
- personalization
- conflict detection
- egocentric KB
- RAG
- graph traversal
one_liner: 提出 PACE 数据集与 PACEMAKER 多智能体框架，通过冲突感知查询重构、多跳图遍历与证据过滤提升隐式冲突判断能力
practical_value: '- **冲突感知查询重构**：不要直接用原始 query 检索，先让 planner 生成可能的冲突维度（时间、个人约束、资源状态），再生成
  counter queries 去检索隐式约束。在电商推荐或 Agent 决策中，可主动生成反事实查询（如“用户是否对某成分过敏”“该时段是否有冲突日程”）以覆盖不兼容场景。

  - **多跳图遍历 + 加权 RRF 融合**：为个性化知识库离线构建 k-NN 文档图，在线检索时先混合 dense+BM25 获取种子，再 BFS 扩展邻居，最后用冲突感知过滤器筛选证据。反事实查询检索结果给予更高权重，有助于发现弱相关但决策关键的证据。

  - **证据筛选优于全量上下文**：实验显示 Full KB 反而不如精选 top-10 证据，缺失部分 gold facts 会显著降低冲突判断准确率。工程上应避免把整个用户画像或海量行为日志直接塞给
  LLM，先检索筛选决策关键证据，尤其对冲突类请求。

  - **训练-free 且索引阶段无 LLM 调用**：多智能体框架冷启动成本低，适合频繁更新的个性化 KB。可借鉴离线建图 + 在线 agent 检索的架构，降低延迟和成本。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
个性化助理不仅应执行用户请求，还需判断请求在用户当前情境下是否合适。现有基准多关注显式风险或安全检测，忽略真实场景中隐式情境约束：用户请求表面合理，但结合自我中心知识库中的隐藏事实（如同伴饮食限制、日程冲突、场所临时状况）可能变得不适当。这要求从数千个分散的原子事实中检索并组合分布式证据，难度远高于简单 RAG。

## 方法关键点
- **PACE 数据集**：基于 persona 扩展生成自我中心知识库，包含 ego/alter 关系。查询分为 Temporal、Personal、State 三类冲突，正负样本平衡。总计 3,249 个查询、376,448 个 facts、185 个 profile；平均每查询 4.01 个 gold facts，分散在约 2,035 个 facts 中，使直接关联查询与冲突证据非常困难。
- **PACEMAKER 多智能体框架**：冲突规划器先生成最多 3 个冲突维度，再由多视图查询生成器产出原始查询视图和反事实查询视图，显式探查潜在冲突前提。混合检索融合 dense+BM25，反事实视图赋予更高权重；对融合结果构建 k-NN 文档图，以过滤后的种子文档为入口做 BFS 多跳遍历；最后通过冲突感知过滤器选出 top-10 决策关键证据，交给答案生成器给出判断与理由。整个过程训练-free，索引阶段无 LLM 调用。

## 关键结果数字
- 在 Qwen 开源配置下，PACEMAKER 的 Recall@5 为 26.23，优于 Sparse 19.77 和 Dense 17.90；PASS 68.82% vs Sparse 62.73/Dense 62.39；冲突查询 PASS 53.20 vs 41.80/37.78。
- GPT 配置下 Recall@5 达 36.05，PASS 75.35，冲突 PASS 59.17，均显著超过检索 baselines。
- Oracle（给定 gold facts）PASS 86.89–91.26%，而 Full KB（全量上下文）仅 57.49–73.10%，说明证据筛选比上下文数量更关键。
- 消融显示移除多跳遍历导致冲突 PASS 从 59.17 降至 52.41，移除查询规划降至 54.17，移除证据选择降至 58.87。
- 与 GraphRAG/HippoRAG 2 相比，PACEMAKER 在冲突查询 PASS 上为 54.42，显著高于 34.98 和 43.57。

最值得记住的一句话：冲突检测中证据完整性比模型推理更关键，先精准检索出完整冲突证据再让 LLM 判断，优于把全量 KB 交给模型。
