---
title: 'TabFM: A Zero-Shot Foundation Model for Tabular Data'
title_zh: TabFM：表格数据的零样本基础模型
authors:
- Weihao Kong
- Erez Louidor Ilan
- Shuxin Nie
- Taman Narayan
- Rajat Sen
- Yichen Zhou
- Deqing Fu
- Samet Oymak
- Abhimanyu Das
affiliations:
- Google Research
arxiv_id: '2609.37959'
url: https://arxiv.org/abs/2609.37959
pdf_url: https://arxiv.org/pdf/2609.37959
published: '2026-09-28'
collected: '2026-09-30'
category: Other
direction: 表格基础模型 · 零样本学习
tags:
- Tabular Foundation Model
- In-Context Learning
- Zero-Shot
- Feature Engineering
- LLM-guided AutoML
- Synthetic Data
one_liner: 400M参数表格基础模型，以in-context learning实现零样本监督预测，在TabArena 51数据集上超越AutoML与现有表格基础模型
practical_value: '- 针对推荐/广告中的表格数据预测（CTR/CVR、用户行为特征建模），可以借鉴 TabFM 的行列解耦注意力：列向 ISAB
  做 O(T·m) 跨样本聚合，行向 SAB + RoPE 做特征交互，CLS tokens 池化支持 16k 样本不爆炸，适合大规模样本 in-context
  推理。

  - TabFM+ 的推理期多视图增强很实用：随机列排列 + 交叉特征/SVD 特征注入 + NNLS 集成 + Platt 校准；在冻结模型权重下即可提升稳健性，可低成本迁移到现有特征工程管线。

  - TabFM-Auto 思路：用 LLM 生成特征工程代码，内部闭环 CV 评分迭代，冻结主模型权重；可借鉴做推荐系统特征自动发现，如交叉特征、聚合特征、目标编码等，减少人工试错。

  - 纯合成 SCM 数据训练的通用表格表示能零样本迁移，提示可以构建因果结构模拟用户/物品特征生成，减少对真实标签数据的依赖，用于冷启动或小样本场景。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：传统表格监督学习依赖逐数据集调参，GBDT 与 AutoML 每次从零开始。表格基础模型试图通过 in-context learning 一次前向得到预测，但表格数据的行可交换性、混合列类型以及朴素注意力 O(T²H²) 的复杂度限制其规模。TabFM 用 400M 参数 Transformer 解决这一问题。

**方法关键点**：
- 输入层：Fourier 频率银行做 cell embedding，dyadic feature grouping（offsets 0,1,3）捕捉局部特征交互；数值/分类列分开投影。
- 架构：交替 column-wise ISAB（诱导点注意力，O(T·m)）与 row-wise SAB + RoPE，通过 8 个 CLS tokens 池化为固定宽度行表示；24 层 in-context predictor 用非对称 mask 保证查询条件独立，支持 16,384 上下文行。
- 预训练：100% 合成数据，从结构因果模型（SCM）采样，联合随机化表形状、类别比例、缺失、噪声、类别平衡；四阶段课程从 2,048 到 16,384 行，保持每步 token 数固定。
- TabFM+：冻结权重，多视图推理：交叉特征与 Truncated SVD 特征池，随机列排列/分类重编码/标准化/Yeo-Johnson/离群值 clip，32 视图通过正则化 NNLS 与 Platt 校准集成。
- TabFM-Auto：LLM（Gemini 3.8 Flash）闭环生成特征工程代码，3 折 CV 评分，6 小时/96 次评估，冻结基础模型权重。

**关键实验**：TabArena 51 数据集（38 分类 13 回归），对比 AutoGluon、TabPFN-3/2.6、TabICLv2、EXAONE-Tabular、LightGBM 等 67 配置。零样本 TabFM 分类 Elo 1768.6，回归 Elo 2055.2，均在默认基础模型中第一；TabFM+ 分类 +69.4 Elo、回归 +134.0 Elo；TabFM-Auto 分类 +172.1 Elo、回归 +337.2 Elo，41/51 数据集优于零样本 TabFM，回归全部 13 数据集改善，improvability 0.00%。

**最值得记住的一句话**：通过行列解耦注意力 + 纯合成 SCM 预训练，TabFM 实现可扩展到 16k 行的表格 in-context learning，并在冻结权重上加多视图集成和 LLM 闭环特征工程大幅超越 AutoML。
