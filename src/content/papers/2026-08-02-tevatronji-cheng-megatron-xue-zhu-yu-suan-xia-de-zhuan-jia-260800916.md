---
title: 'Tevatron Meets Megatron: Expert-Parallel LLM Reranker Training on an Academic
  Budget'
title_zh: Tevatron集成Megatron：学术预算下的专家并行LLM重排序训练
authors:
- Zhichao Xu
- Xueguang Ma
- Shengyao Zhuang
- Luyu Gao
- Wenqian Ye
- Yu Wang
- Jamie Callan
- Jimmy Lin
affiliations:
- University of Utah
- University of Waterloo
- The University of Queensland
- Carnegie Mellon University
- University of Virginia
arxiv_id: '2608.00916'
url: https://arxiv.org/abs/2608.00916
pdf_url: https://arxiv.org/pdf/2608.00916
published: '2026-08-02'
collected: '2026-08-04'
category: RecSys
direction: LLM重排序 · 专家并行高效训练
tags:
- MoE
- Expert Parallelism
- LLM Reranker
- Tevatron
- Megatron
- LoRA
one_liner: 为Tevatron重排序工具包引入Megatron训练后端，通过专家并行实现30B MoE重排序器训练，同时保持HF兼容。
practical_value: '- **在资源受限下训练大规模MoE重排序模型**：利用Megatron的专家并行（EP）将MoE层的专家分布到多个GPU，仅激活少量专家，可在两台8×H200节点上训练Qwen3-30B-A3B（30B总参，激活约3B），突破PyTorch
  FSDP1不支持EP的限制。

  - **加速训练并保持部署兼容性**：Megatron后端在推荐配置（TP=2/DP=4）下比FSDP1全分片快约22%，且训练产出可直接加载为Hugging
  Face checkpoint，无缝接入vLLM等推理引擎，部署零转换成本。

  - **LoRA适配MoE时注意目标模块划分**：使用命名目标组注册表（如指定`moe_experts`、`moe_shared`，冻结`router`），避免盲目适配全部128个专家FFN或遗漏关键层，这是LoRA在MoE重排序中不严重掉点的关键工程trick。

  - **蒸馏训练可离线标注教师分数**：将教师分数预计算存入数据集，训练时无需加载教师模型，节省显存和计算量；蒸馏与对比学习在不同数据集上各有优势，可根据业务场景灵活选择，并在重排序任务中简化训练管线。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**  
现代重排序方法趋向十亿参数交叉编码器、MoE骨干和知识蒸馏，但现有训练基础设施（Hugging Face Trainer + DeepSpeed/FSDP）存在缺陷：DeepSpeed ZeRO‑2有梯度累积bug，FSDP1全分片内存安全但吞吐低，且两者均不支持专家并行（EP），无法高效训练MoE重排序器。Tevatron 3.0旨在以有限学术预算填补这一空缺。

**方法关键点**  
- 在Tevatron工具包中集成Megatron‑Core训练后端，保持原有数据路径、评估流水线和HF格式检查点。  
- 引入张量并行（TP）、流水线并行（PP）和专家并行（EP），EP将MoE层专家分区投送，只需激活部分专家，大幅降低每GPU显存。  
- 双向权重桥接实现HF↔Megatron格式互转，训练后直接导出vLLM可用的标准checkpoint。  
- 支持对比学习和列表式KL蒸馏；蒸馏教师分数离线预计算，训练时不增加模型前传。  
- 为MoE设计LoRA目标组注册表（attn, moe_experts, moe_shared, router），精准适配关键层，避免参数量爆炸或效果严重下降。  
- 统一评估接口支持本地ranklists打分和远程HTTP服务器池（vLLM/HF）重排序，便于吞吐测试。

**关键结果**  
在RLHN‑680K数据上训练Qwen3‑8B（密集）与Qwen3‑30B‑A3B（MoE），于BEIR‑15基准上评估：  
- **MoE vs 密集**：MoE激活参数约3B，不到密集8B的一半，NDCG@10与密集相差不超过0.006，质量相当；推理吞吐在vLLM下高43%（2,622 vs 1,834 pairs/s）。  
- **LoRA效果**：rank‑16 LoRA在密集8B上仅比全参数微调低0.007‑0.011 NDCG@10，MoE上配合专家感知适配同样高度还原。  
- **训练效率**：Megatron推荐配置（TP=2/DP=4）训练密集8B用时8h55m，较FSDP1全分片快22%；EP使16卡训练30B MoE成为可能。  
- **蒸馏 vs 对比**：总体指标接近，蒸馏在部分任务上略优，可视任务特性选用，但同一‑量级教师蒸馏增益有限。

**一句话总结**  
Tevatron 3.0以Megatron后端实现专家并行，在学术预算下解锁30B MoE重排序器训练，且证明MoE可用不到一半激活参数达到密集模型同等质量，同时推理更快。
