---
title: Predicting Alignment Generalization with Value Representations
title_zh: 用价值表示预测对齐泛化
authors:
- Andy Liu
- Mehar Bhatia
- Karolina Stanczak
- Mona Diab
- Vered Shwartz
- Daniel Fried
affiliations:
- Carnegie Mellon University
- Mila - Quebec AI Institute
- McGill University
- ETH Zurich
- University of British Columbia
arxiv_id: '2610.12410'
url: https://arxiv.org/abs/2610.12410
pdf_url: https://arxiv.org/pdf/2610.12410
published: '2026-10-08'
collected: '2026-10-10'
category: Eval
direction: LLM对齐泛化预测 · 价值表示
tags:
- alignment generalization
- value representations
- activation analysis
- LLM post-training
- model behavior
- robustness
one_liner: 建立对齐泛化预测任务，激活表示比文本描述更准（ρ=0.45 vs 0.05），并构建首个经验价值分类
practical_value: '- 电商/广告场景下，通过 RLHF/DPO 对齐业务目标（如用户满意度、多样性）时，可构建类似“对齐泛化矩阵”：对每个业务指标微调小模型，测量对其他指标的行为影响，用激活表示预测目标间冲突，提前识别相互干扰。

  - 该方法用模型在应用特定策略/价值观时的隐层激活作为 embedding，比直接用文本描述效果好得多（ρ=0.45 vs 0.05）。在 Agent 或多任务推荐模型中，可采集策略提示下的激活构建“业务目标向量”，用于度量策略相似性、辅助多目标权重设计。

  - 论文发现多价值对齐目标中价值相似度与模型鲁棒性显著相关。实际可借鉴该指标评估多业务指标组合的冲突程度，避免训练目标过窄导致线上行为漂移。

  - 跨模型共享价值空间的初步证据支持构建统一目标表示：如召回、粗排、精排等多个模型协同的推荐系统，可用相同“业务价值向量”对齐不同模型的行为，提升整体一致性。注意预测精度仍有限（ρ=0.45），适合作为粗筛或辅助决策工具。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**  
LLM 后训练希望模型展现亲社会价值观，但针对窄行为训练仍会意外影响未见环境。需要预测对特定价值微调后会如何改变模型在其他 held-out 价值观上的行为。

**方法关键点**  
提出“对齐泛化预测”任务：收集 66 个现代对齐目标中的价值观，通过逐一微调模型测量对全部价值的行为影响，构建泛化矩阵。基准两类表示方法：基于文本描述的价值 embedding vs 基于模型在上下文中应用价值时的激活表示。最佳激活方法获得 ρ=0.45，而描述基线仅 ρ=0.05。进一步用预测泛化的表示度量多价值对齐目标中价值相似度，发现该相似度与模型鲁棒性显著相关；还发现跨模型共享价值空间的初步证据，据此构建首个经验驱动的 LLM 价值分类。

**关键结果数字**  
66 个价值；最佳激活表示 ρ=0.45 vs 文本描述 ρ=0.05；价值相似度与鲁棒性显著相关。
