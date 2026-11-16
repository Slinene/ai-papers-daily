---
title: 'Explanations that Transfer: Interpreting Medical Retrieval with Sparse AutoEncoders'
title_zh: 可迁移的解释：用稀疏自编码器解释医学检索
authors:
- Diane Bouchacourt
- Gaëtan Brison
affiliations:
- Doctolib AI Research Lab, Paris, France
arxiv_id: '2611.18179'
url: https://arxiv.org/abs/2611.18179
pdf_url: https://arxiv.org/pdf/2611.18179
published: '2026-11-13'
collected: '2026-11-16'
category: Other
direction: 可解释稠密检索 · 稀疏自编码器
tags:
- Sparse Autoencoder
- Dense Retrieval
- Interpretability
- InfoNCE
- Out-of-Domain Generalization
- Medical IR
one_liner: 将稀疏自编码器用于医学稠密检索，在保留检索性能的同时得到可解释、可跨语料迁移的稀疏特征
practical_value: '- 可以在推荐/搜索的召回阶段，对已有 frozen query/item embedding 后接一个 TopK SAE，用
  MSE+InfoNCE 联合训练；不重训大模型即可获得可解释稀疏特征，并在 in-domain 提升排序质量。

  - 稀疏度 k 和字典规模 m 是有效的容量旋钮。做跨行业/跨场景迁移时，不要只追训练域 NDCG；目标域与训练域分布较远时，选小 k/m 可减少过拟合，提升
  OOD 稳定性。

  - 解释性管道可复用：对每个神经元取 top activating 文本 + TF-IDF/LLM 生成语义标签，再用 Activation Prediction
  LLM 验证。这能解释某个商品/内容为何排在前面，定位是哪些类目、属性、人群概念主导排序，用于 debug 与审核。

  - SAE 神经元可作为离散语义特征，后续可结合倒排索引、steering 或 Semantic ID，做可控检索和可解释生成推荐。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
医学检索依赖黑盒稠密 embedding，查询-文档相关性难以解释，且微调到特定医学语料后容易在跨域语料上掉点。需要一种既能保持/提升检索质量、又能提供可解释特征，同时不过拟合训练域的方法。

## 方法关键点
- 冻结 embedding 模型（BGE、MedEmbed、Gemini），对 query/document 稠密向量训练 TopK SAE，m≫d，每输入只保留 k 个非零激活。
- 联合损失 `L = L_rec + λ L_NCE`：MSE 重建保留原始语义；InfoNCE 直接用医学 ground-truth 正负对拉近相关 query-doc、推开负样本，避免原模型相关性结构不可假设。
- 检索用 sparse code 的 cosine similarity 排序。
- 解释性三通道：Snippets（top activating 文档/query）、TF-IDF 关键词、Interpreter LLM 生成标签/描述/关键词；再用 Activation Prediction LLM 预测神经元是否激活，评估解释质量。解释只在 CURE 上构建，直接迁移到 OOD 语料。

## 关键结果
在 CURE 上训练，评估 6 个医学检索数据（CURE + 5 OOD：MIRIAD、NFCorpus、R2MED 三个子集）。in-domain 所有 k 都超过原始 embedding，BGE dense 61.87 vs original 53.06，k=256 也能到 60.50；在语料离 CURE 较远的 R2MED 上，稀疏 k≤256 与 dense 持平或更好，说明稀疏容量约束可减少跨域过拟合。解释性上，Interpreter LLM 与 TF-IDF 的激活预测 Pearson r 在 CURE 约 0.44，OOD 0.23-0.33；5 位医学专家对 30 个神经元的人工评估达到 r=0.81、AUROC 0.92。案例显示这些神经元能解释为什么相关/不相关文档排名靠前。

一句话：稀疏性不仅给了可解释特征，还作为容量控制改善跨域迁移。
