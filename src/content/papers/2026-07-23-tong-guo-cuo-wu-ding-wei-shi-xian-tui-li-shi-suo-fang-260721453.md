---
title: Test-Time Scaling via Error Localization
title_zh: 通过错误定位实现推理时缩放
authors:
- Rajiv Shailesh Chitale
- Rahul Madhavan
- Taneesh Gupta
- Deepanway Ghosal
- Aravindan Raghuveer
affiliations:
- Google DeepMind
arxiv_id: '2607.21453'
url: https://arxiv.org/abs/2607.21453
pdf_url: https://arxiv.org/pdf/2607.21453
published: '2026-07-23'
collected: '2026-07-24'
category: Reasoning
direction: 推理时缩放 · 错误定位引导前缀树搜索
tags:
- Test-Time Scaling
- Error Localization
- Tree Search
- Token-Level Credit Assignment
- Feedback-guided Generation
one_liner: 利用反馈在 token 级定位错误，保留正确前缀分支执行，大幅提升推理时搜索的 token 效率
practical_value: '- **Agent 多步推理的自我修正**：在 Agent 执行复杂任务（如工具调用、多轮对话）时，可利用 TTEL 的 token
  级错误定位思想，根据环境反馈（如 API 报错）的 log 概率偏移找到出错步骤，仅回退到该步骤重试，避免从头重复整段推理，可大幅降低 token 消耗。

  - **生成式推荐 / 广告文案的“局部重写”**：当生成推荐理由或广告创意被判为低质时，可借鉴 TTEL 的「前缀保留 + 后缀分支」策略：不重写全文，而是通过模型在有无反馈条件下的
  token 概率差定位问题片段，只替换可疑部分，保留高概率前缀，提升生成效率和质量。

  - **null‑baseline 过滤噪声信号**：方法中引入非诊断性反馈 null‑feedback 减去上下文引入的通用概率偏移，得到真正由反馈驱动的不一致。在业务场景（如评分反馈修正）中，可以直接模仿这一
  trick，避免因模型对长文本的自然概率衰减而误判错误位置。

  - **推理预算固定下的更优 Pareto 前沿**：TTEL 在同等 token 预算下 pass@k 更高，表明在实时性要求高的在线服务（如搜索、广告）中，采用局部修补的树搜索可取代独立重采样，更划算地使用推理资源。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

## 动机
测试时扩大采样量（如 Best‑of‑K）通常提升 LLM 在推理任务上的表现，但独立采样丢弃失败轨迹，造成大量冗余计算；顺序多轮修正虽引入反馈，却将反馈当作全局指令，难以精准定位错误，甚至重复犯错。根本问题在于：环境反馈是轨迹特异的，但现有方法把它当作“从头重试”的通用信号，导致计算浪费。

## 方法关键点
- **Token 级错误定位**：对一条失败轨迹，用有反馈的条件概率 $p^{(T)}_t(f)$ 与无反馈的学生概率 $p^{(S)}_t$ 对比，得到原始概率下降 $\Delta_t(f)$。
- **Null‑基线过滤**：为消除单纯追加文本引起的概率漂移，再计算一个非诊断性反馈 $f_\emptyset$ 下的基线下降 $\Delta_t(f_\emptyset)$，以 $g_t = \Delta_t(f) - \Delta_t(f_\emptyset)$ 作为真正由反馈驱动的错误信号 $E_{\text{filtered}}$。
- **前缀保留与分支**：选取 $g_t$ 最大的位置 $t^*$ 作为分支点，截断轨迹保留正确前缀 $y_{<t^*}$，从该点生成新分支，实现最大前缀复用。
- **树搜索策略**：当无定位信号时触发完全重启，避免无效延续；整体算法不依赖外部奖励模型或梯度更新。

## 关键实验
- **基准**：LiveCodeBench（131 题）、AIME‑25（30 题）、HMMT‑25（30 题），与独立采样、多轮修正、递归自聚合（RSA）对比。
- **核心结果**：Qwen3‑8B 在 LiveCodeBench 上，TTEL 的 pass@64 达 71.0%，但 token 消耗仅约为独立采样的一半（360.4k vs. 735.0k），形成严格占优的 Pareto 前沿。在无环境反馈的数学基准上同样占优，例如 AIME‑25 上 pass@16 达 82.0%。
- **消融验证**：移除 null‑基线后，平均 spike 数量从 19.3 暴增至 486.0，pass@k 显著下降；不以完整推理轨迹作为上下文也会导致性能恶化，证明精确错误定位需同时保留完整 trace 和可诊断反馈。

> **最值得记住的话**：“与其把反馈当作从头再来的指令，不如用它找到推理在哪里开始错，然后只重写错误之后的部分。”
