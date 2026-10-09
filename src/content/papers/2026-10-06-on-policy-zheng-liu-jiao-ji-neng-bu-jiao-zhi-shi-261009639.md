---
title: On-Policy Distillation Teaches New Skills but Not New Knowledge
title_zh: On-Policy 蒸馏教技能不教知识
authors:
- Yixuan Tang
- Yi Yang
affiliations:
- The Hong Kong University of Science and Technology
arxiv_id: '2610.09639'
url: https://arxiv.org/abs/2610.09639
pdf_url: https://arxiv.org/pdf/2610.09639
published: '2026-10-06'
collected: '2026-10-09'
category: Training
direction: On-policy 蒸馏的知识/技能迁移机制
tags:
- On-Policy Distillation
- Knowledge Distillation
- Reverse KL
- Forward KL
- Compositional Skill
- LoRA
one_liner: reverse-KL on-policy 蒸馏主要迁移组合推理技能，几乎不迁移事实知识；改用 forward KL 才能迁移新事实
practical_value: '- 如果目的是给推荐/搜索/Agent 的轻量 LLM 注入新事实（新品知识、活动规则、2026 新实体、query 改写约束），别只靠
  reverse-KL OPD；优先 teacher-demo forward KL 或 SFT，否则学生仍用旧记忆生成错误答案。

  - 如果目的是提升多跳推理/规划（商品属性组合、优惠规则计算、对话策略树状拆分），可用 student rollout + reverse KL 的 OPD，重点放在组合执行，不引入新事实。

  - 混合目标如 ToDi 可同时获得事实与组合提升，在蒸馏预算有限时可替代单纯 reverse KL；GKD/EOPD 仍偏技能迁移。

  - 事实与技能更新在 LoRA 子空间近似正交：事实更新集中在末层，组合技能集中在浅/中层。可为知识更新和推理能力使用独立 LoRA 分支或分层学习率，减少互相干扰。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
On-policy distillation (OPD) 在 LLM 后训练中广泛用于加强推理，但端到端分数无法区分学生获得的是新事实知识还是多步组合技能。论文用可控合成环境把二者独立开，回答“蒸馏到底迁移了什么”。

**方法关键点**  
- 事实 = 随机 lookup table：25 张表（20 initial / 5 held-out），每张表 100 个 digit pair→digit 映射，无代数规律，只能记忆。  
- 组合技能 = 用相同 facts 的 chain vs branching tree；tree 需要跨中间步骤取回并合并结果，并拆分 shared / teacher-only / unseen 结构。  
- 先训初始学生 S0，再构造 T_f（+held-out facts）、T_s（+tree skill）、T_fs、T∅；用 reverse-KL、student rollout 的 OPD 蒸馏。  
- 解耦 prefix source 与 KL 方向，比较 teacher/student prefix × forward/reverse KL；并检查 LoRA 更新方向。

**关键结果**  
- 四模型平均：T_s 学生在 unseen tree 达 79.10%（baseline 0.72%）；T_f 学生在 held-out fact 单步仅 13.12%，fact-chain 仅 0.54%。  
- 换 forward KL：Qwen3-4B fact-single 从 10.95%→54.10%，Gemma-2-2B 从 32.95%→94.10%；student rollout 主要降低组合任务 NLL。  
- 真实 benchmark：Knowledge-2026 11.25%→9.64%，无知识迁移；Math-2026 17.41%→23.88%，+6.47pp 推理迁移。  
- LoRA 更新上，事实与技能更新近似正交；事实更新集中在末层，组合技能更新集中在早中层。

> 最值得记住：标准 reverse-KL OPD 更适合“教会模型组织已有知识”，不适合“注入新事实”；要更新事实优先 forward KL 或混合目标如 ToDi。
