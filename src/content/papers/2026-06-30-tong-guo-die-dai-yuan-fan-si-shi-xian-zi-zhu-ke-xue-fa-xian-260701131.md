---
title: Autonomous Scientific Discovery via Iterative Meta-Reflection
title_zh: 通过迭代元反思实现自主科学发现
authors:
- Bingchen Zhao
- Sara Beery
- Oisin Mac Aodha
affiliations:
- University of Edinburgh
- Massachusetts Institute of Technology
arxiv_id: '2607.01131'
url: https://arxiv.org/abs/2607.01131
pdf_url: https://arxiv.org/pdf/2607.01131
published: '2026-06-30'
collected: '2026-07-03'
category: Agent
direction: 自主发现 · 迭代元反思
tags:
- LLM
- Agent
- Meta-reflection
- Scientific Discovery
- Hypothesis Testing
one_liner: 提出 DiscoPER 框架，让 LLM 通过二阶元反思机制自主迭代发现科学规律，在生态基准上恢复 89% 已知模式
practical_value: '- **二阶反思机制可迁移至搜索/推荐 Agent**：在自动生成 Query 或探索推荐策略时，引入定期复盘已探索空间，识别模式、偏见与空白，主动跳转至高价值未覆盖区域，提升长尾覆盖与策略多样性。

  - **统计检验作为硬约束**：任何生成的新假设必须通过统计验证，这一点可直接用于广告文案 A/B 测试、推荐策略上线流程，让 Agent 决策具备统计可信度。

  - **工具调用扩展多模态特征**：推荐系统可仿照 DiscoPER 通过 Tool Use 无缝接入图像理解、OCR 等工具，从商品图片、评论区截图等多模态源提取结构化信息，丰富用户和物品特征。

  - **自动特征工程与模型搜索**：将开放式探索与元反思结合，用于自动化生成并验证特征组合、模型结构，周期性反思哪些方向尚未尝试，提高有限算力下的搜索效率。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有基于 LLM 的科学发现系统大多要求预设研究方向，且假设生成过程相互孤立，无法从历史发现中归纳结构性规律、识别知识空白，限制了真正开放式探索的能力。

**方法**：提出 DiscoPER 框架，由 LLM 代理动态生成并执行代码，在不预设目标的情况下开放式挖掘数据集。核心创新在于引入二阶元反思机制：系统定期将此前已验证的发现作为输入，通过元分析识别宏观模式、混淆因素和未探索的假设空间，从而重定向后续探索方向。每一个新假设必须通过统计检验才被归档为发现。搜索空间还通过工具使用得到扩展，代理可实时调用多模态处理工具（如图像理解），从非结构化数据中提取有用变量。

**结果**：在多模态生态知识基准 iNatDisco 上，DiscoPER 成功复现了 9 个已知科学规律中的 8 个，假设支持率达到 72.7%，显著优于经典因果发现算法和纯 LLM 引导的基线模型。消融实验证实二阶元反思能持续提升发现质量，且系统性能随数据量增加而提升。
