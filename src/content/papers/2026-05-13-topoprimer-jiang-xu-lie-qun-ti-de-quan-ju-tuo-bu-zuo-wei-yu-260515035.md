---
title: 'TopoPrimer: The Missing Topological Context in Forecasting Models'
title_zh: TopoPrimer：将序列群体的全局拓扑作为预测模型的缺失上下文
authors:
- Zara Zetlin
- Kayhan Moharreri
- Maria Safi
affiliations:
- Apple
arxiv_id: '2605.15035'
url: https://arxiv.org/abs/2605.15035
pdf_url: https://arxiv.org/pdf/2605.15035
published: '2026-05-13'
collected: '2026-05-20'
category: RecSys
direction: 时序预测基础模型增强 · 拓扑数据分析
tags:
- persistent homology
- spectral sheaf
- time series forecasting
- cold start
- seasonal spikes
- foundation model adapter
one_liner: 将持久同调和谱层坐标作为冷冻上下文注入预测模型，缩小冷启动差距且抗季节性漂移
practical_value: '- **冷启动与新品上架**：新商品无历史销售数据时，可通过预计算的谱层坐标和群体TDA指纹立即定位其在全局流形中的位置，无需等待历史积累。在内部数据上，TopoPrimer
  在零周历史时 MAE 比普通 Transformer 低 27%。

  - **季节性大促波动**：大促期间需求分布剧烈偏移，传统模型 MAE 上涨 46–50%，而拓扑先验能稳定预测，退化幅度控制在 10% 以内。可将该思路用于电商大促、节假日等场景的库存与销量预测。

  - **轻量适配器范式**：对于已经部署的 Chronos/TimesFM 等预训练基础模型，只需冻结主干网络并训练一个参数量不到主干 0.1% 的拓扑适配器（处理
  TDA、谱层坐标、上下文统计量与缓存预测的分支，输出残差修正），即可在几乎不增加推理成本的情况下嵌入群体拓扑信号。

  - **拓扑预判准则**：用 H1/N（循环密度）快速诊断领域是否具有可利用的循环共动结构（例如电网、天气有真正循环，零售日历周期导致的假循环无效），提前决定是否引入
  TDA 分支，避免在无效领域引入噪声。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
时间序列预测模型（含 Chronos、TimesFM 等基础模型）仅从单条序列的历史建模，丢失了序列群体间的全局关系结构。实际领域中（电商商品群、电网用户群、交通传感器网），全体序列形成一个具有几何结构的流形：聚类、循环共动、边界等。该结构无法从单条序列获取，却可系统性地辅助预测，尤其对冷启动和季节性尖峰有重要意义。

**方法关键点**
- **群体 TDA 指纹**：计算序列间 Pearson 相关距离，构建 VIetoris–Rips 过滤，提取持久同调的 H0（聚类）、H1（循环共动）、H2（边界）的持久景观（persistence landscape），固定为一个 125 维向量，供整个领域共用。
- **谱层坐标**：利用实体-时间矩阵的截断 SVD，取左奇异向量作为每序列的 256 维坐标，反映其在群体流形中的位置。该坐标无需训练，优于学习式神经层网络。
- **注入方式**：全训练 Transformer 模型将拓扑上下文向量广播加到每个输入 token；冻结预训练模型仅训练轻量适配器，分支处理 TDA、谱层、上下文统计与基础预测缓存，输出残差修正。

**关键结果**
四个公开基准（METR-LA, ECL, Monash Weather, M5）上，TopoPrimer 在 Chronos/TimesFM 骨干上普遍提升。ECL 上 Chronos MSE 降低 7.3%，Weather 上 Transformer MAE 降低 7.9%。内部大型数据集（30 万+序列）显示：微调骨干后拓扑增益几乎不变（ΔMAE -0.024），证明拓扑与序列训练互补；季节性峰值窗口内，普通模型 MAE 上浮 46–50%，拓扑模型仅上浮 10%；冷启动场景 MAE 降低 27%。
