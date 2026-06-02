---
title: 'Trustworthy Recommendation in the Era of Large Language Models: Opportunities
  and Challenges'
title_zh: 大模型时代可信推荐：机遇与挑战综述
authors:
- Bohao Wang
- Yu Cui
- Zhenxiang Xu
- Jujia Zhao
- Chenxiao Fan
- Jizhi Zhang
- Weiqin Yang
- Shengjia Zhang
- Sirui Chen
- Yang Zhang
affiliations:
- Zhejiang University
- Leiden University
- University of Science and Technology of China
- National University of Singapore
arxiv_id: '2606.00540'
url: https://arxiv.org/abs/2606.00540
pdf_url: https://arxiv.org/pdf/2606.00540
published: '2026-05-30'
collected: '2026-06-02'
category: RecSys
direction: LLM增强推荐的可信性综述
tags:
- LLM
- Trustworthy AI
- Recommender Systems
- Bias
- Explainability
- Robustness
one_liner: 系统梳理LLM推荐在鲁棒性、公平性、可解释性等六维度的13项机遇与18项挑战，揭示其双刃剑效应
practical_value: '- **冷启动与数据增强**：可借鉴LLM生成合成交互（如ColdLLM、LLM-search）或提取语义嵌入（MoRec）来缓解新物品/新用户冷启动，电商上新时直接调用LLM生成高质量伪样本辅助训练。

  - **攻击防御策略**：在Agent推荐系统中，警惕记忆污染攻击（如DrunkAgent）；可部署LLM驱动的防御模块（如LoRec）做恶意用户检测，或利用语义一致性检测伪造文本（P-Scanner）。

  - **偏见缓解工程**：微调推荐LLM会放大流行度偏见，可结合逆倾向加权（IPS）或DPO框架（如SPRec）做解耦训练；推理时通过随机打乱候选集多次生成并聚合结果（STELLA、RecRanker）缓解位置偏见。

  - **可解释性落地**：利用LLM生成个性化自然语言解释直接提升用户信任（如Chat-REC），但需用人类反馈或奖励模型对齐；在评估阶段，可直接用LLM作为可解释质量的多维度自动评测器，降低人工成本。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：推荐系统正从单纯追求精度转向综合可信性，需同时满足鲁棒、公平、可解释、事实正确、可控、隐私保护等多目标。大语言模型（LLM）的引入深刻改变了推荐范式，但现有研究碎片化，缺乏统一视图。本文旨在系统回答：LLM如何重塑推荐系统的可信性图景？

**方法**：
- 综述超过200篇顶会/期刊文献，构建全新三层分类法，覆盖LLM-based与LLM-enhanced两种推荐范式。
- 从六个可信维度（鲁棒性、偏见与公平、可解释性、事实性、可控性、隐私）分别梳理机遇与挑战：
  - **鲁棒性**：机遇包括用LLM防御数据投毒、文本攻击（如LoRec、SemanticShield），以及数据去噪（LLM4DSR）和分布偏移适应（DRDT）；挑战则包括LLM引入的新攻击面（文本对抗、后门攻击、Agent记忆操纵）和自身知识噪声。
  - **偏见与公平**：机遇包括利用LLM缓解冷启动（ColdLLM）、弱流行度偏见；挑战包括微调放大流行度偏见（需IPS/DPO解偏）、LLM继承的社会刻板印象导致用户/物品侧不公平、新引入的位置偏见（候选顺序影响输出）等。
  - **可解释性**：机遇体现在用户侧自然语言解释（LlamaRec、ReXPlug）和模型侧思维链透出（ThinkRec、LatentR3）；挑战包括过度依赖外部知识、生成误导性解释（幻觉）、个性化过度导致客观性丧失。
  - **事实性**：LLM生成推荐易产生虚构物品与知识幻觉，需通过RAG（K-RagRec）或知识图谱约束（KGRec）改善。
  - **可控性**：对话交互赋予用户更灵活的控制力（RecLM-gen），但面临语义歧义和提示敏感性。
  - **隐私**：LLM可减少对显式行为数据的依赖，但训练/推理中的记忆泄露风险（MIARS）亟待解决。
- 总结评估协议：常用数据集（MovieLens, Amazon等）和度量指标（NDCG, Diversity, Fairness metrics等），并指出当前评估离散、缺乏统一基准。

**关键洞见**：LLM在提升推荐能力的同时，也扩展了攻击面并引入新偏见/幻觉；未来需在Agent可信性、多目标权衡、理论保障与高效推理等方向突破。论文为从业者提供了机遇和风险的全面地图。
