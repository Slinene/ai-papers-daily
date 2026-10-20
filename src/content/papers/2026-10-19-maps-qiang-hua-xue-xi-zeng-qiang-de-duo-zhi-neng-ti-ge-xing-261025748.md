---
title: 'MAPS: A Multi-Agent Personalized Script-Driven Video Advertising System Enhanced
  by Reinforcement Learning'
title_zh: MAPS：强化学习增强的多智能体个性化脚本驱动视频广告系统
authors:
- Zhongyu Wang
- Chen Zuo
- Qingxuan Sun
- Jiayang Qiao
- Qiuhao Qian
- Songyan Cui
- Guocheng Chen
affiliations:
- Beihang University
- Kuaishou Technology
arxiv_id: '2610.25748'
url: https://arxiv.org/abs/2610.25748
pdf_url: https://arxiv.org/pdf/2610.25748
published: '2026-10-19'
collected: '2026-10-20'
category: MultiAgent
direction: 多智能体广告生成与 RL 对齐
tags:
- Multi-Agent
- RL
- GRPO
- Video Advertising
- Personalization
- LLM-as-a-Judge
one_liner: 多智能体闭环生成个性化视频广告脚本，结合 GRPO 多维奖励，在线 CTR/CVR/ARPU 显著提升
practical_value: '- Profile Agent 用 MLLM 从异构行为序列提炼四维用户画像（topical interests、presentation
  style、implicit needs、decision-making tendencies），可替换传统 embedding 画像，适合 Agent 化推荐/广告系统的用户理解模块。

  - 奖励函数拆成 Rule-based Structural + LLM-as-a-Judge Personalization + Product Alignment，权重
  0.3/0.4/0.3；业务里生成文案/脚本/素材时可直接复用，结构合规用规则、偏好对齐和事实一致性用 LLM Judge，避免只优化 CTR 跑偏。

  - SFT + GRPO 两阶段训练：SFT 冷启动学格式，RL 用组内相对优势和 KL 约束贴近 SFT；LoRA rank 32 微调 Qwen3-VL-8B。GRPO
  不需要 critic，适合用 LLM-as-a-Judge 做 reward 的生成对齐任务，工程成本低。

  - Reflector Agent 对线上负反馈做 profile-level vs script-level 归因，只回传 minimal revision，避免全量重新生成；适合低延迟闭环迭代，在推荐/广告系统中可把反馈打到画像或脚本局部，而不是重跑
  pipeline。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

动机：传统个性化视频广告多采用 retrieval-based 范式，从预生产素材库匹配用户特征，受静态库存和反馈延迟限制，无法做到细粒度个性化，且用户反馈只能影响下一轮生产。MAPS 将其转变为在连续创意空间中的动态生成优化。

方法关键点：
- 四个协同 Agent 形成闭环：Profile Agent（Qwen3-VL-32B）从历史交互和当前上下文提炼四维用户画像；Scripter Agent（Qwen3-VL-8B）生成结构化脚本；Director Agent（Kling-Omni）结合产品视觉资产合成视频；Reflector Agent 对线上信号归因并回传 minimal revision。
- Scripter 采用两阶段训练：SFT 学脚本格式与结构；GRPO RL 用多维奖励对齐个性化与产品一致性。奖励 Rtotal=0.3·Rstruct+0.4·Rpers+0.3·Rprod，其中 Rstruct 为规则检查格式/完整性/一致性/物理合理性，Rpers 和 Rprod 均采用 LLM-as-a-Judge 分别评估呈现/内容偏好与产品身份/品牌/卖点一致性。
- 闭环机制：Reflector 区分 profile-level 与 script-level 原因，做出低延迟、有界成本的局部修订，使创意跨曝光迭代演化，无需整条 pipeline 重跑。

关键结果：
- 离线在 PCG-Bench 和 PCI-Bench 上，MAPS 在个性化、产品对齐、视频质量、多样性和集成质量全面超过 NextAds 等基线；消融显示加入 RL 后个性化 +1.25、产品对齐 +1.04。
- 在线 A/B（快手广告某场景）：相比生成式基线 GRM，CTR +2.87%、CVR +2.74%、ARPU +9.85%；相比 DLRM 检索基线提升更高（+4.88%/+4.01%/+12.89%）。

最值得记住的一句话：把 script 作为规划与生成之间的中心接口，用多维奖励 RL 同时对齐用户偏好与产品事实，是让广告从检索素材走向生成创意的关键。
