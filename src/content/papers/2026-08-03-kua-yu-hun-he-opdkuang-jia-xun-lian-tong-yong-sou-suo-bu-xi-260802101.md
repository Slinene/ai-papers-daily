---
title: Cross-Domain Hybrid OPD for Generalizable Search Agents
title_zh: 跨域混合OPD框架：训练通用搜索Agent而不牺牲通用智能
authors:
- Hongzhan Chen
- Xiaoyu Liu
- Dengming Zhang
- Minzhou Huang
- Dongliang Xu
- Jingcheng Xie
- Dongxiang Fang
- Bowen Qin
- Minsheng Hao
- Yaozong Shen
affiliations:
- Tencent Yuanbao Team
- Shanghai Innovation Institute
arxiv_id: '2608.02101'
url: https://arxiv.org/abs/2608.02101
pdf_url: https://arxiv.org/pdf/2608.02101
published: '2026-08-03'
collected: '2026-08-04'
category: Agent
direction: 搜索Agent强化学习与多域蒸馏混合优化
tags:
- RL
- OPD
- Alignment Tax
- Search Agents
- GRPO
- Curriculum Learning
one_liner: 结合搜索RL与多领域专家在线策略蒸馏(OPD)，同步优化搜索能力与通用推理，有效缓解对齐税
practical_value: '- **混合训练避免能力退化**：在业务中对搜索/推荐Agent做专项RL（如对话式推荐、多步检索）时，可借鉴混合批次设计——在RL损失中混入通用任务，用教师模型的token级KL惩罚保持通用能力，避免模型变成只会搜索的“偏科生”。

  - **多域专家蒸馏优于单一教师**：电商场景中可训练多个领域教师（如商品知识、促销文案、售后规则），通过在线策略蒸馏将领域知识注入搜索Agent，比单一通用教师更有效，且不会覆盖学到的搜索策略。

  - **难度课程学习提升教师质量**：为教师模型构造难度分层（基于Pass@k统计），先从中等难度样本学习密集信号，再扩展到全谱困难样本，能显著提升教师对困难问题的教学能力，这一策略可直接用于业务中领域专家模型的训练。

  - **工具交互协议与奖励设计**：采用XML格式工具调用协议和统一的验证器（规则、RM、代码执行），可迁移到需要调用商品搜索、优惠查询等API的电商Agent中，并利用GRPO优化工具使用策略。'
score: 9
source: arxiv-cs.CL
depth: full_pdf
---

## 动机
用强化学习(RL)训练自主搜索Agent时，模型会显著偏向检索与工具调用，从而损害其通用推理、指令遵循等基础能力，形成“对齐税”(alignment tax)。对于追求全能的电商/推荐助手而言，搜索只是交互的一环，这种能力退化不可接受。因此，如何在提升搜索表现的同时保持并增强通用智能，成为关键挑战。

## 方法关键点
- **两阶段训练框架**：基于Hunyuan3 (MoE, 20B激活参数) 构建。Stage I 仅用GRPO在搜索任务上优化，获得自主规划、迭代检索与证据合成能力。Stage II 联合优化搜索RL与多域专家在线策略蒸馏(OPD)。
- **多域专家教师**：独立训练数学、编程、逻辑推理、科学四个领域的专家模型，每个教师采用基于Pass@k的难度课程学习：先从中等难度样本获取密集学习信号，再引入全难度谱系并上采样困难样本，以此获得更强的领域推理能力。
- **混合强化学习与蒸馏目标**：训练时混合搜索样本与通用领域样本。搜索样本使用GRPO的原生奖励；通用样本则根据域标签路由到对应教师，利用教师给出的token级 logits 计算反向KL散度作为优势信号（A_OPD = -log(π_student/π_teacher)），与GRPO统一在PPO clip框架下优化。
- **工具交互环境**：Agent通过XML标签调用web搜索、图片搜索、视频搜索3种工具，环境返回结果后Agent继续生成或输出最终答案，形成多轮检索-推理循环。

## 关键结果
在Hunyuan3 (A21B)上的实验显示：
- **Stage I**：搜索能力大幅提升（AS-MultiHopQA +0.33, AS-WideSeekQA +0.36），但多数通用基准下降，如Minerva Math -5.88，BBEH Mini -5.62，AIME25 -3.00。
- **Stage II**：通用能力明显恢复并超越基座模型，AutoCodeBench v2 +5.21%，BBEH Mini +7.64%，HYEval3.1逻辑推理 +9.74%，而搜索性能基本维持或进一步提升（AS-MultiHopQA +0.34, AS-WideSeekQA +0.38）。
- 消融表明，混合RL无法替代OPD（例如BBEH Mini从47.86%降至35.22%），多专家显著优于单专家，课程学习对教师质量至关重要（困难层准确率提升5.49个点）。

## 核心洞见
搜索专项能力与通用智能不是零和博弈，通过精心设计的混合目标（搜索RL + 多域OPD）可以同时强化两者，为务实构建全能型AI Agent提供了一条可行路径。
