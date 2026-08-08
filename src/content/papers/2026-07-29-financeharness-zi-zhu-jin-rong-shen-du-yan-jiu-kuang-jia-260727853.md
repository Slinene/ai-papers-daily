---
title: 'FinanceHarness: Autonomous Financial Deep Research Framework'
title_zh: FinanceHarness：自主金融深度研究框架
authors:
- Yijia Xiao
- Rujun Han
- Yanfei Chen
- Zifeng Wang
- Ke Jiang
- Zhongying CuiZhu
- Vishy Tirumalashetty
- Wei Wang
- Burak Gokturk
- Tomas Pfister
affiliations:
- Google Cloud AI Research
- University of California, Los Angeles
arxiv_id: '2607.27853'
url: https://arxiv.org/abs/2607.27853
pdf_url: https://arxiv.org/pdf/2607.27853
published: '2026-07-29'
collected: '2026-08-08'
category: Agent
direction: Agent驱动的金融深度研究框架
tags:
- Deep Research
- Agent
- Finance
- Benchmark
- Tool Use
- LLM
one_liner: 提出面向金融领域的自主深度研究框架及点时间基准FinanceGym，将代理评分从25.3%提升至32.4%
practical_value: '- **领域专用Agent工作流设计**：电商搜索推荐Agent可借鉴分层harness思想，封装商品查询、行为分析、趋势预测等工具，构建多步骤推理流水线（如竞品分析→选品策略→文案生成）。

  - **点时间基准避免数据泄露**：针对促销预测、季节品推荐等时间敏感任务，可参照FinanceGym的pre-cutoff/post-cutoff评估设计，确保测试集不包含未来信息，真实反映模型能力。

  - **奖赏建模指导Agent优化**：可对推荐报告、搜索策略输出定义自动评分标准（如覆盖率、新颖性、时效性），用于RLHF或拒绝采样微调，提升Agent执行质量。

  - **专家验证基准的效用**：在构建垂直领域Agent评测集时，引入专家人工验证确定难度和真实水平，避免纯自动指标误导，发现顶尖模型仍有较大改进空间。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：通用深度研究系统产生的报告无法满足金融领域需求，金融研究需结合历史模式分析与未来事件预测，且需点时间基准防止信息泄露。

**方法关键点**：
- 提出 **FinanceHarness**：分层式Agent框架，集成金融专用工具（如数据检索、趋势分析）和从业者引导的工作流，自动完成环境搭建、Agent执行循环与奖赏建模。
- 设计 **FinanceGym** 基准：包含论文驱动的研究问题，评分标准结合截止日期前（pre-cutoff）的已有知识与截止日期后（post-cutoff）的实际事件，实现可验证的时序评估。

**关键结果**：
- 专家人工验证通过率82%，说明基准合理。
- 即使最先进的LLM和Agent在该基准上的总分仍低于40%，表明任务极具挑战性。
- 采用相同开源基座模型，FinanceHarness将整体评分从25.3%显著提升至32.4%，验证了框架的有效性。
