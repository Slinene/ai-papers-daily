---
title: 'UniFormer: Efficient and Unified Model-Centric Scaling for Industrial Recommendation'
title_zh: UniFormer：统一的模型中心缩放框架用于工业推荐
authors:
- Bo Chen
- Jinlong Jiao
- Tijian Hu
- Ruihao Zhang
- Yanzhi Liu
- Chenghou Jin
- Qinglin Jia
- Baixuan He
- Hechang Pan
- Yiwu Liu
affiliations:
- Kuaishou Technology
arxiv_id: '2606.27058'
url: https://arxiv.org/abs/2606.27058
pdf_url: https://arxiv.org/pdf/2606.27058
published: '2026-06-25'
collected: '2026-06-26'
category: RecSys
direction: 模型中心缩放 · 统一特征与任务交互
tags:
- Model Scaling
- Unified Architecture
- Multi-task
- Attention
- User-Item Decoupling
- Kuaishou
one_liner: 统一特征空间与任务空间的联合缩放，实现快手线上观看时长+0.7%~1.1%提升，推理加速48%
practical_value: '- **语义分组 tokenization 实现用户-物品解耦**：将无序列特征分为与候选物品独立/依赖两组，推理时独立部分计算一次复用所有候选，大幅降低时延；可借鉴于电商推荐中用户画像、上下文等请求级特征的重用。

  - **多视图 FFN 灵活分配参数**：为序列（S-FFNs）、无序列（NS-FFNs）、任务（T-FFNs）分别配备独立 FFN，避免容量瓶颈，支持定向扩容；在广告排序模型中可对不同特征类型（行为、属性、任务）配置可独立扩展的模块。

  - **多序列交叉注意力防止偏好塌缩**：短/长行为序列分离交叉注意并自适应融合，保留异构兴趣；电商场景可对点击、收藏、加购等不同长度序列独立建模后再融合，提升个性化。

  - **任务 token 参与注意力交互**：将任务特征作为 query 与高阶特征做交叉注意力，再自注意力捕获任务间关系，可替代传统 MMoE 等多任务模块，便于统一缩放。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：工业推荐模型通常采用组件中心缩放——单独放大行为建模、特征交互或任务建模模块，导致模块间割裂、计算资源浪费。近期工作尝试在特征空间内联合缩放序列与交互，但尚未纳入任务空间。为此，需一种统一的模型中心缩放框架，同时兼顾训练/推理效率、预防偏好塌缩和灵活参数分配。

**方法关键点**：
- **整体架构**：堆叠的 Feature‑space Interaction Module (FIM) 和 Task‑space Interaction Module (TIM)，均使用标准注意力+FFN，实现特征与任务空间的联合缩放。
- **语义 tokenization**：将序列特征（短期、长期压缩）和 non‑seq 特征按是否依赖候选物品分组，推理时可一次计算用户侧 token 并复用，实现用户‑物品解耦。
- **FIM**：多序列交叉注意力分别处理短/长行为序列（用可学习系数自适应融合），再通过自注意力增强特征交互；之后用 NS‑FFNs 处理 non‑seq 特征，防止序列偏好塌缩。
- **TIM**：任务 token 对 FIM 的输出做交叉注意力捕获任务‑特征关系，再通过自注意力 + T‑FFNs 建模任务间依赖，类似可扩展的 MMoE。
- **多视图 FFN**：S‑FFNs（序列）、NS‑FFNs（non‑seq）、T‑FFNs（任务）各自专用，实现精细化容量扩充。
- **工程优化**：用户级公共特征压缩减少冗余；可变长 FlashAttention 消除 padding；BF16 训练；推理时通过 attention mask 解耦用户与物品，QPS 提升 48%。

**关键结果**：
- 离线：快手工业数据集上，UniFormer 在 Effective‑view / Long‑view / Like / Follow 四项任务的 GAUC 均显著超过最强基线 MixFormer，其中 Effective‑view GAUC 提升 0.53%（MixFormer 为 0.43%），Like 提升 0.53%（0.33%）；参数增至 1B 后仍有稳定提升，呈现缩放规律。
- 线上 A/B：在快手和快手 Lite 两个场景，应用停留时长分别 +0.101%/+0.260%，观看时长 +0.729%/+1.113%，互动指标（点赞、评论、收藏等）也有显著正向提升。
