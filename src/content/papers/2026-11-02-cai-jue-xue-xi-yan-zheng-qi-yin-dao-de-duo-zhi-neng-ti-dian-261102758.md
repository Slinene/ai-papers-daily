---
title: 'Learning to Adjudicate: Verifier-Guided Multi-Agent Reasoning for E-Commerce
  Relevance'
title_zh: 裁决学习：验证器引导的多智能体电商相关性推理
authors:
- Shi Shu
- Hao Chen
- Baopu Qiu
- Chao Wei
- Weiru Zhang
- Xiu Li
- Xiaoyi Zeng
affiliations:
- Tsinghua Shenzhen International Graduate School, Tsinghua University
- Alibaba International Digital Commerce Group
arxiv_id: '2611.02758'
url: https://arxiv.org/abs/2611.02758
pdf_url: https://arxiv.org/pdf/2611.02758
published: '2026-11-02'
collected: '2026-11-03'
category: RecSys
direction: 多智能体协作相关性判定
tags:
- Multi-Agent
- Relevance Modeling
- GRPO
- Experience Replay
- Knowledge Distillation
- E-Commerce Search
one_liner: 提出 CADRE 框架，用冻结三专家加可训练 Verifier 做选择性辩论，并以成功经验回放 GRPO 优化后蒸馏到轻量学生模型
practical_value: '- 多智能体架构可迁移：将商品属性、用户意图、平台规则拆成独立 expert，共享冻结 LLM backbone，只训练 Verifier
  做证据裁决。相比 all-in-one CoT 避免单一上下文冲突，训练成本低，适合相关性审核、广告质量分等复杂判定。

  - 选择性辩论控制成本：只在三专家第一轮 label 不全体一致时触发 Verifier 提问和专家修订；一致时直接采用 initial adjudication。离线/在线都能大幅降低多轮交互开销，尤其适合高
  QPS 场景。

  - Successful-experience replay：把 terminal label 正确的轨迹存 pool，每个 input 保留最多 8 条，Replay-GRPO
  时每个 input 加 2 条 replay 轨迹与 8 条 fresh rollouts 混合算 group advantage。可在有限 rollout budget
  下稳定 RL、提升长尾难例。该 trick 可复用到 RLHF/多轮 agent 训练。

  - CoT latent distillation：多智能体 teacher 生成 CoT，用 frozen BGE-M3 编码成 embedding，学生 mBERT
  加 cosine loss + CE，推理时只过学生模型。线上 A/B RPM +1.69%、CTR +0.76%，RS +0.3pp，说明 reasoning
  signal 蒸馏到轻量交叉编码器是低成本落地路径。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
电商搜索相关性判断经常需要同时理解用户意图、比对商品属性并套用业务规则。单一 CoT 上下文容易让某种视角覆盖掉关键证据，例如图 1 中“矩形≠方形”的属性冲突被意图解释覆盖，最终误判为强相关。复杂 query-product 对往往存在多视角证据冲突，要求模型在匹配准则下判定哪条证据具有决定性。现有 DPO/KTO/GRPO 等方法对已生成判断做偏好/奖励优化，但难以解决冲突裁决与有限 rollout 预算下难例成功轨迹稀缺的问题。

**方法关键点**
- 三专家共享冻结 Qwen3-14B：Analyst 关注属性匹配，Intent 结合历史点击/搜索行为，Ruler 依据平台规则原文；专家独立生成首轮报告和 label。
- 可训练 Verifier 接收 query-product 和三份报告，做初始裁决；当三专家首轮 label 不全体一致时，Verifier 针对每位专家生成 focused question，专家修订后 Verifier 再给最终裁决。专家不直接通信，避免过早收敛。
- 训练分四步：Qwen3.8-Max 生成多轮交互 SFT 初始化；GRPO 做 on-policy 优化，reward 含格式、层级标签准确、reasoning 一致性以及 debate shaping；用 GRPO checkpoint 收集 terminal label 正确的轨迹进入经验池；Replay-GRPO 从 SFT 重启，混合 8 条 fresh rollouts 和 2 条 replay 轨迹更新。
- 为线上低延迟，将 CADRE 作为 teacher，把多轮 CoT 经 frozen BGE-M3 编码后，用 cosine loss 对齐 mBERT 学生的 [CLS] 表征，再加 CE 分类损失蒸馏。

**关键结果**
在 78,997 train / 18,710 test 的 7 类电商相关性数据集上，CADRE 达到 ACC 0.8334、Macro-F1 0.7766、Weighted-F1 0.8321，比 LLM-Replay-GRPO + context 分别高 3.73、13.64、4.06 个百分点；比 Expert Oracle 的 0.8051 ACC 高 2.83 个百分点，说明 Verifier 能纠正三专家都错的情况。学生模型用 Experts CoTs + Verifier CoT 蒸馏，比仅用 gold label 的 mBERT 在 ACC 上提升 3.53 个百分点。线上 7 天 A/B 中，蒸馏学生相对生产 baseline 获得 RPM +1.69%、CTR +0.76%，RS 绝对提升 0.3 个百分点。

**最值得记住的一句话**
把互补专家与可训练裁决者分离，并通过选择性辩论和成功经验回放，能让有限 rollouts 的 RL 稳定产出可蒸馏的高质量相关性判断。
