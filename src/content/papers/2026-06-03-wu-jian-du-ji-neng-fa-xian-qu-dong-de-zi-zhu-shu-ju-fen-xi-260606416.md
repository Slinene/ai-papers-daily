---
title: Unsupervised Skill Discovery for Agentic Data Analysis
title_zh: 无监督技能发现驱动的自主数据分析代理
authors:
- Zhisong Qiu
- Kangqi Song
- Shengwei Tang
- Shuofei Qiao
- Lei Liang
- Huajun Chen
- Shumin Deng
affiliations:
- Zhejiang University
- Ant Group
arxiv_id: '2606.06416'
url: https://arxiv.org/abs/2606.06416
pdf_url: https://arxiv.org/pdf/2606.06416
published: '2026-06-03'
collected: '2026-06-05'
category: Agent
direction: Agent 技能发现 · 无监督对比蒸馏
tags:
- Skill Discovery
- Data Analysis
- LLM Agents
- Unsupervised Learning
- Self-Improvement
one_liner: DataCOPE从无标注探索轨迹中利用自适应检查表与答案一致性自我提炼可复用数据分析技能，无需人工标注
practical_value: '- **无监督技能迭代方案可降标成本**：利用代理探索轨迹的自洽性、答案聚类或自生成检查表作为质量信号，结合对比蒸馏更新技能，尤其适合电商场景中报告自动生成、客服问答等任务，避免高成本人工标注。

  - **报告评估：自适应检查表与交替优化**：对于商品分析报告、广告文案等开放性输出，可引入Checklist Agent动态生成任务相关评估准则并与生成代理交替优化，防止过拟合，提升输出完备性。

  - **推理任务：答案聚类 + 自洽性辅助筛选**：在处理固定答案的电商问答、候选推荐时，通过答案聚类形成群体信号，辅以自洽性估计过滤错误一致，可有效发现稳定推理模式。

  - **技能粒度需平衡通用与专用**：实验表明过粗或过细的技能颗粒度会损害效果，为业务线构建Agent技能库时应先评估任务多样性再划分技能类别。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：数据科学代理在不同任务中的灵活性受限于固定的流水线或昂贵的模型微调。推理时注入可复用技能是一种轻量方案，但发现有效技能通常依赖人工标注，而数据分析任务的成功标准因格式（报告 vs. 答案）而异，标注成本高且难统一。

**方法**：DataCOPE 提出一个闭环无监督技能发现框架，协调三个模块迭代运作：1）**Data-Analytic Agent** 在当前技能下采样探索轨迹；2）**Unsupervised Verifier** 从轨迹中提取相对质量或一致性信号，不依赖真实标签。对于报告式任务，采用**自适应检查表验证器**（Adaptive Checklist Verifier）：生成任务特定检查项、评分报告、并交替优化 Checklist Agent 技能以防止过拟合；对于推理式任务，采用**答案一致性验证器**（Answer Agreement Verifier）：对最终答案聚类，计算自洽性作为辅助不确定性信号；3）**Skill Manager** 基于这些信号将轨迹分为正例组与负例组，通过对比蒸馏提炼可复用的分析策略、错误规避规则，更新技能。

**实验**：在两个基准上评估：Deep Data Research（报告式数据科研任务）和 DABStep（多步推理），随机划分 1:3 探索/测试集。与无技能基线和 Skill Creator 对比，DataCOPE 在报告任务上平均提升 9.71%，推理任务平均提升 32.30%，且在 Claude、GPT-5.2、DeepSeek-V4-Pro、Qwen3.5 等不同模型上一致有效。消融显示移除检查表或答案聚类会导致大幅性能下降；技能迭代在前两轮收益显著，后期可能饱和。无监督技能在报告任务上甚至超过少量标注轨迹的监督方法，展示了极高的标注效率。

**核心结论**：无监督验证器驱动的对比蒸馏是实现数据分析代理自我提升的有效范式，自适应检查表和答案一致性信号是两大关键，且发现技能可跨模型迁移。
