---
title: Enhancing Numerical Prediction in LLMs via Smooth MMD Alignment
title_zh: 通过平滑 MMD 对齐增强大语言模型的数值预测
authors:
- Zhuo Zuo
- Li Yue
- Wenhao Zheng
- Chenpeng Wang
- Xianggen Liu
affiliations:
- College of Computer Science, Sichuan University, Chengdu, China
- Dongfang Electric (Chengdu) Academy of Science and Technology Co., Ltd., Chengdu,
  China
- Institute of Medical Information & Library, CAMS & PUMC, Beijing, China
arxiv_id: '2606.27731'
url: https://arxiv.org/abs/2606.27731
pdf_url: https://arxiv.org/pdf/2606.27731
published: '2026-06-26'
collected: '2026-06-29'
category: Training
direction: LLM 数值预测 · 分布对齐训练损失
tags:
- SMMD
- MMD
- numerical prediction
- loss function
- LLM training
- kernel design
one_liner: 提出 SMMD 损失，用数值距离核与图平滑将对齐预测分布，一致提升 LLM 数值精度
practical_value: '- **数值敏感推荐场景损失替代**：在需精确数值的任务（如价格预估、销量预测、广告出价、用户评分）中，可将标准交叉熵替换为 SMMD，将输出视为连续分布对齐而非离散
  token 分类，减少“数字错位”错误。

  - **数值子词表与距离核设计**：显式划分数值 token 子词表，构造基于值距离的 RBF 核，将 token 概率分布映射到数值空间进行 MMD 匹配。电商搜索排序中的分数校准、点击率预估等场景可直接复用此核构建策略。

  - **局部平滑正则引入**：利用核图在相邻数值间施加输出残差平滑约束，抑制跳变预测。推荐系统中用户偏好分数、物品特征值等的生成，可借鉴该平滑项提升预测一致性与鲁棒性。

  - **即插即用训练组件**：SMMD 仅修改损失项，不改变模型结构，可轻量集成到现有 LLM fine-tune 流程中，尤其适合需要数值输出的 Agent
  决策（如动态定价、预算分配）。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：LLM 在处理需要精确数值输出的任务时常常不可靠，因为标准交叉熵将数字 token 视为无顺序的离散类别，完全忽略了数值间的度量结构和大小关系。

**方法**：提出 SMMD（Smooth Maximum Mean Discrepancy）损失。首先在数值子词汇表上定义基于数值差的 RBF 核，将 token 级的预测概率和目标分布映射到核空间，用 MMD 度量并最小化预测与真实数值分布之间的差异；同时，在核诱导的图上对相邻数值的预测残差施加平滑正则，强制局部一致性。SMMD 是纯损失函数层面的改进，不改变模型架构。

**结果**：在数学推理、算术计算、时钟时间识别和图表问答四个数值敏感任务上，基于多个开源 LLM 和 VLM 骨干评估，SMMD 相比交叉熵以及近期提出的数值目标损失（如 NumDec、NTK 等）一致提升准确率。消融表明 MMD 和平滑项效果互补，且基于距离的核设计是关键，简单的 one-hot 核无法带来增益。
