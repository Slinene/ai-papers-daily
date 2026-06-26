---
title: 'Qwen-Image-Agent: Bridging the Context Gap in Real-World Image Generation'
title_zh: Qwen-Image-Agent：弥合真实世界图像生成的上下文鸿沟
authors:
- Zekai Zhang
- Jiahao Li
- Jie Zhang
- Kaiyuan Gao
- Kun Yan
- Lihan Jiang
- Ningyuan Tang
- Shengming Yin
- Tianhe Wu
- Xiaoyue Chen
arxiv_id: '2606.26907'
url: https://arxiv.org/abs/2606.26907
pdf_url: https://arxiv.org/pdf/2606.26907
published: '2026-06-24'
collected: '2026-06-26'
category: Agent
direction: Agent驱动上下文补全的图像生成
tags:
- Agentic Image Generation
- Context Gap
- T2I
- Plan-Search-Memory
- IA-Bench
one_liner: 提出统一Agent框架，通过规划、推理、搜索、记忆逐步补全缺失上下文，解决T2I模型在真实请求中性能不足的问题
practical_value: '- **Agent化模糊意图补全**：用户输入常为欠说明的短句，借鉴“上下文规划—上下文接地”两步范式，在电商文案生成、广告创意、搜索Query推荐等场景中，可先通过推理或检索外部知识将模糊需求展开为完整生成指令，提升下游模型性能。

  - **搜索与记忆增强**：框架中显式引入搜索工具获取实时知识，并利用记忆模块积累历史偏好，对需要动态商品信息、促销活动更新的推荐文案生成或对话式购物Agent有直接参考价值。

  - **能力拆解与基准设计**：将Agent能力分解为Plan、Reason、Search、Memory四个维度并构建对应测试集，该方法可迁移到推荐/搜索Agent的评估，围绕电商特有的约束（如合规、冷启动）设计子任务。

  - **多工具编排的工程启示**：将多个能力模块（推理、搜索、记忆、反馈）统一在一个Agent中，通过规划调度协作，为解决推荐系统中多源信息融合和实时决策提供工程范式。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有T2I模型依赖完整、明确的提示词，但真实场景下用户请求常模糊、隐含，或需要最新知识。论文将此挑战定义为“上下文鸿沟”——用户上下文与模型所需充足生成上下文之间的不匹配。

**方法关键点**：提出Qwen-Image-Agent，一个以“上下文为中心”的统一Agent框架。将用户输入视为部分上下文，通过两步构建完整上下文集：
1. **上下文感知规划**：识别缺失的上下文维度，并规划如何获取、使用它们。
2. **上下文接地**：从推理、搜索、记忆、反馈四个渠道收集所需上下文。
框架整合Plan、Reason、Search、Memory与Feedback机制，使生成过程能自动补全信息、检索最新知识、利用历史记忆并迭代优化。

为评估Agent图像生成，还构建了IA-Bench基准，覆盖规划、推理、搜索、记忆四项核心能力。在IA-Bench、Mindbench、WISE-Verified上，Qwen-Image-Agent均超越强基线，达到SOTA。例如，在IA-Bench整体得分上大幅领先，验证了上下文补全机制的有效性。
