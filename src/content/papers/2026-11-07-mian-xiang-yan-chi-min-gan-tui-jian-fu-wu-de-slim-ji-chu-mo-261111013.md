---
title: Slim Foundation Models for Latency-Critical Recommendation Serving
title_zh: 面向延迟敏感推荐服务的 Slim 基础模型：LLM 增强 CTR 的在线结构化剪枝
authors:
- Danyal Aftab
- Anas Zafar
- Assadig Abakr
- Steven Davy
affiliations:
- Technological University Dublin
- National University of Computer and Emerging Science
arxiv_id: '2611.11013'
url: https://arxiv.org/abs/2611.11013
pdf_url: https://arxiv.org/pdf/2611.11013
published: '2026-11-07'
collected: '2026-11-10'
category: RecSys
direction: LLM 增强 CTR 的在线结构化剪枝与融合
tags:
- LLM4Rec
- CTR Prediction
- Structured Pruning
- LoRA
- Latency Optimization
- Semantic Fusion
one_liner: 剪枝 LLaMA3-8B 至 4.5B 并配合 LoRA 场感知微调与语义融合，在线 CTR 延迟降 3.4× 且精度保持 99%+
practical_value: '- 如果目录/特征经常变化，离线缓存 LLM embedding 会失效；可借鉴依赖感知结构化剪枝把 LLM 压到 4.5B 量级，直接进在线请求路径，避免离线全量重算。

  - 冷启动物品/长尾用户：场感知任务 + InfoNCE 能产出紧凑 field-level 语义 embedding，LoRA 只训 adapter，适合把标题、品牌、品类等
  textual metadata 低成本映射为推荐侧可用语义特征。

  - 融合方式可复用：不要直接 concat LLM embedding，而是算 field embedding 间的 cosine similarity，经可学习变换后对现有
  CTR 的 pairwise feature interaction 做重加权；这几乎不增加 CTR 主干参数，可插入 FM/DeepFM/FinalMLP 等模型。

  - 精度-延迟 tradeoff：论文给出 8B/6B/4.5B/2B 的单调退化曲线，4.5B 是较佳平衡点；线上若对延迟更敏感可考虑更小 backbone
  或蒸馏，核心是先做结构化剪枝再 LoRA，而不是只做量化。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
LLM 能给 CTR 预测带来语义先验，尤其对冷启动物品和长尾用户有帮助；但 8B LLM 在线推理成本过高，已有 LLM 增强 CTR 方法大多离线缓存 LLM 输出，目录变更时需要重算，且没有真正消除计算负担。该工作研究通过结构化剪枝把 LLM 压到可以在线服务的规模。

## 方法关键点
- 依赖感知结构化剪枝：基于 DepGraph/LLM-Pruner 构建参数依赖图，用泰勒重要性估计（包含损失对参数梯度和二阶 Hessian）分组剪枝，将 LLaMA3-8B 压至 4.5B 参数。
- 场感知 LoRA 微调：用结构化 prompt 让 LLM 判断特征值属于哪个 field，例如把 'Black Rose' 分类为 'Movie Title'；采用 InfoNCE 对比损失训练，只更新 LoRA 适配器，剪枝后的 backbone 冻结。
- 语义引导融合：提取 field embedding，计算 pairwise cosine similarity，经可学习变换后重加权 CTR 模型的 feature interaction；训练时用 KL 散度对齐 CTR 与 LLM 的 embedding 分布，总损失为 BCE + λ KL。

## 关键实验
在 Amazon Gift Cards、Video Games、Digital Music 和 MovieLens-1M 四个数据集上，结合 FM、DeepFM、FwFM、FmFM、FinalMLP、Wukong 六个 CTR backbone 评估。SlimFM 参数量 4504M、MACs 275G、单样本延迟 15.99–17.58ms；相比 KAR 延迟降低 3.1–3.4×，相比 LLM-CF 降低 2.7–2.9×。平均 AUC 相对 base CTR 提升：Gift Cards +1.69%、Video Games +1.36%、Digital Music +1.39%、MovieLens-1M +0.13%。剪枝到 4.5B 保留 99.77% 的平均 AUC，精度退化随剪枝比例单调且平缓。

## 最值得记住的一句话
结构化剪枝 + LoRA 场感知微调 + 语义融合，把 LLM 从离线缓存搬进在线 CTR 请求路径，实现 1.8× 参数压缩、最高 3.4× 推理加速，同时保住 99% 以上精度。
