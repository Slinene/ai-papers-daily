---
title: 'Piccolo: Co-Evolving Decision Models and Data through Recursive Self-Improvement'
title_zh: Piccolo：通过递归自改进协同进化决策模型与数据
authors:
- Zhenqing Ling
- Qirui Jiao
- Daoyuan Chen
- Cheng Chen
- Xinji Mai
- Haowen Gao
- Zhuo Zhang
- Xuchen Pan
- Mengsu Ding
- Jiaji Deng
affiliations:
- Alibaba Group
arxiv_id: '2611.24651'
url: https://arxiv.org/abs/2611.24651
pdf_url: https://arxiv.org/pdf/2611.24651
published: '2026-11-17'
collected: '2026-11-19'
category: Agent
direction: Agent 化数据工程与递归自改进
tags:
- decision model
- agentic data engineering
- recursive self-improvement
- multimodal
- model merging
- semantic slices
one_liner: Piccolo 决策模型家族用 Agent 化数据工程与递归自改进，在 Decision Index Vision 等决策基准刷新同尺寸最优
practical_value: '- 在电商搜索/推荐的 query 理解、工具路由、商品图片审核等场景，可借鉴「候选集 softmax 直接输出概率」接口：不生成文本，只对候选
  label 的 logit 做 softmax，得到置信度。这比生成式 LLM 推理更快、校准更直接，适合高 QPS 线上判别器。

  - 同时监控训练 loss 与业务分片准确率：论文显示 KL 从 0.66 降到 0.64 时净准确反而 -13。推荐/Agent 系统应按类目、场景、难度切片记录准确率，发现
  loss 与业务指标背离时及时下调该 slice 训练权重。

  - 用语义切片和 research memory 管理数据配比：为每条样本打 domain/capability/difficulty label，聚合训练动态定位问题；某类目推荐效果退化时可回查该
  slice 训练占比并重新平衡，比盲目加数据更高效。

  - 固定数据池长期训练会带来能力退化：1M 曝光后 Harness/Text 掉点，Data 才微涨。电商推荐系统应周期性更新数据配比，而不是静态数据反复训练。

  - 权重空间编辑（module scaling / interpolation / low-rank directions）可在不重新训练的情况下融合多路模型能力，适合搜推系统合并多个精排模型或生成式分支；但需同时验证主业务和辅助任务，避免单点提升掩盖回归。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
现实自主系统在 open-ended 生成之外，关键瓶颈是快速、可校准的决策：动作选择、工具路由、guardrail 过滤、数据清洗等。传统生成式模型做候选打分推理成本高且校准不足。Piccolo 针对这一需求构建 0.8B–27B 多模态决策模型家族，直接输出候选概率。

## 方法关键点
- 决策接口：输入 state/question/candidate set，为每个候选分配单 token label，从 LM head 读取这些 label 的 logit 做 softmax，得到概率分布；支持 Choice/Score/Noul 三类任务。
- 多模态架构：视觉 encoder + connector + 语言 backbone，bidirectional attention，可选 OCR sidecar。
- Agentic Data Engineering：research agent 在语义切片（domain/capability/difficulty）上分析 loss/accuracy/错误变化，提出数据修订、混合重平衡、合成等 proposal，再执行训练实验；共享 research memory 保存模型血缘、配方、结论。
- 训练与优化：CE 监督 + candidate-level RL + weight-space editing（checkpoint 插值、module scaling、低秩方向）。数据池 663K 样本（311K 文本 + 352K 图像-文本），约 600 次实验。

## 关键结果
Piccolo-27B 在 Decision Index Vision Full 75.59、Private 70.97、Public 80.22，均第一；9B/4B 同尺寸第一。27B 在 HarnessJevBench 84.41、DataJevBench 82.60、JevBench 92.21。实验揭示三个反直觉结论：固定 recipe 下更早 backbone 可能优于新一代（Qwen3.5 Vision 79.97 > Qwen3.6 79.59 / Qwen3.8 77.86）；4B–9B 通过定向数据治理可逼近 27B baseline；loss 单调下降阶段准确率仍可能反转。

## 最值得记住的一句话
“Advancing frontier decision models requires more than scaling parameters or static datasets; it requires scaling the research loop itself.”——把数据选择、实验管理、失败分支复用变成可积累工程化资产，而非单次超参搜索。
