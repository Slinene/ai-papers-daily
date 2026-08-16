---
title: 'Refusing Intent, Not Form: Wrapper-Based Intent-Group Supervision for LLM
  Safety'
title_zh: 拒绝意图而非形式：基于包装的意图组监督用于LLM安全
authors:
- Ping Wu
- Haibo Tong
- Feifei Zhao
- Han Shen
- Yu Shi
- Yilin Zhao
- Sicheng Shen
- Guobin Shen
- Yun Luo
- Yi Zeng
affiliations:
- BrainCog Lab, Institute of Automation, Chinese Academy of Sciences
- School of Artificial Intelligence, University of Chinese Academy of Sciences
- Beijing Key Laboratory of Safe AI and Superalignment
- Ant Group
arxiv_id: '2608.13304'
url: https://arxiv.org/abs/2608.13304
pdf_url: https://arxiv.org/pdf/2608.13304
published: '2026-08-13'
collected: '2026-08-16'
category: Training
direction: LLM 安全对齐训练 · 意图组监督
tags:
- LLM Safety
- Jailbreak Defense
- Data Augmentation
- Fine-tuning
- Over-refusal
- Intent-Group
one_liner: 提出 WIFA 自动增强数据，通过意图组配对和锚定训练改善 LLM 对有害包装的拒绝并减少过度拒绝。
practical_value: '- 数据增强思路：在训练推荐系统或 LLM Agent 时，可针对同一用户意图的不同表达（如 query 改写、prompt 模板变化）构造结构匹配的正负例对，强制模型关注意图而非表面形式，提升鲁棒性。

  - 两阶段训练策略：先使用难例（如对抗性样本）进行安全/鲁棒性增强，再通过一致性正则化减少对良性样本的误判，可迁移到电商推荐中需要平衡安全过滤与用户体验的场景。

  - 锚定一致性训练：对同一意图的不同表达进行决策分数对齐，确保模型对相似请求响应一致，适用于多轮对话推荐或跨场景的意图识别，减少对同义表达的波动。

  - 工程实现提示：无需人工标注每个包装的意图，通过自动配对有害与良性样本可高效构建增强数据，降低数据成本；适用于需要大量多样性表达的业务场景。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

动机：安全对齐模型往往学习表面形式捷径：包装过的有害提示绕过安全机制，而结构相似的良性提示被过度拒绝。传统安全微调在 prompt 级别学习 comply/refuse 决策，未能捕捉底层意图。

方法关键点：提出 Wrapper-Based Intent-Form Augmentation (WIFA)，自动生成意图组增强数据：将包装的有害示例与结构匹配的包装良性反例配对，无需外部教师或每个包装的手工意图标签。WIFA 作为数据层用于两条互补微调路径：
- WIFA-Boost：两阶段高安全配方，先进行安全增强，再进行常规指令微调或其他步骤。
- A-GCRT：锚定组一致性拒绝训练，对同一意图不同包装的拒绝/服从决策分数进行正则化，并将有害组与良性组锚定在决策边界的相反两侧。

结果：在 Qwen 设置中，WIFA-Boost 在 transformed-harmful refusal 上达到最强；A-GCRT 将 OR-Bench 过度拒绝率从基线的 25.7% 降至 17.4%。复现的基线方法未能达到这些工作点。Llama 结果和消融实验（数据构造方式、两阶段顺序、A-GCRT 组件）支持意图组解释，但未声称普遍低于基线过度拒绝。
