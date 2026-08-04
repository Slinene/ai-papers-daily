---
title: 'LiveMem: Maintaining Memory State Continuity in Long-Running LLM Inference'
title_zh: LiveMem：在长运行LLM推理中维护记忆状态连续性
authors:
- Zhichen Liu
- Ruihan Sun
- Hengjie Yang
- Zipeng Wu
- Zhaohan Chen
- Xiaofan Zhang
- Yang Xu
affiliations:
- NatureSelect.AI
- Southern University of Science and Technology
- Xidian University
arxiv_id: '2608.02515'
url: https://arxiv.org/abs/2608.02515
pdf_url: https://arxiv.org/pdf/2608.02515
published: '2026-08-03'
collected: '2026-08-04'
category: Agent
direction: 长运行LLM的内在记忆状态连续性
tags:
- LiveMem
- GDN2
- memory state continuity
- context turnover
- post-training
- LLM
one_liner: 通过并行循环记忆分支和上下文更替训练，使LLM在证据离开工作上下文后仍能依靠记忆状态保持推理连续性。
practical_value: '- **记忆侧分支可迁移至长会话推荐Agent**：在对话推荐或客服Agent中，可在每层注意力旁添加类似GDN2的循环模块，将用户长期行为序列压缩至固定记忆状态，当上下文窗口溢出时仍维持偏好感知。

  - **训练范式：强制证据移出上下文**：模仿LiveMem的post-training，通过分块管理使旧历史离开注意力，迫使模型依赖记忆状态回答，从而训练出真正的“记忆利用”能力，适合电商长生命周期用户建模。

  - **课程学习策略激活记忆分支**：先用全量行为日志（或长文档）预热记忆模块，再用均衡任务数据微调，可有效激活侧分支，避免模型短路依赖注意力上下文。

  - **评估记忆真实有效性的方法**：借鉴LongMemEval设计，构造证据与当前窗口距离递增的测试集，精确衡量模型是否真正记住了被淘汰的信息，适合评估推荐Agent记忆续航能力。

  - **工程收益：上下文分块与KV淘汰**：采用基于chunk的FIFO队列管理KV缓存，在推理时释放旧chunk，降低显存，支撑极长交互session的推理服务。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**  
持续运行的助手和Agent面临无限增长的交互历史，受限于上下文窗口的LLM必须不断替换工作上下文。现有RAG和摘要类方法只提供历史访问，无法在上下文更替时维持连续的内部状态。本文提出“状态连续性”需求：通过固定容量的记忆状态，在整个生命周期中持续传递信息，与外部检索互补。关键在于，记忆状态必须在原始证据退出工作上下文后仍能影响模型行为，而不仅仅是一个形式的循环结构。

**方法关键点**  
- **架构**：在每个解码器层的注意力旁添加并行的Gated DeltaNet-2（GDN2）循环分支。GDN2维护固定大小的记忆状态矩阵，通过遗忘、擦除和写入操作在线更新，其输出直接与注意力输出相加。主注意力路径仅保留有限窗口内的KV缓存，系统提示作为注意力锚点常驻。  
- **上下文更替**：输入按chunk组织，当窗口内token总数或chunk数超过阈值时，最旧的chunk被逐出，其KV缓存被释放，但信息已保留在记忆状态中。训练和推理时均采用该调度，保证一致性。  
- **记忆导向后训练**：训练记忆分支，冻结注意力主干。先使用长文档QA数据预热侧分支，再用包含QA、分类、多查询的均衡数据微调。随后采用GRPO进行RL探索，奖励函数结合准确度和格式惩罚，迫使模型在证据完全脱离窗口后仍能借助记忆状态回答。  

**关键结果**  
- 在Wiki QA、Conversation、TTL、Long QA四类任务上，LiveMem总体准确率0.519，远超Qwen3-4B（0.458）和δ-Mem（0.327）等基线，在各任务上表现均衡。  
- LongMemEval测试中，当支持证据完全移出上下文窗口时，LiveMem-RL准确率达16.5%，比无记忆基线高10个百分点以上，证实记忆状态真实携带了历史信息。  
- 消融表明：侧分支全参数训练优于LoRA；课程学习（长文本预热+均衡微调）效果最佳；证据距离增加，准确率仅缓慢下降，表明记忆状态具备持久性。

**核心启示**  
LiveMem证明，通过显式的上下文更替和强制训练，可以让LLM获得真正的“生命周期记忆”，使模型在上下文替换后依然保持推理连续性，为构建长运行Agent提供了一条实用路径。
