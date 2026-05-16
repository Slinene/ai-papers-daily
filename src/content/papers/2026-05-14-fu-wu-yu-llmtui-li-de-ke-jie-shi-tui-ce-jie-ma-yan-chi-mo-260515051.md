---
title: An Interpretable Latency Model for Speculative Decoding in LLM Serving
title_zh: 服务于LLM推理的可解释推测解码延迟模型
authors:
- Linghao Kong
- Megan Flynn
- Michael Peng
- Nir Shavit
- Mark Kurtz
- Alexandre Marques
affiliations:
- MIT
- Red Hat AI
arxiv_id: '2605.15051'
url: https://arxiv.org/abs/2605.15051
pdf_url: https://arxiv.org/pdf/2605.15051
published: '2026-05-14'
collected: '2026-05-16'
category: LLM
tags:
- LLM
- SpeculativeDecoding
- LatencyModel
- Little'sLaw
- MoE
- Serving
one_liner: 利用Little's Law构建简单延迟模型，解释负载变化时推测解码的加速比如何随接受率和草案长度演化
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**  
推测解码（Speculative Decoding, SD）通过小模型草拟多token再经大模型并行验证来加速LLM推理，但现有评估多在单请求或固定batch下进行。生产环境中请求率波动，有效batch size由调度器动态决定，SD的实际收益常常随负载增加而衰减甚至反转。需要一个可解释的模型描述SD在真实服务中的延迟行为，为系统配置提供指导。

**方法关键点**  
- 使用Little’s Law将不可观测的有效批大小B与请求率RPS、端到端延迟L关联：B = RPS × L。  
- 将服务延迟分解为负载无关与负载相关两部分（C1 + B×C2），代入B后得到延迟的闭合形式：L = C1 / (1 - RPS × C2)，该公式在预饱和区精确描述了非推测和推测解码的延迟。  
- 将SD拆分为prefill、verify和draft三个阶段，按接受率α、草案长度k计算平均接受长度E，得到有效成本C1,eff、C2,eff。模型显式揭示了SD降低固定开销（C1,R < 1）但往往增加负载相关成本（C2,R > 1）的趋势。  
- 导出加速比公式：Speedup = (1 / C1,R) × (1 + (1 - C2,R) × r/(1-r))，其中r = RPS × C2,D，清晰分离零负载加速比与负载依赖项。  
- 对MoE模型引入专家覆盖率因子ϕ(T)，刻画稀疏激活在低并发下带来的额外收益及其随负载增加的消退，扩展了统一模型。

**关键实验结果**  
- 在vLLM + GuideLLM栈上对Llama-3.1-8B/70B、gpt-oss-20b和Qwen3系列模型进行请求率扫描，覆盖多种prefill/decode长度、α=50-100%、k=1-10。  
- 归一化延迟曲线完美坍缩至函数 y = 1/(1-x)，验证模型普遍性。  
- 按SD配置拟合的有效成本C1,eff、C2,eff与实际逐配置拟合的C1、C2高度一致，拟合精度R²接近1。  
- MoE模型低负载下模型R²从0.83-0.90提升至0.98-0.99，说明稀疏覆盖修正有效。  
- 系数缩放实验表明c1,v、c1,d、c2,v、c2,d与模型参数量成近似线性关系，且对序列长度具有可预测的依赖性。

**核心结论**  
推测解码的加速增益通常只在低负载下显著，高负载下因负载相关成本升高而快速衰减，除非接受率极高。草案长度在低负载宜大以摊薄固定成本，而在高负载宜小以减轻负载相关成本，系统部署时应根据实时α和RPS动态选择最优k。
