---
title: Active Learners as Efficient PRP Rerankers
title_zh: 主动学习实现高效PRP重排序
authors:
- Jeremías Figueiredo Paschmann
- Juan Kaplan
- Francisco Nattero
- Santiago Barron
- Juan Wisznia
- Luciano del Corro
affiliations:
- Universidad de San Andrés
arxiv_id: '2605.14236'
url: https://arxiv.org/abs/2605.14236
pdf_url: https://arxiv.org/pdf/2605.14236
published: '2026-05-14'
collected: '2026-05-21'
category: RecSys
direction: 生成式检索重排序 · 噪声成对比较主动学习
tags:
- PRP
- Active Learning
- Reranking
- LLM
- Noisy Pairwise Comparisons
- Efficiency
one_liner: 将PRP重排序建模为噪声成对比较的主动学习，通过自适应调度和随机方向提示，在低预算下大幅提升Top-K质量
practical_value: '- 在LLM成对重排序场景中，用主动排序（如Mohajer锦标赛+堆提取）替代冒泡/快速排序，在相同调用预算下NDCG@10可提升9点以上；工程上只需替换调度逻辑，不改变提示、不增加模型推理。适合电商搜索/推荐中候选商品重排等预算敏感场景。

  - 随机方向提示仅需一次LLM调用完成成对比较，将系统性的顺序偏差转化为零均值噪声，直接削减50%的调用成本，且不损失排序质量。实现简单：随机化文档在prompt中的顺序即可。

  - 若存在可靠的先验排序（如BM25或粗排分），PAC主动排序进一步用少量锚点比较快速收敛至top-K，调用量可低至180次左右，适合极低延迟场景。

  - 两种主动排序均支持查询内并行：莫哈杰的各锦标赛之间、PAC的锚点比较均可并发，实际延迟可通过批量推理大幅压缩，适合高吞吐线上服务。'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
传统PRP将LLM的成对偏好判断输入经典排序算法（如冒泡、快速排序），但LLM判断是噪声的、含有顺序偏差且可能不满足传递性，排序算法却在浪费预算追求全局全序而非优化top-K。预算受限时，这种方法在top-K质量上表现低效。

### 方法关键点
- **问题重定义**：将PRP重排序视为“噪声成对比较下的预算主动学习”，目标是在给定LLM调用次数内最大化top-K质量。
- **主动排序算法**：选用两种符合噪声容忍、top-K客观且支持“随时输出”的算法：
  - **Mohajer**（锦标赛+堆提取）：通过多个锦标赛集中比较可能的top候选，自适应分配比较到K边界附近。
  - **PAC最佳K**：利用BM25先验，仅与K×m个候选比较，再对赢家集冒泡排序。
- **随机方向提示**：以50%概率随机调换文档顺序，将单次调用中的位置偏差转化为零均值噪声，使比较满足p_ij = 1-p_ji，无需双向调用即可无偏聚合。
- **实现无改**：不改变LLM提示或模型，仅替换调度逻辑；支持查询内并行。

### 关键实验结果
- 在TREC DL 2019/2020上，使用Flan-T5-XL，N=100,K=10，NDCG@10为指标。
- 双向oracle下，B=300时Mohajer达到66.1，比最佳排序基线（BubbleSort 56.4）高出9.7点；在B=200–450区间持续领先。
- 随机方向oracle进一步压缩“达到峰值质量”所需调用：Mohajer在B=250即收敛至68.0，而双向需要450次。端到端BEIR任务中，随机方向Mohajer平均仅232次调用获得与QuickSort 1669次调用相仿的NDCG@10（56.8 vs 56.8），节省7倍调用。
- 统计显著性检验证明主动方法在预算内显著优于排序。

> 最值得记住的一句话：对待PRP重排序应像对待噪声反馈的主动学习，聪明的比较调度比堆砌调用数更能高效锁定top-K。
