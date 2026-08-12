---
title: Scheduling Mixed RL Rollouts Beyond Prefix Locality
title_zh: 面向混合 RL 推理负载的 KV 缓存感知准入调度
authors:
- Zetao Hong
- Song Yuan
- Yuanhao Ding
- Yibo Zhu
- Daxin Jiang
- Zhibin Wang
- Chen Tian
affiliations:
- Nanjing University
- StepFun
arxiv_id: '2608.11152'
url: https://arxiv.org/abs/2608.11152
pdf_url: https://arxiv.org/pdf/2608.11152
published: '2026-08-11'
collected: '2026-08-12'
category: LLM
direction: LLM RL 混合负载推理调度优化
tags:
- KV cache
- admission control
- mixed rollout
- LLM serving
- RL post-training
- routing
one_liner: 路由层依据工作负载类型与 KV block-time 需求动态控制 session 准入，避免 KV 缓存击穿，吞吐提升超 50%。
practical_value: '- 在需要大规模 LLM 推理的业务（如商品问答、推荐理由生成、多轮 Agent 导购）中，可借鉴 MISA-T 的**按工作负载类型分配
  KV 保护额度**：为短输入长输出的 RLVR 型、均衡 RLHF 型、长上下文多轮 Agent 型请求分别设定 session 准入上限，防止某个类型挤占缓存导致全局命中率崩塌。

  - **KV block-time 估算方法**可直接复用：用 session 平均块数 × 类级驻留时间而非单纯 kv 块数衡量资源需求，尤其适用于含工具调用、等待外部
  API 的 Agent 场景，能更准确地预留缓存空间。

  - **自适应 overload 收缩**机制可替代静态并发数调优：根据近端缓存命中率下降与等待队列长度自动下调准入上限，避免手动扫参；在模型、序列长度或混合比例变化时无需重新调节。

  - 实验表明 **KV offload 与路由层准入控制完全兼容**（开启 CPU 备份后 GPU KV 利用率更高且吞吐提升 35.6%），对于采用分级缓存（HBM/CPU）的部署可直接叠加，无需改动调度逻辑。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

## 动机
现代 LLM 强化学习后训练中，推理层需要同时服务多种异构的 rollout 负载：RLVR（短提示/长解码）、RLHF（中等长度）和 Agent 多轮交互（长前缀跨工具调用留存）。仅靠 prefix-aware 路由无法控制不同 workload 对 KV-cache 的争抢，高并发下会产生缓存击穿→冷预填充→更长的排队→进一步挤占缓存的恶性循环，导致吞吐大幅下降、前缀命中率跌至 5% 以下。

## 方法关键点
- **自适应 session 准入**：从实时 KV 块需求和过载压力中推导全局 session 上限，当命中率下降或队列堆积时自动收窄，保护已驻留 session，消除静态并发数反复调优。
- **工作负载感知的 KV 容量分配**：按 RLVR、RLHF、Agent 三类负载的即时需求数量和 KV footprint（块数）划分保护性 KV 配额，再转换为类级 session 上限，在全局 cap 内设置软配额，避免单一负载挤占全部容量。
- **驻留时间加权的 KV 记账**：将各类负载的 KV 需求定义为 `N_b × k_bar_b × T_bar_b`（块数 × 驻留时间），让配额与“块‑时间”积成比例，准确反映多轮 Agent 在工具调用期间持续占用缓存的特点。
- **轻量实现**：仅需请求标签、运行时指标和 session 缓存快照即可在现有推理引擎（如 vLLM）的路由层上叠加，不改动模型执行或 KV 管理器。

## 关键结果
- 在 Step3.7 (196B MoE) 和 Qwen3.6-35B-A3B 的 rollout-only 实验中，MISA-T 相比 sweep 调优的 vLLM Router 分别提升 **53.3%** 和 **43.6%** 的 rollout 吞吐，前缀命中率保持在 **97.8%** / **95.3%**。
- 50 轮端到端 RL 训练中，MISA-T 使迭代时间降低 **22.8%**，吞吐提升 **35.6%**，前缀命中率从 74.5% 提高到 **96.2%**，且消耗的 workload 混合比例更接近训练方目标（TV 距离从 4.14 降为 2.71 p.p.）。
- 消融表明：仅类不可知的 session 准入比单纯路由提升 ~20%；加上 workload-aware 配额再提升 ~10%；引入驻留时间加权又获得额外 ~10‑24% 的提升。

**最值得记住的结论**：路由层按各类负载的 KV block-time 产品分配准入额度，是阻止混合 RL rollout 缓存击穿与资源挤占的关键，且可与 KV offload 无缝叠加。
