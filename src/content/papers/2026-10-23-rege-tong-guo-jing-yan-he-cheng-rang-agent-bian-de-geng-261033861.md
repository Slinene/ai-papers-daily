---
title: 'ReGE: Stronger Agents through Experience Synthesis'
title_zh: ReGE：通过经验合成让 Agent 变得更强
authors:
- Jiarong Liang
- Yubo Wang
- Zijie Liu
- Yuxuan Zhang
- Ping Nie
- Wenhu Chen
affiliations:
- University of Waterloo
- University of North Carolina at Chapel Hill
- University of British Columbia
arxiv_id: '2610.33861'
url: https://arxiv.org/abs/2610.33861
pdf_url: https://arxiv.org/pdf/2610.33861
published: '2026-10-23'
collected: '2026-10-28'
category: Agent
direction: Agent 经验合成与复用
tags:
- Agent
- Experience Synthesis
- Trajectory Aggregation
- Test-time Compute
- Inference Cost
one_liner: 把多次尝试的轨迹与产物联合合成为自包含指导，低 token 成本提升同模型后续执行成功率
practical_value: '- 如果已经在做 agent 或搜索推荐的多路并行采样（例如同一个 query 跑多个策略），别只做投票或 best-of-n；把完整轨迹截断后直接喂给一个
  coach 一次性合成“执行计划 + 关键事实 + 失败坑点”，能显著减少指导构建 token（>95%）且保留成功率。

  - 工程实现上，截断原始轨迹（steps 120 / reasoning 200 chars / commands 160 chars / artifact 6000
  chars）而不预先做 per-trajectory LLM 摘要，可避免独立摘要的信息割裂，Joint synthesis 比 Independent summaries
  短约 1/4，总 tokens 降约 20–32%。

  - 即使 source 池中都是失败尝试，也能提取可用操作路径（如浏览器任务的打开方式），因此不要丢弃失败的 rollout；mixed 成功/失败池带来的增益最大。

  - 低端模型 + ReGE 可达到高端模型同等成功率而成本仅 28%，这为在线服务降本提供了可复用模式：用便宜模型做多次尝试 + 一次性经验合成，替代单次昂贵模型。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：交互式 Agent 的重复尝试能发现一次运行遗漏的事实、可执行操作与失败教训，但完整轨迹长、正确性未知，且环境重置后无法继承文件/状态。如何低成本地把这些经验转化为 fresh attempt 的有效指导，是本文要解决的问题。

**方法关键点**：
- ReGE 框架，主实现 ReGE-Syn：coach 一次调用，读取有界渲染的源轨迹与 artifacts，输出自包含指导；学生从初始环境状态 s0 重新执行，根据当前观察 adopt/adjust/verify。生成、合成、执行使用同一 base model，无参数更新、无更强教师。
- 源表示：每 attempt 截断 120 steps，reasoning/commands 各截断 200/160 chars，artifact 上限 6000 chars；不生成 per-trajectory LLM summary，避免信息割裂。
- 指导内容：facts、operations、pitfalls 放在执行步骤旁；可包含 candidate answer 及验证方式。ReGE-Sel 作为变体，直接选择一条轨迹作指导。

**关键结果**：
- 四个 benchmark（Terminal-Bench 2.0、Spider2-Lite、AndroidWorld、BrowseComp-Plus）上，ReGE 平均成功率高 9.9pp（GPT）/ 8.8pp（Claude）。
- gpt-5.6-luna+ReGE 在 468 paired tasks 平均达 67.4%，与 gpt-5.6-sol 的 67.0% 相当，而成本（含 source pool）仅为 28%（$0.214 vs $0.766）。
- 在 matched BrowseComp-Plus，相比 adapted AggAgent，guidance-construction tokens 减少 98.2%/95.5%，combined construction+execution tokens 减少 15.7%/35.4%（不含 source generation）。
- 消融显示：process records 降低学生步数；mixed 成功/失败池增益最大；Joint synthesis 的 guidance 长度约为 Direct history/Independent summaries 的 1/4，总 tokens 降 19.8%/31.8%。

**最值得记住的一句话**：与其对多次尝试做投票或独立摘要，不如把截断的原始轨迹一次联合合成为可执行指导，让同一个低端模型在干净环境里重新执行并验证。
