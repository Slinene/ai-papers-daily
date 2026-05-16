---
title: 'Beyond Binary: Reframing GUI Critique as Continuous Semantic Alignment'
title_zh: 超越二元：将 GUI 评价重铸为连续语义对齐
authors:
- Yuchen Sun
- Pei Fu
- Shaojie Zhang
- Anan Du
- Xiuwen Xi
- Ruoceng Zhang
- Zhenbo Luo
- Jian Luan
- Chongyang Zhang
affiliations:
- 上海交通大学
- 小米
arxiv_id: '2605.14311'
url: https://arxiv.org/abs/2605.14311
pdf_url: https://arxiv.org/pdf/2605.14311
published: '2026-05-14'
collected: '2026-05-16'
category: Agent
tags:
- GUI Critic
- Metric Learning
- Contrastive Learning
- Test-Time Scaling
- Affordance
- GUI Agent
one_liner: 将 GUI 动作批评从二元分类改革为连续度量学习，在共享 Affordance 空间中恢复层次语义结构，无需额外标注
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

**动机**  
GUI Agent 的 Test-Time Scaling (TTS) 依赖 Critic Model 对候选动作排序，然而现有方法均将批判建模为二元分类。这种简化导致两个结构缺陷：Affordance 坍缩——将层次化的可用性空间压平为 0/1 标签，使得有效但次优动作与语义干扰项难以区分；噪声敏感——二元目标过度拟合模糊的决策边界。实证分析显示，二元模型在 BBBench 上的分数分布严重纠缠，Suboptimal 与 Semantic Distractor 的得分无法分辨，揭示分类准确率不等于真正的语义建模。为可靠 TTS，GUI 批判必须恢复连续的动作质量排序。

**方法关键点**  
- **功能等价假说**：用户指令与最优动作是同一意图的两种表达，共享相同的功能 Affordance。  
- **BBCritic 框架**：将批判转化为连续语义对齐的度量学习问题。  
  - 共享 VLM 编码器将「指令+截图」与「候选动作+截图（带 Set-of-Mark）」分别投影到共享 Affordance 空间，用余弦相似度作为 critic score。  
  - 采用 InfoNCE 损失替代 BCE，利用密集动作空间中的分布依赖关系，自动挖掘语义硬负样本，并保持对标签模糊的鲁棒性。  
  - 两阶段课程学习：Stage 1 通过 OmniParserV2 布局解析生成全量负样本，建立全局语义拓扑；Stage 2 用 VLM rollout 收集高置信度但失败的轨迹作为语义硬负样本，锐化 Suboptimal–Distractor 边界。全程使用弱监督，零额外标注。  

**关键实验**  
- **BBBench 基准**：首个密集动作空间（平均每页≈30 个候选）并带四层层次化标注（Optimal, Suboptimal, Semantic Distractor, Unrelated Error）的 GUI 评判基准，共 18,192 条人类验证样本。  
- **语义建模**：BBCritic-3B 在 NDCG@All 达到 80.56，超越 7B 参数的二元 SOTA（如 GAIA、GUI-Critic-R1），且在各 Pairwise Preference Accuracy 上保持稳定的层级排序。  
- **TTS 提升**：在 AndroidControl 上提升 +15.1 成功率（Qwen2.5VL-7B 基线+ BBCritic-3B->62.3%），在 GUI Odyssey 上提升 +15.3。  
- **跨平台零样本泛化**：未见过桌面/网页数据，在 ScreenSpotV2 上平均增益 14.2%，在 Mind2Web 上增益 7.3%。  
- **鲁棒性分析**：在随机标签噪声下，二元模型决策边界迅速崩溃，BBCritic 保持稳定；消融实验证实两阶段课程互补，Stage 1 建立拓扑，Stage 2 锐化边界。

**核心启示**  
GUI 批判的本质是度量学习，而非分类。
