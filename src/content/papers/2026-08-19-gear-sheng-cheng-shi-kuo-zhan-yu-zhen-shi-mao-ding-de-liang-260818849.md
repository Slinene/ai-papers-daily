---
title: 'GEAR: Generative Expansion and Real Anchoring for Two-Stage Distillation of
  Tabular Foundation Models'
title_zh: GEAR：生成式扩展与真实锚定的两阶段表格基础模型蒸馏
authors:
- Qi Qin
- Jiajie Zhu
- Dali Chen
- Yuzhao Zhang
- Jia-Xing Han
- Yu Su
- Peng Zhang
- Ying Yan
- Yifan Sun
affiliations:
- Renmin University of China
- Ant Digital Technologies, Ant Group
- Nanjing University
arxiv_id: '2608.18849'
url: https://arxiv.org/abs/2608.18849
pdf_url: https://arxiv.org/pdf/2608.18849
published: '2026-08-19'
collected: '2026-08-21'
category: Training
direction: 表格基础模型蒸馏 · 生成式扩展
tags:
- knowledge distillation
- tabular foundation models
- synthetic data
- out-of-fold
- MLP
- GBDT
one_liner: 用生成样本只作为教师查询位置，再用 OOF 真实数据锚定，把表格基础模型压缩为 CPU 可部署的 MLP/树模型
practical_value: '- 在电商/广告场景用大型上下文依赖模型（TFM/LLM）做 teacher、蒸馏到线上轻量模型时，可复用两阶段协议：先用生成样本只作为
  teacher query 点、丢弃生成标签，避免 generator 标签 bias；再回到真实样本做 OOF soft/hard 混合锚定。

  - OOF teacher prediction 是防自标签泄漏的关键。推荐/广告中如果用 teacher 对训练样本打分再蒸馏，样本本身在 teacher context
  里会造成泄漏；按 fold 排除后再 query，能明显提升蒸馏稳定性和泛化。

  - 对 LightGBM/XGBoost 这类树模型，直接蒸馏容易不稳定；但先用合成 teacher soft targets 预训练、再真实锚定，二分类 AUC
  能超过 CatBoost。适合在现有在线树模型上引入 foundation model 蒸馏，保持工程兼容性。

  - 生成器质量决定扩展上限：TabDiff/TabPFGen 优于低容量 Copula/CTGAN；若没有合适生成器，优先用基于真实表条件生成的生成器，生成量
  K 控制在 10-20 附近，边际收益已经递减。'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

## 动机

表格基础模型（TFMs）依靠 in-context learning 取得强性能，但每次推理都要携带完整标注上下文表，延迟和内存成本随 context size 与 query workload 急剧上升，难以大规模部署。直接蒸馏到轻量 MLP/树模型可以消除 context 依赖，但真实表能提供的 teacher-query 位置有限，小样本下覆盖不足；且真实行往往在 teacher 自己的 context 中，会产生 self-label leakage。

## 方法关键点

**两阶段蒸馏协议**：
- **Stage 1 生成式扩展**：用生成器生成协变量，只把这些协变量作为 frozen teacher 的 query 位置，训练学生纯模仿 teacher soft targets；明确丢弃生成器给出的标签，避免 bias。
- **Stage 2 真实锚定**：从 Stage 1 初始化，回到真实表；使用 out-of-fold（OOF）teacher predictions，与真实 hard labels 混合成目标函数，避免自标签泄漏并修正生成分布与真实分布的 mismatch。
- **风险证书**：刻画生成 query 量 M 与生成器保真度 TV(P_X,Q_X) 的权衡，理论解释合成扩展的递减回报与真实锚定的必要性。

## 关键实验

在 TALENT 和 TabArena 上，使用 TabICL、TabPFN、TabDPT 作为 teacher，TabPFGen/Copula/CTGAN/TabDiff 作为生成器，学生为 MLP 或 LightGBM/XGBoost。

- GEAR 的 MLP 学生相比 supervised MLP：二分类 AUC 提升 1.81–2.00 点，多分类提升 1.19–1.35 点；相比 real-data-only distillation 分别再提升 1.76–2.19 和 2.09–2.40 点。
- 在二分类上，两阶段蒸馏让 LightGBM 提升 1.11–1.53 AUC 点、XGBoost 提升 0.98–1.38 点，且 MLP/LightGBM/XGBoost 三者 mean AUC 都超过最强非 TFM baseline CatBoost。
- 推理中位时间降低 57–2866×，峰值预测内存降低 1.9–3.3×，同时保持比匹配 supervised baseline 更高的 AUC。
- 消融显示：两阶段训练比混合训练更稳定，非退化率高 4.2–48.7 个百分点；TabDiff 通常带来最强提升。

最值得记住的一句话：**生成样本只是 teacher 查询位置，不是带标签训练样本；真实 OOF 锚定负责把学生拉回目标分布。**
