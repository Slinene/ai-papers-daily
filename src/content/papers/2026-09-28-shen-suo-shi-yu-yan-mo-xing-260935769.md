---
title: Telescopic Language Models
title_zh: 伸缩式语言模型
authors:
- Zhilin Guo
- Boqiao Zhang
- Hakan Aktas
- Kyle Fogarty
- Nursena Koprucu Aslan
- Wenzhao Li
- Canberk Baykal
- Albert Miao
- Siyu Hong
- Yixiao Liu
affiliations:
- University of Cambridge
- University of British Columbia
- Google
arxiv_id: '2609.35769'
url: https://arxiv.org/abs/2609.35769
pdf_url: https://arxiv.org/pdf/2609.35769
published: '2026-09-28'
collected: '2026-09-29'
category: Training
direction: 弹性 LLM 训练 · 随机前缀监督
tags:
- telescopic language models
- elastic inference
- stochastic prefix supervision
- nested capacity
- Matryoshka
one_liner: 单次训练让嵌套级联每个深度前缀均为有效语言模型，AULB降43–44%
practical_value: '- 业务需要为不同延迟/成本部署多档 LLM 或小模型时，可尝试嵌套宽度递增架构 + 随机前缀全锚点训练：单次训练得到一个可任意深度截断的模型，替代多份
  artifact，降低 GPU 成本（论文中比 vanilla 三模型方案低 1.7 倍）。

  - 若只有少数固定 latency 档位，把 prefix sampler 集中在目标出口深度，可在单次训练的同时获得接近独立子模型的出口质量；若需要弹性降级或流量自适应，用
  uniform sampler 换取全深度连续覆盖，两者是采样分布上的训练期选择。

  - 中间深度崩溃的主因之一是 readout head 未校准而非主干能力不足；若不重训，可先对崩溃前缀做 cheap head-only fine-tune，虽仍落后全训练约
  6 倍，但能恢复部分可用性，适合快速止血。

  - 该方法在 200M 代理规模验证，迁移到 7B+ 的推荐/Agent 在线服务需自行验证；但每步仅两次 forward-backward、推理无额外开销，工程上易试错。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**：一个部署的语言模型通常要覆盖多种算力预算（端上助手到数据中心），现状是每个预算单独训练或事后压缩，成本倍增。嵌套容量级联（MLMS）一次生成多个子模型，但只监督少数固定出口，未训练深度的 PPL 崩溃到 10²–10⁵，连续弹性无法实现。

**方法关键点**：
- 保持 MLMS 嵌套架构不变（宽度递增的子模型级联，每个前缀自带 RMSNorm 和 LM head），只改训练目标。
- 每步随机采样一个前缀深度 k~π，对该前缀计算 next-token CE loss，同时计算全模型的 CE loss，二者加权求和（λ=γ=1），每步恰好两次 forward-backward。
- 默认 π 为 uniform，覆盖所有深度；推理时按任意深度截断直接使用，无额外结构。
- 采样分布 π 是训练期 dial：集中到固定出口换取出口质量，扩散到全深度换取连续覆盖。

**关键实验**：在 200M 代理套件、20B FineWeb-Edu tokens、相同数据流下对比 MLMS 四个配置与独立训练的 50M/100M/200M vanilla twins。Uniform TLM 在所有 20 个 layer prefix 有效，PPL 从 k=1 的 81 平滑下降到 k=20 的 15；AULB 降至 3.28，比 MLMS 的 5.73–5.90 下降 43–44%；满容量 200M PPL 14.99 与 MLMS 14.98 持平，训练成本 131 GPU-h，比无蒸馏 MLMS 低约 12%，比 vanilla 三模型方案低 1.7 倍。LODA 精度 38.9 vs 21.8。固定出口 MLMS 在 50M/100M 出口仍略优，但 TLM 提供两者之间的连续可用点。

**最值得记住的一句话**：决定模型弹性的是训练目标而非嵌套结构本身；随机前缀监督 + 全锚点可以把同一个级联变成每个深度都有效的模型。
