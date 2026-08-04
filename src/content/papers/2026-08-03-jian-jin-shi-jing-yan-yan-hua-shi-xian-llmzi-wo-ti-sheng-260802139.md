---
title: Self-Improving Large Language Models via Progressive Experience Evolution
title_zh: 渐进式经验演化实现LLM自我提升
authors:
- Shijie Ren
- Xiting Wang
- Meng Li
- Yujie Guo
- Yunhang Yao
- Ziheng Peng
- Xunlong Wang
- Yuetan Chen
- Haoyang Zhou
- Yunlong Liang
affiliations:
- Renmin University of China
- Tencent Inc.
arxiv_id: '2608.02139'
url: https://arxiv.org/abs/2608.02139
pdf_url: https://arxiv.org/pdf/2608.02139
published: '2026-08-03'
collected: '2026-08-04'
category: Training
direction: LLM自我演化 · 经验蒸馏与RL混合
tags:
- Self-Improvement
- Experience Distillation
- Reinforcement Learning
- On-Policy Self-Distillation
- GRPO
- Experience Evolution
one_liner: 统一显式经验演化与隐式RL优化的两阶段后训练框架，通过全局经验池萃取可迁移知识并内部化，提升数学推理与数据效率
practical_value: '- **全局经验池与演化**：在推荐或Agent中，可维护一个经验池，从成功/失败交互轨迹中抽象可复用策略（如用户偏好模式、失败原因），并定期合并、去重、演化，减少冗余和冲突经验。

  - **特权引导自蒸馏(OPSD)**：推荐模型在线更新时，可用历史优质决策作为特权信息构造 teacher，对当前策略进行 on-policy 蒸馏，既保留行为多样性又注入有效先验。

  - **两阶段优化提升数据效率**：先用经验蒸馏初始化模型，降低全部采样错误的比例，再应用 GRPO 等 RL 算法，可大幅减少无效探索，适合在线广告/推荐中低反馈场景。

  - **经验效用验证机制**：用探针集评估每条经验的边际收益，可过滤低质量经验；在推荐系统策略迭代中，可类似评估新增规则或策略是否带来正向增量。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**  
现有LLM自我演化方法割裂：测试时方法（如提示、反思）可将经验作为上下文，但无法内部化为模型能力；训练时RL通过稀疏奖励间接吸收经验，探索效率低且依赖初始模型强度。缺少一个将交互轨迹显式转化为可迁移经验并蒸馏进模型参数的中间阶段。

**方法**  
提出 SPEE，包含两个阶段：  
1. **显式经验演化**  
   - 从当前策略采样的成功/失败轨迹中，用经验提取器抽象出可迁移的经验条目（正例总结有效推理模式，负例标识失败模式）。  
   - 维护一个全局经验池，通过演化算子合并、去重、泛化，并在探针集上评估每条经验的边际效用，过滤低质量经验。  
   - 用特权引导在线策略自蒸馏（OPSD）将经验内化：teacher 分支看到问题+经验，student 分支仅看到问题，通过最小化 on-policy 分布与 teacher 分布的 KL 散度强化策略。  
2. **隐式策略优化**  
   - 以蒸馏后的策略作为初始化，应用 GRPO（组内相对优势）进行探索，发现经验池未覆盖的高奖励行为，形成闭环迭代。

**实验结果**  
在 Qwen3 1.7B/4B/8B 基座上，用 DAPO-math-17k 训练，在 AIME24/25、GSM8K、MATH500、MinervaMath 上平均准确率分别提升 +4.87、+6.96、+6.53 个百分点，一致优于 GRPO 和 SDPO。SPEE 所需训练轨迹比 GRPO 少约 28%。消融证实经验池和第二阶段缺一不可。

**一句话核心**  
SPEE 架起了外部经验利用与参数级优化的桥梁，通过渐进式经验演化与内化，再以 RL 挖掘新能力，构成可持续的自我改进闭环。
