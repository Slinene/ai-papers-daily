---
title: 'ResearchMath-14K: Scaling Research-Level Mathematics via Agents'
title_zh: ResearchMath-14K：基于多智能体的研究级数学推理数据集构建与训练
authors:
- Guijin Son
- Seungyeop Yi
- Minju Gwak
- Hyunwoo Ko
- Wongi Jang
- Youngjae Yu
affiliations:
- Seoul National University
- OneLineAI
- Yonsei University
arxiv_id: '2605.28003'
url: https://arxiv.org/abs/2605.28003
pdf_url: https://arxiv.org/pdf/2605.28003
published: '2026-05-26'
collected: '2026-05-28'
category: Training
direction: 多智能体数据合成与推理训练
tags:
- MultiAgent
- Math
- Dataset
- Reasoning
- Fine-tuning
- Research-level
one_liner: 首个大规模研究级数学问题数据集，结合多智能体过滤的推理轨迹微调，平均提升开源模型9.2个百分点
practical_value: '- 多智能体协同构建高质量训练数据：可借鉴该 pipeline 思路，用多个 Agent 分工采集、清洗、验证电商/推荐领域的复杂任务数据（如生成式推荐中的
  Semantic ID 映射规则或 Agent 协作指令），减少人工标注成本。

  - 利用不完美推理轨迹提升模型性能：即使模型生成的推理路径存在错误，通过 agentic filtering（如自动检查步骤一致性、引用真实性）仍可提取有用监督信号，适用于低资源场景下的推荐模型微调或
  Agent 策略学习。

  - 避免生成中的虚构引用：论文揭示新模型产生更多虚假参考文献的现象，迁移到电商场景中，在生成式推荐或 Agent 对话系统里需设计引用验证机制，防止捏造商品属性或虚假用户评论，提升可信度。

  - 开源数据集与 Agent 过滤策略可直接复用：ResearchMath-14K 的数据构建方法和过滤代码或可改造，用于生成电商问答、多轮对话的推理轨迹，通过类似
  self-consistency 和 citation check 的机制提高数据质量。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：当前大规模数学推理数据集多为竞赛或教科书级别，缺乏真正的研究级问题，导致开源模型无法处理真实数学研究中的未知问题推理。为填补这一空白，需要构建一个大规模的研究级数学问题数据集并探索如何利用不完美推理轨迹提升模型能力。

方法：提出 ResearchMath-14K，通过多智能体管道从学术论文、预印本等来源自动采集 14,056 个研究级问题（覆盖数学各领域）。进一步使用两个开源模型生成 220K 条教师推理轨迹（ResearchMath-Reasoning），观察到新模型产生 5.6 倍引用和 5.0 倍虚假引用，存在逃避行为（如不尝试、虚构文献）。设计 agentic filtering 自动过滤低质轨迹（如检查引用真实性、推理一致性），然后用过滤后数据微调 Qwen3 系列（4B-30B）。

结果：微调后模型在自建研究数学基准上平均提升 9.2 分，证明了即使非全正确的推理尝试，经过智能体过滤也能为研究级推理提供有效监督。数据集已开源。
