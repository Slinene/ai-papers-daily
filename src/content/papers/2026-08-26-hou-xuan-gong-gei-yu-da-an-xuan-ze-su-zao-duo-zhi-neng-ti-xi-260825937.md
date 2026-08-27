---
title: Candidate supply and answer selection shape the value of LLM judging in multi-agent
  systems
title_zh: 候选供给与答案选择塑造多智能体系统中 LLM 评判价值
authors:
- Jia-Hao Ji
- Sijie Li
- Jiabei Cheng
- Zixi She
- Jin-Tai Yu
- Zhiyuan Yuan
affiliations:
- Fudan University
- Shanghai Jiao Tong University
- Shanghai Academy of Artificial Intelligence for Science
arxiv_id: '2608.25937'
url: https://arxiv.org/abs/2608.25937
pdf_url: https://arxiv.org/pdf/2608.25937
published: '2026-08-26'
collected: '2026-08-27'
category: MultiAgent
direction: 多智能体推理 · LLM 评判与终选
tags:
- LLM judge
- multi-agent systems
- candidate generation
- answer selection
- rank AUC
- test-time compute
one_liner: 将多智能体推理拆成生成-交流-终选，证明 LLM 评委价值随候选正确率、任务和生成器变化，混合频率与排名可救回少数正确答案
practical_value: '- 在电商/搜索/Agent 工作流中，把「候选生成→交互/召回→终选」拆开埋点，重点统计正确/高相关候选是否已出现却被多数投票或流行度排序丢掉；先看生成供给，再优化选择。

  - 多智能体集成或 LLM 终选不要只用多数投票：采用 answer frequency 与 judge rank 的 rank-power 加权（wi=(k-i)^t，t=2-4），可在固定候选池中救回少数高质量候选，本文提升约
  7pp，适合小候选池和冷门但正确的商品/query 候选。

  - LLM judge 不是静态能力：上线前用实际上游生成器的候选分布评估 rank AUC 与 pgen 的关系，监控低可用性区间可能低于随机；对高难度、冷启动或候选正确率很低的场景谨慎使用
  judge。

  - 算力路由：小候选集（k≤6）用 judge 比扩大采样更划算；大池且候选正确率较高时多数投票更稳，judge 边际收益下降甚至为负。可据此做动态选择策略。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

**动机**  
多智能体系统（MAS）经常已生成正确答案，最终却仍报错。现有对比通常同时改变生成、通信和终选规则，无法定位增益来源。论文把 MAS 抽象为候选生成→信息演化→终选三个阶段，重点研究 LLM judge 何时能提供有效的选择压力，以及终选规则如何利用这种信号保护已生成的正确候选。

**方法关键点**  
- 在 MedXpertQA 2,450 题上比较 single、majority voting、open committee、anonymous evidence board 四种协议，控制生成与通信差异。  
- 构建离线排序基准：用 DeepSeek-V4-Flash 和 Mimo v2.5 生成候选池，统计每个问题的正确候选占比 pgen；LLM judge 匿名排序候选 rationale，用 rank AUC 衡量辨识正确候选的能力。  
- 在 81,390 个固定 k=8 候选池上回放不同终选规则：多数投票、首名选择、rank-power 加权（wi=(k-i)^t），并扫描 k=2–16 的成本-准确率曲线。

**关键结果**  
- 通信协议相比多数投票仅提升 0.83–1.14pp，但 token 成本达 6.1–10.7 倍；oracle 上限与实际准确率存在 13.13–14.38pp 的 generation–retention gap，说明正确答案已在生成后丢失。  
- Judge rank AUC 随 pgen 呈 sigmoid 上升：主实验半升点 pgen=14.7%，HLE 多选/QA 分别升至 28.6% 和 36.9%；同一 mean AUC 下，不同生成器/推理设置可呈现出几乎平坦与陡峭上升两种关系。  
- 混合频率与排名在 t=2–4 时达到 70.82–70.95%，显著高于多数投票 63.82%；首名选择在 pgen≤0.625 时增益 +6.02–7.87pp，但在 pgen>0.625 时反而 -3.22pp。  
- 小池 k=2 时首名选择增益最大 +13.52pp，每千额外正确成本 US$0.10–0.39；k=14 后无显著优势。

**最值得记住的一句话**  
正确候选是否已被生成、是否可被 LLM judge 识别、终选规则是否采纳该信号，三者共同决定多智能体系统最终输出；judge 的价值取决于候选供给与选择规则，而不是固定不变的模型属性。
