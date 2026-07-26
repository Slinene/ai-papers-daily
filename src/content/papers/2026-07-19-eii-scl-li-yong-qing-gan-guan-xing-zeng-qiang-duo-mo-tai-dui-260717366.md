---
title: 'EII-SCL: Harnessing Emotional Inertia for Multimodal Emotion Recognition in
  Conversation'
title_zh: EII-SCL：利用情感惯性增强多模态对话情绪识别
authors:
- Zilong Huang
- Kong Aik Lee
- Chong-Xin Gan
- Zezhong Jin
- Ruichen Zuo
- Man-Wai Mak
affiliations:
- The Hong Kong Polytechnic University
arxiv_id: '2607.17366'
url: https://arxiv.org/abs/2607.17366
pdf_url: https://arxiv.org/pdf/2607.17366
published: '2026-07-19'
collected: '2026-07-26'
category: Multimodal
direction: 多模态对话情绪识别 · 情感惯性
tags:
- MERC
- Contrastive Learning
- Emotional Inertia
- Multimodal
- Conversation
- Dialogue
one_liner: 提出情感惯性引导的监督对比学习模块，无需额外数据即可提升多模态对话情绪识别
practical_value: '主要是学术贡献，但以下点可借鉴到对话式推荐、智能客服等对话系统中：

  - 在对话状态追踪中引入情感惯性先验：假设用户情绪短期连续，可在特征序列上构建正负样本窗口，设计对比损失增强情绪特征一致性。

  - 插件式模块设计：EII-SCL 作为即插即用的模块，可嵌入现有多模态对话模型（如多模态 RecBot），无需修改主网络结构。

  - 无需额外标注：通过利用对话历史标签构造时序邻域样本，不增加标注成本，适合实际业务中标签稀疏的场景。

  - 时序窗口对比方法可迁移到会话推荐：在序列推荐中，利用用户短期行为惯性构造对比样本，提升兴趣漂移建模。'
score: 6
source: arxiv-cs.MM
depth: abstract
---

**动机**：多模态对话情绪识别（MERC）现有方法主要建模复杂上下文依赖，却忽略对话中的情感惯性——情绪状态在短时间内倾向于保持，这导致情绪转变建模不佳。

**方法**：提出情感惯性引导的监督对比学习模块（EII-SCL）。在对话的时序窗口内，利用情感惯性先验构造正样本（同一窗口内同情绪样本）和负样本（窗口内情绪突变的样本），设计监督对比损失，从而增强特征空间的簇内一致性和簇间分离性。该模块与现有 MERC 模型无缝集成，无需额外数据或标注。

**结果**：在 IEMOCAP 和 MELD 两个基准上，EII-SCL 均一致超越当前最优方法，证明情感惯性作为先验的有效性。
