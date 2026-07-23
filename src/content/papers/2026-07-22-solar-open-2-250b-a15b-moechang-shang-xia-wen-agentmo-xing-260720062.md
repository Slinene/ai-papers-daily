---
title: Solar Open 2 Technical Report
title_zh: Solar Open 2：250B-A15B MoE长上下文Agent模型
authors:
- Sungrae Park
- Sanghoon Kim
- Gyoungjin Gim
- Jungho Cho
- Hyunwoong Ko
- Minbyul Jeong
- Minjeong Kim
- Keunwoo Choi
- Chaehun Shin
- Chanwoong Yoon
affiliations:
- Upstage
arxiv_id: '2607.20062'
url: https://arxiv.org/abs/2607.20062
pdf_url: https://arxiv.org/pdf/2607.20062
published: '2026-07-22'
collected: '2026-07-23'
category: Agent
direction: 大规模长上下文Agent模型训练
tags:
- MoE
- Hybrid Attention
- Long Context
- Agent
- Model Distillation
- Korean LLM
one_liner: 通过混合注意力与多专家蒸馏，以1/6参数量达到1.6T模型韩文办公Agent水平
practical_value: '- **混合注意力降显存**：每三个线性注意力层插一个softmax层、取消位置编码来实现1M token上下文窗口，在长轨迹Agent或对话系统中可大幅降低KV缓存开销，适合电商客服、端到端推荐流等需要处理超长历史序列的场景。

  - **多教师在线策略蒸馏（MOPD）**：先训练12个垂直域专家，再用在线蒸馏合并为单一模型，可复用于电商搜索推荐中的多任务学习（例如同时蒸馏意图识别、商品理解、对话规划等专家），避免维护多个专用模型。

  - **数据价值策展**：质量与稀有度感知的筛选、混合比例优化使10T数据优于原20T数据，在同等算力下提升效率。可借鉴到构建领域特定预训练语料（如电商搜索日志、商品描述），用更少token达到更好任务性能。

  - **参数骨架迁移预训练**：从上一代模型继承共享参数骨架（5.69B），其余从头预训练，既保留了原有知识又适配新架构。在推荐模型升级（如从稠密模型转MoE）时可大幅节省再训练成本，快速获得强初始点。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：面向长周期Agent任务，需处理完整轨迹的1M token上下文，同时保持韩文能力领先。从Solar Open 1（102B-A12B）扩展，在固定预算下追求高效训练。

**方法关键点**：
- **1M上下文混合注意力**：每3个线性注意力层中插入1个softmax注意力层，无位置编码，用带负特征值的门控delta规则，降低显存并支持超长序列。
- **继承式预训练**：从Solar Open 1迁移5.69B共享参数骨架，其余参数（包括新增专家）从头预训练，加速收敛。
- **数据价值策展**：通过质量和稀有度过滤、混合比优化，将20T数据池精选为10T，在相同token预算下超越原方案。
- ** Agent技能构建**：训练12个领域专家，用多教师在线策略蒸馏（MOPD）合并为单一模型。

**关键结果**：英文方面，MMLU-Pro、LiveCodeBench、APEX-Agents领先同规模模型；韩文方面，平均分超越所有对比模型（含闭源API）；在韩文办公Agent基准Ko-GDPval上，以不到1/6参数量与DeepSeek-V4-Pro（1.6T）性能相当。
