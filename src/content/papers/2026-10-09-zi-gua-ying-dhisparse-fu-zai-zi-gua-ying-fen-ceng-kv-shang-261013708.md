---
title: 'Adaptive DHiSparse: Speculative Decoding over a Load-Adaptive KV Hierarchy'
title_zh: 自适应 DHiSparse：负载自适应分层 KV 上的投机解码
authors:
- Naji Alazhar
- Wassel Alazhar
affiliations:
- Umans AI
arxiv_id: '2610.13708'
url: https://arxiv.org/abs/2610.13708
pdf_url: https://arxiv.org/pdf/2610.13708
published: '2026-10-09'
collected: '2026-10-13'
category: LLM
direction: 长上下文 LLM 推理 · 分层 KV 投机
tags:
- Speculative Decoding
- KV Cache
- Long-context Serving
- Hierarchical Sparse Attention
- Load-Adaptive Residency
- DFlash2-DSpark
one_liner: 把 DSpark/DFlash2 投机解码接入分层稀疏 KV，并用可回收 optional residency 随负载调整 GPU 驻留，显著提升长上下文吞吐
practical_value: '- 长上下文 Agent / LLM4Rec 场景：不要全量 resident 或全量 offload，用「固定 hot cache
  + 可回收 optional history」；低负载多驻留 GPU，高负载按整请求回收，host 永远有备份，能同时保吞吐和并发。

  - 接入投机解码时，draft KV 用窗口 ring 限制大小，按 `W + Kmax` 加 page 对齐分配；验证阶段多个 query 的 top-k 选择做
  union 去重，同一 miss row 只 host copy 一次，本文中可减少约 29% fetch。

  - verification staging 按 live layer group 复用，而不是给每层分配；GLM 78 个 payload 层只留 4 个 arena，staging
  从 24.0 GiB 降到 1.23 GiB，这对多 query 验证和长上下文服务非常关键。

  - 调度上可用式(13)判断投机是否划算：当 speculative 与 non-speculative 的 active session 比低于 TPOT 改善比时，投机不再增加吞吐，应动态收窄
  block 或关闭投机，避免高负载下白白等待 slot。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**：长上下文 LLM 服务通常先耗尽 KV cache 内存；HiSparse 的分层稀疏 KV 没有草稿模型投机解码路径，且固定 cache 预算不能随负载伸缩，低负载浪费 HBM，高负载又卡并发。

**方法关键点**：
- 负载自适应 residency：固定 hot cache + tail 保护 working set，immutable history 用可回收 optional pages；低负载多驻留 GPU，高负载整请求回收，host 永远有备份。
- 投机验证复用：DSpark/DFlash2 的 proposal/acceptance 不变；对每个 request/source，将一轮 K 个 query 的 top-k 选择做 union 去重，同一缺失 row 只 host copy 一次，各 query 保持自己的有序 selection 和 causal mask；overflow 行放 staging。
- 有界 speculative state：draft KV 只用窗口 ring，大小由可见窗口 W + 当前 block Kmax 加 page 对齐；verification staging 按 live layer group 复用，GLM 78 层只需 4 个 arena。

**关键结果**：GLM-5.3 100K context、C128 时 Adaptive DHiSparse + DFlash2 达 793 tok/s/decode GPU，是 HiSparse 1.45×、非投机 adaptive 1.27×；TTFT 降 2.1×。相同 latency bound 下，可支撑 4× concurrency、2.3–3.7× output。DeepSeek-V4.1-Flash 500K、C512 + DSpark 达 resident+DSpark 的 1.85× output。Load step 中 optional residency 把 host fetch 从 14.2% 降到 1.4%，压力下释放内存。

最值得记住：**把内存分配跟负载和验证执行绑定，而不是固定 budget，是长上下文投机服务吞吐的关键。**
