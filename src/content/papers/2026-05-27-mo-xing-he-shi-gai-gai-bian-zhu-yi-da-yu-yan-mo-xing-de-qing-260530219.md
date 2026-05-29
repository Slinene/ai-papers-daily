---
title: When Should Models Change Their Minds? Contextual Belief Management in Large
  Language Models
title_zh: 模型何时该改变主意？大语言模型的情景信念管理
authors:
- Haoming Xu
- Weihong Xu
- Zongrui Li
- Mengru Wang
- Yunzhi Yao
- Chiyu Wu
- Jin Shang
- Yu Gong
- Shumin Deng
affiliations:
- Zhejiang University
- HomologyAI
arxiv_id: '2605.30219'
url: https://arxiv.org/abs/2605.30219
pdf_url: https://arxiv.org/pdf/2605.30219
published: '2026-05-27'
collected: '2026-05-29'
category: Agent
direction: Agent 多轮交互中的信念状态管理
tags:
- CBM
- Belief Tracking
- Multi-turn Interaction
- RL
- LLM
- Evaluation
one_liner: 提出情景信念管理（CBM）与BeliefTrack基准，诊断并改善LLM在多轮交互中维持证据对齐信念的能力
practical_value: '- 在多轮对话推荐或交互Agent中，可引入信念状态追踪机制，明确区分有效证据与无关噪声，避免模型因用户闲聊或情绪化内容而改变购物意图或推荐结果。

  - 使用基于Jaccard相似度的密集奖励替代稀疏匹配，能提供更平滑的优化信号，适用于微调需要维持动态用户偏好集的推荐对话策略。

  - 借鉴BeliefTrack的封闭世界–符号验证设计，构建推荐场景的离线诊断集：定义有限商品池作为信念空间，设计多轮对话模板精确测试模型是否因干扰信息产生非预期推荐变化。

  - 表征操控方法表明，从RL训练中提取的隐藏层方向可以无参数地提升基础模型的多轮一致性，为在资源受限时快速改善现有多轮Agent提供了轻量方案。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
长时多轮交互中，大模型需要管理不断积累的信息：决定何时更新状态、何时保持不变、何时忽略无关噪声。现有研究大多关注知识冲突或单轮推理不稳定性，缺乏系统衡量模型在连续交互中如何维持与证据对齐的信念。为此，本文提出**情景信念管理（Contextual Belief Management, CBM）**，形式化为模型在多轮交互中保持预测信念状态与形式证据对齐的任务，并构建封闭世界基准**BeliefTrack**以精确诊断。

## 方法关键点
- **任务环境**：BeliefTrack 包含规则发现（RD）和电路诊断（CD）两个环境，每种环境均定义有限信念空间（候选假设集合）和符号验证器，可自动计算每一轮的Oracle信念状态。
- **失败诊断**：定义三类精确的逐轮失败模式——**Failed Stay**（应保持却改变）、**Failed Update**（应更新却未变）和**Failed Isolation**（加入无关噪声后预测改变）。
- **改进方法**：
  - 训练无关的**信念追踪提示（BT-Prompt）**：在系统提示中显式注入证据过滤、候选重检和修正规则。
  - **信念状态奖励的强化学习（GRPO）**：用预测信念状态与Oracle状态的Jaccard相似度作为密集奖励，只在Dsaty和Dupdate数据上训练，不包含噪声轨迹。
- **分析工具**：通过提示式探测（追踪Oracle假设的排名）和表征操控（从RL模型提取隐藏层方向注入原始模型），解释失败机制并验证可迁移的修复模式。

## 关键实验
- **测试模型**：Qwen2.5-7B-Instruct、Qwen3.5-9B 等。
- **主要结果**：
  - 原始模型存在严重CBM失败，Qwen2.5-7B的FSR/FUR/FIR均在97–99%。
  - BT-Prompt增益有限且不一致，部分指标反而上升（如RD的FUR上升15.0%）。
  - RL训练将Qwen2.5-7B的RD-FSR/FUR降至0.0%/2.0%，CD-FSR/FUR降至0.0%/0.0%，跨环境FIR降低63.9%以上。平均失败率降低70.9%。
  - 表征操控在RD任务上将FSR/FUR/FIR分别降低78.6%、92.3%、48.8%，且可跨任务迁移。

## 核心结论
“信念状态奖励的RL训练不仅大幅减少了信念管理失败，还能泛化至未见的任务环境与噪声类型，表明LLM可以通过奖励学习获得可迁移的信念维持能力。”
