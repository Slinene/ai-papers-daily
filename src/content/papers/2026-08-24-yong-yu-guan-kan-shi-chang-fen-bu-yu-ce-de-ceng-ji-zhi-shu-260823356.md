---
title: Hierarchical Exponential-Gaussian Mixtures for Watch-Time Distribution Prediction
title_zh: 用于观看时长分布预测的层级指数-高斯混合模型
authors:
- Sofia Gulevskaia
- Mikhail Trapeznikov
- Aleksandr Poslavsky
- Alexander D'yakonov
affiliations:
- AI VK
- Lomonosov MSU
arxiv_id: '2608.23356'
url: https://arxiv.org/abs/2608.23356
pdf_url: https://arxiv.org/pdf/2608.23356
published: '2026-08-24'
collected: '2026-08-25'
category: RecSys
direction: 观看时长分布预测 · 混合密度网络
tags:
- watch-time prediction
- mixture density network
- variance collapse
- recommendation
- distributional modeling
- A-B test
one_liner: 修复EGMN方差坍塌与组件冗余，通过层级skip-watch分解和KL方差正则提升排序与完播预测，工业A/B显著提升session depth
practical_value: '- 若业务目标是停留时长、完播率等多阈值事件，可考虑将点回归头替换为单一分布头（如指数-高斯混合），同一密度可同时输出期望WT、P(Y>τ)、P(Y>ρd)等信号，避免为每个阈值单独训练模型；但模型选择应使用排序指标（如XAUC）而非NLL，因为方差坍塌会让NLL不可靠。

  - 混合分布头极易发生方差坍塌和组件冗余，结构化初始化是关键：Gaussian means 均匀分布在归一化支撑上（如 k/(K+1)），σ 初始化为 1.5/K，指数成分
  λ 初始化为短时长先验（1/0.05）。消融显示去掉该初始化，工业 XAUC 从 0.7188 暴跌至 0.6841。

  - 层级 skip–watch 分解（sigmoid gate 分开快速跳过与真正观看）比 flat softmax 更可解释且排序更好；移除 EGMN 的 forced
  Gaussian shift 和 entropy regularization 通常能提升稳定性。

  - 对于过参数化混合（如 K≥8），可加 mean-agnostic 的 KL 方差正则：按视频时长分桶估计参考方差，只约束每个 Gaussian 的方差，既防止
  collapse 又能改善尾部阈值预测；在 K=3 时不必加该正则，以免轻微牺牲排序。生产部署延迟增加约1.2ms，通常在30ms约束内可接受。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

动机：短视频推荐中观看时长（watch-time, WT）是核心互动信号，但分布呈 near-zero inflation、long tail 和 multimodality，点回归无法支持 threshold event 和 uncertainty。EGMN 用指数-高斯混合分布建模，但大规模复现发现方差坍塌（σ→0）、组件冗余/不活跃、初始化敏感，甚至弱于 MSE-VR。需要更稳定的分布头。

方法关键点：HEGM 改用层级 skip–watch 分解：sigmoid 输出 p_skip 控制指数成分（快速跳过），(1-p_skip) 进入 Gaussian mixture（观看部分），替代 flat softmax。全局归一化 y=y_raw/s，不按用户/物品归一化。结构化初始化：Gaussian means 均匀分布 k/(K+1)，σ=1.5/K，指数 λ=1/0.05。移除 EGMN 的 forced Gaussian shift 和 entropy regularization。增加 mean-agnostic 的 KL-based variance regularization：按视频时长分桶估计参考方差，只约束每个 Gaussian 方差，防止 collapse 且不限制 mean。最终损失为 NLL + λ_reg MAE + λ_KL KL。

关键实验：在 KuaiRec、VK-LSVD 和工业数据集（282M interactions）上与 MSE-VR、MAE-VR、CREAD、EGMN 对比，以 XAUC 为主指标。工业上 HEGM XAUC 0.7188（EGMN 0.6585, CREAD 0.7146, MSE-VR 0.7070），MAE 12.97；60s 绝对阈值 ROC AUC 0.8903 vs EGMN 0.8356。消融显示去掉结构化初始化 XAUC 跌至 0.6841；KL 正则对 K=3 略降排序，但对 K=12 将 collapse rate 从 47.88% 降至 0%。1.5个月生产 A/B：session depth +9.26%，deep watch (≥10s) +5.75%，skips (Y<3s) -6.23%，总观看时长基本持平。推理延迟 median +1.22ms，p99 +0.3ms，在30ms约束内。

最值得记住的一句话：分布头的结构先验（层级分解+结构化初始化）比熵正则更关键，NLL 因方差坍塌不可靠，生产选择应使用排序指标 XAUC。
