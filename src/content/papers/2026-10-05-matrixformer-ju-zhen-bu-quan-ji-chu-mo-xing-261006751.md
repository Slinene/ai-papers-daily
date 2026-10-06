---
title: 'MatrixFormer: A Foundation Model for Matrix Completion'
title_zh: MatrixFormer：矩阵补全基础模型
authors:
- Dwaipayan Saha
- Jacob Feitelberg
- Kyuseong Choi
- Raaz Dwivedi
- Anish Agarwal
affiliations:
- Columbia University
- Cornell Tech
arxiv_id: '2610.06751'
url: https://arxiv.org/abs/2610.06751
pdf_url: https://arxiv.org/pdf/2610.06751
published: '2026-10-05'
collected: '2026-10-06'
category: RecSys
direction: 矩阵补全基础模型 · 零样本推荐评分
tags:
- Matrix Completion
- Axial Attention
- Foundation Model
- Synthetic Pretraining
- Recommender Systems
one_liner: 二维网格 token + 轴向注意力的预训练矩阵补全模型，零样本跨域完成插补、评分预测与因果面板补全
practical_value: '- **二维矩阵原生表示替代 entry-wise 展开**：把 user-item 评分矩阵或特征矩阵直接建模为二维 token
  网格，用轴向 attention（行内 feature attention + 列内 datapoint attention）同时捕捉用户维度和物品维度结构，避免像
  TabImpute 那样把每个 entry 变成一条样本导致上下文重复、显存爆炸；在大规模稀疏矩阵补全或召回后特征填充场景可直接复用该架构。

  - **合成低秩/潜因子矩阵预训练，零样本迁移**：训练时完全用合成矩阵，显式混合低秩、宽秩谱、潜因子以及 MCAR/MAR/MNAR 多种缺失机制，并加入稀疏行/列模拟冷启动；训练好的权重可以不做
  fine-tune 直接用于真实推荐评分矩阵、表格缺失值、甚至 LLM benchmark score completion，适合作为内部数据补全或缺失特征填充的基础组件。

  - **Observed-error ensembling 做领域自适应**：用观测样本上最小化标准化重构误差拟合通用补全专家和推荐专家的混合权重，权重解析、单一标量、无需训练；在跨域或新业务数据上可以先跑两个专家、按观测误差自动决定谁的预测更可信，这是一种低成本的多模型融合
  trick。

  - **单次前向 + 窗口推理支持大规模矩阵**：模型一次前向预测全部缺失值，固定列宽下随行数扩展比 entry-wise 方法快 107×；实际线上可用窗口/分块策略（如最多
  2000 行、1000 列）处理大矩阵，并在重叠窗口取平均，兼顾速度与精度。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

## 动机
矩阵补全广泛存在于表格插补、因果面板推断、推荐系统评分预测和 LLM benchmark score completion。现有表格基础模型（如 TabImpute）将每个矩阵 entry 展开为独立样本，在每个目标上重复上下文，丢失二维结构，且推理开销随矩阵规模快速增长。本文希望预训练一个矩阵原生 transformer，在单次前向中为所有缺失值输出完整预测分布，并零样本适配多种下游矩阵补全任务。

## 方法关键点
- **输入表示**：将部分观测矩阵 X 和缺失 mask M 编码为二维网格 token；观测值用共享 value-embedding MLP，缺失值用 learned mask token + 额外 missingness embedding；外围加入可学习的 row/column CLS tokens。
- **轴向注意力架构**：每个 transformer block 交替执行 feature attention（行内跨列）和 datapoint attention（列内跨行），分别建模同一对象的其他变量和同一变量在其他对象上的经验结构；使用 pre-norm RMSNorm、SwiGLU FFN、learned residual gain 和 RoPE。
- **分布预测 head**：共享 decoder MLP 输出 5000 个 bin 的 bar distribution，点预测取分布均值；所有缺失 cell 可并行预测，单次前向完成整个矩阵补全。
- **合成预训练**：完全基于合成矩阵，混合四个家族（低秩、两类宽秩谱、潜因子）和多种缺失机制（MCAR/MAR/MNAR，含稀疏行/列）；训练目标结合对数似然、对 frozen teachers 的 Huber 蒸馏损失和 CDF/ranked probability score；分阶段训练并做 size extension 到 2000×1000。
- **集成策略**：MatrixFormer 为通用 Impute 专家和推荐 RecSys 专家的观测误差凸融合，按每个输入矩阵在观测样本上解析拟合一个混合权重，不训练任何参数。

## 关键实验与结果
- **推理速度**：1024×10 矩阵完成补全 0.0389s，比 TabImpute 快 107×（4.167s）。
- **表格插补**：MissBench 总体 NRMSE 1.580（TabImpute legacy 1.585）；UCI 总体 0.998（ICE 1.172），MCAR/MAR/MNAR 子项均最优。
- **推荐评分预测**：MovieLens 100K RMSE/MAE 0.8874/0.7279，Netflix small 0.8617/0.7330，低于 SVD、PMF、UserKNN 等基线。
- **因果面板**：六个面板中五个获得最低 normalized score；加州吸烟 treated-block RMSE 0.159 vs SDiD 0.212。
- **LLM benchmark score completion**：在 MTEB、Merged、BenchPress 上 R² 高于 Gaussian baseline，最稀疏 Merged R² 0.6464 vs 0.3625；MMLU 上略低于 Gaussian。

最值得记住：**用二维网格 token + 轴向注意力替代 entry-wise 表格展开，能在保持行列结构的同时获得 107× 推理加速，并让同一个预训练权重零样本跨域完成多种矩阵补全任务。**
