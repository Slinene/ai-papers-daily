---
title: 'MMSearch-OPD: Easy Made Hard, Hard Made Learnable for Long-Horizon Multimodal
  Search Agents'
title_zh: 可控数据升格 + 联合 RL/在线蒸馏的长程多模态搜索智能体
authors:
- Huanyao Zhang
- Jiepeng Zhou
- Jiaye Lin
- Ontai Tang
- Jingtian Hao
- Mugeng Liu
- Ru Peng
- Lang Mei
- Xiaohan Yu
- Liyan Liu
affiliations:
- Peking University
- HKUST(GZ)
- Tsinghua University
- The University of Hong Kong
- Huawei Cloud BU
arxiv_id: '2610.22240'
url: https://arxiv.org/abs/2610.22240
pdf_url: https://arxiv.org/pdf/2610.22240
published: '2026-10-15'
collected: '2026-10-16'
category: Agent
direction: 多模态搜索 Agent 训练
tags:
- Multimodal Search
- Agent
- RL
- On-policy Distillation
- Data Synthesis
- Long-Horizon
one_liner: 用可控问题升格与联合 RL/在线蒸馏，把易题变难、难轨迹变可学
practical_value: '- 可复用的问题升格框架：Expand/Blur/Visualize 把已有简单 VQA 或搜索日志升级为长链、实体消歧、跨模态证据任务；电商场景可把“这是什么商品”改写成多跳品牌/历史/场景链，并要求买家秀或商品图反搜验证，提升训练数据难度。

  - 难度与质量双筛选：先用直接答案探针过滤参数化捷径，再用专家 rollout 的 Pass@k 评估难度并分池；业务上可先易样本 SFT，再难样本 RL，减少奖励噪声和人工标注成本。

  - RL 训练中加入行为惩罚与 token 级 OPD：只对失败或不完美轨迹启用在策略蒸馏，教师信号按 reward gap 加权，并指数衰减 λ；这比纯终局奖励更稳定，适合搜索/推荐
  Agent 的 RLVR 训练。

  - 监控行为经济性：训练后期 tool call 和 response length 下降但答案奖励不降，说明可先鼓励长程探索、后收紧效率；在线上 Agent
  优化中可用同样指标做早停。'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

动机：长程多模态搜索需要持续获取文本与视觉证据，但高质量困难训练问题稀缺，且终局奖励无法有效反馈中间过程。

方法关键点：
- Refine 数据管线复用已有的简单 image-question 对：BuildLink 抽取种子实体链；Expand 在链尾追加 L 个 web 证据支持的 hop；Blur 对 M 个节点用 W 条间接事实替换实体名，强制消歧；Visualize 选 N 个节点附加最多 P 张可检索图像和 Q 条视觉事实，提升跨模态证据要求。
- 质量控制：直接答案探针去除参数化捷径；专家工具 rollout 的 Pass@k 近似评估难度，并据此选择 SFT 演示和 SFT/RL 分池。
- 训练：教师由更大模型 SFT 后冻结；学生先 SFT 初始化，再联合 GRPO（答案奖励 + 行为惩罚）与 token 级 OPD。OPD 仅对不完全正确的轨迹启用，log 概率差按 reward gap 加权，指数衰减系数降低教师依赖。

关键实验：在 MMSearch、LiveVQA、BrowseComp-VL、MM-BrowseComp、MMSearch-Plus、BrowseComp-V3、VisBrowse-Bench 七个 benchmark 上，MMSearch-OPD-9B 平均 60.2，比同底座 agentic workflow 高 15.3 点，比 DeepVoyager-VL-8B 高 9.6 点；27B SFT 教师平均 63.2。Refine 使 BrowseComp-V3 +15.0、VDR +6.8、SimpleVQA +6.3、FVQA +2.0，平均 tool call 从 6.61 增至 33.71。Pipeline 逐级增难时，100 题准确率从 79% 降到 33%，但 ImageSearch+FetchImage 占比从 6.3% 升至 47.5%。RL 阶段 answer reward 从 0.347 提升到 0.587，后期 tool call 与回复长度下降但答案质量不降。

最值得记住的一句话：用可控制的数据升格把容易的问题变难，再用 reward-gap 加权的选择性在线蒸馏把难轨迹变得可学。
