---
title: 'CASCADE Against Jailbreaks: Combination Across Stages with Controlled Attack-Defense
  Evaluation'
title_zh: CASCADE 对抗越狱：跨阶段组合与受控攻击-防御评估
authors:
- Jiale Luo
- Eric Han
affiliations:
- School of Computing, National University of Singapore
arxiv_id: '2609.21793'
url: https://arxiv.org/abs/2609.21793
pdf_url: https://arxiv.org/pdf/2609.21793
published: '2026-09-18'
collected: '2026-09-21'
category: Eval
direction: LLM 安全防御组合与评估
tags:
- jailbreak
- LLM safety
- defense combination
- evaluation
- prompt injection
one_liner: 首个系统研究 LLM 越狱防御跨阶段组合，标准化评估框架发现组合防御显著提升安全性
practical_value: '- 若业务中部署 LLM Agent（如对话式推荐、自动生成广告文案），不要依赖单一防御，建议采用分层管道：输入阶段过滤 + 输出阶段监控，组合可显著降低越狱成功率。

  - 评估自家 LLM 应用安全性时，应统一攻击成功率定义并控制攻击查询预算，避免不同设置下的不可比性，文中 CASCADE 框架可直接借鉴。

  - 优先选择那些在组合后效用损失最小的防御对，例如输入改写 + 输出分类器，而非追求单个最强防御。

  - 该工作主要面向安全攻防，对推荐/广告算法核心指标无直接提升，但可作为 LLM 应用上线前的安全测试规范。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

动机：LLM 越狱防御分布在推理管道的不同阶段（如输入修改、输出守卫），但缺乏对防御组合的系统研究；以往工作因攻击成功率定义不一致、实验设置碎片化，难以比较不同防御的有效性。

方法关键点：提出 CASCADE 框架，设定统一的威胁模型（直接、黑盒、单轮攻击），通过标准化的攻击成功率公式和受控查询预算确保公平评估；纳入 19 种攻击与 15 种防御，系统评估阶段内和跨阶段防御组合。

关键结果：没有单一防御在所有攻击下最优，但精心选择的组合（如输入过滤 + 输出监控）能在保持较低效用损失的同时大幅提升安全性；作者据此给出分层防御管道的实用建议。
