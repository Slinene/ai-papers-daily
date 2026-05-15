---
title: 'STALE: Can LLM Agents Know When Their Memories Are No Longer Valid?'
title_zh: STALE：大模型智能体何时知晓记忆已过时？
authors:
- Hanxiang Chao
- Yihan Bai
- Rui Sheng
- Tianle Li
- Yushi Sun
affiliations:
- 武汉大学
- 香港中文大学
- 香港科技大学
arxiv_id: '2605.06527'
url: https://arxiv.org/abs/2605.06527
pdf_url: https://arxiv.org/pdf/2605.06527
published: '2026-05-06'
collected: '2026-05-15'
category: Agent
tags:
- LLM Agents
- Memory
- Implicit Conflict
- Benchmark
- State Tracking
- CUPMEM
one_liner: 提出STALE基准评估LLM隐式记忆冲突，揭示检索与行动脱节，及写入侧状态裁决的有效性
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**

长期记忆对于LLM智能体维持用户个性化至关重要，然而现有基准仅评估静态事实的检索，忽略了一个关键失效模式：**隐式冲突**——新观察使旧记忆失效，但对话中从未明确否定。例如，用户先提及“每天骑车上班”，后来提到“昨天打篮球摔断了腿”，虽未直接否定骑行习惯，却隐含地使骑行通勤记忆不再适用。现有记忆评测不要求模型推断并传播此类隐式状态变化，导致模型可能继续使用过时的信念。

**方法关键点**

- 将隐式冲突形式化定义为两个公理：信念不兼容（新观察逻辑上否定旧信念）和非显式否定（对话中无直接纠正）。将冲突分为两类：Type I 共指冲突（同一属性先后有矛盾值）和 Type II 传播冲突（新观察更新另一属性，通过因果链使旧信念失效，如环境变化间接否定位置）。
- 构建STALE基准：自动化+人工验证生成400个冲突场景，每个场景包含3种探测维度（状态分辨SR、前提抵抗PR、隐式策略适应IPA），共1200个评估查询；对话上下文达到150K tokens，覆盖100+日常主题。
- 提出三维探测框架：SR直接询问旧信念是否仍有效，PR以旧状态为前提提问要求拒绝，IPA让模型在无提示下应用更新后的状态。
- 原型系统CUPMEM引入写入侧状态裁决：新信息到来时显式判定旧记忆是否过期、替换或未知，并通过状态拓扑传播更新相关记忆，查询时只使用被授权的当前状态，从而阻断过时记忆的干扰。

**关键实验与结果**

- 评估10余种系统，包括GPT-5.4、Gemini-3.1-pro、Llama-3.3-70B、Qwen3.5等LLM以及LightMem、Zep等记忆框架。
- 最强模型Gemini-3.1-pro总体准确率仅55.2%；前提抵抗维度普遍极低（如Gemini-3.1-pro Type I PR 30.0%，多数模型接近0%），表明模型即使能识别过时记忆仍轻易被错误前提带偏。
- Type II传播冲突显著难于Type I：Gemini-3.1-pro从Type I SR 92.0%跌至Type II SR 69.0%。
- 在共享GPT-4o-mini骨干下，CUPMEM将总体准确率从8.7%提升至68.0%，PR维度从接近0提升至Type I/II的78.0%/75.0%，验证了写入侧裁决和状态传播的有效性。
- 诊断显示，记忆框架虽能检索到新证据（LightMem新证据检索率77.5%），但无法使其成为决策依据，导致了“当前状态裁决鸿沟”。

**最值得记住的一句话**

识别记忆已过时远不等于能主动抵制以旧状态为前提的提问，模型在隐式冲突面前的推理与应用之间存在显著断层。
