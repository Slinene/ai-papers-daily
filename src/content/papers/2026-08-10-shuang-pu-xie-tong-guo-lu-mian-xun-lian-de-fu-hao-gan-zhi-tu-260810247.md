---
title: 'DualSpectralCF: Training-Free Sign-Aware Spectral Collaborative Filtering'
title_zh: 双谱协同过滤：免训练的符号感知图滤波推荐
authors:
- Guanqun Yang
- Tong Qi
- Xiaoxue Han
affiliations:
- Stevens Institute of Technology
- University of Maryland, College Park
arxiv_id: '2608.10247'
url: https://arxiv.org/abs/2608.10247
pdf_url: https://arxiv.org/pdf/2608.10247
published: '2026-08-10'
collected: '2026-08-12'
category: RecSys
direction: 训练免梯度谱方法 · 负反馈融合
tags:
- spectral CF
- sign-aware
- training-free
- negative feedback
- cold-start
one_liner: 两个即插即用的训练免梯度组件，将显式负反馈融入谱协同过滤，无需训练即超越多个骨干模型。
practical_value: '- **零成本引入显式负反馈**：电商平台常有1星差评、踩按钮、极低观看率等信号，可将它们作为负样本，通过两个标量超参（γ, κ）直接融入现有的谱协同过滤骨干（如GF-CF、ChebyCF），无需重新训练，总耗时仅增加16%-59%，特别适合快速迭代。

  - **负信号仍视作主题信号**：实验中最优γ始终为负值（如-0.5），表明差评物品仍反映用户兴趣领域，只是需要降低正向权重。电商推荐中可把踩过的品类仍然作为弱信号，避免完全忽略用户兴趣面。

  - **冷启动用户显著收益**：对训练行为≤5条的冷启动用户，引入负反馈后Recall@20最高提升29.2%（Epinions）。电商新用户交互少，可专门对冷启群体启用sign-aware分支。

  - **工程实现极简**：不改动原有模型的滤波器参数，仅替换用户交互向量和物品相似度矩阵为符号版本；多项式滤波器骨干不需要重新特征分解，复杂度保持不变。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现实推荐系统普遍收集显式负反馈（1星评价、踩、低观看比），但现有免训练的谱协同过滤（谱CF）完全忽略负样本；引入负反馈的图方法又必须依赖梯度训练，成本高昂。该工作在经典的谱CF框架 `ˆr_u = F(M) r_u` 上，通过两个组件将负反馈信号融入，保持训练免梯度且骨干无关。

### 方法关键点
- **通用抽象**：所有谱CF骨干均可写为 `ˆr_u = F(M) r_u`，M为物品-物品拉普拉斯或相似度，F为多项式滤波器。
- **组件A：符号输入信号 r±_u**：将用户交互行替换为 +1（正）、-γ（负），γ作为可控超参。实验发现γ最佳值始终非正（如-0.5），因负反馈仍揭示话题注意力，仅需降压而非反向排斥。
- **组件B：符号物品-物品算子 M±**：将M替换为 `L± = I - ˜R+⊤˜R+ + κ ˜R−⊤˜R−` 或 `ˆP± = ˜R+⊤˜R+ + κ ˜R−⊤˜R−`，κ≥0控制负协同的惩罚强度。多数骨干κ=0.1即可。
- **超参（γ, κ）**：仅新增两个标量，无需改变滤波器形状，无需梯度，可直接结合ChebyCF、GF-CF、Turbo-CF等。

### 关键结果
在5个符号感知基准（Amazon-CDs/Vinyl, Epinions, KuaiRand, KuaiRec）上评测：
- **精度提升**：所有实例在全部数据集上匹配或超越无符号骨干，最高Recall@20提升+32.6%（Turbo-CF在KuaiRand）。DualSpectralCF-Cheby在4/5数据集上超过LightGCN（需训练）。
- **效率优势**：比SIGformer快7.7-155.3倍，却达到其70.7%-90.7%的Recall@20；训练免梯度实例耗时仅8.5-23.8秒。
- **冷启动增益**：对训练样本1-5条的用户，Recall@20最高提升+29.2%（Epinions），负信号有效缓解正样本稀疏问题。
