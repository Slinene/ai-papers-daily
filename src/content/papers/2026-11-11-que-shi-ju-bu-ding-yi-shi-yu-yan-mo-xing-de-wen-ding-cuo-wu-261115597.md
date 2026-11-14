---
title: 'When Local Definitions Are Missing: Stable Errors in Language Models'
title_zh: 缺失局部定义时语言模型的稳定错误
authors:
- Zengqing Wu
- Chuan Xiao
affiliations:
- University of Osaka
- Nagoya University
arxiv_id: '2611.15597'
url: https://arxiv.org/abs/2611.15597
pdf_url: https://arxiv.org/pdf/2611.15597
published: '2026-11-11'
collected: '2026-11-14'
category: Eval
direction: LLM 错误分析与稳定错误检测
tags:
- Language Models
- Local Definitions
- Error Analysis
- Confidence Calibration
- Self-Consistency
- Domain Adaptation
one_liner: 研究 LLM 在缺少文档局部定义时对熟悉词汇误解，发现重复采样与置信度均不可靠标记错误
practical_value: '- 电商场景中商品规则、售后条款、活动说明常对常见词赋予特殊含义（如“满减”“包邮”“会员”），LLM 作为客服或推荐 Agent
  容易按常识误解。可借鉴论文做法：在上下文注入源文档的局部定义，或用 RAG 检索定义片段，而非依赖模型预训练语义。

  - 模型自我报告置信度和多次采样结果不能作为错误检测的可靠信号。工程上应增加外部验证步骤，如规则校验、知识库比对或人工抽检，避免仅靠模型自我判断。

  - 可用一个小模型给定标注答案键，预测大模型在哪些题目上容易出错，用于线上风险预估、低置信请求路由到人工或降级处理。

  - 对含大量领域自定义术语的文档（如电商合同、社区规范）构建问答任务时，应显式标注被重定义的词汇，并测试模型在有/无定义下的差异，以量化模型对局部定义的敏感度。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**  
语言模型常用于回答合同、技术手册、在线社区等问题，但这些文档常为常见词赋予特殊含义（如游戏社区中“tank”指保护队友的玩家）。模型若没有读到局部定义，会沿用通用语义，给出看似合理却错误的答案。该研究系统考察这一现象。

**方法关键点**  
- 构建多项选择题，数据来源包括合成词汇、商业合同（CUAD）、Reddit 社区词汇表和去中心化交易所文档。  
- 让三个语言模型分别在有/无局部定义的条件下作答。  
- 不使用答案键，检验模型重复采样答案与自我报告置信度能否标记错误。  
- 额外让一个小型开源模型获得答案键，测试其能否预测大型模型在哪些问题上出错。

**关键结果**  
- 被重新定义的常见词导致最多错误；模型常重复同一错误答案，且重复采样和置信度均不能可靠提示错误。  
- 源文档中的局部定义能修复合成题中大多数错误，但模型自己生成的“先验定义”无效；在真实合同数据上，源定义仅修复约一半错误。  
- 给定答案键的小模型能按出错概率对问题进行排序，可用于预筛高风险问题。  
- 结论呼吁模型评测应结合完整源文档，特别是局部定义来检验答案正确性。
