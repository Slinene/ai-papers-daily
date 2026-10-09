---
title: 'Autoregressive Retriever: Improving Query Understanding from Item Feedback
  for Universal Multimodal Retrieval'
title_zh: 自回归检索器：利用物品反馈提升通用多模态检索
authors:
- Jianfei Zhao
- Yifan Wang
- Feng Zhang
- Xin Sun
- Chong Feng
- Zhixing Tan
- Yang Luo
- Boyuan Pan
- Xu Kai
- Yao Hu
affiliations:
- Beijing Institute of Technology
- Zhongguancun Academy
- Zhongguancun Laboratory
- Xiaohongshu
- Southeast Academy of Information Technology, Beijing Institute of Technology
arxiv_id: '2610.11666'
url: https://arxiv.org/abs/2610.11666
pdf_url: https://arxiv.org/pdf/2610.11666
published: '2026-10-08'
collected: '2026-10-09'
category: RecSys
direction: 自回归检索 · 强化学习反馈选择
tags:
- multimodal retrieval
- autoregressive retrieval
- query feedback
- reinforcement learning
- MLLM
- GRPO
one_liner: 自回归检索器 ARR 交替检索物品与更新 query embedding，用 SFT+RL 学习反馈选择，显著提升多模态检索性能
practical_value: '- 在电商搜索/召回中，可以用粗排或初始检索的 top 结果作为反馈，重新编码 query 得到更精确的 embedding，尤其对跨模态或模糊
  query 有帮助。线上可先跑一步初始检索，再用反馈强化，2 步之后收益递减，成本可控。

  - 训练时采用「多步对比学习 + degradation penalty」，能确保 query 加入反馈后不会变差，同时提升首轮 embedding 质量。即使线上不做多步检索，也能从这种训练中受益。

  - RL 优化反馈选择时，冻结主干和 item 索引，仅训练 query 侧 LoRA，将策略优化与线上索引解耦，避免重训全库 embedding，是工程友好的设计。GRPO
  以最终 reciprocal rank 为奖励，适合优化点击/成交等业务指标。

  - 如果资源有限，可只实现 SFT 阶段，已经能带来较大提升；RL 需要轨迹采样和奖励计算，适合追求更高检索质量且能接受训练成本的场景。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
通用多模态检索通常对 query 单独编码，不随候选集变化，导致 query-item gap：query 可能信息不全或意图隐晦，无法利用候选集合信息。已有 reasoning 增强只从输入本身提取信息，未利用检索反馈。

**方法关键点**
- 自回归检索：N 个 query states，每步检索一个 item，将其内容追加到 query 历史，重新编码得到下一个 embedding，最终 embedding 用于排序。item embedding 保持独立可索引。
- SFT：从预训练模型离线构建 top-10 反馈池，随机采样轨迹，逐步对比学习，所有步骤均有损失；增加 degradation penalty 防止后续状态变差；仅初始步骤反向传播 item embedding，后续 stop gradient。
- RL：冻结 SFT 主干和 item index，训练 query 侧 LoRA；将反馈物品视为 action，用 GRPO 优化选择，奖励为最终 reciprocal rank；加入 gate 的 final embedding contrastive loss，只对低奖励轨迹施加辅助监督。

**关键结果**
- M-BEIR：2B ARR-RL 平均 56.7，8B 平均 61.0，较最强基线 TRACE 58.8 高 2.2。
- Zero-shot 7 benchmarks：8B ARR-RL 平均 79.01，超过最强基线 ELV A 74.10。
- 多步反馈收益递减，2 步之后提升很小；SFT 多步训练也能提升首步检索（+0.40），RL 进一步改善首步（+0.73 相对 SFT N=1）。
- 消融：去掉 degradation penalty 反馈增益消失；去掉 GRPO 性能下降较多；去掉 final embedding contrastive 也会下降。

**一句话**
检索器可以把检索过程变成自回归序列，在观察候选后自我修正 query embedding，同时保持 item 索引固定，用 RL 直接优化反馈选择。
