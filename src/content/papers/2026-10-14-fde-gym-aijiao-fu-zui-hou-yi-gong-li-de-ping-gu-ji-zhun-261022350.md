---
title: 'FDE-Gym: The Last Mile of AI Delivery'
title_zh: FDE-Gym：AI交付最后一公里的评估基准
authors:
- Dongxu Yang
- Hongda Yan
- Renxin Wang
- Baoli Zhang
- Haojia Zuo
- Ying Zhao
- Youmin Chen
- Xiaojian Liao
- Congming Gao
- Tianyang Jiang
affiliations:
- DeepLethe
- Tsinghua University
- Shanghai Jiao Tong University
- Beijing University of Posts and Telecommunications
arxiv_id: '2610.22350'
url: https://arxiv.org/abs/2610.22350
pdf_url: https://arxiv.org/pdf/2610.22350
published: '2026-10-14'
collected: '2026-10-17'
category: Eval
direction: Agent 交付能力评估基准
tags:
- Agent Benchmark
- Forward-Deployed Engineer
- LLM Evaluation
- Customer Delivery
- Business Metric
one_liner: 构建95个真实客户交付任务基准，评估智能体在模糊需求下提升客户业务指标的能力
practical_value: '- 将业务KPI作为Agent评价的最终尺度，而非任务完成率：电商客服/推荐Agent可借鉴，用转化率、GMV、用户时长等业务指标直接衡量交付效果，避免只优化中间指标。

  - 显式对利益相关者交互计费（stakeholder contact cost），鼓励Agent高效提问：对话式推荐或澄清式搜索中，可加入用户打扰成本，训练Agent平衡信息获取与用户体验，减少冗余询问。

  - 任务指令分层（L0-L3）隔离信息缺失的影响：可用于评估推荐系统在用户查询模糊或需求误导时的表现，定位是约束发现、问题定义还是实现能力的瓶颈。

  - 警惕“字面合规”陷阱：直接按用户请求实现可能无法提升业务指标，需要挖掘未明说的约束。在电商场景中，不能仅根据用户显式点击行为推荐，还要理解深层业务目标（如利润、库存、长期留存）。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
现有Agent基准多假设任务已被良好定义（issue、spec、ticket），但真实客户交付中，前向部署工程师（FDE）必须澄清模糊需求、在线上系统工作、发现未明说的约束。论文认为这是AI交付的“最后一公里”：只按赞助方要求实现系统，往往无法改善客户自身的业务指标。FDE-Gym填补了这一空白，通过95个源自真实项目的任务，评估Agent能否从模糊请求出发，最终交付可度量的业务改进。

## 方法关键点
- **任务构建**：20个客户场景、18个行业，由行业专家从2024年以来在中国、新加坡、美国的真实交付项目改编。每个场景含原始任务及多个变体（改变关键事实），共95个任务。
- **环境与交互**：模拟客户环境，包含可修改的生产系统、文档数据、130+个脚本化利益相关者。Agent需通过提问发现约束，但每次交互产生费用（stakeholder contact cost），且部分人员有联系限制。
- **评分机制**：FDE-Gym Score = 标准化业务提升（U）减去事故调整和交互成本。U = (KPI_delivered - KPI_baseline) / (KPI_reference - KPI_baseline)，0表示无改进，1表示参考解，负值表示比不做更差。只有分数≥0.8且无事故才算解决。
- **指令分层**：同一任务提供四个级别的指令（L0完全指定规则和评分 → L3仅赞助方原始请求，可能误导），隔离实现能力、约束发现和问题澄清的难度。
- **反作弊锚点**：每个任务必须满足：参考解≥0.95、啥也不做=0、字面合规≤0.2、捷径策略≤0.8，并用270+种捷径策略测试。

## 关键实验
评估13个模型配置（7家提供商）。主要结果（L3设置，95个任务）：
- 最佳模型Claude Opus 5.5平均得分0.56，仅解决14/95任务；13个配置中5个解决0个任务。
- 从L0（规则已知）到L1（需发现约束）是关键瓶颈：三个领先模型平均得分从0.73-0.82骤降至0.39-0.62，下降0.28（95% CI 0.17-0.39），而L1→L3仅进一步下降0.04。
- 即使获得所有关键事实，领先模型在仅23个任务中的10个达到0.8以上业务提升；交互成本进一步侵蚀得分0.14-0.22。
- 弱模型经常比不做更差：Claude Haiku 4.5在79/95任务上得分低于0（基线），Mistral Small 4在51个任务上未扣成本前就低于基线。
- 对比外部基准（Terminal-Bench、Vibe Code Bench、Finance Agent），那些解决率高达88%、90%、61%的模型在FDE-Gym上仅得0.19-0.56，表明组件能力不等于交付能力。

最值得记住的一句话：**AI交付的最后一公里不在编码，而在于从模糊甚至误导的请求中发现真正业务问题，并用可度量的客户指标证明改进——当前最佳模型只能做到参考解的56%。**
