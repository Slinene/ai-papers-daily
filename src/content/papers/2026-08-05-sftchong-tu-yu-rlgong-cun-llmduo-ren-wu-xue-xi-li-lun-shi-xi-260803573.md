---
title: 'SFT Conflicts, RL Coexists: A Theoretical and Empirical Analysis of Multi-Task
  Learning for LLMs'
title_zh: SFT冲突与RL共存：LLM多任务学习理论实证分析
authors:
- Kejian Zhu
- Zhuoran Jin
- Shangqing Tu
- Hongbang Yuan
- Yushi Bai
- Kang Liu
- Juanzi Li
- Jun Zhao
affiliations:
- 中国科学院自动化研究所
- 中国科学院大学
- 清华大学
arxiv_id: '2608.03573'
url: https://arxiv.org/abs/2608.03573
pdf_url: https://arxiv.org/pdf/2608.03573
published: '2026-08-05'
collected: '2026-08-11'
category: Training
direction: 多任务RL训练的解耦与并行化
tags:
- SFT
- RL
- multi-task
- gradient interference
- Parallel-RL
- model merging
one_liner: 多任务SFT导致性能崩溃，RL因梯度近似正交而共存，基于此提出Parallel-RL解耦并行训练
practical_value: '- **多任务RL解耦训练**：利用RL更新稀疏且近似正交，可对搜索/推荐的不同目标（如相关性、CTR、多样性）单独训练RL模型，再通过参数求和或平均合并，避免多阶段SFT带来的灾难性遗忘。

  - **具体合并方法**：先独立用GRPO训练各任务得到ΔW，合并时首选简单求和或平均；若存在干扰，采用TIES方法稀疏化合并，消除参数冲突；最后用少量混合数据（5%）快速适应，可进一步提升整体性能。

  - **模块化能力注入**：当需要向现有模型添加新能力（如新业务域）时，可对新任务进行RL微调，然后将ΔW合并入主模型，无需重训整个系统，且不影响原有任务表现。

  - **训练范式选择指导**：SFT更新范数大、任务间重叠高，不适合多阶段或并行训练；推荐系统中若需微调LLM，应优先使用RL，并在多任务设定下避免多阶段SFT，以保持旧任务性能。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
在多任务训练中，监督微调（SFT）常随阶段增加导致性能剧烈下降，而强化学习（RL）却能实现多任务稳定提升。这一现象——“SFT冲突，RL共存”——缺乏系统解释，阻碍了高效多任务LLM训练。

## 方法关键点
- **实证分析**：在数学、科学、逻辑、代码四个推理任务上对比SFT与RL（GRPO）。发现RL参数更新幅度极小（L2范数~0.03，SFT为~7.4），且不同任务更新向量余弦相似度接近零（~10⁻⁵），而SFT相似度高达0.1~1.0；RL更新稀疏，SFT密集。
- **理论推导**：推导梯度干扰上界。SFT干扰由梯度范数限制（`norm-limited`），数值大；RL因优势函数零和性质消去平均梯度，仅保留极小残差，且受on-policy生成限制，干扰由残差方差限制（`variance-limited`），导致跨任务梯度近乎正交。
- **Parallel-RL框架**：基于RL更新的正交性，各任务独立进行RL训练后，对ΔW求和、平均或使用TIES/SVD合并。还可选择5%样本快速适应（Adapted Parallel-RL）。

## 关键实验与结果
- 多阶段SFT平均准确率比基模型下降23.1%，多阶段RL提升24.9%。
- 单任务RL对其他任务几乎无损，SFT则导致严重遗忘（平均下降5.1%）。
- Parallel-RL在1.5B/7B模型上，简单求和合并保留95%单任务RL性能，TIES合并保留97.4%，Adapted Parallel-RL达到单任务RL的102.8%，性能超越单独微调。
- 消融实验表明，移除某任务的ΔW仅使该任务性能骤降（平均7.1%），对其他任务影响极小（+0.6%），验证任务能力解耦。
