---
title: 'Evolving with Open Worlds: Towards Recursive Self-Improvement for Future Forecasting'
title_zh: 与开放世界共进化：面向未来预测的递归自改进
authors:
- Zhipeng Chen
- Yunsen Liang
- Yanxi Chen
- Hongkang Zhao
- Lingyun Feng
- Ruiyang Ren
- Guoxin Chen
- Jia Deng
- Feng Chang
- Chuan Hao
affiliations:
- Renmin University of China
- IQuest Research
- Nanyang Technological University
arxiv_id: '2610.29784'
url: https://arxiv.org/abs/2610.29784
pdf_url: https://arxiv.org/pdf/2610.29784
published: '2026-10-20'
collected: '2026-10-22'
category: Agent
direction: Agent 递归自改进 · 未来事件预测
tags:
- recursive self-improvement
- agentic forecasting
- RLVR
- skill distillation
- environment evolution
- calibration
one_liner: 构建代理-环境闭环，通过参数、技能、环境三轴演化实现递归自改进，连续三周登顶FutureX
practical_value: '- **搜索-预测解耦**：将证据获取（搜索团队）与预测（预测团队）分离，缓存检索结果用于训练，避免实时环境中标签污染；电商推荐中可把商品信息获取与排序/CTR模型拆开，用冻结特征训练，防止召回路上的信息泄露。

  - **技能库外部化**：把成功/失败轨迹蒸馏为显式技能条目，注入推理而不更新权重，适合低资源在线场景；推荐系统可把用户行为序列提炼为可复用的召回规则、排序模板或人群策略，实现低成本快速迭代。

  - **环境演化生成对抗难样本**：根据模型错误动态生成薄弱点任务，形成课程学习；电商场景可针对低转化人群、长尾类目或新场景自动生成更难样本，让精排/重排模型持续提升。

  - **校准指标先行**：用 Brier score / calibration 而非仅 accuracy 评估概率预测，能更早发现模型概率判断改善；在 CTR/CVR
  预估中应同时监控校准度，校准提升往往先于 AUC 显现。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
当前 AI 系统大多参数冻结，依赖外部更新；理想系统应能从自身经验中持续变强。未来事件预测提供动态、可验证、非平稳的环境，适合研究递归自改进（RSI）。但固定数据集无法支撑递归进化，需要构造一个不断产生新任务、且能自动给出真实反馈的“活环境”。

**方法关键点**
- 三个模块闭环：Prometheus（动态环境，从每日新闻合成预测问题）、Branchus（搜索团队+预测团队，输出完整推理轨迹）、Athena（递归进化引擎，三轴更新）。
- **参数进化**：用 RLVR + RFT 在可验证奖励上更新预测团队；关键设计是搜索-预测解耦——搜索团队在问题开放时缓存证据，预测团队只在冻结证据上训练，避免事件解决后标签污染和查找答案的捷径。
- **技能进化**：从轨迹中蒸馏可复用预测技能，外置技能库，不更新权重，只需少量实时轨迹即可提升推理，适合在线珍贵数据。
- **环境进化**：从失败轨迹中提取任务合成技能，让 Prometheus 针对代理当前薄弱点生成更难、更精确的问题，形成对抗性课程学习。

**关键实验**
- 外部 FutureX 排行榜连续三周第一，rating 最高相对提升 195%；自建评估上四个 LLM 均位列前三，最佳 BT 62.2，超过最强基线 +10.7。
- RLVR 使数值校准分数提升 0.31–0.38；技能进化使 Brier 从 0.135 降至 0.122，MAPE 从 2.80% 降至 2.28%，且随轮次持续改进。
- 环境演化使技能覆盖 domain 从 320 增至 337，RFT 在对抗性难样本上 Brier 降低 1.6%、AUROC 提升 2.7%。

**最值得记住的一句话**
递归自改进的真正瓶颈不在模型参数，而在于环境能否持续提供新鲜、可验证且针对性变难的经验；参数、技能、环境三者必须共同演化。
