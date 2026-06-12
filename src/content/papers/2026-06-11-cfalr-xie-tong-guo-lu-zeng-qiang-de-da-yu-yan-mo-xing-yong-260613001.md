---
title: 'CFALR: Collaborative Filtering-Augmented Large Language Model for Personalized
  Fashion Outfit Recommendation'
title_zh: CFALR：协同过滤增强的大语言模型用于个性化时尚穿搭推荐
authors:
- Yujuan Ding
- Junrong Liao
- Yunshan Ma
- Yi Bin
- Wenqi Fan
- Tat-Seng Chua
- Qing Li
affiliations:
- The Hong Kong Polytechnic University
- University of Electronic Science and Technology of China
- Singapore Management University
- Tongji University
- National University of Singapore
arxiv_id: '2606.13001'
url: https://arxiv.org/abs/2606.13001
pdf_url: https://arxiv.org/pdf/2606.13001
published: '2026-06-11'
collected: '2026-06-12'
category: GenRec
direction: 生成式推荐 · 个性化穿搭生成
tags:
- Fashion Recommendation
- LLM
- Collaborative Filtering
- Outfit Generation
- Hybrid Encoding
one_liner: 首个协同LLM语义理解与CF交互模式的穿搭生成框架，通过混合编码和输出层融合显著提升个性化推荐效果。
practical_value: '- **混合特征注入 LLM 的方式**：将文本、视觉（ResNet-50）、CF 嵌入（CPTM）通过独立的可训练线性投影层映射到
  LLM 的 token 空间，形成统一的 item/user 表示，可直接用于电商物品建模，弥补文本描述视觉细节不足和 CF 交互信号缺失。

  - **多阶段训练策略**：先冻结投影层用纯文本微调 LoRA，再联合训练投影层与 LoRA，避免特征空间差异带来负向干扰，这种渐进式训练可迁移到其他混合特征+LLM
  的推荐任务。

  - **CF 增强的生成推理**：在 LLM 输出 logits 上直接插值 CF 模型的预测分布（加权和），解决 LLM 在输入条件简单（如仅用户或单件物品）时建模能力不足的问题，运算成本极低，适合已有
  CF 模型和 LLM 的团队快速上线。

  - **组合推荐任务的评估体系**：采用个人化精确率（PP）、套装兼容性（OC）、平均配对兼容性（MPC）以及 LLM-as-a-Judge 和人评，为电商中的搭配推荐、捆绑推荐提供了可复用的多维度评估框架。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
个性化穿搭推荐需同时兼顾用户偏好与物品美学兼容性。传统协同过滤（CF）在数据稀疏时失效，预定义模板无法涵盖快速变化的时尚趋势和冷启动物品，而 LLM 虽具备强大的语义理解和先验知识，但其基于 token ID 的语义空间与推荐所需的用户-物品交互空间存在根本错位，导致无法直接用于穿搭生成。

**方法关键点**
- **任务形式化**：将用户-穿搭交互转为自然语言描述的 Personalized Fill-In-The-Blank (P-FITB) 任务，以 Vicuna-7B 为骨干。
- **混合编码**：对物品同时使用文本描述、ResNet-50 视觉特征和 CPTM 模型提取的 CF 特征，通过可训练的线性投影层将后两者映射为 LLM 的 token 嵌入；用户则结合交互历史物品的混合表示与自身 CF 特征。
- **训练策略**：第一阶只用纯文本微调 LoRA 模块；第二阶联合优化投影层和 LoRA，有效规避不同特征空间的学习冲突。
- **CF 增强生成**：推理阶段在 LLM 输出概率上乘以系数 λ 并与 CF 模型概率线性插值，生成最终预测分布，解决 LLM 在输入简短时交互模式建模偏弱的问题。

**关键实验结果**
在 Polyvore 和 IQON 两个基准上，CFALR 在 P-FITB 任务中，1/4/1/10/1/20 三档难度下的准确率分别达到 0.6498/0.3957/0.2459（Polyvore）和 0.6103/0.3654/0.2018（IQON），全面超过 CPTM、Qwen3.5-VL、Bundle-MLLM 等强基线。在 POG 任务中，PP、OC、MPC 三项指标同样最优（如 Polyvore 上 PP 0.2428，OC 0.4626，MPC 0.3556）。消融实验验证了文本、视觉、CF 三种特征及混合编码的有效性，以及 CF 增强机制对改善 LLM 在输入稀疏时表现的重要作用。
