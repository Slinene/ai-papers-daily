---
title: 'Agentic Discovery of Neural Architectures: AIRA-Compose and AIRA-Design'
title_zh: 基于智能体的神经架构自主发现：AIRA-Compose 与 AIRA-Design
authors:
- Alberto Pepe
- Chien-Yu Lin
- Despoina Magka
- Bilge Acun
- Yannan Nellie Wu
- Anton Protopopov
- Carole-Jean Wu
- Yoram Bachrach
affiliations:
- FAIR at Meta
arxiv_id: '2605.15871'
url: https://arxiv.org/abs/2605.15871
pdf_url: https://arxiv.org/pdf/2605.15871
published: '2026-05-14'
collected: '2026-05-18'
category: Agent
direction: Agent 驱动的神经架构自动发现
tags:
- Agent
- Architecture Search
- Self-Improving AI
- Transformer-Mamba Hybrid
- Neural Architecture Design
- LLM Agent
one_liner: 用多智能体协作在有限预算内自主搜索 Transformer-Mamba 混合架构，性能与效率超越人工设计基准
practical_value: '- **多智能体组合搜索可复用**：在电商推荐模型的 CTR/序列模块中，可借鉴AIRA的11-agent协作模式，将Attention、MLP、Mamba等计算原语作为搜索空间，用固定GPU预算自动探索高效混合架构，减少人工试错成本。

  - **小尺度评估+外推策略**：对推荐模型结构搜索，先在百万参数量级快速评估候选设计，再extrapolate到生产级大模型，这种“低成本过滤”能显著提升搜索效率，可复用于召回、排序模型的架构迭代。

  - **直接由Agent编写算子与脚本**：AIRA-Design让Agent生成注意力机制和训练脚本，这一思路可迁移至长序列推荐场景（如用户行为序列），自动优化长程依赖处理，降低对专家手工设计的依赖。

  - **固定预算下的多Agent竞赛机制**：多个Agent在限定时间/资源内并行提出方案并相互评估，这种竞争性协作可应用于推荐系统的超参优化、特征工程自动化，快速找到性价比最高的配置。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：实现自改进AI，探索LLM agent能否自主设计出超越标准Transformer的基础模型架构，推动递归式自我进步。

**方法**：提出双框架：
- **AIRA-Compose**：11个agent在24小时计算预算内，以Attention、MLP、Mamba为基本原语进行组合搜索。先在百万参数量级评估候选模型，再外推至350M/1B/3B参数级预训练。最终得到14个新架构，分为Transformer基的AIRAformers和Transformer-Mamba混合的AIRAhybrids。
- **AIRA-Design**：20个agent直接编写新型注意力机制和训练脚本，处理长序列依赖，在Long Range Arena和Autoresearch基准上评测。

**关键结果**：
- 1B参数预训练下，AIRAformer-D和AIRAhybrid-D在下游任务准确率分别比Llama 3.2高2.4%和3.8%。
- 缩放效率显著提升：AIRAformer-C比Llama 3.2快54%，AIRAhybrid-C比Nemotron-2快23%。
- AIRA-Design设计的注意力架构在文档匹配和文本分类上仅比人类SOTA差2.3%和2.6%；训练脚本优化超基准，验证bits-per-byte达0.968。
