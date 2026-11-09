---
title: 'Rethinking Latent Reasoning for Generative Recommendation: Beyond Teacher-Generated
  CoT and Recurrent Hidden-State Feedback'
title_zh: 反思生成式推荐中的隐式推理：超越教师生成 CoT 与循环隐状态反馈
authors:
- Yiwen Chen
- Fuwei Zhang
- Zehao Chen
- Deqing Wang
- Hehan Li
- Peizhi Xu
- Hanmeng Liu
- Shuanglong Li
- Xin Pei
- Fuzhen Zhuang
affiliations:
- Beihang University
- Baidu
arxiv_id: '2611.09006'
url: https://arxiv.org/abs/2611.09006
pdf_url: https://arxiv.org/pdf/2611.09006
published: '2026-11-06'
collected: '2026-11-09'
category: GenRec
direction: 生成式推荐 · 隐式推理与 thought tokens
tags:
- Generative Recommendation
- Latent Reasoning
- Thought Tokens
- Semantic ID
- Sparse Encoder
- SFT
one_liner: 提出 PHiT，用历史物品语义关键词直接监督可预填 thought tokens，以 SFT 替代教师 CoT 和循环反馈，在四个推荐基准上超过
  LASAR
practical_value: '- 在基于 Semantic ID 的生成式推荐中，可以用 SPLADE 等稀疏编码器对 item 的 title/brand/category/description
  离线编码并缓存，按用户历史聚合 top-K 关键词，作为 thought tokens 的辅助监督，替代昂贵的教师 LLM CoT 蒸馏；构造成本从 145 分钟降到约
  113 秒。

  - 采用固定 thought token IDs 插入 history 与 target SID 之间，通过一次 causal prefill 获得用户相关隐状态，避免
  Coconut 式循环 hidden-state feedback，可直接接入 vLLM 等标准 token/KV-cache serving 路径；推理时只增加
  N 个 token 位置，无额外生成或自定义执行循环。

  - 做 CoT 步骤裁剪前，先做步骤级诊断：分别看每步对最终答案似然和下一步连贯性的贡献。论文发现 history analysis 是唯一双正贡献步骤，preference/intent
  步骤负贡献；只保留 history 部分可减少 61% 监督文本且指标全面提升。

  - 关键词多标签目标极度不平衡时，用 class-balanced BCE：正负项分别按集合大小归一化，避免负样本淹没梯度；thought token 状态用
  mean pooling + 线性 head 预测，训练后丢弃辅助 head。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
生成式推荐把 next-item 预测建模为 SID 的自回归生成，但 latent reasoning 方案面临两个工程障碍：监督需要先由教师 LLM 为每条样本生成 CoT 轨迹，推理又常依赖 Coconut 式循环 hidden-state feedback，难以接入标准 serving 引擎。作者希望同时摆脱教师 CoT 监督和循环执行接口。

## 方法关键点
- **步骤级诊断**：在 Beauty 上对 CoT 步骤做删除实验，发现 history analysis 对目标 SID 似然和下一推理步连贯性均为正贡献，而 preference construction 与 intent inference 对答案贡献为负；在 Instruments 上只保留 history 步骤可减少约 61% 监督文本且 6 个指标全面提升。
- **PHiT 目标构造**：用冻结 SPLADE 对每个 item 文本（title/brand/category/description）编码得到词级权重并缓存；对用户历史做权重聚合，选 top-K=16 关键词作为多标签语义目标，完全不需要教师 LLM 生成。
- **模型设计**：在词表中新增 N 个固定 thought tokens，插在 history 与 target SID 之间；同一组 token ID 通过 causal attention 产生用户相关隐状态，mean pooling 后由线性 head 预测历史关键词目标。训练损失为 SID 自回归损失 + class-balanced BCE 关键词损失，仅用 SFT，λ=1.0，N=8。
- **推理**：丢弃 sparse encoder 和 auxiliary head，只把固定 thought token IDs 与 history 一起做一次标准 causal prefill，再解码 SID；无额外自回归中间步骤和自定义 hidden-state feedback。

## 关键结果
在 Beauty、Instruments、Sports、Steam 四个基准上，PHiT 仅用 SFT 在全部 24 个主指标上取得最优，22 个显著超过最强 baseline；其中 Sports HR@20 较 LASAR 提升 21.7%，NDCG@20 提升 12.2%。Beauty 消融显示，匹配历史的语义监督优于 shuffled targets、CoT alignment 与 CoT keywords。监督构造从 Qwen3.6-35B-A3B 生成 CoT 的 145 分钟降至 113 秒（单 GPU）。

## 最值得记住的一句话
用历史物品语义关键词直接监督可预填的 thought tokens，可以在不生成教师 CoT、不引入循环反馈的前提下，让生成式推荐获得隐式推理收益。
