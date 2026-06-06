---
title: LLM Anonymization Against Agentic Re-Identification
title_zh: 抵抗智能体重识别的LLM匿名化框架
authors:
- Ziwen Li
- Jianing Wen
- Tianshi Li
affiliations:
- Northeastern University
arxiv_id: '2605.30848'
url: https://arxiv.org/abs/2605.30848
pdf_url: https://arxiv.org/pdf/2605.30848
published: '2026-05-31'
collected: '2026-06-06'
category: Agent
direction: Agent 智能体对抗性隐私保护
tags:
- LLM
- Anonymization
- Agentic Re-identification
- Privacy-Utility Trade-off
- Mask-Reconstruct
one_liner: 提出掩码-重建的匿名化方法，通过自适应隐私范围平衡抗智能体重识别与文本实用性
practical_value: '- 处理用户评论文本或客服对话时，可借鉴掩码-重建流水线：先用LLM定位敏感上下文并遮蔽，再由另一个LLM生成保留语义的非敏感替代表述，既防重识别又保留分析价值。

  - 引入对抗隐私检查环节：模拟网络搜索代理尝试重识别，可作为内部隐私测试工具，确保发布数据前充分抵御真实威胁。

  - 设计多维实用性评估：不仅看语义相似度，还考量事实一致性、上下文连贯性等，对评估匿名化后文本在下游任务（如意图分类、查询理解）中的可用性有参考。

  - 自适应隐私范围调节：根据数据用途动态调整遮蔽强度（如个性化分析保留更多细节，聚合统计可严格匿名），为业务中动态平衡合规与效用提供工程思路。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：LLM智能体具备网络搜索能力后，文本匿名化面临新威胁——细微上下文线索可被交叉引用重识别个人，但移除这些线索又损害下游分析价值。现有方法未能有效应对此类智能体重识别。

方法：提出AURA框架，采用掩码-重建范式，将隐私定位与实用性重建解耦。具体流程：1) LLM识别并遮蔽文本中可能关联身份的上下文；2) 生成多个候选改写；3) 通过对抗性隐私检查（模拟网络搜索重识别）和实用性保留检查（基于受访者事实、编码本事实及上下文联合实用性网格）筛选最优结果。自适应隐私范围允许按需调整遮蔽粒度。

结果：在真实用户采访记录上测评，使用网络搜索智能体发动重识别攻击。AURA相比基线（删除标识符、文本扰动、非对抗改写）在隐私-实用性前沿上提升显著：在同等隐私保护下，更好保留了受访者档案事实和上下文连贯性；在同等实用性下，抗重识别成功率提高。掩码-重建设计被验证为关键，尤其在固定隐私范围内能最大化保留语境信息。
