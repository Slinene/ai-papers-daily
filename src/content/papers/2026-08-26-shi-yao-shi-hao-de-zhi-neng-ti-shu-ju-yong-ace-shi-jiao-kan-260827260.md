---
title: What Makes Good Agentic Data? An ACE Lens on Data Generation for LLM Agents
title_zh: 什么是好的智能体数据？用 ACE 视角看 LLM 智能体数据生成
authors:
- Xingshan Zeng
- Zishan Xu
- Boju Zhang
- Yuzhou Wu
- Lingzhi Wang
- Jianghao Lin
- Liangyou Li
- Yasheng Wang
- Lifeng Shang
- Xin Jiang
affiliations:
- Huawei Technologies Co., Ltd
- Shanghai Jiao Tong University
- Northwestern University
- Harbin Institute of Technology, Shenzhen
- Shenzhen Loop Area Institute
arxiv_id: '2608.27260'
url: https://arxiv.org/abs/2608.27260
pdf_url: https://arxiv.org/pdf/2608.27260
published: '2026-08-26'
collected: '2026-08-28'
category: Training
direction: LLM Agent 训练数据生成
tags:
- LLM Agents
- Data Generation
- Training Data
- ACE Framework
- Agentic Data
one_liner: 提出 ACE 框架（准确性-复杂度-多样性）统一评估和设计 LLM 智能体的交互数据生成
practical_value: '- 构建电商/搜索 Agent 训练数据时，可直接用 ACE 框架做数据质检：Accuracy 确保任务信号与环境反馈一致，Complexity
  根据目标模型能力分配难度，Diversity 覆盖不同用户意图、商品类目和交互路径，避免只堆数据量。

  - 将交互数据统一表示为 (E,q,τ,v) 四元组（环境、任务、交互轨迹、验证器），便于多源数据融合、版本管理和过滤，适合电商场景中模拟用户对话、搜索行为、工具调用等混合数据。

  - 优先采用执行锚定的数据生成：让 Agent 实际调用工具并记录真实结果或环境反馈，而不是只生成最终答案，防止模型学到“看似合理但无法执行”的交互模式。

  - 多样性不要只做表面改写（换词、换句式），要扩展行为覆盖：增加异常处理、多轮协商、不同查询路径等，这对电商 Agent 应对长尾场景尤其重要。'
score: 7
source: huggingface-daily
depth: abstract
---

## 动机
LLM Agent 依赖生成的交互数据学习与环境交互，但现有工作分散在不同领域，评估异构，难以提炼通用机制。数据生成需要同时保证环境、任务、交互和成功信号的一致性，且数据要“有用”而非仅仅“丰富”。

## 方法关键点
论文提出两级框架：
1. **数据表示**：将智能体数据统一为四元组 (E, q, τ, v)——环境规范、任务信号、交互实现、可选验证器，并据此区分前向与反向生成范式。
2. **ACE 透镜**：把生成看作约束分布设计。
   - **Accuracy（准确性）**：建立可行支撑集，确保数据有依据且内部一致，强调执行锚定而非表面合理。
   - **Complexity（复杂度）**：根据声明的学习器能力和执行配置分配学习质量，难度应相对学习器校准。
   - **divErsity（多样性）**：控制覆盖和冗余，超越表面变化或数据集规模。

## 关键结果
综述显示趋势：准确性走向执行锚定，复杂度走向学习器相对化，多样性走向行为覆盖扩展。核心挑战不是生成更多数据，而是持续分配有效、信息丰富、非冗余的经验，以适应智能体和环境的演化。
