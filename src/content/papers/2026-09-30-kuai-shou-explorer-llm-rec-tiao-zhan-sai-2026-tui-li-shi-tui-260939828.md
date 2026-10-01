---
title: 'KUAISHOU Explorer LLM-Rec Challenge 2026: Reasoning Generative Recommendation'
title_zh: 快手 Explorer LLM-Rec 挑战赛 2026：推理式生成推荐
authors:
- Jiangxia Cao
- Hao Peng
- Wenlong Xu
- Jiaxin Deng
- Zhixin Ling
- Xingmei Wang
- Kun Shang
- Can Tang
- Zhihuai Cai
- Jun Du
affiliations:
- Kuaishou
arxiv_id: '2609.39828'
url: https://arxiv.org/abs/2609.39828
pdf_url: https://arxiv.org/pdf/2609.39828
published: '2026-09-30'
collected: '2026-10-01'
category: GenRec
direction: 生成式推荐 · Semantic ID + LLM 推理
tags:
- Semantic ID
- Generative Recommendation
- LLM Reasoning
- RL
- Multi-task SFT
- Competition
one_liner: 系统总结多任务推理生成推荐挑战赛，开源 OneReason 数据与评测，提炼推理监督、RL 与偏好优化的关键经验
practical_value: '- 在生成式推荐中加入思考链（CoT）不一定提升效果，关键是控制推理轨迹质量。冠军方案发现，把命中目标 SID 的采样轨迹加入训练但
  mask 掉答案 loss，只优化 reasoning 部分，可以降低 think 与 nothink 候选重叠，提升两者互补性；直接全量监督会伤害候选多样性。迁移到业务：做
  reasoning 数据增强时，对 target 重复的轨迹要限制数量并控制答案监督强度。

  - 不同域的推理收益不同，亚军方案采用混合格式：电商用 think，短视频/广告/直播用 nothink，效果优于全 think 或全 nothink。业务上多场景生成式推荐不必强求统一
  SFT 格式，可按域验证推理格式的实际增益。

  - 处理多任务 SFT 长度差异时，pack-level cross-entropy 有效：先在 pack 内按 token 平均，再跨 pack 等权平均，防止长
  response 驱动训练。这对同时训练 item 理解、用户理解、推荐等任务尤其有参考价值。

  - 层级 SID 的 RL 奖励稀疏问题可通过 prefix guidance + hierarchical credit assignment 缓解：仅在无正确前缀时补充前缀引导，advantages
  计算只比较同一父前缀下的候选，mask 掉给定前缀的梯度，避免只学会浅层一级码，提升全 SID 命中率。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
生成式推荐把下一项预测建模为序列生成任务，OneRec 等基于 Semantic ID 的模型已工业落地。引入 LLM 推理（CoT）被认为是下一阶段方向，但初步工作发现推理并不总带来推荐收益。挑战赛旨在连接 LLM 与推荐系统，统一建模物品理解、用户理解、推荐和世界知识，推动 recommendation foundation model。

**方法关键点**
- 基础模型 OneReason-0.8B/8B-pretrain 从 Qwen-3 扩展，加入多粒度 Semantic ID 语义对齐预训练：token / item / relation / user 四级，连接物品 SID 与自然语言。
- 数据：944,802 条 SFT 种子（think/nothink 两种 response 格式）、50 万匿名用户跨短视频/电商/广告/直播四域交互序列、35,914,095 个 item 的 SID-caption 对齐。
- 任务：物品理解（SID↔caption）、用户理解（相关行为选择 + 兴趣演化链生成）、跨域推荐（think + nothink 各 Pass@32 合并）、世界知识选择题。
- 评测：物品描述用双加权 F1；用户相关行为选择用 F1；兴趣链用 Action-Logic score；推荐用 PIDPass；知识用 accuracy。测试共 18,842 例。

**关键结果**
冠军方案：模型自采样推理轨迹 + Target-SID-Masked RFT，mask 答案 loss 提升 think/nothink 互补性。亚军：约束改写 item description + 按域混合 think/nothink 格式。季军：staged post-training，pack-level cross-entropy + DPO 偏好优化。第四名：prefix guidance + hierarchical credit assignment 解决多级 SID 奖励稀疏。Top5 总分在 1.40–1.44，其中推荐相关任务占主要权重。

**最值得记住的一句话**
推荐场景下 CoT 不是越多越好，只有为推荐目标专门设计推理监督并控制答案损失，推理才真正提升生成式推荐效果。
