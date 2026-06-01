---
title: Exploring Autonomous Agentic Data Engineering for Model Specialization
title_zh: 探索自主智能体数据工程实现模型专业化
authors:
- Yujie Luo
- Xiangyuan Ru
- Jingsheng Zheng
- Jingjing Wang
- Yuqi Zhu
- Jintian Zhang
- Runnan Fang
- Kewei Xu
- Ye Liu
- Zheng Wei
affiliations:
- Zhejiang University
- Platform and Content Group, Tencent
arxiv_id: '2605.30407'
url: https://arxiv.org/abs/2605.30407
pdf_url: https://arxiv.org/pdf/2605.30407
published: '2026-05-27'
collected: '2026-06-01'
category: Agent
direction: Agent 驱动的数据工程与模型专业化
tags:
- Agentic Data Engineering
- Model Specialization
- LLM Agent
- Synthetic Data
- Iterative Optimization
- Curriculum Learning
one_liner: 将数据工程形式化为端到端闭环任务，让LLM自主策划训练数据以驱动学生模型专业化，在三个领域取得显著增益
practical_value: '- **用 Agent 闭环自动化领域微调数据生产**：借鉴 Iterative Agent 架构，将数据策展建模为 Draft→Debug→Repair→Improve
  迭代循环，利用学生模型在公开验证集上的性能作为反馈信号，贪心地选择历史最佳提交，可复用于电商推荐场景的指令数据合成（如商品描述生成、搜索词改写）。只需提供任务描述、种子池和
  API 预算，无需人工设计数据流水线。

  - **多样性比质量更依赖迭代**：分析显示，迭代主要提升生成数据的多样性（instruction/response diversity），而响应质量提升有限。在构建商品/店铺推荐数据时，可重点通过迭代扩展问题覆盖范围，避免重复生成高难度但同质化的样本。

  - **用 Greedy Public-Score Selection 提升鲁棒性**：由于合成数据引入高方差，单次提交可能性能骤降。采用贪心策略保留公开集上历史最佳提交，能显著减少灾难性遗忘与波动，这一简单方法可直接用于
  Agent 驱动的数据优化管线。

  - **警惕 LLM 的数据量保证缺失与格式处理陷阱**：实验显示主流 Agent 普遍缺乏对最终数据集大小的主动校验，且在处理 LaTeX/代码等复杂格式时大量样本被过滤。在生成电商知识问答数据时，务必在
  Agent 工作流中显式加入数量检查和格式补全模块，必要时限制单次数据生成逻辑的复杂度，避免 API 输出截断。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：大模型在通用任务上表现优异，但迁移到电商、金融等专业领域时仍依赖高质量领域微调数据。现有数据策展方法依赖人工设计的流水线，面对新领域需要大量配置。本文探究能否将 LLM 作为自主数据工程师，独立完成端到端的数据工程（策略规划→提示设计→数据合成→验证→迭代优化），并通过学生模型的后训练性能反馈来驱动优化。

**方法关键点**：
- 形式化 **Agentic Data Engineering** 任务：固定 teacher 模型（数据合成）和 student 模型（微调评估），让 Agent 通过生成代码调用 teacher API 合成训练数据，目标最大化 student 微调后在隐藏测试集上的性能增益。
- 设计两种 Agent 模式：**One-Shot**（单次生成提交）和 **Iterative Agent**（闭环迭代，通过 Draft→Debug→Repair→Improve 四个操作利用环境反馈自我改进）。
- 构建涵盖 **Science (SciBench)、Code (LiveCodeBench-TOP)、Finance (FinanceReasoning)** 三个专业化领域的评估环境，所有任务采用规则化评分以保证反馈可靠性。
- 提供可选的种子数据池（1k 原始问题），测试 Agent 从零生成与从种子改进的能力。

**关键结果**：
- Iterative Agent 全面优于 One-Shot：GPT‑5.2 从零起始的平均相对增益从 40.73% 提升到 **57.29%**；DeepSeek‑V3.1 在迭代加种子的设置下从 12.50% 飙升至 57.65%。
- 加入 1k 种子数据后，多数模型的增益额外提升 30% 以上，尤其稳定了脆弱的一次生成。
- 与人类设计的 DataFlow 框架对比，GPT‑5.2 自主设计的流水线取得更高增益（93.19% vs. 65.82%），说明 LLM 能灵活适配任务，自动对齐数据分布。
- 迭代主要增强 **数据多样性**而非响应质量；Agent 在数量保证和复杂格式处理上存在显著失败模式（如 Claude‑4‑Sonnet 输出截断率高达 59.31%）。

**值得记住的一句话**：LLM 智能体可以自主实现数据工程的端到端闭环优化，但当前仍需显式加入质量保障和数量校验机制才能稳定落地。
