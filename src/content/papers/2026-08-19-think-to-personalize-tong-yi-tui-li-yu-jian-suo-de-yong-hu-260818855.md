---
title: 'Think-to-Personalize: Unifying Reasoning and Retrieval for User-Centric Personalized
  Dense Retrieval'
title_zh: Think-to-Personalize：统一推理与检索的用户中心个性化密集检索
authors:
- Angqing Jiang
- Gaoming Zhang
- Jianchun Song
- Kena Qi
- Dayao Chen
- Wei Lin
- Defu Lian
affiliations:
- University of Science and Technology of China
- Meituan
arxiv_id: '2608.18855'
url: https://arxiv.org/abs/2608.18855
pdf_url: https://arxiv.org/pdf/2608.18855
published: '2026-08-19'
collected: '2026-08-20'
category: QueryRec
direction: LLM 推理驱动的个性化查询改写与密集检索
tags:
- Dense Retrieval
- LLM Reasoning
- Personalized Search
- GRPO
- Query Rewriting
- E-commerce
one_liner: 提出 TTP 框架，用 LLM 显式推理用户历史生成意图增强查询，并与密集检索端到端联合训练，线上订单量提升 0.46%
practical_value: '- **端到端联合优于解耦流水线**：把 LLM 生成的 intent-enhanced query 与共享检索编码器联合训练，比独立
  rewrite-then-retrieve（Decoupled-Stage）在 General 上 Recall@20 高 1.63 个点，Broad 上高 3.66
  个点；电商搜索/召回链路若已有 LLM 改写模块，可尝试将其嵌入检索塔共同优化。

  - **意图增强数据构造可复用**：用大模型按偏好抽取、意图消歧、查询纠正三类进行改写，生成 5 候选，再用 reranker 按 ground-truth 成交商品过滤并采样
  top3，同时保留不改写样本防止过度个性化；这套流程可直接迁移到搜索 query 改写、搜索建议或 push 文案生成。

  - **RL 对齐的两个关键 trick**：GRPO 中用**冻结 SFT 模型**计算检索奖励，避免 reward hacking（unfrozen reward
  model 导致平均 R@20 从 44.97 暴跌到 29.53）；奖励用 ΔS_pos + ΔS_margin 两项，并**动态选择奖励最大的 rollout**
  作为对比正样本，显著稳定训练。

  - **在线效率方案**：head query 走离线个性化 cache（覆盖 10.59% QV），miss 用蒸馏 305M 双塔实时服务，蒸馏时加入 <q_r,
  p+> 和 <q, q_r> 目标，保留大部分效果（平均 R@20 43.10 vs 教师 44.97），端到端延迟仅增 0.15ms，适合大规模部署。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：本地生活电商搜索中，用户查询常稀疏、模糊（如 “Luck” 指代 Luckin Coffee，“Shrub” 指代咖啡品牌），形成 intent gap。已有个性化检索依赖隐式行为编码，缺乏显式推理能力；LLM 改写方案则与检索分离，生成目标与检索效用错位。

**方法关键点**：
- TTP 将用户历史购买序列（商品标题、类目、菜单等序列化）与当前 query 输入共享 LLM，生成 `<think>意图增强查询</think><embed>`，取 `<embed>` 末隐层作为查询向量；物品侧共享同一编码器。
- 教师数据：Qwen3-32B 按偏好抽取、意图消歧、查询纠正三类推理生成改写候选，用 bge-reranker-v2-m3 按成交商品过滤，保留不改写样本防止过度个性化。
- 两阶段训练：SFT 联合生成损失与 InfoNCE 对比损失，LoRA 微调 Qwen2.5-3B-Instruct；RL 用 GRPO，奖励=格式+长度惩罚+检索奖励（正样本绝对增益 ΔS_pos 和边际增益 ΔS_margin），冻结 SFT 模型做奖励模型，动态选择检索奖励最大的 rollout 作为对比正样本。

**关键实验**：
- 自有 General、Broad、LongTail 三测试集上，TTP(SFT+RL) 的 Recall@20 分别 47.52、48.74、38.65，明显超过隐式个性化 baseline MAPs（45.76/45.57/33.84）和解耦式 Decoupled-Stage（45.89/45.08/35.18）；Broad 上比 Qwen-Embedding 提升 7.47 个点。
- 公开 Amazon PersonalWAB HR@20 达 90.17，KuaiSearch R@20 达 16.21，均最优。
- 线上 A/B：订单量 +0.46%，QV CXR +0.41%，额外延迟 0.15ms。
- 消融：动态正样本选择去除后平均 R@20 掉至 37.71，unfrozen reward model 掉至 29.53，验证冻结奖励和样本筛选的必要性。

**最值得记住的一句话**：把显式用户意图推理和密集检索放进同一编码器端到端优化，并用冻结 SFT 模型提供稳定检索奖励，是弥合模糊查询个性化意图鸿沟的有效范式。
