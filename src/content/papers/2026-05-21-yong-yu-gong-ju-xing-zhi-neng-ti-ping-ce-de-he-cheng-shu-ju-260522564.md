---
title: 'SynAE: A Framework for Measuring the Quality of Synthetic Data for Tool-Calling
  Agent Evaluations'
title_zh: 用于工具型智能体评测的合成数据质量框架SynAE
authors:
- Shuaiqi Wang
- Aadyaa Maddi
- Zinan Lin
- Giulia Fanti
affiliations:
- Carnegie Mellon University
- Microsoft Research
arxiv_id: '2605.22564'
url: https://arxiv.org/abs/2605.22564
pdf_url: https://arxiv.org/pdf/2605.22564
published: '2026-05-21'
collected: '2026-05-22'
category: Eval
direction: 工具调用型Agent 合成数据评估
tags:
- synthetic data
- agent evaluation
- tool-calling
- validity
- fidelity
- diversity
one_liner: SynAE从有效性、保真度、多样性三维度系统评估合成多轮工具调用Agent轨迹的质量
practical_value: '- **合成Agent数据质量检查清单**：在电商Agent评测中引入SynAE的多轴评估，避免仅靠单一指标（如任务完成率）判断合成数据可用性，特别关注有效性（工具调用是否真的能完成任务）与下游排名一致性（Ranking
  Divergence）。

  - **工具规划保真度指标**：借鉴Tool Usage Match、k-Step Planning等指标，量化生成式推荐中多步工具调用序列的合理性，防止合成数据引入不切实际的工具使用模式。

  - **指令-响应结构保真度**：采用Key Node Dependency和Attribute Match检查合成对话的轮次依赖和统计属性，确保合成指令与真实用户意图分布一致，适用于对话推荐系统。

  - **迭代优化合成流程**：参考案例中“先诊断再升级”的策略：先用SynAE定位diversity瓶颈，再尝试轻量改写（如关键词替换）快速验证，最后用更高能力模型做全合成，每一步都用SynAE反馈调整，适合电商Agent的合成数据增强。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
多轮工具调用Agent的评测常依赖静态交互轨迹数据集，但真实数据常因隐私或稀疏无法直接使用，合成数据成为主流替代。缺少系统量化合成数据与真实数据差异的方法，导致评测结果不可靠。

### 方法关键点
- **评估维度**：有效性（工具调用、输出是否完成指令）、保真度（合成数据与真实数据的结构和语义相似度）、多样性（覆盖率）。
- **保真度指标**：
  - 指令-响应：Key Node Dependency（相邻轮次语义依赖）、Attribute Match（统计/语义属性分布距离）、KNN-Precision/Recall、FID。
  - 工具调用：Tool Usage Match（工具分布TV距离）、Tool Call Number Match（调用次数W2距离）、k-Step Planning（条件工具序列分布）。
  - 下游评估：Task Difficulty Difference（不同Agent在两个数据集上的成功率差异）、Ranking Divergence（模型排名Spearman相关）。
- **有效性**：默认用LLM-as-a-judge判断工具调用和输出是否完成指令，支持替换为规则检查器。
- **多样性**：Vendi Score（基于嵌入的指数熵）与Attribute Diversity（用户指定属性的熵）。
- **输入**：真实数据集、合成数据集、可选的领域先验和评测Agent。

### 关键结果
在T1、BFCL、ACP三个基准上，通过受控合成方法（Blank Filling、Oversampling、In-Context Generation、Invalidation）和工业工具NVIDIA NeMo验证：
- 随掩码率p增加，Blank Filling的输出KNN-Precision从近1降至近0，但多样性提升；Oversampling随重复率r增加保真度与多样性同时下降。
- Invalidation实验中，有效性随替换比例v线性下降（斜率约-1）。
- 单一指标无法全面反映质量：例如In-Context Generation中k=3提升Precision但降低Recall；Ranking Divergence在工具调用场景下即使规划模式变化仍保持高位，说明模型排名相对稳健。
- 案例研究展示利用SynAE诊断→轻量改写→模型升级的迭代改进流程，最终用GPT-4o-mini在保持有效性的同时将多样性从0.48提升至0.70。

**最值得记住的一句话**：任何单一指标都不足以完全刻画合成Agent轨迹的质量，必须从有效性、保真度、多样性三个维度进行综合评估。
