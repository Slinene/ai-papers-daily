---
title: Token-Operations-Oriented Inference Optimization Techniques for Large Models
title_zh: 面向 Token 操作的大模型推理优化技术
authors:
- Shiguo Lian
- Kai Wang
- Zhaoxiang Liu
- Wen Liu
- Minjie Hua
- Yutong Liu
- Jiangze Yan
- Xin Wang
- Cong Wang
- Yilin Zhang
affiliations:
- China Unicom (Data Intelligence / Data Science and AI Research Institute)
- Tsinghua University
- Peking University
- Fudan University
- Zhejiang Lab
arxiv_id: '2606.20295'
url: https://arxiv.org/abs/2606.20295
pdf_url: https://arxiv.org/pdf/2606.20295
published: '2026-06-18'
collected: '2026-06-19'
category: LLM
direction: 大模型推理成本与效率优化
tags:
- Inference Optimization
- Token Operations
- KV Cache
- Speculative Decoding
- Model Quantization
- Model Routing
one_liner: 首次提出四层 token 推理优化架构，系统梳理降本增效的产业技术路径
practical_value: '- **模型路由与多模型融合**：推荐系统常需多模型（精排、粗排、RAG等）协同，可借鉴论文的模型路由与融合调度策略，减少总推理调用量，降低
  token 成本。

  - **KV Cache 命中与跨阶段复用**：对话式推荐、Agent 记忆、长会话推荐中，跨请求的 KV Cache 缓存与预填充策略可直接降低首 token
  延迟，提升交互体验。

  - **量化与投机解码落地**：对部署在 CPU/端侧的 LLM4Rec 模型，采用 INT4/INT8 量化、投机解码等典型技术可将推理成本压缩 3-5 倍，适合高并发推荐场景。

  - **动态批处理与负载均衡**：在推荐模型在线服务中，动态 batching 与跨节点的负载均衡可平滑流量峰值，保障推荐链路稳定性，尤其适合大促峰值保障。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：大模型服务从“可调用”向“可运营”演进，面临推理成本高、吞吐低、稳定性不足的挑战。该文以 token 操作为中心，提出一套覆盖全链路的推理优化技术架构。

**方法**：首次给出四层技术框架：① **多模型融合层**，含模型路由与协同推理，减少冗余计算；② **模型优化层**，包括量化、蒸馏、线性注意力、MoE 等轻量化与高效结构；③ **计算-模型融合层**，聚焦推理引擎优化，如算子融合、动态批处理、KVCache 管理及投机解码；④ **计算-网络-模型融合层**，涉及分布式 KVCache、负载均衡与跨节点调度，保障大规模集群下的供给稳定。论文系统性梳理各层的技术原理与产业现状，并分析在真实业务中的降本增效价值。

**结果**：该架构为“减少 token 生产成本、提升 token 服务效率、保障 token 供应稳定”提供了可行技术路径，推动大模型商业落地的可运营性。
