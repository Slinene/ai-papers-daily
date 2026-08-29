---
title: 'V-Rubrics: Visual Faithfulness via Rubric-Based Reinforcement Learning'
title_zh: V-Rubrics：基于Rubric强化学习的视觉忠实性训练
authors:
- Shulin Tian
- Minglun Li
- Yuhao Dong
- Hao Ding
- Jiarui Yao
- Haiwen Diao
- Jingkang Yang
- Hongyuan Zhu
- Ziwei Liu
affiliations:
- S-Lab, Nanyang Technological University
- A*STAR
- UIUC
arxiv_id: '2608.25580'
url: https://arxiv.org/abs/2608.25580
pdf_url: https://arxiv.org/pdf/2608.25580
published: '2026-08-25'
collected: '2026-08-29'
category: Multimodal
direction: 多模态VLM后训练 · Rubric奖励
tags:
- VLM
- GRPO
- Rubric Reward
- Visual Faithfulness
- RLHF
- Multimodal
one_liner: 将参考答案分解为原子命题，从视觉忠实、推理一致、指令遵循三方面给结构化rubric奖励，提升VLM多模态后训练
practical_value: '- 将粗粒度结果奖励拆成rubric子项（视觉事实、推理步骤、约束满足），对广告文案、推荐解释、商品QA等LLM评估与RL奖励设计可复用：避免只给整体好坏，能定位错误点并给予结构化部分信用。

  - 使用prefix-localized partial credit：当有支撑证据span时只奖励相关前缀，不惩罚后续冗余，适合多步推理生成任务中做更精确的credit
  assignment。

  - 训练数据构造：规则过滤+拒绝采样分数划分难度，再用强LLM统一prompt标注rubric，可低成本获得可扩展的奖励标注集；业务上可对商品描述、视频帧QA等构造领域微调数据。

  - 先SFT冷启动再做GRPO，并用相同SFT检查点对比answer-only GRPO，可迁移到LLM-based推荐/Agent训练流程，验证奖励抽象对后训练的实际增益。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：VLM生成答案流畅但缺乏视觉证据，单个无支撑对象、图表数值或中间推理错误会破坏整体可信度。作者认为这是多模态后训练中的credit-assignment失败：标量结果奖励只说明答案可接受，无法定位哪些视觉事实未被接地、哪些推理步骤无效、哪些指令约束被遗漏。

**方法关键点**：提出V-Rubrics，将参考答案分解为原子命题，沿 Visual Faithfulness (VF)、Reasoning Consistency (RC)、Instruction Following (IF) 三个维度对生成答案打分。先基于OpenMMReasoner-SFT-874K冷启动数据微调Qwen3-VL-8B-Instruct得到SFT检查点；再从17个视觉接地数据源构造V-Rubrics 50K（50,248样本），经过规则过滤、拒绝采样分数确定难度，并由Gemini-3-Pro统一标注。训练时使用component-wise、prefix-localized rubric credit进行GRPO。

**关键结果**：Rubric-based GRPO相比共享SFT基线和answer-only GRPO均有提升，在知识导向和视觉接地推理基准上增益最大，验证rubric作为视觉后训练奖励抽象的有效性。
