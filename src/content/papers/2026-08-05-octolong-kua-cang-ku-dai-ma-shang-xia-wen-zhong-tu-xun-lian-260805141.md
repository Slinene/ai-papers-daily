---
title: 'OctoLong: Mid-Training On Cross-Repository Code Contexts Enhances Long-Context
  Modeling'
title_zh: OctoLong：跨仓库代码上下文中途训练增强长上下文建模
authors:
- Indraneil Paul
- Falko Helm
- Goran Glavaš
- Iryna Gurevych
affiliations:
- UKP Lab & Center for Applied Cybersecurity ATHENE, TU Darmstadt
- CAIDAS, University of Würzburg
arxiv_id: '2608.05141'
url: https://arxiv.org/abs/2608.05141
pdf_url: https://arxiv.org/pdf/2608.05141
published: '2026-08-05'
collected: '2026-08-06'
category: LLM
direction: 长上下文数据工程 · 递归依赖增强
tags:
- long-context
- code-context
- mid-training
- data-engineering
- agentic-tasks
- cross-repository
one_liner: 通过递归检索代码依赖构建富含长距离依赖的长上下文数据，仅占12%训练数据即大幅提升长程检索与Agent任务
practical_value: '- **构造富含依赖的长序列训练数据**：对于需要处理用户长期行为序列的推荐或搜索场景，可借鉴通过解析商品间显式/隐式依赖（如共现、因果、点击链）来生成高信息量的长上下文样本，而非简单的时间拼接，提升模型对长程依赖的建模。

  - **少量高质数据即可生效**：论文证明仅将12%的依赖丰富数据混入训练即可大幅提升长上下文性能。在资源有限的业务中，可针对特定长尾任务，低成本构造小批量高质量长序列样本，快速注入所需的长程推理能力。

  - **Agent 长历史状态追踪**：对于多步工具调用的Agent系统，可引入类似的依赖图构建思路，在上下文窗口中动态维护工具调用链之间的隐式依赖，缓解长horizon下的状态丢失问题。

  - **分阶段扩展上下文的训练策略**：先在大规模短上下文上预训练，再利用构造的长上下文数据进行中程微调扩展窗口，最后指令微调，这一流程可在不损失原有能力的前提下高效扩展推荐或Agent模型的最大输入长度。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：当前语言模型上下文长度呈指数增长，但用于扩展长上下文能力的训练数据以书籍、论文和独立代码库为主，普遍缺乏长距离依赖关系，限制了模型在长程检索、状态跟踪及Agent任务上的表现。

**方法**：提出OctoLong数据工程流水线——结合AST解析、语言服务器和包管理器，递归检索代码引用（函数调用、类导入等），构建包含数百万token且跨文件、跨仓库依赖关系的代码上下文。将该数据按12%比例混入约50B token的总训练语料，对600M至14B参数的基座模型进行上下文扩展的中途训练，再经10B token指令微调得到OctoLong-Instruct系列模型。

**结果**：与18个主流开源长上下文模型对比，在长程检索（Needle-in-a-Haystack类）、长期状态追踪（LongMemEval等）、仓库级代码理解（RepoBench）及复杂Agent任务（SWE-Bench Partial）上均取得显著提升；同时发现短期代码API使用能力也有所增强，证明少量依赖增强数据即可高效释放长上下文潜力。
