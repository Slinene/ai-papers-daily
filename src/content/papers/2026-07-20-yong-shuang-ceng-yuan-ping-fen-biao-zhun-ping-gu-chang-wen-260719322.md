---
title: 'Two-Level Meta-Rubrics for Evaluating Open-Ended Generation: GAMUT, a Benchmark
  for Factual Completeness'
title_zh: 用双层元评分标准评估长文本生成的事实完整性：GAMUT基准
authors:
- Xilun Chen
- Zhaleh Feizollahi
- Ross Goodwin
- Seungwhan Moon
- Scott Yih
- Pinar Donmez
- Babak Damavandi
- Luna Dong
affiliations:
- Meta AI
arxiv_id: '2607.19322'
url: https://arxiv.org/abs/2607.19322
pdf_url: https://arxiv.org/pdf/2607.19322
published: '2026-07-20'
collected: '2026-07-23'
category: Eval
direction: 长文本生成评估 · 事实完整性
tags:
- Factual Completeness
- Long-form Evaluation
- Meta-Rubric
- LLM-as-a-Judge
- Multimodal
- Benchmark
one_liner: 提出双层元评分框架，将结构化回答要求编译为二进制检查表，构建首个多模态日常深度研究事实完整性基准GAMUT
practical_value: '- **结构化评估思想可迁移到生成式推荐场景**：当用LLM生成商品描述、购买理由或搭配建议时，可用类似“元评分标准→二进制检查表”的方式，将产品卖点、品牌调性等要求编为可自动评分的
  checklist，避免人工审核偏差。

  - **开放集合覆盖率评分可用于推荐多样性评估**：Flexible List 的“基线覆盖率+额外加分”机制，类似推荐列表中长尾商品覆盖度的评估，可设计为“至少命中k个相关类目”的自动打分规则。

  - **多层级重要性权重的工程落地**：将回答内容分为 Answer-Critical/Valuable/Context 三个等级并全局加权，推荐系统的解释生成也可采用类似分层，保障核心产品信息被覆盖，次要信息锦上添花。

  - **双层设计分离“期望描述”与“实际打分”**：工程上可将复杂的评测标准维护在结构化层，打分时用机械规则展开为简单判断项，降低LLM法官的评分方差，适合大规模生产环境中的自动化评估。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
现有长文本事实性评估主要聚焦于准确率（precision），通过拆分-检索-验证流水线检查已生成断言的正确性，但对召回率（recall）——即回答是否包含了完整信息——关注不足。更关键的是，无论是精度还是召回方法，都假设事实性可被拆解为一组独立布尔判断的列表，忽略了真实回答中常见的开放集合覆盖、顺序过程及事实间关系。这导致评估失真：例如一道菜的传统做法可列举多种食材（开放集合），回答只需覆盖足够多种而非特定几种；又比如工艺流程必须描述正确顺序，单纯的逐条判断无法捕捉此类错误。因此，需要一种能表达回答结构（重要性、顺序、分组）的评估表示，同时保证自动评分的可靠性。

## 方法关键点
- **双层元评分框架**：第一层为结构化元评分标准（meta-rubric），描述完整答案应包含的内容结构，包括简单知识、严格列表、灵活列表、过程、关系五种类型，并赋予 Answer-Critical / Valuable / Context 三个重要性层级；第二层通过机械规则将元评分标准编译为扁平二进制检查表，供LLM法官打分。
- **评分机制**：对每个检查项LLM给出满足/部分满足/遗漏/矛盾四种判决，映射为分数后按重要性加权得到GAMUT分数（范围-1到1，矛盾惩罚重于遗漏）。
- **数据集构建**：基于可穿戴设备拍摄的1938张真实图像，生成了1813个“日常深度研究”问题（如“这个糕点为何层次分明？”），覆盖10个领域。问题创建和评分标准生成均通过前沿LLM提出初稿，再由多位专家标注员多轮修订，确保评分标准有证据支撑且非模型幻觉。
- **测试模型**：评估了Gemini、Claude、GPT、Qwen、Llama等14个前沿及开源模型，使用Gemini 3.1 Pro作为主评官，且更换评官后排名稳定。

## 关键结果
- 最佳模型Gemini 3.1 Pro仅得58.7%的GAMUT分数，所有模型在Answer-Critical级别都有大量遗漏（missing verdicts）；模型之间差距主要来自遗漏而非错误回答。
- 评分标准结构广泛存在：98%的问题需要至少一种非简单知识的结构，其中灵活列表占86%，过程占17%。
- 纯文本变体实验显示，去掉视觉识别后所有模型加分约10–20点，且排名基本不变，表明基准衡量的是知识完整性而非感知能力差距。
- 更换三个不同的LLM评委，排名几乎一致，表明框架对评委选择鲁棒。
