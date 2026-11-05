---
title: Generative Retrieval under Real-Time Supply Constraints in Local Commerce
title_zh: 实时供给约束下的本地商业生成式检索
authors:
- Shaopeng Liang
- Biao Zhang
- Hongzhen Ye
- Zeyang Hou
- Ma Jiang
- Jintao Tu
- yunxi. hz
- Zhijia Fang
- Jianqiang Cao
- Junxue Rao
affiliations:
- Rajax Network Technology (Taobao Shangou of Alibaba)
arxiv_id: '2611.06323'
url: https://arxiv.org/abs/2611.06323
pdf_url: https://arxiv.org/pdf/2611.06323
published: '2026-11-04'
collected: '2026-11-05'
category: GenRec
direction: 生成式检索 · 实时供给约束解码
tags:
- Generative Retrieval
- Constrained Decoding
- Semantic ID
- Local Commerce
- Beam Search
one_liner: 将请求级可服务 SID 编译为共享 CSR 前缀索引，并在 beam search 中保留原始模型分数与父状态对齐，以抑制供给幻觉
practical_value: '- 在本地电商/外卖的生成式商户检索中，不要只做 catalog-valid trie 约束，应支持 request-time
  eligible SID set 编译成前缀索引；位置、天气、交通造成的 supply hallucination 会占用大量 beam，后过滤无法恢复已浪费的搜索预算。

  - 工程实现可借鉴：用后台 CPU 任务排序并构建 CSR 索引，与模型 prefill 重叠；将不可变 index 上传后由所有 beams 共享，避免每步传输
  dense mask；对 L=3 的短 SID，上传和 host-device 同步成本很关键，需重点优化。

  - 评分实现要保存 full-vocab logsumexp，用原始模型条件概率做跨 parent Top-K 选择；不要 mask 后 renormalize，否则不同
  parent 可用 token 数不同会改变排序。

  - 评估时不能只看服务端 RT，要关注有用实体数、零结果率、客户端端到端延迟；30k 条目的请求体可能达数百 KB，需要紧凑编码，同时注意有效 beam count
  传播，避免临时收缩被误当作最终输出宽度。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
本地零售/外卖的生成式检索必须同时保证相关性和可服务性。位置、天气、交通会让同一商户 SID 在不同请求下从可用变不可用；模型容易生成 catalog 有效但 supply 不可用的“供给幻觉”，后过滤会浪费 beam 容量和推理预算，因为已经探索过的高分候选不可用就无法恢复。因此需要把请求时实际可服务的供给集直接约束到 decoding 搜索前沿。

## 方法关键点
- 请求级供应快照：上游供应服务物化 eligible SID set，生成 L=3 商户 SID。
- 异步编译：CPU worker 将 eligible SID 排序并构建 CSR 前缀索引，与模型 prefill 重叠；首次采样前把 index 上传 GPU，所有 beams 共享索引，但各自维护约束状态。
- 约束 beam search：每步 mask 非法 next token；评分用原始模型 logits：score = parent_score + z - logsumexp(full vocab)，而非 mask 后 softmax 再归一化，避免不同 parent 可用 token 数不同导致排序翻转。
- 状态传播：约束状态随 beam parent 对齐推进；有效 beam count 随 frontier 动态变化，避免把临时 beam 收缩误当作最终输出数。

## 关键结果
- 在 daily catalog 约束的 matched-beam case 中（Laoxiangji/Jintie，beam [50,150,300]），商户过滤数从 170/299 降至 29/299；供给幻觉 120→0，但 distance filtering 26 不变，证明需要请求级约束。
- C++ CSR 构建约 3ms 排序 + 1ms 构建；30k 条目下服务端 RT 仅 +0.6ms，但客户端 mean 增加 19.1ms，揭示端到端成本不能只看 engine。
- 捕获请求回放中 26,419 条目的 Jintie 场景输出 231 beams，pipeline 可运行；但尚未证明匹配质量下的净计算节省。

## 最值得记住的一句话
约束解码不仅是 mask，还必须保留原始模型 logits 和父状态；评估收益要用 useful yield 与端到端成本，而不是只看内核或服务端 RT。
