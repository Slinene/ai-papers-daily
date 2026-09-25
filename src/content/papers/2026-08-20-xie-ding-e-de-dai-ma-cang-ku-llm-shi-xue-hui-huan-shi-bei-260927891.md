---
title: 'Schrödinger''s Code Repository: Have LLMs Learned SWE-bench or Memorized It?'
title_zh: 薛定谔的代码仓库：LLM 是学会还是背下了 SWE-bench？
authors:
- Silin Chen
- Yufei Yang
- Xiaodong Gu
- Yuling Shi
- Chengcheng Wan
- Haibing Guan
affiliations:
- Shanghai Jiao Tong University
- Xi'an Jiaotong University
- East China Normal University
- Shanghai Innovation Institute
arxiv_id: '2609.27891'
url: https://arxiv.org/abs/2609.27891
pdf_url: https://arxiv.org/pdf/2609.27891
published: '2026-08-20'
collected: '2026-09-25'
category: Eval
direction: LLM 评估 · 防泄漏动态实例化
tags:
- LLM Evaluation
- Data Leakage
- Repository-level Benchmark
- Coding Agents
- SWE-bench
- Dynamic Instantiation
one_liner: 提出动态实例化仓库的评估框架，通过四种变换擦除熟悉线索，证明 LLM 编码智能体部分依赖记忆表面特征
practical_value: '- 构建 Agent 或模型评测集时，对公开数据做表面扰动（重命名变量/函数、重排文件布局、语义等价改写）可暴露模型对表面特征的记忆，适用于
  RAG 检索评测、商品知识问答或推荐 Agent 场景。

  - 若模型在扰动后性能显著下降且交互轮次增加，说明其依赖记忆而非泛化检索；线上 Agent 遇到陌生仓库/商品目录结构时应关注探索成本，可引入定位模块或结构化索引减少无谓搜索。

  - 四个变换层级可作为数据增强手段，训练模型对命名和布局不敏感，提升 Agent 在未见数据上的鲁棒性。

  - 保留可执行行为同时擦除命名与布局思路，可用于生成语义等价的防泄漏测试集，避免线上评测被事先见过的文档或代码污染。'
score: 6
source: huggingface-daily
depth: abstract
---

动机：仓库级编码基准（如 SWE-bench）基于流行开源仓库，静态表示导致数据泄漏风险，模型可能靠记忆命名规则、文件布局等表面线索取得高分，而非真正理解仓库逻辑。

方法关键点：将测试仓库视为评估时隐变量，在智能体进入环境时动态实例化一个语义等价但表面差异化的仓库版本。通过四个变换层级逐步擦除熟悉线索：①问题陈述重构；②命名空间重映射；③文件内布局重排；④保留功能的代码重写。所有变换均保持原始可执行行为不变，但破坏模型可能记忆的仓库侧表面特征。

关键结果：在 SWE-bench Verified 和 SWE-QA 上评测主流 LLM 编码智能体，移除熟悉仓库线索后性能一致下降，交互成本（interaction cost）显著增加。额外成本主要源于仓库探索和定位难度上升，说明当前智能体的强表现部分来自对表面线索的记忆，而非稳健的仓库推理能力。
