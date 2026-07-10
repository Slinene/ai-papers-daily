---
title: 'BACH: A Bayesian Admixture of Contrastive Heads for Multi-Interest Two-Tower
  Retrieval'
title_zh: BACH：多兴趣双塔检索的贝叶斯混合对比头模型
authors:
- Quoc Phong Nguyen
- Paul Albert
- Long Vuong
- Vuong Le
- Julien Monteil
affiliations:
- Amazon
arxiv_id: '2607.08107'
url: https://arxiv.org/abs/2607.08107
pdf_url: https://arxiv.org/pdf/2607.08107
published: '2026-07-09'
collected: '2026-07-10'
category: RecSys
direction: 多兴趣双塔模型 · 变分混合路由
tags:
- Multi-Interest Retrieval
- Variational Inference
- Two-Tower
- Mixture Model
- Power-Spherical
- Admixture
one_liner: 将多兴趣检索建模为用户混合模型，用变分推断产生软路由和个性化权重，缓解头坍缩并提升 top‑rank 质量。
practical_value: '- 用软路由替代硬 argmax：训练时每个头都接收梯度，直接缓解 winner‑take‑all 头坍缩。电商多兴趣场景可避免热门品类独占所有头，提升冷门兴趣召回覆盖。

  - 学习 per‑user 兴趣重要性权重 π_u：由门控塔单独产出，服务时结合到排名分数中，替代简单的 max‑union 或均匀加权。电商推荐中不同类目偏好强度差异大，用学习的重要性权重可更精准分配展示配额。

  - 全局兴趣码书 + 预计算检索：当兴趣头固定为全局码书，仅 π_u 个性化，候选列表可离线预计算，实时服务只需按 π_u 重排缓存列表，省去每个用户的 ANN
  查询。适合延迟敏感的大规模电商检索，且支持冷启动与新上下文快速适配。

  - 训练‑服务一致性带来显著增益：实验证实对所有候选做 max‑over‑heads（all‑multihead）比仅在正样本上取 max 有 9–29% R@100
  提升，提醒应始终让训练评分规则与服务一致。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：双塔检索用单个向量压缩用户，难以覆盖多个兴趣；现有多兴趣模型多采用硬路由（argmax）训练，容易导致头部坍缩，且无法给出 per‑user 的兴趣重要性，服务时只能假设各头均匀重要。

**方法关键点**
- 将用户 k 个兴趣头建模为 **per‑user 混合模型**，每个头对应一个 softmax 组件，生成物品的条件概率为各组件加权和。
- 用 **变分推断** 拟合该混合模型，引入球面后验（power‑spherical / von Mises‑Fisher）作为识别后验，计算软责任 γ，使得所有头都接收梯度，打破硬路由的赢者通吃。
- 学习 **用户专属混合权重 π_u**（通过独立的门控塔），训练时同时优化 ELBO；服务时用自归一化的混合密度 \(m(i|u)=\sum_r \pi_u^{(r)} C_d(\kappa_r) \omega_{\kappa_r}(\langle u^{(r)}, v_i\rangle)\) 排序，保持训练‑服务一致。
- 浓度 κ_r 仅通过 KL 项进入 ELBO，**无需先验即可自正则**，避免过平滑或 one‑hot。
- 提供 **全局码书变体**：兴趣头共享，仅 π_u 个性化，服务退化为预计算列表的加权重排，大幅降低在线计算量。

**关键实验结果**
- 数据集：MovieLens-20M、Taobao、Netflix，全部为序列推荐 next‑item 检索任务。
- 对比基线：单向量双塔、硬路由多兴趣 (all‑multihead, pos‑multihead)、MIND、ComiRec、SASRec。
- BACH 在所有头数 (k=8,16,32) 下均优于最强基线 all‑multihead：
  - MovieLens‑20M：p‑BACH (k=32) AUPRC 0.069 vs. all‑multihead 0.067 (+3.6%)；
  - Taobao：v‑BACH (k=32) AUPRC 0.023 vs. 0.022 (+5.0%)；
  - Netflix：v‑BACH (k=32) AUPRC 0.091 vs. 0.080 (+12.7%)。
- 路由消融表明，**all‑multihead 全面优于 pos‑multihead**（R@100 提升 9–29%），验证了训练‑服务一致的重要性。
- 浓度 κ 在不同运行中始终保持在 20–30 的合理范围，无需超参调优。
