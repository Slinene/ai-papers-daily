---
title: 'Cap-and-Track: Optimizing LLM Inference Request Dispatch Across Shifting Capacity'
title_zh: Cap-and-Track：动态容量下 LLM 推理请求调度优化
authors:
- Benjamin Novotny
- Doug Szeto
- Chang Wang
- Shicheng Chen
- George Zhihua Yuan
- Bob Kamma
- Michael Ge
- John Xin Zhou
- Andrea Olgiati
affiliations:
- Meta
- Google
arxiv_id: '2611.24891'
url: https://arxiv.org/abs/2611.24891
pdf_url: https://arxiv.org/pdf/2611.24891
published: '2026-11-18'
collected: '2026-11-19'
category: LLM
direction: LLM 推理调度 · 容量自适应
tags:
- LLM-serving
- admission-control
- congestion-control
- durable-queue
- vLLM
- capacity-shifting
one_liner: 以 per-replica 快速拒绝与基于 429 的 MIMD 调度，使 LLM 异步推理在容量变动下保持高利用率
practical_value: '- 在生成式推荐 / 广告文案 / query 改写等离线或异步 LLM 服务中，启用 per-replica 请求 cap（如
  vLLM max_num_seqs 上方的小幅 oversubscription，如 128→140）作为快速失败信号，替代引擎内无界等待队列，防止请求超时后仍占用
  GPU 导致 goodput 跌到 0；这比依赖超时或延迟信号更稳定。

  - 调度侧采用 multiplicative-increase/multiplicative-decrease，只根据 HTTP 429 拒绝占比调整发送速率，不用固定全局
  rate；每 15s 一个 leader 汇总各 worker 计数，按队列分配速率，容量变动无需重调参数。可直接用于内部推理网关或 Agent pipeline
  的批量任务分发。

  - 引入 durable priority queue（如 FOQS / Kafka 类）把溢出请求放在执行引擎外等待，用优先级区分时效性；低优先级 backfill
  可排队数小时，高优先级仍保持低延迟。电商搜索/广告的离线 LLM 任务（商品理解、自动文案、向量生成）可据此区分实时与后台任务。

  - 工程上：engine 内等待队列只需足以填满 batch，相关参数（batch size、cap、timeout）联合调优；用队列深度而不是固定峰值扩展资源，可显著节省
  GPU（文中 43% 少 H100）。对 Agent 会话类交互流量需谨慎，论文未覆盖该场景。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**  
LLM 异步推理中，需求（日周期、事件、backfill）和容量（共享池拥塞、弹性缩容、fleet resize）都在变化，且生成输出长度未知，固定发送速率会快速过时；引擎内排队会让请求超时后仍执行，造成 goodput 崩塌。生产环境一天超 3 亿请求，需要不依赖容量重调的调度。

**方法关键点**  
- CAP：在饱和资源处做 fail-fast 准入检查，返回 HTTP 429。内部模型服务器在 vLLM 上方设置 per-replica cap（如 max_num_seqs=128，cap=140），provider 天然返回 429，gateway per-caller 配额也能作为 CAP。  
- TRACK：每 15s 一个 leader 根据队列的 refusal share 调节发送速率，MIMD 控制：拒绝占比 ≤2% 时上升 3%，超过 50% 乘 0.85，超过 65% 乘 0.5；只用 429 信号，忽略 timeout 和其他错误。  
- 等待队列：FOQS durable priority queue 放在执行引擎外，拒绝请求返回 worker 本地 ready queue 头部，不 bounce 不重 stage；lease 到期才回 FOQS。  
- 工程化：单 leader + consistent hash ring + hysteresis，restart 时 freeze rate，quiet hours 防止爬升，运行时所有参数可调。  

**关键实验**  
- 无 CAP replay：引擎忙但 goodput 跌到 0 且不恢复；有 CAP 时稳定。  
- 稳定 ceiling replay：TRACK 每 host 108.5 req/s vs 固定 100% 速率 107.0 vs 120% 速率 109.5，拒绝占比分别 3.8%、1.1%、15.5%；容量减半后 TRACK 自动下降，恢复后约 5 分钟回到满容量。  
- 生产 A/B：classifier 流量用 39 张 H100 对 precursor 68 张（少 43%）；zero-shot 等量 GPU 下排空共享 backlogs 中位快 3 小时，GPU 服务请求多 9%；reserved capacity 平均利用率 95.8%，backlogged 周 99.1%。

**最值得记住的一句话**  
Cap the engine queue, follow refusals, keep dispatch stateful, and size the fleet for freshness.
