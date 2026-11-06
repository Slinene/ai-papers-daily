---
title: The SIMPLE Law for Energy Cost of LLM Inference
title_zh: LLM 推理能耗的 SIMPLE 定律
authors:
- Hiari Pizzini Cavagna
- Andrea Proia
- Daniele Cesarini
- Zeynep Kiziltan
- Andrea Bartolini
affiliations:
- University of Bologna
- CINECA
arxiv_id: '2611.03330'
url: https://arxiv.org/abs/2611.03330
pdf_url: https://arxiv.org/pdf/2611.03330
published: '2026-11-01'
collected: '2026-11-06'
category: LLM
direction: LLM 推理能耗解析建模
tags:
- LLM inference
- energy modeling
- KV cache
- GQA
- agentic serving
- token economics
one_liner: 四参数 SIMPLE 定律建模 LLM 推理能耗，跨 13 模型 R²=0.969、MAPE 11.97%，无需校准。
practical_value: '- **能耗/成本预估与容量规划**：可直接用 SIMPLE 的四参数解析式，按 hidden dim、层数、GQA 分组等超参数估算任意
  dense LLM 在 H100 类硬件上的推理能耗与 token 成本，无需逐模型校准；适合在电商/Agent 场景中评估不同 LLM 的部署成本和 ROI。

  - **GQA 架构选型**：激进 GQA KV 分组可带来最高 3× per-token 能耗下降；在生成式推荐、实时对话 Agent 等 token 量大的在线服务中，优先选
  GQA 模型或调大 KV group 数，以降低长序列 KV-cache 成本。

  - **Agentic/RAG 长上下文成本控制**：Agentic 请求能耗为非 agentic 的 13×，且 prefix caching 只能省 prefill（-93%），KV-cache
  解码成本不降；实践中应限制工具调用/历史对话长度，或引入状态压缩/稀疏注意力，避免多轮上下文线性推高能耗。

  - **Reasoning budget 设置**：Intelligence per Joule 有峰值，增加推理 token 预算后期能量增速快于精度；可以在业务中设置
  reasoning token 上限或早停策略，用能耗-效果帕累托寻找最优预算，而不是一味追求更长推理。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：LLM 按 token 计费，但 token 能耗不同：每个 token 进入 KV-cache 会提升后续 token 成本，序列能耗非线性增长；现有 SOTA 能耗模型是拟合式，需逐 LLM 校准，缺少由架构超参数显式表达的解析定律。

**方法**：针对 MHA 与 GQA，从 hidden dimension、层数、head 数、KV group 等超参数推导计算与内存访问复杂度的闭式表达式，得到四参数 SIMPLE 定律，将推理能耗拆为 prefill 与 decode；decode 再拆为 KV-cache 访问成本与 next-token 计算成本。在 6 个家族 13 个 dense LLM（OPT、LLaMA、Gemma、Falcon、Qwen2、Granite）的 H100 实测轨迹上验证。

**关键结果**：SIMPLE 无需逐模型拟合，达到 R²=0.969、MAPE=11.97%，误差为 SOTA 的 1/3.1–1/3.5。能耗规律：prefill 能耗随 hidden dimension 二次增长；更强 GQA KV 分组使 per-token 能耗最多比 MHA 降 3×；增加 reasoning token budget 使输出长度越过解析能量最小点，能量超线性增长，Intelligence per Joule 在中间预算达峰、4×预算区间内最多降 3.14×；Agentic serving 单请求能耗为非 agentic 的 13.0×，prefix caching 虽减少 93% prefill 成本，但 KV-cache 项不受影响，缓存 agentic 请求仍贵 4.8×。
