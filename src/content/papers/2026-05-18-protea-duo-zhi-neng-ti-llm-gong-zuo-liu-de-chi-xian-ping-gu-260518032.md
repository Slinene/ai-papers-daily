---
title: 'PROTEA: Offline Evaluation and Iterative Refinement for Multi-Agent LLM Workflows'
title_zh: PROTEA：多智能体 LLM 工作流的离线评估与迭代优化工具
authors:
- Kazuki Kawamura
- Satoshi Waki
- Kei Tateno
affiliations:
- Sony Group Corporation
arxiv_id: '2605.18032'
url: https://arxiv.org/abs/2605.18032
pdf_url: https://arxiv.org/pdf/2605.18032
published: '2026-05-18'
collected: '2026-05-19'
category: Agent
direction: 多智能体工作流离线评估与迭代优化
tags:
- multi-agent
- workflow
- evaluation
- prompt refinement
- offline testing
- LLM-as-a-judge
one_liner: 通过后向节点评估和图级瓶颈定位，实现多智能体工作流的离线测试驱动迭代优化，减少对人工中间标注的依赖
practical_value: '- **后向节点评估降低标注成本**：利用最终答案参考和下游依赖关系自动生成中间节点预期输出，适合电商推荐链路（意图解析→召回→排序→生成）中缺乏细粒度中间标注的场景。

  - **图级诊断+节点级理由**：将 PASS/WARN/FAIL 状态直接覆盖在工作流图上，并按优先级排序节点，开发者可快速定位导致推荐结果偏差或文档检查失败的瓶颈节点，避免逐节点翻看链路。

  - **闭环提示词修订与重评估**：在选中节点后，系统基于评审理由生成可编辑的提示词修订草案，并在 accept 后自动执行全链路重跑与评估，带来类似于 CI
  回归测试的快速迭代体验，可直接迁移到生成式推荐或多轮对话 Agent 的 prompt 调优。

  - **LLM-as-a-judge 与阈值设置**：可配置的多维度评分标准和阈值映射（PASS/WARN/FAIL），可用来自动评估中间输出（如召回相关性、排序合理性）并向业务反馈，适合构建监控或离线诊断管道。'
score: 10
source: arxiv-cs.CL
depth: full_pdf
---

**动机**  
多智能体 LLM 工作流通过拆分职责能提升性能，但错误常从上游节点传播，且调试时缺少中间标注；现有评估工具多聚焦端到端指标，难以定位具体节点问题。

**方法关键点**  
- **工作流表示**：将多智能体系统建模为有向无环图（DAG），每个节点是一个 LLM 调用，支持从 LangGraph 等框架导入。  
- **后向节点评估（Backward Node Evaluation）**：当只有最终答案参考时，利用最终答案和图结构生成候选节点预期输出，再与观测输出对比评分，减少人工标注。  
- **节点级诊断**：LLM-as-a-judge 按可配置评分准则打分，映射为 PASS/WARN/FAIL 并附加理由，在图界面上突出显示问题节点。  
- **闭环提示词优化**：针对选定节点，基于评审理由和评分方向生成可编辑的提示词修订草案；开发者接受后自动重跑并对比历史分数。  
- **自动迭代模式（AUTOLOOP）**：支持多次 evaluate→revise→re-evaluate 循环，仅在持续改善时保留修订。

**关键结果**  
- 两个接近生产的内部工作流：文档检查准确率从 64.3% 提升至 83.9%（N=5 节点）；对话推荐 Hit@5 从 0.30 提升至 0.38（N=6 节点）。  
- 自动迭代压力测试：5 个独立生成的最小提示词工作流中 4 个得分提升，其中 3 个提升超过 0.3 分（如排课工作流从 0.186 升至 0.800）；基线为无修订重复运行。  
- 6 名有经验的 LLM 开发者在形成性用户研究中认可图级定位、节点级理由和可编辑修订的价值。

**最值得记住的一句话**  
PROTEA 通过后向推断将昂贵的中间标注转化为可自动生成的节点预期，并将评估、诊断、修订合并进同一个开发者闭环，大幅降低了多 Agent 工作流离线迭代的成本与门槛。
