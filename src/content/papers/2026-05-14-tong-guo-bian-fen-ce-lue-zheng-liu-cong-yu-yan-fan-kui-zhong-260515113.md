---
title: Learning from Language Feedback via Variational Policy Distillation
title_zh: 通过变分策略蒸馏从语言反馈中学习
authors:
- Yang Li
- Erik Nijkamp
- Semih Yavuz
- Shafiq Rayhan Joty
affiliations:
- Salesforce AI Research
arxiv_id: '2605.15113'
url: https://arxiv.org/abs/2605.15113
pdf_url: https://arxiv.org/pdf/2605.15113
published: '2026-05-14'
collected: '2026-05-16'
category: LLM
tags:
- Variational Policy Distillation
- Self-Distillation
- EM
- RLVR
- Language Feedback
- Trust Region
one_liner: 将语言反馈学习形式化为变分EM，通过教师与学生的协进化蒸馏持续提升推理性能
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**  
强化学习从可验证奖励(RLVR)在复杂推理任务上受困于二元奖励的稀疏性，导致严重的探索瓶颈。近期自蒸馏方法通过语言反馈构建密集监督，但把反馈条件的教师视为固定启发式，随着学生提升，教师零样本解读能力停滞，蒸馏信号枯竭。

**方法关键点**  
- 将语言反馈学习形式化为变分推理，导出期望最大化(EM)框架：E步主动优化教师，M步将教师知识蒸馏至学生。  
- E步采用非成对偏好优化(BCO)和动态信任域(以当前学生策略为参考先验)，让教师学会从诊断性反馈中提取高奖励分布，同时确保目标始终在学生可达范围内。  
- M步对学生on-policy rollout进行token级KL散度最小化，将教师的条件化指导内化至无需反馈的学生策略。  
- 教师与学生共享同一网络权重(通过附加反馈区分)，消除多模型内存开销，并支持非对称更新频率以平衡计算成本。

**关键实验**  
在LiveCodeBench(v6子集)上，VPD使用Qwen3-8B取得49.62%的pass rate，优于GRPO(45.61%)、SDPO(47.33%)及各种混合方法。在SciKnowEval科学推理上，Qwen3-1.7B平均准确率74.34%，远超GRPO(69.81%)和SDPO(66.34%)，并消除SDPO的后期退化。消融证实动态先验和适当E步更新频率(每5次M步更新1次)是关键。但在数学推理(Math500)和基座模型冷启动中，VPD虽能延缓退化但仍落后于纯RL，揭示了语言反馈自蒸馏的固有边界。

**核心启示**  
“通过引入动态信任域，VPD将自蒸馏转化为安全且可扩展的协进化过程，但纯稀疏RL在严格数学推理上仍是王者。”
