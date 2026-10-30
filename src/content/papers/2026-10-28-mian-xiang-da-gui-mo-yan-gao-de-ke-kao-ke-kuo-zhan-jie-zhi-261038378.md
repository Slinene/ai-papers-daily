---
title: Towards Reliable, Scalable, and Value-Aligned Generative Recommendation for
  Large-Scale Advertising
title_zh: 面向大规模广告的可靠可扩展价值对齐生成式推荐系统
authors:
- Yatong Xiao
- Yibo Sheng
- Lixiang Wang
- Mingjie Sun
- Yunhao Sha
- Pengfei Zhang
- Shengyu Wang
- Peng Wang
- Wenjin Wu
- Peng Jiang
affiliations:
- Kuaishou Technology
arxiv_id: '2610.38378'
url: https://arxiv.org/abs/2610.38378
pdf_url: https://arxiv.org/pdf/2610.38378
published: '2026-10-28'
collected: '2026-10-30'
category: GenRec
direction: 生成式推荐 · Semantic ID · 价值对齐
tags:
- Generative Recommendation
- Semantic ID
- Value Alignment
- Model Scaling
- Advertising
- Beam Search
one_liner: 通过多路径SID、五维容量扩展和统一价值引导生成与判别，快手广告生成式推荐实现3.07%收入提升
practical_value: '- **Multi-Path SID**：对 embedding 聚类边界模糊的物品保留 top-m 条第一层路径，避免单路径
  SID 被 beam search 剪枝后完全不可达。电商/广告场景中物品语义边界普遍模糊，可低成本提升召回覆盖，且不增加解码深度。

  - **PCGM 词汇记忆扩展**：用 prefix 条件门控记忆表代替稠密 FFN 门控，按前缀长度检索不同粒度的 SID 嵌入，垂直方向层独立，水平方向支持
  1/2/3-gram。在不增加每次解码稠密计算的前提下大幅提升参数容量，适合在线延迟敏感系统。

  - **Diagonal Hyper-Connections**：多流残差 + 对角门控，每个子层只计算一次注意力/FFN，却可以扩展多条信息通路。相比直接加宽或加深
  Transformer，在相同吞吐下获得更好表示能力，可复用于推荐模型的序列编码器。

  - **Prefix-level value + PV-BeamSearch**：将序列级奖励自底向上聚合为前缀价值，训练轻量级 per-level 价值头，推理时用
  RRF 融合生成概率排名和价值排名，从 level≥2 开始干预。有效解决高价值 prefix 被过早剪枝的问题，且无需外部重排模型。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：生成式推荐将物品检索转化为 SID 自回归生成，快手 GR4AD 已在 4 亿用户广告系统部署，但生产暴露三大瓶颈：确定性 SID 分配对语义边界敏感，大量广告位于第一层聚类边界，单路径分配导致被剪枝后不可达；常规骨干缩放收益递减且服务 QPS 断崖式下降；序列级价值优化无法对中间 SID 决策做细粒度信用分配，生成概率与商业价值（eCPM）严重错位，基础模型 HitRate@10 仅 0.021。

**方法关键点**：
- **Multi-Path SID**：保留 top-m 个第一层聚类中心，每个中心独立进行后续残差量化，一条广告获得 m 条长度 L 的检索路径，不增加解码深度；训练采用块状多目标，推理按广告去重。
- **五维容量扩展**：避开朴素加深加宽，沿输入信号丰富与 SwiGLU 编码器、PCGM 前缀条件门控记忆（层特定 SID 记忆表 + prefix n-gram，多项式哈希，门控注入 FFN）、多流残差对角线超连接（4 路流，read-compute-write，每个子层只算一次）、SARP 语义锚定推理预填充（在 BOS 和 s1 间插入可学习推理 token，粗粒度原型监督）五个互补维度。
- **UniVGD 统一价值对齐**：PV-RSPO 自底向上将叶子奖励聚合为前缀价值，训练逐层轻量价值头；PV-BeamSearch 在 beam 搜索时对 level≥2 用 RRF 融合生成概率排名和价值排名；判别式重排复用同一解码器，rank token 拼接完整 SID 与广告侧特征，Lambda Loss 和 OLR 双头打分，RRF 融合。

**关键结果**：在线 A/B 测试（5% 流量，7天，p<0.05）累积收入提升 3.07%，其中 Multi-Path SID +0.58%，五维扩展至 +2.00%，UniVGD 再 +1.07%。扩展效率对比：0.49B 参数模型 +1.41% 收入且保留 85% QPS，而 0.50B 朴素缩放仅 +0.53% 且 QPS 33%。价值对齐：HR@10 从 0.021 提升到 0.298（约 14 倍）。

**最值得记住的一句话**：生成式推荐的可靠性不应只靠加参数，SID 路径冗余、前缀级价值学习和推理期价值融合的协同，是在严格延迟约束下持续提升商业收益的关键。
