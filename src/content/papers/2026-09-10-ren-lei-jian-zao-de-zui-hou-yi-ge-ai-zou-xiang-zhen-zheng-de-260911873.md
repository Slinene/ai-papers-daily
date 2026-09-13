---
title: 'The Last AI Built by Humans: Toward Genuine Recursive Self-Improvement'
title_zh: 人类建造的最后一个AI：走向真正的递归自我改进
authors:
- Yi Duan
- Ying Liu
- Zirui Tang
- Haodong Chen
- Jun Zhou
- Yumou Liu
- Bangrui Xu
- Yukai Wu
- Sidi Chen
- Yuhan Zhou
affiliations:
- Shanghai Jiao Tong University
- Theseus Labs
- Tsinghua University
- ByteDance
- Shanghai AI Lab
arxiv_id: '2609.11873'
url: https://arxiv.org/abs/2609.11873
pdf_url: https://arxiv.org/pdf/2609.11873
published: '2026-09-10'
collected: '2026-09-13'
category: Agent
direction: 递归自我改进与Agent自治路线图
tags:
- recursive self-improvement
- autonomy
- LLM
- agent
- continual learning
- HCI
one_liner: 提出递归自我改进的完整路线图与 Headroom-Closed Index，系统梳理从执行自治到元改进的演化路径
practical_value: '- HCI（Headroom-Closed Index）可以作为衡量模型在特定任务上还有多少提升空间的诊断指标：在电商搜索/推荐场景中，可先用
  HCI 评估当前 LLM 在 query 理解、意图改写、生成式推荐等任务中的能力天花板，避免在不值得投入的方向上做无谓的迭代。

  - RSI 的自治等级框架可直接映射到推荐系统 Agent 的构建：先实现 improvement-execution autonomy（自动执行模型更新、策略调整），再逐步升级到
  improvement-strategy autonomy（自动选择训练数据、loss 设计、超参搜索），最后尝试 experience-acquisition
  autonomy（自动从线上反馈中挖掘新经验）。

  - 论文强调不同场景对 RSI 的要求和速度不同：电商推荐属于反馈信号密集、环境变化快的场景，更适合从经验获取自治切入；而生成式商品推荐（GenRec）需要结合
  Semantic ID 生成与用户行为反馈，可借鉴 RSI 中环境适应自治的思路，让 Agent 自动调整生成策略以适配活动、季节等变化。

  - 持续学习与元改进在推荐模型中的工程化落地：借鉴文中经验获取与递归元改进，可以在现有推荐模型迭代 pipeline 中加入自动化的数据选择、在线评估和策略回滚机制，减少人工调参，提升模型对新品类、新用户的适应速度。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

动机：现有 LLM 在模型规模和数据扩展上逐渐逼近收益递减，能力提升陷入瓶颈。论文用 Headroom-Closed Index（HCI）量化模型在特定能力维度上离“封闭上限”的剩余提升空间，揭示继续堆参数和数据的边际效益有限，需要新的提升范式。

方法关键点：提出递归自我改进（RSI）概念，将其定义为 AI 系统把经验和反馈转化为持久改变，同时提升自身能力和未来改进过程。给出发展路线图，按自治程度递进：improvement-execution autonomy（能自动执行改进动作）、improvement-strategy autonomy（能自动选择改进策略）、experience-acquisition autonomy（能自动获取经验）、environment-adaptation autonomy（能自动适应环境变化），最终达到 recursive meta-improvement（对改进过程本身进行改进）。论文还结合科学发现、具身智能、软件工程等场景，分析各自对 RSI 的不同要求和演化速度，并列举 Anthropic、Eureka、ASPIRE 等业界实践作为佐证。

关键结果：没有给出单一基准数字，而是通过 HCI 分析和路线图框架，指明现有 LLM 在多数任务上仍远离能力上限，但单纯模型规模增长已不能有效打开这些 headroom；RSI 的核心瓶颈在于经验获取的多样性、策略选择的可靠性和环境反馈的闭环速度。论文认为真正的 RSI 需要跨场景的元学习和基础设施支持，目前仍处于早期阶段。
