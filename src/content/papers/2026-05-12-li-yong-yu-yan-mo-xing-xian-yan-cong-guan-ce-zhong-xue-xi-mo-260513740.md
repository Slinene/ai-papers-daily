---
title: Learning POMDP World Models from Observations with Language-Model Priors
title_zh: 利用语言模型先验从观测中学习POMDP世界模型
authors:
- Valentin Six
- Frederik Panse
- Mathis Fajeau
- Lancelot Da Costa
- Mridul Sharma
- Alfonso Amayuelas
- Tim Z. Xiao
- David Hyland
- Philipp Hennig
- Bernhard Schölkopf
affiliations:
- Max Planck Institute for Intelligent Systems
- IRIIS
- University of California, Santa Barbara
- University of Tübingen
- University of Oxford
arxiv_id: '2605.13740'
url: https://arxiv.org/abs/2605.13740
pdf_url: https://arxiv.org/pdf/2605.13740
published: '2026-05-12'
collected: '2026-05-19'
category: Agent
direction: LLM引导的POMDP世界模型归纳
tags:
- POMDP
- LLM
- world model
- particle filter
- code generation
- MiniGrid
one_liner: LLM生成可执行POMDP代码，通过信念滤波与软距离似然评分，无需隐藏状态即可匹配有监督方法的样本效率
practical_value: '- 在无法获取用户真实意图（隐藏状态）时，可用LLM生成候选的状态转移与观测模型代码，基于历史行为（点击/购买序列）的粒子滤波和软距离似然进行评分迭代，无需人工标注隐藏状态。

  - 将LLM生成的确定性观测模型通过距离核软化，使任何观测都有非零似然，避免粒子滤波崩溃；这一技巧可直接用于离散观测（如商品ID、行为类别）的模型评估。

  - 使用UCB选择父节点进行多轮候选修订，平衡探索与利用，可借鉴到自动化模型搜索或策略迭代的优化流程中。

  - 以可执行代码形式输出世界模型，可审计、可复现，便于部署到在线规划（如用户状态推断与折扣策略），比纯LLM模拟更稳定、更廉价。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
部分可观察环境（如机器人导航、电商用户行为推断）中学习世界模型通常需要大量交互或事后获得隐藏状态监督。本文探究LLM的先验知识能否替代隐藏状态监督，仅从观测-动作-奖励轨迹中归纳出可执行的POMDP模型。

**方法关键点**  
- **模型表示与生成**: LLM根据少量离线轨迹和自然语言任务描述，一次性生成可执行的Python代码，包含转移模型、观测模型、奖励函数和初始状态分布。  
- **信念滤波评估**: 使用粒子滤波传播候选状态，将LLM生成的确定性观测输出通过观察距离核（如网格匹配度、方向差异）软化为非零似然，计算信念期望对数似然作为模型评分，无需真实状态。  
- **迭代优化**: 基于得分和执行诊断（观测距离最大片段、奖励/终止误判）及多模型转移分歧（QBC），用UCB选择父候选进行多轮修订，最终从得分接近最优的候选集中采样最终模型。  
- 该流水线使模型评估与下游规划（A*信念空间规划）共享同一信念表达。

**关键实验与结果**  
在5个MiniGrid环境（Empty、Corners、Lava、FourRooms、Unlock）上，Pinductor的平均奖励和胜率与有隐藏状态监督的POMDP Coder基本持平，并显著超越有状态监督的表格基线（如Unlock中Pinductor胜率83% vs 表格10%）。仅需2-6条离线轨迹即可达到较强性能；信念熵随episode步数平稳下降，且对真实状态的命中率不断上升，表明模型维持了有效推断。消融表明性能随LLM能力提高而改善，并随语义信息减少而下降。

**核心启示**: LLM先验能通过“代码生成+信念评分”闭环替代隐藏状态监督，在部分可观察设定下高效学习可执行世界模型。
