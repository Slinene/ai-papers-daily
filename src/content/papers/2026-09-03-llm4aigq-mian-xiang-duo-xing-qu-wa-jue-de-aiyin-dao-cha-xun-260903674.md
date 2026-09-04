---
title: 'LLM4AIGQ: LLM-based AI Guidance Query Generation Framework for Multi Interest
  Mining'
title_zh: LLM4AIGQ：面向多兴趣挖掘的AI引导查询生成框架
authors:
- Xiangchen Pan
- Jiayi Xu
- Jing Wang
- Xing Fang
- Lingyun Zhu
affiliations:
- Huazhong University of Science and Technology
- Alibaba Group
- Nankai University
arxiv_id: '2609.03674'
url: https://arxiv.org/abs/2609.03674
pdf_url: https://arxiv.org/pdf/2609.03674
published: '2026-09-03'
collected: '2026-09-04'
category: QueryRec
direction: 生成式query推荐 · 多兴趣LLM
tags:
- LLM
- Query Recommendation
- Multi-Interest
- SFT-RL-DPO
- E-commerce
- Nearline-Online
one_liner: 用SFT-RL-DPO三阶段训练LLM，从多行为序列中分解多兴趣并生成高价值引导query，线上nearline生成+在线检索
practical_value: '- 用教师模型（更大LLM）对历史行为序列做兴趣分割并生成引导query，再让小模型SFT学习单兴趣风格，避免直接多兴趣SFT导致的模式坍缩；可迁移到电商搜索词推荐、push文案生成等场景。

  - RL多层级奖励设计：将think过程匹配、query长度与商业价值（judge模型S/A/B评级）、兴趣内语义与风格多样性、兴趣间内容多样性分开奖励，用GRPO优化；这种细粒度奖励拆解适合多目标生成式推荐任务。

  - DPO蒸馏推理能力：用RL checkpoint的think输出作为正样本，非think输出作为负样本，并过滤语义相似度高的pair，实现非think模式下的推理能力迁移，大幅减少线上推理token，降低延迟。

  - 工程部署：nearline生成+在线检索映射表，每N次交互触发LLM生成query写入表，在线直接检索；同时用LLM对item标题做短标题压缩，输入token减少26.8%，RT降低10.7%，值得在LLM
  serving中复用。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
传统AI引导查询生成采用两阶段Query-to-AIGQ范式：先通过多路召回从用户画像、历史行为、item侧信息和当前query中推断主查询，再规则泛化为引导query。这种级联式流程存在信息损失和语义漂移，且主查询推导依赖user-item共现，难以建模用户多兴趣，导致生成的引导query商业价值低、与购买意图错配。LLM具备强语义理解和生成能力，可端到端直接建模用户多兴趣并生成引导query，避免级联损失，但面临多兴趣噪声、缺乏显式ground truth、在线推理延迟三大挑战。

## 方法关键点
- **数据预处理与上下文压缩**：保留最近50条多行为（搜索、点击、加购、收藏、购买），用LLM将原始item标题压缩为短标题，去除营销冗余，减少输入token。
- **三阶段训练**：
  - **SFT**：用教师模型对历史序列做兴趣分割，得到多个单兴趣子序列，每个子序列对应引导query，训练学生模型学习AIGQ风格，避免直接多兴趣SFT的模式坍缩。
  - **RL**：在混合多兴趣序列上，要求模型显式推理兴趣划分、消费意图推断和query生成；设计think级（兴趣分割匹配+格式）、query级（长度约束+商业价值judge模型评分）、interest级（语义相似度+风格多样性+数量格式）、global级（兴趣间内容多样性）四层奖励，用GRPO优化。
  - **DPO**：将RL checkpoint的think模式输出作为正样本，非think模式输出作为负样本，并过滤语义相似度高的pair，蒸馏推理能力到非think模式，以降低线上推理token数。
- **部署架构**：nearline生成（每N次交互触发LLM生成query写入映射表）+在线检索（用户进入界面时实时查表），满足低延迟高吞吐。

## 关键实验
在淘宝/天猫真实多行为日志上采样：SFT 11,259样本，RL 3,000，DPO 5,000（过滤后3,500），测试1,000。评价指标包括相关性（Recall@k, NDCG@k）和商业价值（S/A/B比例）。对比zero-shot大模型和不同训练阶段变体。
- LLM4AIGQ-ONESFT+RL+DPO取得最佳：Recall@10=0.2101, NDCG@10=0.2377, S ratio=0.8616，显著超过Qwen3-30B-A3B基座（Recall@10=0.1513）和更大模型（Qwen3-235B-A22B Recall@10=0.1412）。
- 消融显示：单兴趣SFT优于多兴趣SFT；去掉任意层级奖励均导致指标下降；DPO偏好对过滤提升明显。
- 在线A/B：10%流量uCTR提升4.46%，40%流量uCTR提升2.53%。

## 最值得记住的一句话
用教师模型蒸馏兴趣分割和引导query生成，再通过SFT-RL-DPO三阶段训练，可以在保持低延迟非think推理的同时，显著提升生成式query推荐的效果。
