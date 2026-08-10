---
title: 'SkillProx: Self-Evolving Agent Skills via Proximal Textual Gradient Descent'
title_zh: SkillProx：通过近端文本梯度下降实现自演化智能体技能
authors:
- Mingxuan Zheng
- Yujin Zhou
- Chuxue Cao
- Boqin Yin
- Yuyao Zhang
- Jiapeng Sun
- Shuaishuai Gong
- Sirui Han
- Yike Guo
affiliations:
- Hong Kong University of Science and Technology
- Macau University
arxiv_id: '2608.07449'
url: https://arxiv.org/abs/2608.07449
pdf_url: https://arxiv.org/pdf/2608.07449
published: '2026-08-07'
collected: '2026-08-10'
category: Agent
direction: 自演化技能 · 近端梯度文本优化
tags:
- LLM Agent
- Skill Evolution
- Proximal Gradient
- Closed-loop Diagnosis
- Knowledge Consolidation
one_liner: 结合闭环诊断验证与验证门控近端精炼，在表格任务上平均准确率超越最强梯度基线3个百分点
practical_value: '- **闭环更新验证**：在更新技能或提示词后，必须在同一批次数据上重新执行并检查硬指标是否提升，仅接受有益更新，避免“看起来合理”但实际有害的修改直接写入。可立即用于搜索推荐系统的指令/策略迭代。

  - **冻结效用审计**：对技能/提示的每个知识单元（如某条规则、示例）做 leave-one-out 评估，量化其边际效用，精准识别负面贡献的冗余内容。可迁移到
  Prompt 管理、工具选择等场景。

  - **验证门控压缩**：通过设置容忍阈值（硬精度不降、单元精度小幅可降）和压缩上限，有序删除或合并低效内容，在控制性能的前提下减少技能长度，降低上下文成本。适用于需要长上下文的
  Agent 或检索增强生成。

  - **前后向分工**：前向负责在线更新，后向负责回溯清理，两种反馈时间尺度互补，可借鉴到推荐系统策略的端到端演化框架中。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

## 动机
当前 LLM 智能体通过积累可复用的文本技能来适应重复任务，但现有技能演化方法存在两个缺陷：**更新不经验证**（诊断直接打补丁，不重新执行确认效果）和**技能无限臃肿**（不断累积冗余、冲突的规则，没有删除机制）。观察发现，重新执行并反馈效果可提升稳定性，而去除负效用的知识单元甚至能将准确率从 46% 提升至 54%。本文因此提出一个模拟近端梯度（Proximal Gradient）的前向-后向框架，兼顾任务性能与技能复杂度。

## 方法
- **前向闭环诊断**：每一轮迭代在训练批次上执行当前技能，诊断失败案例生成补丁；补丁重新在该批次运行，仅当硬准确率不降且单元准确率不降时才接受更新，否则回滚并反馈拒绝信息给后续诊断。最多尝试 3 次，保留接受/拒绝记忆。
- **后向 Prox 精炼**：将前向技能解析为知识单元（章节或参考文件组），在固定验证集上计算每个单元的**边际效用**（移除该单元后的准确率变化）。设定负效用阈值选出候选单元，按负效用程度处理。对每个候选，调用 Shrinker 尝试压缩（合并、降级或移除），需满足结构有效、复杂度严格下降、硬准确率不降、单元准确率降幅 ≤0.02 以及累计压缩 ≤10% 等条件。逐候选应用，通过即替换。
- 整体流程：前向从初始技能演化到中间技能，后向再压缩出最终技能，实现**诊断-近端协同演化**。

## 实验
- **任务**：IID 为 SpreadsheetBench Verified，OOD 为 WikiTableQuestions、HiTab。
- **基座**：Qwen3.5-4B / 27B、Qwen3.6-27B。
- **比较**：No Skill、Human Skill、EvoSkill、Trace2Skill、SkillOpt、SkillGrad。
- **核心结果**：SkillProx 在绝大多数设置下领先。例如 Qwen3.6-27B 上 SpreadsheetBench 达 54.5，比最优基线高 1.2 pp；OOD 上强泛化，SkillOpt 等基线则严重过拟合。消融表明去掉闭环降 1.5 pp，去掉 Prox 降 2.5 pp，二者互补。压缩-准确率曲线显示，适度压缩甚至能提升准确率，去除冗余和干扰。

## 一句话总结
**在线重新执行验证每一笔更新，离线效用审计剔除负贡献片段，让技能持续进化而不臃肿。**
