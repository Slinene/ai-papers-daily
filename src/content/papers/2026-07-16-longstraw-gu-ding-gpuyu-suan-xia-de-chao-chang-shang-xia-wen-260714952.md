---
title: 'LongStraw: Long-Context RL Beyond 2M Tokens under a Fixed GPU Budget'
title_zh: LongStraw：固定GPU预算下的超长上下文RL训练
authors:
- Changhai Zhou
- Kieran Liu
- Yuhua Zhou
- Qian Qiao
- Jun Gao
- Harry Zhang
- Irvine Lu
- Nolan Ho
- Lucian Li
- Andrew Lei
affiliations:
- MindLab
- Fudan University
arxiv_id: '2607.14952'
url: https://arxiv.org/abs/2607.14952
pdf_url: https://arxiv.org/pdf/2607.14952
published: '2026-07-16'
collected: '2026-07-17'
category: Training
direction: RL训练系统优化·长上下文
tags:
- Long-Context Training
- GRPO
- Memory Optimization
- Context Parallelism
- Activation Checkpointing
- Model Architecture
one_liner: 通过分离长提示状态捕获和串行响应回放，在固定GPU数下将GRPO训练上下文扩展至200万token以上
practical_value: '- **长序列推荐模型训练**：若需将用户长期行为序列（如200万长度）作为条件训练生成式推荐或Agent模型，可借鉴LongStraw的“捕获一次、回放多次”模式：用无梯度前向计算并保存固定大小的循环状态或压缩的KV页，然后仅对候选物品序列进行可微分回放，大幅削减峰值显存。

  - **混合注意力架构选型**：Qwen的48个循环层+16个全注意力层的设计启示：对于长历史处理，用循环层（如Gated DeltaNet）避免KV长度线性增长，仅保留少量全注意力层存储必要细粒度上下文，可平衡效果与显存。

  - **MoE训练中的多维并行布局**：GLM同时使用CP（上下文并行）划分长序列和EP（专家并行）划分路由专家，可在固定机器数下扩展长序列训练。推荐系统中若有超大参数模型需处理长序列，可考虑类似并行策略，但需确保梯度完整聚合（论文指出当前未完成KV适配器梯度同步）。

  - **训练系统设计原则**：当显存成为长上下文瓶颈时，优先优化状态生命周期，而非单纯增加并行度。保留仅响应解码所需的状态，释放瞬态激活，并通过串行回放控制激活峰值。这种思路同样适用于大规模用户行为模型或Agent轨迹的离线RL训练。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**
RL后训练的上下文长度远落后于推理，限制了对长轨迹Agent（如工具调用、多轮交互）的有效训练。自注意力的二次计算和长时间留存的前向图导致固定GPU下难以扩展训练上下文。以往方案要么依赖更大规模集群，要么仅优化推理，并未在固定卡数下探索GRPO长上下文执行极限。

**方法关键点**
- **共享提示捕获，串行响应回放**：将GRPO训练图拆分为一次无梯度提示评估和多个短响应可微分回放。提示状态（如循环状态、KV页、MLA隐变量）保存为只读，每个响应重新构建自动微分图，反向传播后立即释放，梯度累积后统一调用优化器。
- **架构自适应状态库存**：Qwen 3.6‑27B（48个循环层+16个全注意力层）保留紧凑GDN状态和CP分片的KV页；GLM‑5.2（21个索引计算层+57个复用索引层，3个稠密+75个MoE层）将MLA隐变量和DSA索引键以CP分片形式存于CPU，逐层暂存至GPU。
- **内存与并行布局**：Qwen用8‑way CP，全注意力前向通过全局LSE归约重构精确输出；GLM用CP32分片长序列，EP32分布256个路由专家，并实施整层检查点以限制回放图。

**关键结果**
- 在8块H20上，Qwen以2.097M上下文和组大小2、8完成GRPO执行，峰值内存约97.5 GB，组大小由2增至8仅多占0.21 GB；压力测试中达4.46 M上下文。
- 在32块H20上，GLM完整回放2.1M提示的78层，端到端执行路径闭环。
- 局限性：所有实验使用确定性响应和奖励，提示状态和Qwen的K/V适配器梯度未同步，GLM绕过标准梯度完成，均未达到正确的分布式更新或全序列梯度等价。

**一句话**
“状态生命周期和物理所有权是RL后训练上下文上限的实际决定因素，而非稀疏度或并行度。”
