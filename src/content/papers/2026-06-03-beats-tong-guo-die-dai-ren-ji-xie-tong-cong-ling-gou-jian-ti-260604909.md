---
title: 'BEATS: Bootstrapping E-commerce Attribute Taxonomies for Search through Iterative
  Human-AI Collaboration'
title_zh: BEATS：通过迭代人机协同，从零构建电商搜索属性体系
authors:
- Yung-Yu Shih
- Shang-Yu Su
- Tzu-I Ho
- Dongzhe Wang
- Yun-Nung Chen
affiliations:
- National Taiwan University
- Rakuten Group, Inc.
- Taiwan Rakuten Ichiba, Inc.
- Rakuten Asia Pte. Ltd.
arxiv_id: '2606.04909'
url: https://arxiv.org/abs/2606.04909
pdf_url: https://arxiv.org/pdf/2606.04909
published: '2026-06-03'
collected: '2026-06-04'
category: RecSys
direction: 电商搜索 · 属性体系构建 · 人机协同
tags:
- Attribute Taxonomy
- Human-in-the-Loop
- LLM Ensemble
- Prompt Refinement
- Dense Retrieval
- E-commerce Search
one_liner: 将多模型LLM生成、合成与精炼与迭代人审结合，从无到有构建电商属性体系，显著改善搜索体验。
practical_value: '- 从零构建电商属性体系的标准化流程：多源LLM生成候选属性→生成式合成合并→精炼去噪，再经开发人员预审与领域专家标注，迭代优化prompt。对于冷启动平台，可快速复制。

  - 多模型集成思路：选用架构、训练数据、规模差异大的LLM（如GPT-OSS、Qwen3文本/视觉版）分别生成，通过多样性保证覆盖，合成模型统一规范。在电商属性生成中，不同模型各有所长（有的擅长技术参数、有的擅长使用场景）。

  - 迭代prompt优化的技巧：根据质量检查与标注反馈，添加负面样例、调整粒度指令、引入类别上下文，并针对系统性错误升级精炼模型。第二轮接受率从89%飙升至99.88%，可直接复用这类迭代策略。

  - 属性标注直接反哺搜索：利用生成的属性类型对商品进行结构化标注，无需预定义值集，即可丰富稠密检索的文本表示。在本实验中，仅凭属性文本增强，双塔稠密检索R@10提升5.7%，NDCG@10提升5.7%，零架构改动。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
新兴市场的电商平台往往只有粗糙的类目体系，缺少细粒度的产品属性（如材质、尺寸、颜色），导致无法实现搜索的筛选导航、特征排序和语义理解。人工构建属性体系成本高昂，而单次LLM生成又存在幻觉和不一致。为此，论文提出BEATS，一个从零冷启动构建属性体系的迭代人机协同框架。

**方法关键点**
- **多源生成**：使用三个异构LLM（GPT-OSS-120B、Qwen3-30B、Qwen3-VL-235B）独立生成候选属性，利用模型多样性提升覆盖面。
- **生成式合成**：由一个合成模型将多个候选集合并为统一属性集，解决命名冲突和重复。
- **目标精炼**：精炼模型交叉对比类目层级，删除冗余、过于泛化或平台已有的属性。
- **人机质量保证**：开发人员主动检查，提前过滤系统性错误；再由领域专家（11位）对每个属性进行三票多数决标注（Accept/Unsure/Reject）。
- **迭代prompt优化**：每一轮结束后，根据检查观察和标注反馈调整生成、合成、精炼阶段的提示词，升级精炼模型。第二轮迭代中接受率从89%跃升至99.88%，拒绝率降至0.015%。
- **下游属性标注**：用LLM为每个商品打上属性值，无需预定义值集；标签结果用于丰富商品文本，增强稠密检索。

**关键实验**
在乐天台湾9大品类（2694子类）上部署，生成67,277个属性，标注超540万商品。稠密检索实验显示，属性增强后的文本使双塔模型Recall@10从66.6提升至70.4（+5.7%）、NDCG@10从49.2提升至52.0（+5.7%）。属性质量评估中，第二轮接受率99.88%，LLM-as-a-judge验证属性标注准确率0.933。
