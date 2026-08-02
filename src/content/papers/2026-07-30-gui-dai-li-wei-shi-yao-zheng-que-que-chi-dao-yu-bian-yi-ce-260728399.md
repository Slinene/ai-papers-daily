---
title: Why Are GUI Agents Correct but Late? Decode on the Decision-Time Critical Path,
  Tested with Pre-Compiled Policy Trees
title_zh: GUI 代理为什么正确却迟到？预编译策略树消除解码延迟
authors:
- Zihan Dong
- Rui Qian
- Qishi Zhan
- Dongshen Peng
- Kaixin Li
- Yu Li
affiliations:
- Georgia Institute of Technology
- Fudan University
- Marquette University
- University of North Carolina at Chapel Hill
- National University of Singapore
arxiv_id: '2607.28399'
url: https://arxiv.org/abs/2607.28399
pdf_url: https://arxiv.org/pdf/2607.28399
published: '2026-07-30'
collected: '2026-08-02'
category: Agent
direction: Agent 决策时延优化
tags:
- GUI Agent
- Policy Tree
- Anticipatory Execution
- Decoding Latency
- Transient Events
one_liner: 提出自适应预期策略树，在空闲时提前规划 GUI 动作分支，事件触发时即时匹配执行，消除自回归解码延迟
practical_value: '- 在实时推荐/竞价系统中，若候选动作集可枚举（如固定模板、预设回复），可用预编译策略树将 LLM 推理从在线关键路径移出，仅保留轻量状态匹配，避免解码延迟导致错过机会。

  - 分支路由准确性是决定效果的关键瓶颈，工业落地时需重点优化状态匹配模型（如训练轻量分类器或规则引擎）以降低误匹配率。

  - 借鉴“延迟感知的树规模控制”：根据系统解码时延动态设定策略树层数，确保覆盖可能的等待时间，避免过度规划浪费资源。

  - 对于多模态 Agent 架构（如电商导购助手），可考虑将屏幕截图的变化检测与预编译分支结合，实现低延迟响应，尤其在闪购、秒杀等瞬态场景。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：GUI 代理在应对弹窗、闪烁等瞬态事件时，即使模型最终给出正确动作，也经常因自回归解码耗时过长，导致窗口已关闭而失败。问题根源在于决策关键路径上的昂贵解码。
**方法**：提出 **AAPT (Adaptive Anticipatory Policy Trees)**，无需修改基模型。在屏幕空闲期，同一多模态模型以类似树搜索的方式构建条件策略树，每个分支包含可观察的守卫条件、预授权的动作和分支特定截止时间；树的大小根据模型自身解码延迟设定。当界面发生变化时，一个轻量观察器对变化帧进行匹配，一旦识别出对应的预编译分支，便立即执行动作，完全跳过文本生成。
**关键结果**：在预注册的配对试验中，AAPT 将瞬态事件成功率从基准的 0.50 提升至 0.79（p=1.8×10⁻³），且零错误动作。消融证实快速观察器解码、有效树规划和准确分支路由三个要素不可或缺，其中分支路由是因果瓶颈。在另一通用多模态模型上复现类似效果（126 次试验，p=4.9×10⁻¹³）。外部基准测试显示，AAPT 与反应式基准总体性能相当，但二者优势互补：AAPT 在候选动作可预先枚举时最强，反应式方法在动作难以穷举时更佳。
