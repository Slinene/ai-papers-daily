---
title: 'rEDMRec: Distilling Large Language Model Reasoning into an Editable Experience
  Memory for Recommendation'
title_zh: rEDMRec：将 LLM 推理蒸馏为可编辑经验记忆用于推荐
authors:
- Minh Hoang Nguyen
- Tung Le
- Huy Tien Nguyen
affiliations:
- University of Science, Ho Chi Minh City, Vietnam
- Vietnam National University, Ho Chi Minh City, Vietnam
arxiv_id: '2608.18952'
url: https://arxiv.org/abs/2608.18952
pdf_url: https://arxiv.org/pdf/2608.18952
published: '2026-08-19'
collected: '2026-08-20'
category: RecSys
direction: LLM 推理蒸馏 · 可编辑记忆推荐
tags:
- LLM recommendation
- reasoning distillation
- editable memory
- multi-agent debate
- retrieval-augmented ranking
one_liner: 把教师 LLM 的推荐推理压缩为四通道可编辑经验记忆，冻结学生 LLM 检索排序，解耦推理成本与在线开销
practical_value: '- 借鉴四通道经验库：把用户长期偏好、短期会话兴趣、商品级感知、硬负样本反事实对比分开存储和检索，而不是把全部 history
  塞进 prompt；电商推荐中可分别用向量库存 lt/st/ip，用 hybrid graph-vector 存 cf，支持按 user_id / item 过滤。

  - 借鉴在线/离线解耦：大模型只做离线知识抽取与记忆写入，线上用冻结的 3B-20B 小模型做纯检索式排序；适合控制在线延迟的广告/推荐场景，新交互只触发记忆
  edit，不触发重训或大模型调用。

  - 借鉴 Add/Delete/Modify/Keep 记忆控制器 + 多智能体 debate 优化：用排名奖励向量（HR@1、HR@k、MRR、DCG 折扣）驱动
  critic/arbiter 修改记忆条目，不梯度更新模型；重复率是前导指标，建议 debate agent 数 k=4 为性价比拐点。

  - 注意容量依赖：强学生可能反而被冗余/泛化条目干扰，短时上下文通道最稳定；在采用大模型排序时，可按学生能力选择性启用长期/商品感知/反事实通道，或控制 bank
  规模减少重复。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
LLM 显式推理能提升推荐质量，但每次请求重复推理成本高，且推理结果用完即弃，既不可复用也不可编辑。现有 ReasoningRec/R2Rec/ R4ec 把推理作为训练信号或 per-request prompt，无法按条目更新；RAG/GraphRAG 检索原始历史或静态图摘要，缺少类型化、可编辑记忆。论文目标是解耦推理深度与在线推理成本。

**方法关键点**  
- 四通道经验记忆：lt（长期偏好）、st（短期上下文）、ip（物品感知）、cf（反事实硬负样本对比）；每个通道独立索引、检索、编辑。  
- 教师 LLM 执行四个抽取 pass（pref/ctx/reas/cf），输出 JSON 字段经 Adapt 归一化为记忆条目，配合 LLM memory controller 的 Add/Delete/Modify/Keep 操作写入向量库或 hybrid graph-vector store。  
- 在线：冻结学生 LLM（3B-20B）编码 query，每通道检索 top-m 条目拼接 prompt 排序；不调用 teacher，不更新学生参数。  
- 优化：预测后奖励向量（HR@1、HR@k、1/rank、1/log2(rank+1)）驱动 K 个 persona debating agents 和 arbiter 合成修订条目，经同一控制器写回记忆。

**关键实验**  
数据集：ML-1M、Amazon Beauty、Steam；10 个学生 backbone 3B-20B。对比 zero-shot、few-shot、RAG、GraphRAG。ML-1M 上 Qwen2.5 3B HR@1 从 best baseline 0.15 升至 0.17，Impv +13.3%（McNemar p<0.001）；Amazon Beauty 同模型 Impv +23.6%；Steam +21.5%。通道消融：短时上下文所有容量层都有效（Δ=-0.04 至 -0.01）；强学生上去掉长期/物品感知/反事实反而提升（+0.03~+0.04），说明容量依赖。Teacher distillation 显示 bank duplicate rate 是前导指标，gpt-5.4-mini 重复率 12.4% 带来最大 +0.060 HR@1；小教师 Llama 3.1 8B Instant 重复率 22.8% 仅 +0.015。Debate 优化 6 epochs 重复率从 18.0% 降到 10.6%，Mixtral 8x7B HR@1 +0.029；agent 数 k*=4 为质量/成本拐点。

**最值得记住的一句话**：把推理成本沉淀为可编辑、类型化记忆，线上用冻结小模型检索，记忆质量（重复率）是下游提升的前导指标。
