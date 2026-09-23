---
title: 'OmniEdu: Open Foundation Models for Learning and Teaching'
title_zh: OmniEdu：面向学习与教学的开放基础模型
authors:
- Hao Liang
- Qihan Lin
- Meiyi Qiang
- Linzhuang Sun
- Hengyi Feng
- Mingrui Chen
- Sizhe Qiu
- Wentao Zhang
affiliations:
- Peking University
- University of the Chinese Academy of Sciences
- Zhongguancun Academy
arxiv_id: '2609.23088'
url: https://arxiv.org/abs/2609.23088
pdf_url: https://arxiv.org/pdf/2609.23088
published: '2026-09-18'
collected: '2026-09-23'
category: Training
direction: 教育 LLM 能力导向指令微调
tags:
- instruction tuning
- data curation
- educational LLM
- capability-oriented
- synthetic data
one_liner: 以能力平衡的指令微调语料构建教育基础模型，在K-12解题、课程定位与教学辅导上全面提升
practical_value: '- 能力导向的数据组织可迁移到电商/推荐 LLM：按“商品理解/意图预测/解释生成/干预策略”等能力划分 instruction
  数据，而不是按任务来源混合；用 token 预算做多样性采样，防止长尾能力被高频任务淹没。

  - 多阶段数据质控流水线值得复用：确定性规则清洗 + 语义审计重写 + 任务特定质量评分，能显著降低垂直领域微调数据噪声；在电商搜索/推荐场景，可先用 LLM
  对候选样本做语义评分，再按预算筛选。

  - 领域数据与通用 instruction 混合（100+ 教育资源 + 通用指令）保持通用能力，避免灾难性遗忘；电商垂直 LLM 微调时可参考类似配比，保留通用对话与推理能力。

  - 分尺度验证（4B/9B/27B）说明数据策略在不同模型规模上稳定有效，业务选型时可先用小模型快速验证数据配方，再扩展到更大模型。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有教育语言模型要么只做解题，要么只做辅导，训练语料通常按来源或任务组织，没有显式平衡多种教学能力。OmniEdu 旨在构建覆盖 K-12 学习与教学的开放基础模型，同时兼顾学科能力、课程定位、诊断推理和教学行动与脚手架。

**方法关键点**：
- 能力导向的指令微调语料，融合 100+ 教育资源与通用指令，围绕上述四类能力组织。
- 多阶段数据管线：确定性清洗、语义审计与重写、任务特定质量评分、token 预算内的多样性选择、教学指令分配。
- 最终得到 69,999 条样本、15.96M 监督响应 tokens，其中教育特定样本 60,951 条。
- 微调 4B、9B、27B 三个规模模型，并在课程定位、K-12 问题解决、教学辅导及通用能力上进行评估。

**关键结果数字**：
- 教育导向微调在三个教育能力组上随模型规模一致提升。
- OmniEdu-27B 在 K12-Bench 上达到 63.12% EM / 76.69% F1，MathFish 85.89%，EDUMATH 86.95%，MathTutorBench Scaffold 78.74%。
- LongTutor 教学平均分 3.02，为所有评估模型中最高。

这些结果表明，精心筛选且能力平衡的监督数据能把通用 LLM 转化为更强的教育系统，同时具备解题、课程理解和教学交互能力。
