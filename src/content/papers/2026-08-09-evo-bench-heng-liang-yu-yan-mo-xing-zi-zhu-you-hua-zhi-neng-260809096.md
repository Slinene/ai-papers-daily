---
title: 'Evo-Bench: Can Language Models Improve Agent Harness?'
title_zh: Evo-Bench：衡量语言模型自主优化智能体框架的能力
authors:
- Lisheng Huang
- Chen Yang
- Hao Zhou
- Huatong Song
- Zongchao Chen
- Ran Le
- Yang Song
- Wayne Xin Zhao
- Tao Zhang
affiliations:
- Gaoling School of Artificial Intelligence, Renmin University of China
- BOSS Zhipin, Beijing, China
arxiv_id: '2608.09096'
url: https://arxiv.org/abs/2608.09096
pdf_url: https://arxiv.org/pdf/2608.09096
published: '2026-08-09'
collected: '2026-08-12'
category: Agent
direction: Agent 自我进化能力评估
tags:
- Agent
- Harness Evolution
- Benchmark
- Self-improvement
- LLM
- Transferability
one_liner: 首个跨搜索、办公、通用领域的基准，评估LLM自主进化智能体harness的能力，发现搜索优势与早饱和现象
practical_value: '- 在设计电商搜索或推荐 Agent 时，可让 LLM 自动优化其工作流程（harness），借鉴“辅助任务进化”方法来筛选对框架敏感的任务，降低试错成本。

  - 注意早饱和现象：迭代优化时设置提前停止条件，避免过度优化导致性能停滞，适用于高频率在线场景。

  - 合成的 harness 作为可迁移的推理模板，跨不同推荐模型复用，可沉淀为内部知识库，统一提升效果。

  - 评估自主进化能力时需隔离基座模型强度与框架贡献，可参考“敏感度感知分层划分”防止过拟合到特定任务集。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有智能体评估多限于静态任务解决，忽视了一个前沿能力——harness evolution，即智能体自主优化自身运行框架的能力。基准测试的缺失使得难以分离框架改进与基座模型强度、避免任务过拟合并捕获长期迭代研究。

**方法关键点**：提出 Evo-Bench，首个跨搜索、办公和通用智能体领域的 harness 进化基准。利用 harness-guided 构建框架：通过辅助任务进化识别对框架改进真正敏感的任务，再基于敏感度进行分层划分，确保评估的跨集合泛化能力。对9个前沿和开源模型进行大规模评测。

**关键结果**：顶级模型通过自主进化获得绝对增益达16.6分，接近最先进的人工设计基线；自主进化在通用任务中超越人工 harness，在搜索任务表现突出，但在办公任务（需高度特异流程）中挣扎；发现早饱和等时间异常；合成的 harness 具有高度可迁移的推理结构，能一致提升多种策略模型。
