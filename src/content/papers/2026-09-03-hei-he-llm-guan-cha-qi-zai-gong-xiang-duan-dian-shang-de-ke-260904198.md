---
title: 'Clean Engineering, Unstable Measurement: A Preregistered Reliability Failure
  of Black-Box LLM Observers on Shared Endpoints'
title_zh: 黑盒 LLM 观察器在共享端点上的可靠性失败：预注册审计
authors:
- Haoyaun Zhu
- Jie Zhang
affiliations:
- School of Electronic and Electrical Engineering, University of Sheffield
- R&D Department, Ranplan Wireless Network Design Ltd.
- R&D Department, Cambridge AI+ Ltd.
arxiv_id: '2609.04198'
url: https://arxiv.org/abs/2609.04198
pdf_url: https://arxiv.org/pdf/2609.04198
published: '2026-09-03'
collected: '2026-09-06'
category: Eval
direction: LLM-as-Judge 测量可靠性审计
tags:
- LLM-as-judge
- reliability
- measurement
- shared endpoints
- preregistration
- evaluation
one_liner: 审计 52,988 次 LLM judge 请求发现同名共享端点重复/次日排名一致性远低于预设门槛，并定位三类失效机制
practical_value: '- 在推荐/广告/搜索链路上用 LLM judge 做离线评估、生成样本筛选或 reward 打分时，别把单次 LLM 排名当稳定信号；先对同一批样本做
  byte-identical 重放，计算 Spearman/test-retest 并预设门槛，验证“仪器”再冻结 gate。论文显示约 2% 调用量的 pilot
  即可提前暴露不可达门槛。

  - 共享 API endpoint 的 LLM judge 不是 frozen instrument，provider metadata（model name、seed、temperature
  等）都预测不了稳定性；若评估结果会回灌训练或影响线上 gate，pipeline 需要增加跨时间窗一致性监控，不能只看 schema/hash 等工程指标。

  - 减少 exact-permutation/精细化排名读数的放大效应；对商品文案、query 推荐、广告标题等排序/评分任务，建议多次重复测量或改用更粗粒度偏好判断，并意识到真实候选差异可能低于仪器噪声。

  - 自部署 batch-invariant kernel 仅在低并发 quiet 时更稳定，并发负载会让不一致放大 8.4 倍；关键评估可以自托管并控制并发，但仍需做重放校准。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

动机：LLM judge 被广泛用于 gate 训练数据、打分生成和驱动榜单，但共享端点上同名模型是否可复现很少被审计。方法：两项预注册实验，共 52,988 次请求；同窗口重复排名要求 Spearman≥0.90，次日 byte-identical replay 要求≥0.99；后续还测试了多 provider、自托管和构造误差。结果：同窗口重复排名一致性仅 0.400，次日重放 0.78，均未达标；工程指标正常。三个机制解释差距：label-to-meaning mapping 偏置与信号本身一样强；候选差异比仪器噪声低七个数量级；byte-identical 输入产生不同排名，exact-permutation 读数会放大噪声。指标替换和采样在 748,000 次模拟中 0/500 通过。等待无帮助（same-day 0.805 vs cross-day 0.800，重复五天仍如此）；四家 provider 中位数 0.74-0.88，元数据无法预测；自托管低并发可改善，但并发负载使不一致放大 8.4 倍；构造误差显示读数分离跟踪错误类型而非大小。论文提炼出三级 snapshot-identity ladder、8 条设计规则和报告 checklist，并指出约 2% 调用量的 pilot 即可提前暴露不可达的评估门槛。
