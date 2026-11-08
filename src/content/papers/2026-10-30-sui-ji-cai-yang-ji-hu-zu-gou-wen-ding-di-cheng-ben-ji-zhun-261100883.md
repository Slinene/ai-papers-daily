---
title: Random Is Almost Enough? Stable and Low-Cost Benchmark Compression via BestRand
title_zh: 随机采样几乎足够？稳定低成本基准压缩方法 BestRand
authors:
- George Ling
- Shanshan Zhong
- Lijin Yang
- Hao Yang
- Nanxiang Li
- Zhongzhan Huang
affiliations:
- Bosch Research
- Carnegie Mellon University
arxiv_id: '2611.00883'
url: https://arxiv.org/abs/2611.00883
pdf_url: https://arxiv.org/pdf/2611.00883
published: '2026-10-30'
collected: '2026-11-08'
category: Eval
direction: 基准压缩与评估稳定性
tags:
- Benchmark Compression
- Random Sampling
- Evaluation Error
- OOD Estimation
- LLM Evaluation
- VLA
one_liner: 揭示基准压缩误差的长尾分布，提出 BestRand 以随机采样成本实现稳定低误差评估
practical_value: '- 离线评测集压缩：推荐/广告模型迭代中评测集往往巨大，可先用随机采样获得低成本基线，再针对长尾高风险样本（对模型排序敏感、分布偏移大的
  item/query）做少量补充采样，以极低成本降低线上评估翻车概率，无需复杂优化即可落地。

  - 构建稳定离线指标：随机子集大部分情况下误差小但存在罕见大误差，且该现象跨模型族/时间稳定。业务上应避免依赖单次随机划分，建议固定评测子集时执行多次采样或按
  BestRand 目标选择尾部风险低的集合，防止 A/B 指标噪声导致错误模型上线。

  - Agent/LLM 链路评估：电商 Agent（query 改写、对话推荐）评估成本高，可应用该方法压缩 prompt/会话样本；论文的 OOD score-range/model-family/temporal
  shift 结果提示要选择跨场景稳定的子集，构造评测集时可加入多模型多样性约束。

  - 工程实现：构建成本仅需竞争方法的 51.3%，无复杂训练，可直接在现有评测框架中替代随机采样，适合快速迭代的推荐模型离线评估 pipeline。'
score: 6
source: huggingface-daily
depth: abstract
---

动机：完整 benchmark 评估 LLM/VLM 成本高，压缩评估子集有需求，但子集估计全量分数的误差分布未被准确刻画。

方法：率先推导子集估计全量 benchmark 分数的误差分布解析近似，发现大部分子集误差小、少数子集误差大，呈长尾分布。随机采样因此以高概率表现良好，但存在罕见大误差导致不稳定；进一步证明该不稳定性是现代基础模型的固有属性，不会随评估模型数量增加而消失。基于此提出 BestRand，保留随机采样的高效率，同时针对长尾尾部进行约束，显著降低高误差风险。

结果：在 70+ 文本、多模态、agent benchmark 及 VLA 评估上验证，BestRand 相比竞争方法高误差风险降低 50.2%，估计误差降低 16.4%，构建成本仅 51.3%；在 score-range、model-family、temporal shifts 三种 OOD 场景下估计误差平均降低 21.8%。代码与数据公开。
