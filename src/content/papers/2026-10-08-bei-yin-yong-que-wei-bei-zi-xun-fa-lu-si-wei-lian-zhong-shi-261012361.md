---
title: 'Cited but Not Consulted: A Counterfactual Audit of Legal Chain-of-Thought
  Faithfulness'
title_zh: 被引用却未被咨询：法律思维链忠实性的反事实审计
authors:
- Saisab Sadhu
- Shreeyans Arora
- Pratinav Seth
affiliations:
- Lexsi Labs
arxiv_id: '2610.12361'
url: https://arxiv.org/abs/2610.12361
pdf_url: https://arxiv.org/pdf/2610.12361
published: '2026-10-08'
collected: '2026-10-11'
category: Reasoning
direction: CoT 忠实度反事实审计与红队评估
tags:
- chain-of-thought faithfulness
- counterfactual evaluation
- legal NLP
- LLM auditing
- mechanistic interpretability
one_liner: 反事实替换法律依据并解码隐藏状态，发现LLM命名法规与判决实际依赖严重脱节，且易受对抗指令操纵
practical_value: '- 在推荐/广告场景让 LLM 生成推荐理由时，别把“提到某个特征/商品属性”当作模型真的基于该特征决策的证据；可借鉴反事实替换：把解释中提到的关键依据换成相反/无关项，看输出
  item/排序是否改变，量化理由忠实度。

  - 用隐藏状态探测/线性探针监测模型在生成解释前是否已定下答案，评估“解释是事后再找理由”的程度，对应生成式推荐解释是否只是装饰。

  - 注意对抗指令注入：用户评论、商品描述、query 中可能隐藏指令，LLM可能高度顺从；在电商搜索/客服 Agent 场景要增加输入过滤和角色边界约束，尤其是生成推荐理由或审核决策时。

  - 工程上，合规/审计所需的推荐或风控决策，不应以自然语言理由作为可靠审计日志，应记录底层特征、模型分数等结构化信号。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**  
法律 LLM 常通过命名法规/先例来证明判决依据，命名本身被当作决策可信的证据。但 CoT 可能只是事后合理化，不一定忠实。  

**方法关键点**  
固定案件事实，将模型命名的法律权威替换为无关权威，并从隐藏状态解码模型逐步形成的判决；跨 7 个开源模型（8B–70B）和四个法律推理基准。还进行红队测试：在案件事实中隐藏对抗指令。  

**关键结果**  
模型显式命名正确权威的比例高达 66.7%–100%，但判决随权威替换而改变的比例低得多：CaseHOLD 仅 0.0%–21.7%，ECHR/SCOTUS 30.0%–76.7%，ContractNLI 43.3%–50.0%。模型规模和法律微调 LoRA 均未缩小该差距。隐藏对抗指令的遵从率达 73.3%–96.4%，远高于判决交换敏感性。  

**结论**  
命名法律权威不是判决依赖该权威的可靠代理，生成的法律解释不宜作为合规或审计证据。
