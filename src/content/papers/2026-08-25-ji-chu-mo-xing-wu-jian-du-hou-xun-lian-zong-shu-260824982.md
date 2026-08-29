---
title: 'Unsupervised Post-Training of Foundation Models: A Survey'
title_zh: 基础模型无监督后训练综述
authors:
- Yijie Xu
- Qianyi Cai
- Huizai Yao
- Yili Wang
- Tianfu Wang
- Cehao Yang
- Xingbo Yao
- Zhiyu Guo
- Aiwei Liu
- Xuming Hu
affiliations:
- HKUST(GZ)
- HKUST
- Xiaohongshu Inc.
- WeChat, Tencent
- CUHK
arxiv_id: '2608.24982'
url: https://arxiv.org/abs/2608.24982
pdf_url: https://arxiv.org/pdf/2608.24982
published: '2026-08-25'
collected: '2026-08-29'
category: Training
direction: 无监督后训练 · LLM
tags:
- Unsupervised Post-Training
- LLM
- Self-Training
- Survey
- Foundation Models
one_liner: 系统梳理80种无监督后训练方法，按内部信号来源分类并提出Input Visibility×Update Persistence统一框架
practical_value: '- 可借鉴无监督后训练思路，利用电商/广告场景中大量无标签的 query、商品描述、用户行为文本对 LLM 做领域适配，减少人工标注成本。

  - 四类内部信号（预测统计、样本关系、自生成目标、内部评估器）中，自生成目标（伪标签、rationale、curricula）在业务语料上最易落地：用当前模型对弱标注数据生成伪标签再做自训练，注意配合置信度过滤。

  - 内部评估器（self-reward）用于排序/推荐模型微调时需警惕误差递归放大，建议与在线 A/B 指标绑定，避免仅依赖模型自评。

  - Input Visibility×Update Persistence 框架可帮助决定部署形态：对时延敏感的在线推荐模块采用离线更新+冻结参数，对离线生成模块可做在线持续无监督更新。'
score: 7
source: arxiv-cs.MM
depth: abstract
---

**动机**
基础模型后训练长期依赖人类标签、偏好数据、强教师或可执行验证器。无监督后训练（UPT）放弃外部监督，仅使用无标注 prompt、文本或目标输入，从模型自身的样本、分布、判断或课程中提取更新信号。UPT 适用于新领域语料快速适配、标签和验证器不可获取的场景。

**方法关键点**
该综述系统梳理了 80 种严格 UPT 方法，按提供更新信号的内部对象分为四类：
- **预测统计优化**：使用 NLL、熵、置信度等统计量。
- **样本关系监督**：利用多数投票、语义聚类等。
- **自生成目标引导**：基于伪标签、rationale、课程进行自举。
- **内部评估器**：模型自评或自奖励。

除分类外，论文指出内部信号与任务结构的选择决定后训练是改善模型还是递归放大误差。并引入正交的 **Input Visibility × Update Persistence** 视角，统一描述部署形态与评估选择。

**关键结果数字**
- 收录 80 种严格 UPT 方法。
- 覆盖 2023 至 2025–2026 年加速涌现的第三波后训练范式。
- 结论表明无监督机制多为模态无关，可通用于文本与多模态大模型。
