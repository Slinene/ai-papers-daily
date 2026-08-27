---
title: Is Next-Chunk Reasoning RL Really Better than SFT? Revisiting Training Strategies
  under no-CoT Data
title_zh: 无CoT数据下推理后训练：混合SFT优于下一块推理RL
authors:
- Yinhao Tang
- Youqing Fang
- Yanan Sun
- Jiangning Liu
- Ziyi Wang
- Xun Zhao
- Weiming Zhang
- Bin Liu
- Kuikun Liu
- Wenwei Zhang
affiliations:
- University of Science and Technology of China
- Shanghai AI Laboratory
arxiv_id: '2608.23256'
url: https://arxiv.org/abs/2608.23256
pdf_url: https://arxiv.org/pdf/2608.23256
published: '2026-08-23'
collected: '2026-08-27'
category: Training
direction: 推理后训练 · 数据混合与RLVR
tags:
- no-CoT data
- Mixed SFT
- RLVR
- next-chunk reasoning
- reasoning post-training
- training efficiency
one_liner: 同一RLVR预算下，单阶段混合no-CoT与long-CoT的SFT比next-chunk reasoning RL效果更好且省60倍以上算力
practical_value: '- 将高质量 long-CoT 与业务中大量“无 CoT”文本（搜索日志、运营方案、商品知识、用户问题简答）在同一个 SFT 阶段混合训练，再做
  RLVR/DPO；不要先无 CoT 后 long-CoT 的顺序 SFT，否则会跨阶段遗忘。适合电商/Agent 中难以标注 CoT 但知识密度高的语料。

  - 评估 Agent 推理、query 理解、推荐理由生成等能力时，不要只看 SFT 后中间 checkpoint；无 CoT 混合会造成格式混乱，pre-RLVR
  掉点不代表能力差，应以 RLVR 后的最终 ceiling 做决策。

  - 若想用 next-chunk reasoning 类 RL 从日志/文档中挖掘隐式推理，注意高熵 token ≠ 需要推理的困难 token；这类目标易塌缩为局部补全模板，且训练算力是混合
  SFT 的 60 倍以上。优先把预算花在数据混合而非新增 RL 阶段。

  - 对搜索/推荐/导购 Agent：保留短答案 + 长推理的联合 SFT 格式，后续用 verifier reward 修复格式不稳定，比中途切换训练目标更有效。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
大量语料（worked solutions、教材推导、研究论文）只含结论或简短推导，缺少显式 CoT 标注；这类 no-CoT 数据知识密度高、规模大，但如何转化为推理后训练信号一直不清楚。近期 next-chunk reasoning RL（NTR/NSR）声称能利用 no-CoT 数据，但既有比较只对 no-CoT SFT 基线，未对同一阶段混合 no-CoT 与 long-CoT 的 Mixed SFT 进行公平对比。

## 方法关键点
- 统一从 Qwen3-30B-A3B-Base 出发，对比五种策略：NTR（RPT）、NSR（RLPT）、Sequential SFT、Mixed SFT、Reasoning SFT，后接完全相同的 RLVR（GRPO + DAPO-Math-17K 精确匹配奖励）。
- 数据：no-CoT 为 421K AoPS 简短解答（约 0.53B tokens）；long-CoT 为 152K DeepSeek-V3.2 生成且答案正确的推理轨迹（约 1.95B tokens）。
- Mixed SFT 在单个 SFT 阶段联合训练 no-CoT + long-CoT；Sequential SFT 先 no-CoT 后 long-CoT；NTR/NSR 从 Reasoning SFT 继续训练。
- 评估 pre/post RLVR：AIME 24/25/26、HMMT 25/26、IMO-Answer（ID），HLE、GPQA-Diamond、MMLU-Pro（OOD）。

## 关键结果
- Mixed SFT 的 post-RLVR ID 均分 67.4，高于 NTR 64.2 和 NSR 63.6；OOD 上 GPQA-Diamond 60.98、HLE 9.24、MMLU-Pro 75.84，均最高。
- Mixed SFT pre-RLVR 仅 27.5，为所有方法最低，但 post-RLVR 达 61.1，提升 33.7 点，说明 pre-RLVR 不是可靠指标。
- 训练算力：NTR 4283.7 GPU hours、NSR 4608.1 GPU hours，Mixed SFT 仅 65.6 GPU hours，差距超过 60 倍。
- 分析显示：NTR 高熵 token 并非真正需要推理的困难 token，生成轨迹退化为局部补全；限制熵塌缩也不能提升 ceiling；在 Mixed SFT 后追加 NTR/NSR 不带来额外收益；Sequential SFT 的第二阶段 long-CoT 会覆盖 no-CoT 知识，retention probe 为 59.19 vs Mixed SFT 68.63。

最值得记住的一句话：更高的 pre-RLVR accuracy 不等于更高的 post-RLVR ceiling，no-CoT 训练策略应在完整 RLVR 管线中评估。
