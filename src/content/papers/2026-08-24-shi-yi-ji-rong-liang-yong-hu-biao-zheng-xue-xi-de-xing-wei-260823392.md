---
title: Towards a Densing Law for User Representation Learning at Billion-Scale Capacity
title_zh: 十亿级容量用户表征学习的行为稠密化定律
authors:
- Bin Dou
- Junru Zhang
- Zhaoyi Yuan
- Wuliang Huang
- Letian Gong
- Baokun Wang
- Huan Li
- Yu Cheng
- Weiqiang Wang
affiliations:
- Ant Group
- Zhejiang University
arxiv_id: '2608.23392'
url: https://arxiv.org/abs/2608.23392
pdf_url: https://arxiv.org/pdf/2608.23392
published: '2026-08-24'
collected: '2026-08-25'
category: RecSys
direction: 用户表征学习 · 行为 tokenization 与 scaling law
tags:
- User Representation Learning
- Scaling Law
- RQ-VAE
- Behavioral Tokenization
- Billion-scale
- Adaptive Quantization
one_liner: 提出用户行为 Densing Law，量化最小充分 tokenization 容量随数据规模幂律增长，并用 RQ-VAE 与自适应分配突破 raw
  scaling wall
practical_value: '- 亿级用户行为序列不要盲目加 raw 数据/模型参数；先诊断是否已饱和（通常几千万用户、60-90 天、0.2B 左右），优先上
  RQ-VAE 行为 tokenization。

  - tokenizer 配置用 Densing Law 预估：ln C* = β + α ln s，只需少量最小充分容量实验即可外推；容量用 C_tok = H
  M log K + η H M d 统一核算。

  - 选 tokenizer 时注意表示空间冗余：SARQ/RQ-VAE 的 α 低于 VQ-VAE，同样数据量需要更小容量；业务上可把 α 作为 tokenizer
  效率指标。

  - 对高 routine 行为做自适应 token 深度分配（ALGN/entropy-based）：高信息段多分 codebook 层，常规段少分，提升 capacity
  efficiency；冻结 tokenizer 后与 raw baseline 同 encoder 对齐，方便归因。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
在十亿级支付宝用户行为上，堆用户量、历史时长、模型参数都出现明显边际收益递减；N≈0.03B、D≈60 天、P≈0.2B 后提升平台化。更隐蔽的问题是 pre-train loss 继续下降但下游 AUC 饱和，说明低信息密度行为日志才是瓶颈，而不是模型能力。

## 方法关键点
- **行为 tokenization**：RQ-VAE 把多源行为 embedding 压成固定 H 长度的离散 token；残差量化使粗粒度 codebook 捕获稳定消费类别，深层 codebook 保留商家/偏好残差。
- **Densing Law**：将 tokenization 容量配置建模为 Pareto 优化，约束形式选最小充分容量 C*；在 utility 递减 frontier 下导出 ln C* = β + α ln(s/s0)，α 与 tokenizer 表达效率和 intra-source uniqueness 有关。
- **容量度量**：C_tok = H M log K + η H M d，便于统一比较。
- **ALGN**：按量化残差/不确定性自适应分配 token 深度，避免 routine 占用过多容量。

## 关键实验
- 数据：支付宝 PayBill/SPM/MiniProgram；用户 100M–2B；下游 50 个分类数据集、22 个检索数据集。
- tokenized vs raw：分类 AUC 在 512 天从 73.96 提升到 74.78；用户量 1e8 时 73.88 vs 74.56；且在 D≈64 天、N≈1.2e7 后优势扩大。
- 模型扩展 0.2B→0.4B 下游 AUC 仅 73.92→73.92，说明容量不再关键。
- 在三种 tokenizer、三个数据源、三类任务上验证 Densing Law，斜率稳定且 α 与 U_d^2 成比例。

## 最值得记住的一句话
信息密度而非原始数据量或模型参数，是亿级用户表征继续 scale 的核心瓶颈。
