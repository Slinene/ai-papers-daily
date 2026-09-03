---
title: Knowledge Distillation During Mid-Training Favors Reasoning over Factual Recall
title_zh: 中训练阶段知识蒸馏偏向推理，损害事实召回
authors:
- Jacqueline He
- Howard Yen
- Shuyue Stella Li
- Margaret Li
- Hanqing Zeng
- Yinglong Xia
- Benyu Zhang
- Zhuokai Zhao
- Qiang Zhang
- Pang Wei Koh
affiliations:
- Meta AI
- University of Washington
- Princeton University
arxiv_id: '2609.01532'
url: https://arxiv.org/abs/2609.01532
pdf_url: https://arxiv.org/pdf/2609.01532
published: '2026-08-31'
collected: '2026-09-03'
category: Training
direction: LLM 知识蒸馏 · mid-training 优化
tags:
- Knowledge Distillation
- Mid-Training
- Token Routing
- Teacher Entropy
- Reasoning
- Factual Recall
one_liner: 发现 mid-training 中标准 KD 产生推理-事实召回权衡，提出基于 teacher entropy 的 Switch Distillation
  做 token 路由以保住推理增益和事实召回
practical_value: '- 在业务基座 LLM 继续预训练/领域适配时，若用大模型做 logit 蒸馏，不要全 token 均匀蒸馏。按 teacher
  预测熵做 token-level 路由：低熵 token（数学、代码、指令模板、强过程性推理）走 reverse KL 蒸馏，高熵 token（商品事实、知识条目、长尾搜索词）保留
  CE 或 ground-truth label，降低对事实型知识获取的抑制。

  - 将能力评估拆成 Reasoning / Factual Recall / Knowledge & Commonsense，分别监控，而不是只看平均分；尤其做搜索/推荐模型蒸馏时，事实召回（如商品属性、SPU
  知识）不能牺牲。

  - 工程实现成本低：只需在已有 teacher logits 上多算 entropy 和 batch 内分位数，不需要额外模型前向或参数，可即插即用；q=20%
  可作为默认值。

  - 如果业务场景是 Agent 能力蒸馏或 query 改写/生成，建议优先选择与 student 容量差距较小的教师（如 7B 教师优于 13B），并在 post-training
  后重新评估，不能只看 mid-training 指标。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：现代 LLM 训练普遍划分 pre-training / mid-training / post-training。mid-training 用精筛数据继续做自监督，数据量远少于 pre-training，因此每个 token 的学习效率很关键。KD 被用来给 student 注入 teacher 分布，但过去研究集中在 pre/post-training，mid-training 中标准 KD 是否成立并不清楚。

**方法关键点**：
- 在 OLMo-2 生态中做 controlled experiments：1B student，pre-training 100B / mid-training 60B，teacher 为 OLMo-2 1B/7B/13B Instruct。
- 发现：pre-training 中 forward KL 能同时提升推理与事实召回；mid-training 中 KD 只提升推理，却拖慢 factual recall，形成 reasoning–recall tradeoff。
- 归因：teacher 在 procedural/数学/指令数据上 entropy 低，在 knowledge-intensive/web/wiki 文本上 entropy 高；低 entropy 对应 teacher top-1 更准。学生从 4T checkpoint 进入 mid-training 时，低 entropy 事实大多已学会，未学会事实集中在高 entropy 区域；而 KD 在这些高 entropy token 上对 gold-token 的梯度约为 NTP 的 0.5×，监督被衰减。
- 提出 Switch Distillation：计算每个 token 的 teacher predictive entropy，在 batch 内取最低 q=20% token 走 reverse KL 蒸馏，其余 token 走 CE；没有额外前向/参数。

**关键实验**：mid-training 后，相对 NTP 的 reasoning 从 26.1% 提升到 44.7%（7B teacher）/42.1%（13B teacher），分别约 1.71×/1.61×；knowledge & commonsense 提升约 19%/13%；factual recall 保留 96.7–96.8%。经过 SFT+DPO+RLVR 标准 post-training，factual recall gap 关闭，reasoning 仍保持 1.25–1.32×、knowledge & commonsense 1.13–1.20× 的相对增益。消融显示：entropy 路由是主要收益来源；随机路由、teacher-correct 路由、oracle domain 路由都不如 entropy；RKL 略优于 FKL。

**最值得记住的一句话**：KD 不应 stage-agnostic；mid-training 中 teacher entropy 是判断该 token 走蒸馏还是 CE 的轻量有效信号。
