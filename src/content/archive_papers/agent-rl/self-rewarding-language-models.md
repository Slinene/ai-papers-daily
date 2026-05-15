---
title: Self-Rewarding Language Models
authors: Weizhe Yuan, Richard Yuanzhe Pang, Kyunghyun Cho, …, Jason Weston
affiliation: Meta AI / NYU
date: 2024-01
venue: arXiv (later ICML 2024)
topic: agent-rl
topic_name: Agent RL
topic_icon: 🤖
idea: Actor 与 Judge 合一：模型用 LLM-as-a-Judge 给自己生成的多个回答打分，组成偏好对做迭代 DPO。Instruction following
  和 Judge 能力同步上升。
paperUrl: https://arxiv.org/abs/2401.10020
tags:
- Self-Reward
- DPO
- Iterative
unverified: false
detail:
  contribution: 首次实证：让同一个 LLM 同时承担 Actor（生成回答）与 Judge（给自己打分）双角色，通过迭代 DPO，两条曲线（任务能力
    + 评判能力）可以同时单调上升，跳出 "固定 reward model 锁死性能" 的天花板。
  background: 传统 RLHF 中 reward model 是被人类偏好训练的、且训完冻结，因此 RM 上限就是人类标注员上限；要做 "超人 agent"，必须打破这一锁定。论文提出的解法是：让
    Judge 和 Actor 共用同一模型，并随训练一起进化。
  method: ① 用 SFT 初始化模型 M0，使其同时具备 instruction-following 与 LLM-as-a-Judge 能力（基于 Open
    Assistant 偏好数据 + EFT 任务）；② M0 对每个 prompt 生成 N=4 个候选回答；③ M0 自己用结构化 prompt 给每个回答打
    0-5 分，挑出 best/worst 形成偏好对；④ DPO 训练得到 M1；⑤ M1 重复以上流程产出 M2、M3。关键约束是：Judge 与 Actor
    必须是同一模型同步更新，避免 "Judge 静止 → 上限锁死" 的旧问题复现。
  experiments: Llama-2-70B 上做 3 轮迭代。AlpacaEval 2.0 win rate 9.94% (M0) → 15.38% (M1)
    → 20.44% (M2) → 20.44% (M3)，超过 Claude 2、Gemini Pro、GPT-4 0613（同期版本）；Judge 自身 NLI
    / pairwise accuracy 同步上升，证明 "自己当法官" 不退化。
  pros: 第一次干净跑通 "自迭代闭环" 在主流 benchmark 上的 monotonic gain；范式简单可复现；显式分析了 Judge 能力同步上升，回应了
    "自评会塌缩吗" 的核心质疑。
  cons: Reward hacking 风险随轮次累积（论文也观察到 length bias 倾向）；强依赖 base 模型本身的 LLM-as-a-Judge
    能力，弱模型起步会失败；只跑到 M3，长期是否会 reward collapse 没有理论保证；M2→M3 几乎停滞暗示存在天花板。
  inspiration: 后续 SPIN、SPPO、Iterative DPO、Meta-Rewarding LMs 一系列工作都以此为参照点；引出 "Judge
    能不能也用 RL 来训练" 这一新课题。
  takeaway: Self-Reward 范式从概念走向实证的里程碑工作。
---

Actor 与 Judge 合一：模型用 LLM-as-a-Judge 给自己生成的多个回答打分，组成偏好对做迭代 DPO。Instruction following 和 Judge 能力同步上升。

## 核心贡献

首次实证：让同一个 LLM 同时承担 Actor（生成回答）与 Judge（给自己打分）双角色，通过迭代 DPO，两条曲线（任务能力 + 评判能力）可以同时单调上升，跳出 "固定 reward model 锁死性能" 的天花板。

## 背景

传统 RLHF 中 reward model 是被人类偏好训练的、且训完冻结，因此 RM 上限就是人类标注员上限；要做 "超人 agent"，必须打破这一锁定。论文提出的解法是：让 Judge 和 Actor 共用同一模型，并随训练一起进化。

## 方法

① 用 SFT 初始化模型 M0，使其同时具备 instruction-following 与 LLM-as-a-Judge 能力（基于 Open Assistant 偏好数据 + EFT 任务）；② M0 对每个 prompt 生成 N=4 个候选回答；③ M0 自己用结构化 prompt 给每个回答打 0-5 分，挑出 best/worst 形成偏好对；④ DPO 训练得到 M1；⑤ M1 重复以上流程产出 M2、M3。关键约束是：Judge 与 Actor 必须是同一模型同步更新，避免 "Judge 静止 → 上限锁死" 的旧问题复现。

## 实验结果

Llama-2-70B 上做 3 轮迭代。AlpacaEval 2.0 win rate 9.94% (M0) → 15.38% (M1) → 20.44% (M2) → 20.44% (M3)，超过 Claude 2、Gemini Pro、GPT-4 0613（同期版本）；Judge 自身 NLI / pairwise accuracy 同步上升，证明 "自己当法官" 不退化。

## 优点

第一次干净跑通 "自迭代闭环" 在主流 benchmark 上的 monotonic gain；范式简单可复现；显式分析了 Judge 能力同步上升，回应了 "自评会塌缩吗" 的核心质疑。

## 局限

Reward hacking 风险随轮次累积（论文也观察到 length bias 倾向）；强依赖 base 模型本身的 LLM-as-a-Judge 能力，弱模型起步会失败；只跑到 M3，长期是否会 reward collapse 没有理论保证；M2→M3 几乎停滞暗示存在天花板。

## 对后续工作的启发

后续 SPIN、SPPO、Iterative DPO、Meta-Rewarding LMs 一系列工作都以此为参照点；引出 "Judge 能不能也用 RL 来训练" 这一新课题。

## 一句话总结

Self-Reward 范式从概念走向实证的里程碑工作。
