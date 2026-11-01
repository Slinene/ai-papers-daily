---
title: 'How I Aligned Your Model: Scaling Up Multilingual Safety Training with Templates'
title_zh: 如何对齐你的模型：用模板扩展多语言安全训练
authors:
- Max Neuwinger
- Hanna Yukhymenko
- Imanol Schlag
affiliations:
- ETH Zurich
arxiv_id: '2610.40516'
url: https://arxiv.org/abs/2610.40516
pdf_url: https://arxiv.org/pdf/2610.40516
published: '2026-10-29'
collected: '2026-11-01'
category: Training
direction: 多语言安全对齐数据增强
tags:
- multilingual safety
- data augmentation
- template-based
- alignment
- low-resource languages
- red-teaming
one_liner: 提出模板化多语言安全数据增强流水线，发布60语言MSafeTemp语料并揭示英语评估会误判多语言安全
practical_value: '- **多语言生成式推荐/搜索的评估必须本地化**：论文证明仅英语评估会漏掉多语言攻击和文化适配后的失败。电商全球场景中，多语言产品描述生成、搜索建议、客服Agent的安全与质量评估同样不能只测英语，需构建目标语言+文化适配的测试集，尤其注意文化特定实体（本地品牌、俗语、敏感话题）。

  - **模板化数据增强可复用于多语言query/文案生成**：从已有的有害/敏感prompt中抽取安全模板，翻译并填充文化真实实体，是低成本扩充多语言训练数据的方法。在推荐系统里可类比地用于生成多语言搜索词、商品标题或营销文案的多样化训练样本，避免人工撰写成本。

  - **安全对齐是部署多语言LLM Agent的硬前提**：搜索推荐Agent会处理用户输入并返回建议，若多语言安全漏洞被利用，后果严重。这篇工作提示在训练或SFT阶段应加入多语言安全数据，且要包括本地化有害实体，而不是简单翻译英语安全样本。

  - **数据质量控制流程值得借鉴**：论文中通过母语者验证、自动过滤等步骤确保生成语料质量，这种流水线可迁移到业务中大规模生成数据时的质量把关环节。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：现有LLM安全对齐高度英语中心化，多语言尤其低资源语言数据稀缺，导致红队攻击在非英语语言更容易成功。英语中可靠的拒绝提示在翻译或融入当地文化实体（极端组织、历史事件、特定俚语）后可能被模型遵从，而开源多语言安全数据规模小且缺乏地域化有害主题。

**方法关键点**：提出可扩展的模板化数据增强流水线：从有害提示中抽取“安全模板”，将其翻译到目标语言，再用文化真实的有害与良性实体填充槽位，生成大规模多语言拒绝与良性语料。作者发布MSafeTemp，一个覆盖60种语言的验证语料，用于多语言安全对齐训练与评估。

**关键结果**：实验表明仅用英语评估会误判多语言安全：多个模型在英语中拒绝的攻击在翻译后成功，文化本地化变体进一步暴露翻译自身未发现的失败。使用模板增强的安全训练数据能提升对齐多样性与质量，改善英语之外的安全性能，证实了模板数据增强对多语言安全对齐的有效性。
