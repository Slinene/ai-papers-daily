---
title: 'OPID: On-Policy Skill Distillation for Agentic Reinforcement Learning'
title_zh: OPID：面向智能体强化学习的在策略技能蒸馏
authors:
- Shuo Yang
- Jinyang Wu
- Zhengxi Lu
- Yuhao Shen
- Fan Zhang
- Lang Feng
- Shuai Zhang
- Haoran Luo
- Zheng Lian
- Zhengqi Wen
affiliations:
- Tsinghua University
- Zhejiang University
- The Chinese University of Hong Kong
- Nanyang Technological University
- Tongji University
arxiv_id: '2606.26790'
url: https://arxiv.org/abs/2606.26790
pdf_url: https://arxiv.org/pdf/2606.26790
published: '2026-06-24'
collected: '2026-06-26'
category: Agent
direction: Agent 强化学习 · 技能蒸馏
tags:
- Skill Distillation
- On-Policy RL
- Agent
- LLM
- Self-Distillation
- GRPO
one_liner: 从在策略轨迹中提取分层后见技能并蒸馏回政策，为多步智能体提供稠密信号，无需外部技能库
practical_value: '- 在构建多步交互的购物助手或搜索Agent时，可直接利用完整对话轨迹自动提取工作流与关键决策技能（如定位商品、处理售后），用于后续训练，无需额外人工标注或外部技能库。

  - 关键优先路由（critical-first routing）可以为长对话推荐系统提供细粒度强化：当用户处于尺寸选择、支付等关键步骤时使用步级技能，其他状态使用全局工作流技能，避免简单拼接带来的相互干扰。

  - 训练过程中技能蒸馏仅依赖历史轨迹和旧策略的重打分，推理时不引入任何额外模块（检索、分析器），适合线上低延迟部署。

  - 该方法可与现有RL训练流程（如GRPO）直接结合，增强样本效率，特别适合小模型或数据稀缺的推荐/Agent场景：仅用60%的交互数据就能达到全量数据的结果水平。'
score: 9
source: huggingface-daily
depth: full_pdf
---

**动机**：长程智能体任务（如购物、搜索、家庭环境交互）中，环境奖励通常稀疏、延迟，难以归因到具体中间决策。现有在策略蒸馏方法常依赖外部技能库或检索，维护代价高且可能与当前策略的状态分布不匹配。

**方法关键点**
- **分层后见技能提取**：从完成的在策略轨迹中，用LLM分析器自动提取两层技能——Episode级（全局工作流或避坑规则）和Step级（关键步的局部决策知识）。
- **关键优先路由**：在识别出的关键时间步使用Step级技能，否则回退到Episode级技能；避免简单拼接，确保每步获得最恰当的粒度。
- **技能自蒸馏**：将选中的技能注入交互历史，让旧策略在原始上下文和技能增强上下文中分别对同一回复重新打分，计算每个token的对数概率差作为稠密的技能优势。
- **联合优化**：将技能优势与GRPO的结果优势加权求和，用PPO裁剪目标进行策略更新；推理时无需任何技能或检索，模型直接从标准历史推理。

**关键实验**
- 环境：ALFWorld（具身家务）、WebShop（电商选购）、Search-based QA（搜索问答），使用Qwen2.5-3B/7B和Qwen3-1.7B。
- 基线：Vanilla、GRPO、Skill-GRPO、OPSD、Skill-SD、RLSD、SDAR等。
- 主要提升：Qwen2.5-3B上，OPID比GRPO在ALFWorld提高+9.3点（84.3 vs 75.0），WebShop提高+10.9点（74.2 vs 63.3），Search QA提高+8.6点（45.0 vs 36.4）；小模型Qwen3-1.7B上提升更显著（+12.8和+26.5）。
- 样本效率：OPID只用60%训练数据即接近全量GRPO性能；跨域泛化：on unseen ALFWorld任务平均提升+7.7点。
- 消融：去掉Episode技能或Step级均导致性能显著下降；非路由版本比路由版低6.8点。

**核心结论**：在策略层次化技能蒸馏将轨迹记录转化为策略内化的决策知识，无需外部库存，有效提升了稀疏奖励下的学习效率与行为合理性。
