---
title: Compiling Autoregressive LLM Control into Policy-Exact Parallel Inference for
  Hierarchical RAG
title_zh: 将自回归LLM控制编译为策略精确的并行推理用于层级RAG
authors:
- Zehao Lin
- Qianfeng Shen
- Xixuan Hao
- Shaobo Cui
- Chunyu Li
- Kai Chen
- Bo Tang
- Zhenjun Wang
- Jin Yan
- Zhiyu Li
affiliations:
- MemTensor (Shanghai) Technology Co., Ltd.
- China Haisum Engineering Co., Ltd.
- The Hong Kong University of Science and Technology (Guangzhou)
- Shanghai Jiao Tong University
arxiv_id: '2610.30664'
url: https://arxiv.org/abs/2610.30664
pdf_url: https://arxiv.org/pdf/2610.30664
published: '2026-10-22'
collected: '2026-10-23'
category: RAG
direction: 层级RAG控制并行编译
tags:
- Hierarchical RAG
- constrained decoding
- tree attention
- parallel inference
- LLM control
- policy-exact
one_liner: 把层级RAG受限解码编译为一次prefill+树因果probe，零输出token复制串行策略
practical_value: '- 对电商/Agent里任何 bounded-horizon constrained LLM controller（选品、路由、工具/query推荐、多步筛选），可把动作空间编译成
  action-prefix tree，用 root prefill + tree-causal probe 一次前向求出所有可达状态；零解码 token、深度-2，直接去掉
  JSON 协议失败和串行延迟。

  - 若业务上「顺序选择有历史依赖」但最终只取集合，可用 probe 计算 order-marginalized posterior，并用 branch-and-bound
  MAP certificate 得到精确集合选择；避免把顺序当成集合决策的 serialization artifact。

  - 上线前用 interaction mass Iseq = KL(P_AR || P_U) 诊断历史依赖强度；若 Iseq 大，说明 unary logit
  shortcut 不能替代串行策略，可以用同一 probe 低成本判断何时需要保留自回归条件。

  - 注意工程限制：bf16 下 near-tie 翻转与跨硬件/跨后端差异同量级；需要强 parity 就换 fp32 或对低 margin round 回退串行；horizon>3
  时 probe 宽度阶乘增长，建议改成 staged/chunked 混合执行。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

动机：层级 RAG/Agent 常把 LLM 当结构化控制器，但执行层仍靠串行受限解码。自由 JSON 易有协议失败；unary logit shortcut 丢失历史依赖；grammar-constrained decoding 必须每个 action token 一次 dependent forward，关键路径长。

方法关键点：
- 将受限动作语法编译成 action-prefix tree：root prefill 解析第一个动作并缓存 KV，随后一次 tree-causal probe 拼接所有可达前缀。
- Probe 使用 block-causal mask 和与串行一致的 position ids，每个状态只看自己的祖先；最后位置 logits 在精确算术下等于串行控制器 logits（Lemma 1），greedy 链可算术恢复。
- 输出 token 为 0，critical path 从 n+m_syn 降为 2；代价是并行宽度变为 Θ(N(k,n))。
- 额外获得 order-marginalized posterior 和 branch-and-bound MAP certificate；并用 KL(P_AR || P_U) 作为 sequential interaction mass，bound unary shortcut 的期望效用损失。

关键实验：QASPER 五个 splits，Qwen2.5-7B/3B，MetaX C500 / H800。编译与串行 greedy 动作序列一致率 84–89%，fp32 replay 提升到 89/90；控制延迟比串行语法解码降 35–47%，比理想化 chunked engine 降 6–7%；所有分歧都发生在 bf16 near-tie 区间。n=4 时 probe 宽度墙导致短 prompt 下不再占优；错误嵌套压力测试中编译控制保持零协议失败。

最值得记住的一句话：bounded-horizon constrained LLM controller 不一定需要 decoding，它可以被 compiling——串行深度换成并行宽度，策略在精确算术下等价。
