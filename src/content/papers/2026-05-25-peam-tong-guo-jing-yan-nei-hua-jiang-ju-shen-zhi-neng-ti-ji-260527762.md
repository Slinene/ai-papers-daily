---
title: 'PEAM: Parametric Embodied Agent Memory through Contrastive Internalization
  of Experience in Minecraft'
title_zh: PEAM：通过经验内化将具身智能体记忆参数化
authors:
- Yuchen Guo
- Junli Gong
- Hongmin Cai
- Yiu-ming Cheung
- Weifeng Su
affiliations:
- Northwestern University
- Northeastern University
- South China University of Technology
- Hong Kong Baptist University
- Beijing Normal - Hong Kong Baptist University
arxiv_id: '2605.27762'
url: https://arxiv.org/abs/2605.27762
pdf_url: https://arxiv.org/pdf/2605.27762
published: '2026-05-25'
collected: '2026-05-28'
category: Agent
direction: 具身智能体经验参数化与持续学习
tags:
- Parametric Memory
- MoE-LoRA
- DPO
- Failure-Correction
- Continual Learning
- Minecraft
one_liner: 将智能体经验从检索式记忆转为参数化技能，通过失败-纠正对比学习与隔离式的MoE-LoRA适配器实现持续巩固。
practical_value: '- **经验内部化减少推理开销**：在推荐/Agent场景中，可将高频技能或用户偏好直接固化到模型参数中（如LoRA适配器），避免每次推理时检索技能库或长上下文注入，可大幅降低延迟（实验中下降42%）和Token消耗（-85%）。

  - **失败-纠正对比训练**：利用失败与纠正后的轨迹对进行DPO训练，让模型不仅模仿成功行为，还能辨别纠正前后差异，此思路可迁移到对话Agent、推荐排序中：收集用户负反馈与修正后的正样本，构造对比学习信号。

  - **按类别隔离的LoRA适配器防遗忘**：在多任务/多领域场景中，为每个类别（如不同商品类目、不同Agent技能）分配独立的LoRA模块，物理隔离参数更新，可天然避免灾难性遗忘，无需复杂正则化。

  - **自触发巩固机制**：基于失败率统计检验自动决定何时更新模型，无需人工设定任务相关阈值，适合电商推荐等动态环境，根据实时表现自适应调整模型更新节奏。'
score: 9
source: huggingface-daily
depth: full_pdf
---

**动机**：现有LLM智能体大多依赖外部记忆（检索轨迹、反思文本），策略参数始终保持不变，导致每次决策都要消耗上下文窗口和检索延迟。论文借鉴认知科学中的互补学习系统理论，提出应将经验从情境记忆逐步巩固到参数记忆中，实现“快速习得-慢速内化”。

**方法关键点**：
- 双速架构：慢速层（GPT-4o）负责推理、规划、验证；快速层为多模态MoE-LoRA（基于Qwen3-VL-8B），按技能类别（craft / gather / combat）物理隔离适配器。
- 经验内化目标：联合行为克隆（BC）与DPO的损失，使用失败轨迹-纠正轨迹对进行对比训练，使适配器不仅学会成功动作，还能区分纠正前后的差异；BC项保障代码语法正确性，DPO项赋予偏好信号。
- 筛选与触发：参数化价值评分（PV）综合考虑调用频率、稳定性、冗余度和遗忘风险，决定“什么值得内化”；自触发巩固（STC）基于近期失败率的统计检验自动触发更新，无需手动设定固定间隔或绝对阈值。
- 推理时优先走快速路径，若适配器存在且验证通过则直接执行；失败则回退到慢速层，并将轨迹存入情境存储待后续巩固。

**关键结果**：在Minecraft的11个长程任务上，PEAM成功率69.7%%，显著优于VOYAGER（54.5%%，p=0.018）；推理延迟降低42%（3.2s vs 5.5s），Token消耗减少85%（4.6K vs 31.2K）；跨类别巩固时遗忘率为0%（共享LoRA遗忘32.4%）；消融证实BC与DPO联合训练对可部署性至关重要，自触发巩固在不同任务分布下具有统计稳定性。
