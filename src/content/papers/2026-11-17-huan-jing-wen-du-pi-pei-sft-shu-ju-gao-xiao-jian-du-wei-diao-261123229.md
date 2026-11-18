---
title: 'Ambient LLMs: Data-Efficient Supervised Fine-tuning via Temperature Matching'
title_zh: 环境温度匹配 SFT：数据高效监督微调
authors:
- Giannis Daras
- Marios Papachristou
- Adam Klivans
- Antonio Torralba
- Constantinos Daskalakis
affiliations:
- MIT
- Arizona State University
- University of Texas at Austin
arxiv_id: '2611.23229'
url: https://arxiv.org/abs/2611.23229
pdf_url: https://arxiv.org/pdf/2611.23229
published: '2026-11-17'
collected: '2026-11-18'
category: Training
direction: LLM 微调 · 温度匹配正则
tags:
- SFT
- Knowledge Distillation
- Temperature Matching
- Catastrophic Forgetting
- Data-Efficient Fine-tuning
one_liner: 提出 Ambient SFT，在 SFT 中匹配高温预训练分布，缓解小数据微调过拟合与灾难性遗忘
practical_value: '- 在电商搜索/推荐场景的 LLM 微调中（如 query 改写、意图识别、商品描述生成），若目标域标注样本少，可将 frozen
  base LLM 作为 teacher，在 SFT 中增加 temperature matching KL 项：用 T=2.5、pc=0.75（25% 步做 TM），额外前向开销仅约
  1.1×，可显著减少通用能力遗忘。

  - 温度是核心超参：T=1 退化为 KD，T→∞ 退化为 SFT，需在 dev 上 sweep T（论文中 T=2.5 在多个任务有效；不同数据源可设 per-source
  T 以缓解混合源过拟合）。不要默认用 KD 的 T=1。

  - 论文给了一个可复用的预判指标：base model 在目标域的 zero-shot perplexity 与 Ambient SFT 收益显著相关（Spearman
  ρ=-0.90）。上线前可先评估 base model 的 zero-shot 损失，若其较小，则采用该方法可能收益更大；数据越稀缺收益越明显。

  - 工程实现上，可直接替换 SFT 优化器：随机采样步骤中，以概率 1-pc 做 teacher 前向（无梯度），并用 temperature-scaled soft
  labels 计算 CE；无需额外数据或模型，适合数据受限的领域适配和 instruction tuning。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**  
Post-training 数据规模远小于预训练，导致 SFT 过拟合、遗忘预训练分布尾部，尤其在小数据集上。传统方案是暴力扩大精调数据，但成本高。论文问：能否用算法提升数据效率，同时避免模型坍缩？

**方法关键点**  
- 提出 Ambient SFT：标准 CE loss + λ KL(p_T_pre || p_T_student)，teacher 为 frozen pre-trained model，student 初始化自 teacher。  
- 温度 T 控制对 teacher 的信任：T→∞ 退化为普通 SFT，T=1 成为 knowledge distillation；实际使用 T>1 匹配高温分布。  
- 随机实现：每步以概率 pc=0.75 做 clean SFT，25% 概率做 temperature matching；额外前向开销约 1.1×。  
- 理论：高温数据可恢复原分布；temperature scaling 使分布差异以 O(T^-2) 收缩；在 log-linear 模型下严格优于 SFT/KD。

**关键实验与数字**  
- Domain adaptation：1.5B 模型适配 5 个域（Python Code、CS、BioMed、News、Reviews），每个约 225M tokens。Ambient SFT 匹配或超越全部 baseline；News 相对最优 baseline 降低 26.7% perplexity（1.99→1.68）。  
- Instruction tuning：Qwen3 1.7B-14B，Dolci-Instruct-SFT 1%（约 20K 样本）。平均相对改进 8.0%-20.3%，7/8 任务超过 vanilla SFT；对比 KD(T=1) 的 +17.0%，Ambient SFT 达 +20.3%。  
- Reasoning：OLMo-3-7B 上 1% Dolci-Think-SFT，5/6 benchmarks 超过 SFT，平均 +3.5%。  
- 数据越稀缺收益越大；base model 在目标域 zero-shot perplexity 与收益的 Spearman ρ=-0.90。

**最值得记住的一句话**  
用 frozen pre-trained model 的高温分布作为正则，是数据稀缺 SFT 的低成本防遗忘方案，T=2.5 是常见默认、额外开销仅约 1.1×。
