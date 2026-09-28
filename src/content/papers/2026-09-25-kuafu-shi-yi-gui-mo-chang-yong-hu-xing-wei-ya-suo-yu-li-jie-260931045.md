---
title: 'KuaFu: Compressing Long User Behavior into Understanding at Billion Scale'
title_zh: KuaFu：十亿规模长用户行为压缩与理解的统一层
authors:
- Jiahao Hui
- Lin Zhu
- Yishen Hu
- Jingdong Shu
- Zetai Jiang
- Xining Ran
- Ben Tan
- Yeshou Cai
- Gong Chen
- Haijie Gu
affiliations:
- Tencent Inc., Shenzhen, China
arxiv_id: '2609.31045'
url: https://arxiv.org/abs/2609.31045
pdf_url: https://arxiv.org/pdf/2609.31045
published: '2026-09-25'
collected: '2026-09-28'
category: RecSys
direction: 用户行为压缩 · LLM 理解
tags:
- user modeling
- context compression
- hallucination
- LLM4Rec
- industrial deployment
- RLHF
one_liner: 以单行为 item 为最小压缩单元，双轴投影将每条行为压到 2–4 token，四阶段训练抑制幻觉，部署后 GMV 提升 1.37%
practical_value: '- 可迁移点 1：采用 item 级压缩而非 sequence 级压缩，使 embedding 只依赖 item 本身，可离线缓存、跨用户/任务复用；缓存随
  item inventory 增长而非 #users×#tasks，极大降低每周十亿用户画像刷新成本。在电商/广告中，商品、内容、广告素材均可预先压缩存储，在线只拼接。

  - 可迁移点 2：双轴投影（token 轴 8→2，width 轴 2560→128，约10×/20×压缩）配合残差与 Down/Up 低秩投影，能把单 item
  缓存从10KB降到0.5KB；适合长行为序列 KV cache 或 prompt 侧压缩，注意压缩宽度对细节丢失的影响，需按 task 选择 ratio。

  - 可迁移点 3：四阶段课程训练：重建→压缩 QA→压缩+生成协同→幻觉感知 RL。尤其基于长度的五桶课程（1,1–3,1–200,1–500,1–1200）是收敛必要条件；直接混合长度
  loss 卡在2.27。可借鉴到长序列 LLM 训练。

  - 可迁移点 4：对生成式用户画像/推荐文案，用分组 DAPO RL 加按危害加权的四类幻觉惩罚（fabrication 0.45、date misattribution
  0.24、logic 0.24、missed detection 0.07）并单独给 completeness bonus，可显著降低 fabrication（33.5→4.5）且不诱发拒答；业务上可用较强
  judge 做分层中间评测，缩短反馈闭环。'
score: 9
source: arxiv-cs.CL
depth: full_pdf
---

**动机**：工业界长用户行为序列直接给 LLM 有成本墙：过滤后单任务序列仍可超过一千个行为 item，序列化成 prompt 达数万 token；十亿用户每周刷新画像需 100K QPM，固定 GPU 预算下必须压缩。但截断或粗粒度压缩会引发四类幻觉——fabrication、omission、date misattribution、broken logic，且缺乏中间阶段评测，只能看到下游指标缓慢劣化。

**方法关键点**：
- 单 item 压缩范式：每个行为 item 独立编码成 memory embedding，只依赖 item 本身，可缓存、跨用户复用、增量追加。
- 双轴投影：token 轴 m→k（8→2），width 轴 d→d'（2560→128），加 pooled residual；约10× token、20× width 压缩，单 item 缓存从 10KB 降到 0.5KB。
- 四阶段训练：重建预训练（长度课程 1/1–3/1–200/1–500/1–1200）→ 压缩 QA post-training → 压缩生成 co-training → 幻觉感知 RL（DAPO + 分类型加权惩罚 + completeness bonus）。
- 分层中间评测：直接对压缩表征打分，缩短反馈闭环。

**关键实验**：
- 生产四任务（内容/电商兴趣、行业/职业、人生阶段）五项指标不弱于无压缩单任务模型，人生阶段 +2.0 pp。
- 相比外部 compressor 基线，in-house 验证集 overall 63.0，领先最强基线 20.6 pp。
- GPU 吞吐 +37%～350%，节省 190 GPUs。
- MRQA 上几乎全面优于基线，out-of-domain 最高 +17.7 EM；RecBench 上 4B 模型超过 8B 模型 1.90 分。
- 线上部署十个月，GMV 提升 1.37%（95% CI [0.71%, 2.03%]）。

**最值得记住的一句话**：压缩的最小单位应当是单个行为 item，而不是整段序列；缓存随 item inventory 增长而非 #users×#tasks，这是十亿规模周级刷新的经济性来源。
