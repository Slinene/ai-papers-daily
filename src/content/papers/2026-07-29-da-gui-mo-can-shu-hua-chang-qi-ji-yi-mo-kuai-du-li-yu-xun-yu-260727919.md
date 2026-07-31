---
title: 'Memory Decoder at Scale: A Pretrained, Parametric Long-Term Memory'
title_zh: 大规模参数化长期记忆模块：独立预训练与解耦扩展
authors:
- Rubin Wei
- Jiaqi Cao
- Jiarui Wang
- Junming Zhang
- Qipeng Guo
- Bowen Zhou
- Zhouhan Lin
affiliations:
- LUMIA Lab, Shanghai Jiao Tong University
- Shanghai Artificial Intelligence Laboratory
- Tsinghua University
arxiv_id: '2607.27919'
url: https://arxiv.org/abs/2607.27919
pdf_url: https://arxiv.org/pdf/2607.27919
published: '2026-07-29'
collected: '2026-07-31'
category: LLM
direction: 参数化长期记忆与 LLM 解耦 · 独立扩展
tags:
- Parametric Memory
- Long-Term Memory
- Memory Pretraining
- kNN Distribution
- LLM Scaling
- Domain Adaptation
one_liner: 将参数化长期记忆模块扩展至 6.9B 参数、300B 令牌预训练，小 backbone 搭配大记忆在多项基准上超越更大纯骨干模型且总参数更少
practical_value: '- **记忆模块即插即用，适合多领域推荐系统快速迁移**：预训练好的通用或领域记忆可以直接插在冻结的推荐模型（如同 backbone）上，仅需少量计算即适配新领域，避免全量微调，显著降低部署成本。

  - **kNN 分布蒸馏到参数模块，避免在线检索**：电商搜索或推荐场景通常需要实时反馈，该方案将检索信号离线蒸馏为参数化记忆，推理时无需外部索引和检索，降低延迟和存储，可直接用于排序或召回的特征增强。

  - **小 backbone + 大记忆的参数效率优势**：在推荐模型中，可以用相对较小的主网络搭配较大记忆模块，在总参数受限时比单纯扩大主网络更高效，例如为轻量召回模型配备大容量记忆来提升冷门物品或长尾查询的覆盖。

  - **记忆训练目标可提升训练数据可追溯性**：论文中的抽取式记忆评估表明记忆能更精准还原训练样本，类似思路可用于推荐系统中关键行为或商品的记忆固化，帮助可解释性和合规审查。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：标准 decoder-only LLM 将长期记忆与推理耦合在同一参数集中，记忆容量无法独立扩展，且领域适配容易导致灾难性遗忘。Memory Decoder 此前只在小规模验证，本文探索其在大规模（百亿令牌级）下的可行性与规律。

**方法关键点**：
1. **大规模 kNN 分布构建**：用冻结的 backbone（Pythia-6.9B）为 207B 令牌的 Pile 数据生成每 token 的最后层隐状态作为检索键，构建近邻分布作为记忆训练目标。为应对索引和搜索瓶颈，设计分布式 Faiss 管道：OPQ 将 4096 维压缩至 256 维，IVF+HNSW 分片索引，并行 GPU 检索。
2. **记忆预训练**：记忆模块（1.4B~6.9B 参数）联合优化 kNN 分布对齐（KL 散度）和标准语言建模损失，蒸馏检索行为。训练时采用稀疏存储 kNN 分布（约 65 个非零项/位置），通过分布式流式加载仅读取所需批次数据。
3. **推理接口**：冻结 backbone 与记忆并行处理同一上下文，输出分布以系数 α 插值，无需在线检索。

**关键结果**：
- **通用记忆**：Pythia-410M+Mem-6.9B 在 17 个基准上平均分 37.34，超越 Pythia-12B（37.24）且总参数少 39%。知识密集型任务（如 TriviaQA、2WikiMultiHopQA）增益最显著。
- **领域记忆**：1.7B 领域记忆使 Qwen3-14B-Base 在 BioInst/LawBench/FinEval 上分别提升 17.96/8.97/3.04 分，跨领域仅需切换记忆模块。
- **跨词汇表迁移**：用 20% 训练预算即可将领域记忆转移到 OLMo 系列，平均提升 4.26~7.77 分。
- **分析**：记忆在 few-shot 下依然有效，记忆大小与训练预算增加持续提升性能；记忆目标显著优于同样预算的继续预训练，且使模型更忠实地复现训练事实。

**核心一句话**：独立预训练并扩展的参数化记忆比单纯扩大骨干模型更参数高效，且支持即插即用的跨模型、跨领域迁移。
