---
title: 'PIA: A Personal Intelligence Agent Turning Health Conversations into Records
  and Records into Understanding'
title_zh: PIA：将健康对话转为记录并将记录转为理解的个人智能体
authors:
- Jeonghun Yoon
- Dongchan Kim
- Hongyeon Yu
- Young-Bum Kim
- Jaegul Choo
affiliations:
- KAIST
- NAVER Corp.
arxiv_id: '2609.31255'
url: https://arxiv.org/abs/2609.31255
pdf_url: https://arxiv.org/pdf/2609.31255
published: '2026-09-25'
collected: '2026-09-28'
category: Agent
direction: Agent 结构化长期记忆与读写决策
tags:
- Agent Memory
- Structured Extraction
- Knowledge Graph
- Temporal Reasoning
- Personalization
one_liner: 提出个人智能体记忆系统，自主决定读写，将对话转为类型化临床记录并合成轨迹级理解
practical_value: '- 结构化事实抽取：用户特征/行为事件先落 schema 化字段（事件日期/数值/类别/来源），不要全用 embedding top-k；便于后续聚合、筛选和趋势计算。

  - 读写解耦与自主决策：让 agent 根据请求类型判断是否需要写记录、读哪些结构，减少无效检索与上下文污染；可在推荐对话/导购 Agent 中分离“用户画像写入”和“上下文读取”路径。

  - 时间与别名归一化：相对时间“昨天/上周”必须解析为绝对时间戳；商品/活动名、用户标签做 alias dictionary 和规则映射，避免 LLM 随意解读。

  - 因果去噪：对生成的 causal links 用静态规则先过滤结构噪声，再进入下游推理；业务中可用活动规则/类目约束过滤无意义关联。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：通用 agent memory 靠摘要、embedding 和 top-k 检索支撑长期记忆，但健康领域需要字段化记录、精确时间与趋势问答；文本摘要会把剂量变成句子，相对时间被模型随意解析，三周血糖趋势无法用相似度回答。

**方法**：PIA 作为个人智能体部署在消费健康 agent 旁，接收自然语言请求后自主决定写或读。记忆线束含四个领域无关控制：extraction、memory、retrieval、understanding；通过可插拔健康模块注入 schema、医学别名词典、知识图谱和时间规则。对话被转成类型化临床记录，再由 retrieval/understanding 合成用户理解。

**结果**：同一查询随注入记忆加深而答案不同：从一维 recall、二维健康快照到三维含因果的轨迹。运行经验显示：自我报告健康数据缺失非随机；问题措辞显著影响合成理解质量；候选因果链接中近 1/3 是结构性噪声，可由规则单独移除。
