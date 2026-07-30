---
title: 'Setoka: A Benchmark for Hierarchical User Understanding in Personalized Agents
  over Heterogeneous Data'
title_zh: Setoka：面向异构数据的个性化 Agent 分层用户理解基准
authors:
- Lingyang Zeng
- Guangze Chen
- Kaichen Yu
- Zhicheng Pan
- Siyang Weng
- Zirui Hu
- Xiangyun Du
- Hailin He
- Rong Zhang
- Chengcheng Yang
affiliations:
- East China Normal University
- The Chinese University of Hong Kong
arxiv_id: '2607.27056'
url: https://arxiv.org/abs/2607.27056
pdf_url: https://arxiv.org/pdf/2607.27056
published: '2026-07-29'
collected: '2026-07-30'
category: Agent
direction: Agent 记忆系统与用户理解评估
tags:
- Memory-augmented Agents
- User Understanding
- Benchmark
- Heterogeneous Data
- Personality Traits
- Hierarchical Reasoning
one_liner: 首个心理学驱动的分层基准，评估记忆 Agent 从显式事实到人格特质的跨源推理能力
practical_value: '- **记忆系统选型与分层设计**：在电商/Agent场景中，简单事实检索（如用户偏好标签）用精确数据库查询即可，但跨多源行为聚合（如长期购物节奏、品类偏好漂移）需要带时间上下文的结构化记忆；更抽象的用户人格推理（如价格敏感性、冲动消费倾向）则需图结构记忆以显式关联分散证据，建议按查询抽象层次选择或组合多种记忆结构。

  - **评估体系分层化**：不要仅用整体准确率验收记忆系统，而应分解为单记录召回、多记录拼接、长周期聚合、跨类别泛化四个层次分别评估，暴露系统短板（例如当前系统情景记忆与行为模式得分骤降），尤其注意区分回答率与准确率，避免模型置信度误判。

  - **异构用户数据的合成与一致性保障**：可利用“事件锚定生成树”方法，先生成连贯的行为模式再扩展为多源记录，确保消息、日志、社交图等不同数据表围绕同一核心事件一致，可用于构造内部评测集，规避真实用户隐私问题。

  - **人格/行为推理的显式建模**：如果业务中需要推断用户深层特质（如新用户冷启动时的人格化推荐），可借鉴心理量表到行为模式的规则映射，将大五人格或消费相关特质转化为可观测的行为频率证据，建立从底层日志到高层画像的因果链，提升可解释性与冷启动效果。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**
现有记忆基准只评估智能体从对话历史中检索显式事实的能力，但真实个性化任务需要推断分散在异构数据（消息、日历、社交图等）中的抽象用户特质，如行为模式和人格。缺乏一个能覆盖从具体记忆到抽象人格的分层评估体系。

**方法关键点**
1. **四层用户理解框架**：基于认知与人格心理学，定义语义记忆（SM）、情景记忆（EM）、行为模式（BP）、人格特质（PT）四个层次，每层对应不同的证据范围与推理操作（选择→链接→聚合→泛化），形成嵌套证据链。
2. **心理测量学驱动的数据生成管道**：①相关感知人格抽样——从多元高斯分布联合采样大五人格分数，保留维度间经验相关性；②基于心理量表的行为模式生成——用BFI-2量表将人格分数映射为具体行为模式及其频率；③事件锚定生成树——将行为模式逐层展开为有时间顺序的事件，父节点顺序生成、子节点并行扩展以保证长期一致性；④所有异构记录从同一事件派生，确保跨表一致性。
3. **查询构造与评估**：每层设计专门查询（SM单字段隐藏、EM部分线索恢复、BP聚合统计、PT相对排名），用LLM评委或Kendall τ评估。

**关键结果**
在10个合成用户（每人约1600条记录、23种模式）上，测试了DeepSeek-V4-Flash、Ministral 3 14B、Gemma 3 4B三种LLM搭配Cognee、HippoRAG 2、Mem0、MemMachine、Letta五种记忆系统。
- **准确率随抽象层次单调下降**：最佳SM得分为0.85，逐层降至EM 0.46、BP 0.28、PT 0.24。
- **内存构建对高层推理更关键**：内存系统在全层平均优于直接数据库查询（DBQuery），但DBQuery在单记录SM上得分最高；MemMachine在EM表现最好（0.46），图结构系统（Cognee、HippoRAG 2）在BP和PT上领先。
- **回答率与准确率背离**：回答率从SM的72%升至PT的93%，但准确率反而下降，小模型Gemma回答率高但准确率最低，说明缺乏校准的猜测会泛化。

**最值得记住的一句话**
“仅改善检索是不够的——管理用户理解的记忆系统必须能够链接、聚合和泛化来自异构来源的证据。”
