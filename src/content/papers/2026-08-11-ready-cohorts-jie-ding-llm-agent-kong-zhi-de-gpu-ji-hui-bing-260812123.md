---
title: 'Ready Cohorts: Bounding GPU Opportunity and Avoiding Host Round Trips in LLM-Agent
  Control'
title_zh: Ready Cohorts：界定 LLM-Agent 控制的 GPU 机会并消除主机往返
authors:
- Josef Liyanjun Chen
affiliations:
- Independent Researcher
arxiv_id: '2608.12123'
url: https://arxiv.org/abs/2608.12123
pdf_url: https://arxiv.org/pdf/2608.12123
published: '2026-08-11'
collected: '2026-08-14'
category: Agent
direction: LLM Agent 控制面 GPU 调度与驻留优化
tags:
- LLM agents
- GPU scheduling
- cohort batching
- device-resident control
- agent runtime
- latency optimization
one_liner: 给出 ready-cohort 边界量化 agent 控制面 GPU 可调度机会，并证明设备端决策比主机往返快 1.19–2.39 倍
practical_value: '- 在高并发 agent 控制循环（如多 session 的商品搜索/推荐路由、预算/策略检查）不要每个 route/state
  更新都回 host 再下发；把二元决策（是否继续调用、选择哪个工具）留在 GPU 上，按论文结果可获得 1.19–2.39x 的端到端加速，且与 host oracle
  完全一致，适合作为工程改造项。

  - 用 ready-cohort 框架先离线评估 GPU 调度收益：固定窗口只拿到 F=30.19% 的控制机会，精确 DP 打包可到 P*=43.00%，上界
  U=45.85%，说明固定窗口漏掉 81.83% 的机会。部署前可用 offline replay 估算 batch size K 和 deadline，避免拍脑袋设置窗口。

  - 在推荐/广告 agent 的 trace 回放中，把 outcome-derived route key 当作 conditioning proxy，不要直接视作可执行身份；实际系统需要单独验证批处理结果与
  host oracle 一致。

  - 固定嵌套设备图若不能减少 host 决策，反而更慢；不要为了 GPU 化而 GPU 化，先确认控制路径是否真正消除了主机往返。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：LLM-agent 服务在模型/工具调用之间反复执行小型确定性状态转移；并发 session 多时控制面本身可能成为调度瓶颈，但单次转移太小，常被固定窗口或主机往返浪费。

**方法关键点**：定义 ready-cohort 边界，用固定分区份额 F、精确离线份额 P*、局部上界 U、在线达成份额 A 四个指标刻画 GPU 可调度机会；在零服务时间、无限容量、等相对 deadline 假设下，用专用动态规划精确计算 P*。另做机制实验，将 GPU 计算的 binary route 留在设备端，对比返回 4 bytes 到 host 再派发。

**关键结果**：在 851-session 公开 trace 的 Poisson 回放中，100k active sessions、K=256、50ms deadline 下 F=30.19%，P*=43.00%，U=45.85%，精确打包恢复固定窗口损失的 81.83% 机会；设备驻留路径在 36 个配置中全部快于主机路径，行中位比 1.19–2.39x；14,557,440 个批处理调用与 host oracle 完全一致；固定嵌套设备图无 host 决策减少时在 60 个配置中全部更慢。
