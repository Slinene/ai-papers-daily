---
title: Empowering GUI Agents via Autonomous Experience Exploration and Hindsight Experience
  Utilization for Task Planning
title_zh: 利用自主经验探索与后见经验提升GUI代理任务规划能力
authors:
- Tianyi Men
- Zhuoran Jin
- Pengfei Cao
- Yubo Chen
- Kang Liu
- Jun Zhao
affiliations:
- Institute of Automation, Chinese Academy of Sciences
- University of Chinese Academy of Sciences
arxiv_id: '2606.27330'
url: https://arxiv.org/abs/2606.27330
pdf_url: https://arxiv.org/pdf/2606.27330
published: '2026-06-25'
collected: '2026-06-26'
category: Agent
direction: GUI Agent · 经验回放与任务规划
tags:
- GUI Agent
- Task Planning
- Hindsight Experience
- MLLM
- Autonomous Exploration
- OOD Generalization
one_liner: 提出PEEU方法，通过自主环境探索与后见经验构造高层次训练数据，显著提升小型MLLM的规划与跨网站泛化能力
practical_value: '- **后见经验构造训练数据**：将失败/成功的交互轨迹反向转化为严格对齐的规划级训练样本，可借鉴到电商Agent的购物任务拆解中，用用户实际浏览-购买路径生成高质量指令数据。

  - **自主环境探索**：让Agent在生产前自动探索网站结构并积累操作经验，类似推荐系统中的冷启动探索，适合构建电商网页的预训练经验库，减少人工标注。

  - **分层任务分解视角**：TDHAF框架揭示高层次任务训练比原子技能训练更利于分布外泛化，提示在构建购物助手时应优先训练完整任务流（如“比价后下单”），而非单个点击指令。

  - **小型MLLM潜力**：7B模型超越32B模型，证明通过数据策略可压缩模型成本，适合边缘部署的电商隐私保护场景。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：多模态GUI代理在自动化重复网页操作中表现不佳，小型开源MLLM虽成本与隐私友好，但存在规划能力弱、跨网站泛化差的问题。

**方法**：提出PEEU方法，包含两层关键创新：(1) 自主探索阶段，代理在环境中随机操作并记录完整轨迹，从中提取通用操作经验；(2) 后见经验利用阶段，根据成功或失败的最终状态反向生成严格对齐的高级规划任务描述，将原始轨迹转化为“任务→规划”的高质量训练对。同时提出任务分解层次分析框架TDHAF，将组合泛化能力按任务粒度分为低/中/高三级进行系统评估。

**结果**：在真实世界基准测试中，基于7B参数的模型达到30.6%准确率，超越Qwen2.5-VL-32B等更大模型。实验分析表明，高层次任务训练比原子技能训练更能提升分布外泛化能力，论证了构造后见高层次任务与利用经验对小型MLLM规划泛化的关键作用。
