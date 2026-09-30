---
title: 'TabFM-Auto: Self-Evolving Pipelines for Tabular Foundation Models'
title_zh: TabFM-Auto：LLM Agent 自进化表格基础模型流水线
authors:
- Deqing Fu
- Huangyuan Su
- Rajat Sen
- Taman Narayan
- Sujay Sanghavi
- Abhimanyu Das
- Weihao Kong
affiliations:
- Google Research
- Google DeepMind
- University of Southern California
- Harvard University
- University of Texas at Austin
arxiv_id: '2609.37989'
url: https://arxiv.org/abs/2609.37989
pdf_url: https://arxiv.org/pdf/2609.37989
published: '2026-09-28'
collected: '2026-09-30'
category: Agent
direction: LLM Agent 驱动表格数据流水线自动进化
tags:
- Tabular Foundation Model
- LLM Agent
- AutoML
- Feature Engineering
- Pipeline Search
- Self-Evolving
one_liner: 将 LLM 编码代理与冻结表格基础模型结合，只进化数据流水线，拿下 TabArena 与 MLE-Bench-Tabular 榜首
practical_value: '- 冻结主模型、只让 LLM agent 搜数据/特征/采样/后处理：在推荐/广告 CTR 模型上，可冻结已训练好的排序/召回模型，让
  agent 围绕它生成特征工程、样本选择、校准代码，用离线验证集反馈，避免边改模型结构边训练的噪声。

  - 从列名/元数据自动生成领域特征：电商表格中大量业务字段（价格、类目、用户/商品 ID），LLM 可生成 price_ratio、category co-occurrence、user-item
  graph degree 等显式特征，免去模型从原始数值中隐式推断。

  - 上下文采样 + 先验校准应对不平衡：类似论文中对少数类过采样多视图并在 log-odds 空间做先验修正，适合电商点击/转化率预估中的正负样本不平衡、稀有类目。

  - 严格测试隔离与防泄漏：搜索只在单 fold 训练集内部 3 折 CV，沙箱禁网且不挂测试集；分类数据 shuffle 防止行号/排序泄漏。这些工程细节可直接照搬进推荐模型自动调参/特征搜索
  pipeline。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
表格基础模型（TabFM 等）在合成表格上预训练，zero-shot 很强，但只看数值和类别索引，不理解列名、任务描述、辅助文件语义；同时 LLM coding agent 从零训练模型时联合搜特征/架构/超参，训练噪声大、易过拟合。将二者结合，让 LLM agent 围绕冻结 TabFM 进化数据流水线，既注入领域语义，又避免重训噪声。

**方法关键点**  
- 流水线分四模块：`preprocess()` 数据清洗与目标变换；`engineer()` 语义特征工程（领域公式、统计特征、辅助文件摘要）；`sample()` 上下文采样（分层/过采样少数类、多视图）；`postprocess()` 校准与逆变换；`TABFM_KWARGS` 控归一化、NNLS 等通用设置。  
- 搜索在训练集内部做 3 折 CV，以验证指标为反馈，保持 TabFM 冻结、无梯度更新；沙箱隔离测试集、断网，防止泄露；每个候选流水线快速评估。  
- 起点是 identity pipeline，agent 迭代 patch `pipeline.py`；搜索完成后冻结 P*，仅在官方 test 上评一次。

**关键结果**  
- TabArena 51 数据集（38 分类/13 回归），五种 TabFM-Auto 配置包揽 Elo 前五；最佳 Codex+Opus 5 将 TabFM 从 1785 提到 2013 Elo（+228），超 4h AutoGluon extreme 约 345 Elo。  
- 分类 Elo 1966.3，回归 Elo 2512.9；oracle improvability 降到 1.26%–1.88%。  
- 发现的 pipeline 迁移到其他冻结 TFM：TabICLv2 +143 Elo，TabPFN-3 +131，EXAONE-Tabular +89。  
- MLE-Bench-Tabular 8 比赛中 Elo 第一（1827），Opus 5 变体赢 86.7% 比赛。  
- 在能识别真实世界列名的 17 个数据集上，领域公式带来 7.3%–8.2% 误差降低，约为匿名表上的 3 倍。

**最值得记住**  
LLM 编码代理 + 冻结基础模型，只搜数据 pipeline，是低噪声、可迁移的自动机器学习范式；领域知识主要从列名和元数据显式转到特征里。
