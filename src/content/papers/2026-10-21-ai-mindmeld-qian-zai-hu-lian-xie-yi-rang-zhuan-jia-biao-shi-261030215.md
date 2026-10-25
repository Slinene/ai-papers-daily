---
title: 'AI Mindmeld: A Latent Interconnect Protocol'
title_zh: AI Mindmeld：潜在互联协议，让专家表示直连 LLM
authors:
- Siavash Golkar
- Jake Kovalic
- Shirley Ho
affiliations:
- Polymathic AI
- New York University
- Yale University
- Flatiron Institute
- Princeton University
arxiv_id: '2610.30215'
url: https://arxiv.org/abs/2610.30215
pdf_url: https://arxiv.org/pdf/2610.30215
published: '2026-10-21'
collected: '2026-10-25'
category: Agent
direction: Agent 工具调用中的专家表示直连
tags:
- Latent Interconnect Protocol
- LLM agents
- connector training
- representation exchange
- tool calling
- frozen LLM
one_liner: 提出 LIP 协议：冻结 LLM 只训练连接器，把专家表示直接映射进 LLM 内部状态，支持零样本跨域组合
practical_value: '- 在电商搜索/推荐 Agent 中，用户、商品、行为序列通常已有高维 embedding；可为这些内部模型训练轻量连接器直接注入
  LLM，而不是先把候选/特征转成文本摘要。冻结基座 LLM 只训 connector，成本低、可随 LLM 版本快速替换。

  - 多专家可组合：商品理解、用户意图、广告文案等专家各自独立训练连接器，新专家接入无需重训旧连接器或 LLM；这种模块化设计适合业务中频繁新增召回/排序模型的场景。

  - 零样本任务迁移提示：用表示注入替代 prompt 拼接，LLM 可被引导到未见过的组合任务（例如从用户 embedding + 商品 embedding 直接生成推荐理由），但需注意当前
  LLM 不经专门训练可能不稳定，建议在 connector 输出层加 norm/对齐损失，或先用领域数据做轻量适配。

  - 工程上可参考连接器映射到 LLM 某几层的 hidden state，类似 soft prompt / prefix injection；在线上服务时可预计算专家表示并缓存，connector
  前向开销很小，便于高 QPS 推理。'
score: 7
source: arxiv-stat.ML
depth: abstract
---

**动机**：LLM 作为科学 agent 调用专家模型时，专家输出必须转成文本、图像等模态，高维表示被严重压缩，且 agent 难以知道自己该请求哪些信息。这成为多专家协作的瓶颈。

**方法关键点**：提出 Latent Interconnect Protocol (LIP)，学习连接器把蛋白质、小分子等专家模型的中间/输出表示直接映射到 LLM 的 internal states；冻结所有预训练模型，只训练连接器，保持实用性和可扩展性。连接三个蛋白质专家和三个小分子专家到 Gemma 3 4B/12B、Kimi K2.6（1T 总参、32B 激活）。独立训练的连接器可组合，无需修改 LLM 或已有连接器；支持熟悉问题和新问题类型，可处理未见过对象。

**关键结果**：实现零样本跨域任务转移，无需联合训练；任务性能和组合性随 LLM 能力提升而提升，零样本任务转移增益尤其明显。主要局限是当前 LLM 未将专家表示作为原生输入训练，接入信息不一定能被可靠解释、整合或用于推理。
