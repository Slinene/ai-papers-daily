---
title: 'From Correctness to Preference: A Framework for Personalized Agentic Reinforcement
  Learning'
title_zh: 从正确到偏好：个性化Agentic RL训练框架
authors:
- Ranxu zhang
- zeyang li
- Jiacheng Huang
- Rui Zhang
- Xiaozhou Xu
- sun zhe
- Yanyong Zhang
- Chao Wang
affiliations:
- University of Science and Technology of China
- Alibaba Group
arxiv_id: '2605.23382'
url: https://arxiv.org/abs/2605.23382
pdf_url: https://arxiv.org/pdf/2605.23382
published: '2026-05-22'
collected: '2026-05-25'
category: Agent
direction: 个性化Agentic RL与偏好评分解耦训练
tags:
- AgenticRL
- Personalization
- PreferenceDisentanglement
- GraphMemory
- RewardDecoupling
- eCommerce
one_liner: 提出PARPO解耦通用质量与个性化偏好奖励并用用户锚点稳定训练，结合偏好解耦奖励模型与演化图记忆，实现闭环个性化智能体优化
practical_value: '- **奖励解耦+用户锚点校准**：在电商客服或推荐Agent中，可将通用任务质量（如回答准确性）与用户偏好（如风格、倾向）分解为两个优化通道，用用户历史平均偏好作为稳定基线，避免跨用户奖励尺度差异导致训练震荡。

  - **偏好解耦降噪**：用户行为常混杂从众与环境因素；采用双分支（兴趣/从众）建模，并利用流行度加权和正交约束分离真实兴趣信号，得到的偏好奖励更干净，可直接用于RL优化。

  - **演化图记忆PSGM**：构建包含用户、技能、工具、场景、轨迹的异构记忆图，通过层次社区发现和两步检索提供个性化上下文；电商Agent可借鉴此结构存储商家操作技能，实现跨场景技能复用与个性化检索。

  - **训练闭环设计**：将偏好识别、策略优化、技能累积形成闭环，训练过程中自动提炼可复用技能，适合构建需要持续进化的个性化Agent（如营销策略推荐、旅行规划等）。'
score: 10
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有Agentic RL多面向可验证任务（如代码、数学），但在电商、旅行规划等真实场景中，同一请求对不同用户的最优行为不同，奖励信号高度个性化。当前方法要么优化通用质量，要么仅在推理时注入用户信息，缺乏训练时直接优化个性化策略的框架。作者指出三大挑战：(1) 通用奖励无法刻画用户偏好且跨用户尺度异质；(2) 观察行为混有从众与情境噪声，难以提取真实偏好；(3) 传统扁平记忆无法支持个性化技能检索。

### 方法关键点
- **PARPO**：将奖励分解为通用任务质量和个性化偏好两个分支，分别计算优势并与用户锚点校准。对每个用户维护历史偏好奖励的移动均值与方差，作为个性化基线（`bu,g = max(组均值, mu⁻γ√vu)`），缓解跨用户奖励尺度不匹配，稳定训练。
- **两阶段偏好解耦奖励模型**：第一阶段通过多视图注意力融合用户画像，重建损失与对比学习训练画像编码器；第二阶段用LightGCN协同信号，分离“兴趣”与“从众”分支，通过流行度反向加权和正交正则迫使解耦，产出用户-动作兼容性得分。
- **偏好对齐技能演化图记忆（PSGM）**：构建用户、技能、工具、场景、轨迹的异构图，用层次社区检测、两步检索（语义召回+二跳邻居扩展）和结构感知排序公式为每步决策提供个性化技能上下文。

### 关键实验
- 在ETAPP、ETAPP-Hard（更强个性化）和工业电商场景SJAgent上，4B/8B Qwen3模型下框架显著超过SkillRL、MemRL等强基线。8B下ETAPP Original的Judge分数从0.7411→0.7708，Hard集从0.7010→0.7275，SJAgent Reward从0.7625→0.8109。
- 消融：移除记忆导致Judge下降0.0702；替换PSGM为扁平检索下降0.0150；移除PARPO的锚点校准下降0.0461（GDPO-style）；去除兴趣/从众分支降0.05左右。
- 人工评估（15专家×20任务）显示，PARPO在“用户相关性”维度优势最大，5组LLM法官一致排名第一。
- 训练动态：PARPO显著提升奖励、成功率、工具调用成功率，KL保持稳定；技能累积呈线性增长，跨场景分布稳定。

> **核心洞见**：个性化Agent训练需要解耦通用质量与用户偏好奖励，并通过用户锚点校准和结构化记忆实现稳定、可扩展的个性化策略学习。
