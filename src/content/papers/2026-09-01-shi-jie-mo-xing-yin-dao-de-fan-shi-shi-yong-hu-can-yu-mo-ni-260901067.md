---
title: World Model-Guided Reinforcement Learning via Counterfactual User Engagement
  Simulation
title_zh: 世界模型引导的反事实用户参与模拟强化学习
authors:
- Ang Li
- Xin Xu
- Bin Liang
- Yue Ma
- Fubang Zhao
- Yangyang Kang
- Kam-Fai Wong
affiliations:
- The Chinese University of Hong Kong
- Zhejiang University
- ByteDance China
- MoE Key Lab of High Confidence Software Technologies, CUHK
arxiv_id: '2609.01067'
url: https://arxiv.org/abs/2609.01067
pdf_url: https://arxiv.org/pdf/2609.01067
published: '2026-09-01'
collected: '2026-09-02'
category: RecSys
direction: 世界模型反事实用户模拟 · 推荐策略 RL
tags:
- World Model
- User Simulation
- Counterfactual RL
- LLM4Rec
- Recommendation
- Engagement Modeling
one_liner: 用冻结 LLM 用户参与世界模型并行预测多候选 item 的异质反馈，转化为奖励训练 1.7B 推荐策略，跨域匹配或超过更大 LLM。
practical_value: '- **把用户反馈模拟器当作离线 RL 奖励源**：对同一 history 采样 G 个候选 item，让 UEWM 并行预测反馈，构造
  same-state 反事实比较；这比从 logs 学 policy 或 SFT distillation 更符合策略梯度对「同状态多动作」的需求。

  - **多信号反馈向量化 + 权重映射奖励**：将点赞、分享、差评、评分、评论文本统一向量化，再用权重向量映射为标量 reward；在电商场景可以把点击、加购、收藏、评论情感按业务目标加权，而不是只看点击率。

  - **小模型策略优化可落地**：用 8B 模拟器奖励训练 1.7B 学生模型，在 Amazon Books/Movies 和 Google Local 上超过
  SFT蒸馏和 DeepSeek-GRM 奖励，说明可低成本获得接近大模型的推荐策略，适合粗排/召回级小模型精调。

  - **跨域迁移的边界要清楚**：UEWM 从中文短视频迁移到英文电商/本地生活做评分/评论预测有效，说明学到的是「从历史推断用户动态」的通用过程；但它是纯文本、只建模用户侧动态，缺少视觉/价格/库存/平台侧约束，接入业务时需补齐多模态与曝光分配机制。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
RL 做用户中心 agent 受限于在线反馈成本、延迟与风险，且日志只记录已曝光 item，难以在同一用户状态下比较不同动作的反事实结果。因此需要一种可靠的用户反馈模拟器，在真实曝光前为策略提供可比较的奖励监督。

**方法关键点**
- 将推荐 item 视为 agent action，异质用户反馈（点赞、分享、收藏、差评、评论）作为 environment observation，历史序列作为 state。
- UEWM 是共享的用户侧语言世界模型，从用户历史中摊销推断个性化互动动态，预测对候选 item 的反馈；同一模型可实例化不同用户动态。
- 训练 recipe：Qwen3-8B 为 backbone；435K 样本、150 步历史上自回归 SFT；20K CoT 数据 mid-training；20K GRPO 后训练，离散信号用正确性奖励，评论文本用 ROUGE-Lsum。
- WMG-RL：冻结 UEWM，下游策略对同一 history 采样 G=8 个候选 item，UEWM 并行预测反馈，向量化后加权得 reward，用 clipped surrogate + KL 约束优化策略。

**关键实验与数字**
- 模拟器保真度：in-domain avg Acc 70.25、avg Macro-F1 63.11，超过 Qwen3-235B 等大模型；评论生成 BERTScore 82.09。
- 零样本迁移：Amazon Books rating Acc 32.90、Movies 34.47、Google Local 29.20，均超过 LettinGO、RLPF 等专用 baseline。
- WMG-RL 主结果：1.7B 学生策略在 Books/Movies/Google Local 上分别达到 41.91/42.84/37.95，超过 SFT蒸馏和 DeepSeek-GRM 奖励，且匹配或超过 OpenAI o3、DeepSeek-R1。
- UEWM 奖励与真实评分 Pearson r=0.70；反事实注入负反馈后预测评分显著下降；10 轮模拟中累积奖励优于 SFT baseline。

最值得记住的一句话：UEWM 不是人类行为的确定性 oracle，而是一个可跨域迁移的同状态反事实奖励 proxy，用它构造的 same-state 比较才是 WMG-RL 真正的价值所在。
