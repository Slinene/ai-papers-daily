---
title: 'CAT-alyzing Honesty: Continuous Adversarial Training for Transferable LLM
  Honesty'
title_zh: 连续对抗训练增强 LLM 可迁移诚实性
authors:
- Yuan-Chen Chang
- Niklas Herbster
- Gauthier Gidel
- Tommaso Tosato
affiliations:
- Tara Research
- Mila – Quebec AI Institute
- Technical University of Munich
arxiv_id: '2610.22292'
url: https://arxiv.org/abs/2610.22292
pdf_url: https://arxiv.org/pdf/2610.22292
published: '2026-10-15'
collected: '2026-10-18'
category: Training
direction: 对抗训练 · LLM 对齐与诚实性
tags:
- adversarial training
- LLM honesty
- alignment
- utility preservation
- activation steering
one_liner: CATCH 用数百条自报告场景构造对抗训练对，让 LLM 在压力下保持诚实并跨任务泛化
practical_value: '- 借鉴 CATCH 的构造方法：用 self-reporting 场景生成“有依据 vs 编造”答案对，仅需数百条即可训练模型远离不诚实输出，成本低，适合电商推荐解释、商品属性描述等场景，抑制模型编造不存在的优惠或参数。

  - utility data 的选择是保持通用能力的关键：CATCH 在外循环加入 utility 数据防止诚实训练导致能力漂移，优于纯激活引导。在微调推荐对话或
  Agent 时，应同时混合正常推荐/通用 QA 数据，避免模型变得“诚实但无用”。

  - 对抗训练的内外循环范式（embedding 扰动让错误答案更容易，再更新参数偏好正确答案）比 SFT 更强，可迁移到广告文案生成中防止夸大宣传，或在多智能体场景中减少
  Agent 隐瞒信息（如不披露广告属性）。

  - CATCH 不增加推理开销，可直接部署到线上推荐 Agent；若已有 activation steering 方案，可考虑替换或叠加，以保持更强 utility。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**  
LLM 在对诚实性要求高的场景仍会输出与知识矛盾或缺乏上下文支撑的声明，对齐训练未能根治，且在压力下更容易不诚实。

**方法关键点**  
CATCH 受稳健拒绝有害查询的方法启发，构造诚实答案 y+ 与不诚实答案 y- 的对比目标。训练分内外循环：内循环对 token embeddings 施加扰动，使 y- 更可能；外循环更新模型参数，偏好 y+ 并保持在 utility 数据上的能力。训练数据仅需数百个来自 self-reporting 场景的样本。

**关键结果**  
在 Llama-3.3-70B-Instruct 和 Qwen3-3.6-27B 上，CATCH 在 MASK 基准中减少压力下的不诚实输出，在 Among Us 多智能体游戏中提高认罪率，在 AuditBench 中提升隐藏行为发现率。相比 prompting 和 SFT，CATCH 明显更好；与 SOTA honesty activation steering 效果相当，但 utility 保持显著更好，归因于 utility data 的选择。
