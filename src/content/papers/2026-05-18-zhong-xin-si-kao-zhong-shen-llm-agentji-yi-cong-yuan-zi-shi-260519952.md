---
title: 'Rethinking How to Remember: Beyond Atomic Facts in Lifelong LLM Agent Memory'
title_zh: 重新思考终身LLM Agent记忆：从原子事实到三层多粒度架构
authors:
- Jingwei Sun
- Jianing Zhu
- Jiangchao Yao
- Tongliang Liu
- Bo Han
affiliations:
- Hong Kong Baptist University
- The University of Texas at Austin
- Shanghai Jiao Tong University
- The University of Sydney
arxiv_id: '2605.19952'
url: https://arxiv.org/abs/2605.19952
pdf_url: https://arxiv.org/pdf/2605.19952
published: '2026-05-18'
collected: '2026-05-29'
category: Agent
direction: Agent 终身记忆与多粒度存储
tags:
- LLM Agents
- Lifelong Memory
- Multi-Granularity
- TextGrad
- Profile Synthesis
one_liner: 提出TriMem，用原始对话、抽取事实和合成画像三层粒度同时保证存储忠实性、检索效率和深层推理，并通过TextGrad迭代优化提示实现终身进化。
practical_value: '- **三层记忆架构可直接迁移到电商客服Agent**：保留对话原文指针（避免丢失产品细节）、提取原子事实（快速检索售后知识）、构建用户画像（整合历史交互推断偏好），三者联合可为长期对话推荐提供高忠实度的上下文。

  - **用TextGrad自动优化抽取/整合提示**：无需修改模型参数，仅靠问答反馈文本梯度迭代，让记忆系统在线适应业务术语变化和对话风格漂移，适合API-only部署。

  - **检索阶段先分析问题关键信息再匹配**：增加一次LLM分析，将问题转化为搜索query，大幅提升检索准确率，可复用于推荐系统中对复杂用户意图的多轮理解。

  - **多粒度索引设计灵感**：在商品知识管理或用户行为记忆库里，可同时维护原始日志、事件摘要和用户兴趣画像，不同粒度服务于不同查询深度，平衡效率与准确性。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
现有LLM Agent记忆系统普遍采用“抽取原子事实”的单一范式：用固定提示将对话压缩为孤立事实，存、检、推理全部依赖这些事实。分析显示，这种设计必然导致信息丢失（丢失14.5%的细节信息）、多证据推理能力崩溃（F1从55.3降至35.8），且固定提示在面对不同对话风格时抽取粒度不稳定，性能剧烈波动。为支撑可靠的长期交互，Agent记忆需同时满足存储忠实性、检索效率和深层推理。  

**方法关键点**  
- **三层粒度架构 (TriMem)**：为每条抽取事实附加源对话标识符（src），保留原始文字的可追溯性；在此基础上，按人物聚合分散事实，逐步构建结构化“画像”（profile），捕获人格、兴趣、行为倾向等高层语义。推理时，检索到事实后可联动召回原文和画像，提供全细节与综合理解。  
- **检索优化**：先由Agent分析问题所需信息和关键词生成搜索query，再与事实库做语义匹配，而非直接用原问题检索，提升召回精度。  
- **提示终身进化 (TextGrad)**：将事实提取提示和画像构建提示视为可优化参数，定义生成答案与参考答案的损失（由LLM评分），用TextGrad的反向传播产生文本编辑建议，迭代优化提示，无需更新模型参数。  

**关键结果**  
在LoCoMo和PerLTQA两个长程对话QA基准上，TriMem全面超越Mem0、LightMem、SimpleMem等强基线。  
- **高能力模型**：GPT-4.1-mini下，TriMem平均BLEU/F1达43.79/54.26，比最佳基线LightMem（37.66/46.69）提升约6个点，同时token消耗仅1217。  
- **轻量模型**：在Qwen3-8B上平均F1 49.65，显著优于xMemory（43.51）和SimpleMem（36.25）；Llama-3.1-8B-Instruct上平均F1 38.70，也超过其他方法。  
- **泛化能力**：在PerLTQA上，TriMem在各类子任务（画像、社交关系、事件、对话）的正确率均领先，如在Profile类正确率达92.46%（Qwen3-8B）。  
- **消融实验**：移除画像或原始对话都会导致性能明显下降；提示进化步数设为4最优，多步会过拟合；检索条目数25时最佳，过多引入噪声。
