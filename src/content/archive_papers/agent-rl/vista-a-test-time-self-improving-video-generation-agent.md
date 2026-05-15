---
title: 'VISTA: A Test-Time Self-Improving Video Generation Agent'
authors: Long, Wan et al.
affiliation: Google Research
date: 2025-10
venue: arXiv
topic: agent-rl
topic_name: Agent RL
topic_icon: 🤖
idea: Test-time 多 agent 闭环：分解 → 多组 prompt 生成视频 → pairwise tournament 选最优 → 视/音/上下文三
  critic 出反馈 → 重写 prompt → 再生成。完全 black-box，对底层 T2V 模型零修改。
paperUrl: https://arxiv.org/abs/2510.15831
tags:
- Test-Time
- Multi-Agent
- Video Generation
- Self-Refine
unverified: false
detail:
  contribution: 把 reasoning RL 里的 "测试期延长思考" 思路平移到视频生成：用多 agent 评判 + prompt 重写 + 重生成的循环，让黑箱
    T2V 模型在不更新参数的情况下显著变好；首次系统化 "视觉 + 音频 + 上下文" 三维度 critic 框架。
  background: T2V 模型（Veo、Sora）对 prompt 极度敏感，单次生成难以同时满足视觉、音频、上下文一致性；普通用户也写不出理想 prompt。重训成本不可承受，必须在
    inference 时做手脚——这正是 inference-time scaling 在多模态生成领域的对应物。
  method: 4 步闭环。**Step 1 分解**：把用户想法转成 structured temporal plan（时间轴上的镜头序列与属性，每段含 visual/audio/context
    三类槽位）。**Step 2 多组生成**：对每段生成 K 个 prompt 变体，调用 T2V 得到 K 个候选视频。**Step 3 Pairwise
    Tournament**：用 LLM 评判员两两比较视频选当轮 winner，避免直接 K-way 排序的不一致。**Step 4 三 critic 反馈**：①
    Visual critic 看构图、动作、物理合理性；② Audio critic 听音画对齐与音效合理性；③ Context critic 检查与用户原意
    / 前后镜头一致性；三方反馈合并后由 prompt rewriter 改写新 prompt → 回到 Step 2。整体跑 5 轮迭代。
  experiments: vs direct prompting 的 win rate 随迭代单调上升：单场景 5 轮 **45.9%**、多场景 **46.3%**；有
    prompt 优化经验的标注员在 **66.4%** 头对头中偏好 VISTA 输出；Veo 2 / 3 上均验证。
  pros: 把 self-refine + multi-critic 工程化得很干净；对底层模型零侵入是落地友好的关键优势；三 critic 分工避免单一 judge
    的 bias，且与人类视频评测维度对应。
  cons: 不更新模型参数，严格说不属于狭义 "自迭代训练"，更接近 inference-time scaling；算力随轮次线性增长（5 轮至少 5K 次 T2V
    调用，成本可观）；tournament 引入打分 bias；目前主要在 Veo 系列验证，跨模型族泛化未知。
  inspiration: 把 Agent 范式带进视频生成的代表作；后续可扩展到 3D 生成、音乐生成、交互式动画等长程多模态任务；也提示 "视频质量 reward
    model" 这一新方向。
  takeaway: Inference-time Self-Improvement 派系的视频代表作，与 R1 的 "训练期 RL 涌现" 形成互补。
---

Test-time 多 agent 闭环：分解 → 多组 prompt 生成视频 → pairwise tournament 选最优 → 视/音/上下文三 critic 出反馈 → 重写 prompt → 再生成。完全 black-box，对底层 T2V 模型零修改。

## 核心贡献

把 reasoning RL 里的 "测试期延长思考" 思路平移到视频生成：用多 agent 评判 + prompt 重写 + 重生成的循环，让黑箱 T2V 模型在不更新参数的情况下显著变好；首次系统化 "视觉 + 音频 + 上下文" 三维度 critic 框架。

## 背景

T2V 模型（Veo、Sora）对 prompt 极度敏感，单次生成难以同时满足视觉、音频、上下文一致性；普通用户也写不出理想 prompt。重训成本不可承受，必须在 inference 时做手脚——这正是 inference-time scaling 在多模态生成领域的对应物。

## 方法

4 步闭环。**Step 1 分解**：把用户想法转成 structured temporal plan（时间轴上的镜头序列与属性，每段含 visual/audio/context 三类槽位）。**Step 2 多组生成**：对每段生成 K 个 prompt 变体，调用 T2V 得到 K 个候选视频。**Step 3 Pairwise Tournament**：用 LLM 评判员两两比较视频选当轮 winner，避免直接 K-way 排序的不一致。**Step 4 三 critic 反馈**：① Visual critic 看构图、动作、物理合理性；② Audio critic 听音画对齐与音效合理性；③ Context critic 检查与用户原意 / 前后镜头一致性；三方反馈合并后由 prompt rewriter 改写新 prompt → 回到 Step 2。整体跑 5 轮迭代。

## 实验结果

vs direct prompting 的 win rate 随迭代单调上升：单场景 5 轮 **45.9%**、多场景 **46.3%**；有 prompt 优化经验的标注员在 **66.4%** 头对头中偏好 VISTA 输出；Veo 2 / 3 上均验证。

## 优点

把 self-refine + multi-critic 工程化得很干净；对底层模型零侵入是落地友好的关键优势；三 critic 分工避免单一 judge 的 bias，且与人类视频评测维度对应。

## 局限

不更新模型参数，严格说不属于狭义 "自迭代训练"，更接近 inference-time scaling；算力随轮次线性增长（5 轮至少 5K 次 T2V 调用，成本可观）；tournament 引入打分 bias；目前主要在 Veo 系列验证，跨模型族泛化未知。

## 对后续工作的启发

把 Agent 范式带进视频生成的代表作；后续可扩展到 3D 生成、音乐生成、交互式动画等长程多模态任务；也提示 "视频质量 reward model" 这一新方向。

## 一句话总结

Inference-time Self-Improvement 派系的视频代表作，与 R1 的 "训练期 RL 涌现" 形成互补。
