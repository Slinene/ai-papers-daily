---
title: Training Specialist Models without Reasoning Trajectories for Domain Expert
  Distillation
title_zh: 无推理轨迹的专家模型训练：领域专家蒸馏的隐式轨迹选择
authors:
- Yilei Tu
- Zihao Li
- Shaoxiong Ji
- Jörg Tiedemann
- Fei Yuan
affiliations:
- University of British Columbia
- Shanghai Artificial Intelligence Laboratory
- University of Helsinki
- ELLIS Institute Finland
- University of Turku
arxiv_id: '2609.13770'
url: https://arxiv.org/abs/2609.13770
pdf_url: https://arxiv.org/pdf/2609.13770
published: '2026-09-11'
collected: '2026-09-16'
category: Training
direction: 专家模型训练与蒸馏 · 隐式推理轨迹
tags:
- specialist distillation
- reasoning trajectories
- domain adaptation
- LLM
- knowledge distillation
- generalization
one_liner: 证明仅用 QA 训练的专家模型会隐式选择推理轨迹，且 tuning 选择直接控制下游学生的领域精度与通用能力平衡
practical_value: '- 在电商/广告场景训练领域 LLM 专家时，如果只有 QA 对、没有 expert reasoning 标注，SFT 的超参（learning
  rate、epochs、数据配比、正则）会直接决定 teacher 生成的推理轨迹分布，进而影响蒸馏出的下游学生。应将专家模型的 tuning 配置视为向学生传递的隐式监督，而不是只盯着
  teacher 的域内指标。

  - 可以把 small student 当作无偏 probe，快速观测专家模型的隐式轨迹质量：不同 domain adaptation 配方做蒸馏后，比较学生的
  specialization-generalization profile，无需额外 reasoning label 即可筛选适合线上均衡的 teacher 版本。

  - 在导购/客服 Agent 的推理链生成场景中，可通过控制专家模型的 distributional drift（如限制训练步数、增加 KL/通用回放）来主动调整下游
  agent 的领域精度与通用能力保留，避免部署后才发现泛化崩坏。

  - 跨模型家族、多语言结果的强相关性说明：多语言电商或跨域蒸馏时，专家模型的隐式选择会遗传给学生，可用同一探针方法做跨语言一致性检查。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：专家蒸馏通常依赖 teacher 生成的 reasoning trajectories，但很多领域 specialist 只用 QA 对训练，没有显式推理监督。这些轨迹从何而来、受什么控制，此前不清晰。

方法关键点：把 student distillation 当作 agnostic probe——学生只继承 specialist 采样出的轨迹，而不继承其参数化或优化约束。通过观察学生，隔离并分析 specialist 的隐式轨迹分布。进一步通过显式控制 specialist 的 distributional drift，系统改变 teacher 与学生之间的 domain precision 与 general-capability retention 平衡。

关键结果：在 27 组 specialist-student 配对中，两者 specialization-generalization profiles 表现出极强相关；在化学、物理、多语言设置下，蒸馏学生均系统反映专家诱导的 profile，且跨不同模型家族成立。结论：当缺少 gold reasoning 时，tuning 选择直接控制传给下游模型的隐式监督。
