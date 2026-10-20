---
title: 'DisaggKD: Efficient Knowledge Distillation through Teacher-Student Disaggregation
  and a Fused Loss'
title_zh: DisaggKD：通过师生分离与融合损失实现高效知识蒸馏
authors:
- Ruixuan Tu
- Yuyang Dong
affiliations:
- The University of Tokyo
- RIKEN AIP
- SB Intuitions Corp.
arxiv_id: '2610.17644'
url: https://arxiv.org/abs/2610.17644
pdf_url: https://arxiv.org/pdf/2610.17644
published: '2026-10-12'
collected: '2026-10-20'
category: Training
direction: 知识蒸馏训练效率优化
tags:
- Knowledge Distillation
- LLM Training
- Memory Efficiency
- Disaggregated Training
- Fused Loss
one_liner: 提出教师-学生分离的KD框架，通过fused loss和prefetch ring突破显存限制，匹配同布局损失并提速
practical_value: '- 在资源受限下做LLM蒸馏（例如蒸馏通用大模型到电商领域小模型用于query理解或排序），采用教师-学生分离部署，教师只前向，学生负责训练，避免同一GPU同时存放两套权重和优化器状态。

  - 实现KD loss时，若词表过大，不必显式构造完整logits张量，可通过行窗口和词表分片（vocabulary shards）的融合kernel精确计算loss，既省显存又保持数值一致，适合大词表场景（如搜索词预测、文案生成）。

  - 在跨节点流水线并行训练中引入prefetch ring协调生产者和训练者，可掩盖通信延迟，提高吞吐，对需要跨节点数据转移的架构有借鉴意义。

  - 使用闭式内存和流量模型提前判断不同布局（colocated vs 分离）的可行性，避免OOM，可在设计训练方案时快速评估，节省试错成本。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：现成KD框架将教师和学生放在同一GPU，每GPU显存限制了大教师模型的使用；大词表KD loss额外产生全词表logits张量，进一步挤占内存。

方法：DisaggKD将教师与学生分离到不同节点。教师仅做前向，把最后隐藏状态流式发送给学生；学生侧持有教师输出头副本，从隐藏状态恢复logits用于KD。设计fused loss，对行窗口和词表分片计算，避免构造全词表logits，且在精确算术上等价于完整损失。引入prefetch ring协调教师生产与学生训练，隐藏通信延迟。提供闭式内存与流量模型，预判不同布局的显存限制。

结果：在Qwen3.5-35B-A3B到9B的蒸馏对上，分离布局匹配同布局的LM loss且速度更快；fused loss使同布局能在更少节点上以更快速度训练；当学生跨多节点时分离布局内存效率更高。对更大模型对，同布局即使使用fused loss仍OOM，而分离布局可以训练。
