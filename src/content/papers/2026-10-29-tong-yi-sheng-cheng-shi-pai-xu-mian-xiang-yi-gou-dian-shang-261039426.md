---
title: 'UGR: Unified Generative Ranking for Heterogeneous E-commerce Recommendation'
title_zh: 统一生成式排序：面向异构电商推荐的跨业务榜单生成
authors:
- Zonghe Shao
- Huabin Chen
- Sitong Lu
- Fangmei Zhu
- Yingcai Ma
- Ge Fan
- Jinguo Gao
- Wei Shi
- Yanfang Liu
- Huiping Chu
affiliations:
- Alibaba Group
arxiv_id: '2610.39426'
url: https://arxiv.org/abs/2610.39426
pdf_url: https://arxiv.org/pdf/2610.39426
published: '2026-10-29'
collected: '2026-10-30'
category: RecSys
direction: 生成式排序 · 多业务混排与广告价值融合
tags:
- Generative Ranking
- Multi-Business Recommendation
- Permutation Preference Optimization
- Advertising Debiasing
- GSP Auction
- E-commerce
one_liner: 在淘宝异构候选集上统一生成多业务排序列表，结合反馈监督与广告debias塔，在线GMV提升2.10%
practical_value: '- 若做生成式排序或混排，优先一次生成最终异构列表，避免“单业务生成 + mixrank”的两阶段方案。论文对照实验显示统一生成在线
  GMV 比 staged 方案多出约 0.72pct，说明最终列表上下文应在一个生成过程内被建模。

  - 广告/商业化场景中，可复制“训练期 ad debiasing tower + 在线只加当前 eCPM”的架构：tower 只看 ad 特征和 logged
  eCPM，训练后移除，推荐分与当前 eCPM 相加。这样能避免历史广告政策污染推荐分，并兼容 GSP 定价，不需要改动拍卖逻辑。

  - 反馈监督可拆成两个层次：WSFT 用 feedback 加权 item-level NLL，PermPO 用同一反馈计算 DCG 构造 list-level
  preference pair。二者互补，适合在曝光序列之外引入转化/交易信号，提升 ranking quality。

  - 处理千级候选可用低秩候选注意力（Linformer 式），把候选轴 KV 投影到少量 latent components，一次编码后 beam search
  复用。论文在生产中仅增加 12ms 延迟，说明该方案能满足在线低延时约束。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：电商推荐需在同一信息流中混排有机内容、广告和其他业务，候选集约 1000。现有生成式排序通常只在单一业务截断候选集上生成，之后通过 mixrank 跨业务混排，导致生成列表与最终曝光列表的位置和 list context 不一致；同时仅模仿曝光序列无法充分利用曝光后反馈；且模型直接拟合历史曝光会把历史广告政策效应留在推荐分里，与 GSP 拍卖下的当前广告价值叠加产生偏差。

**方法关键点**：
- 统一生成：自回归解码直接在整个请求级异构候选集上生成多业务最终排序列表，不再做后续 mixrank。
- 架构：request context encoder 压缩用户/上下文/历史为单 token；候选共享表示空间，用低秩候选注意力对千级候选做全量 contextualization；decoder 根据当前前缀计算 candidate score。
- 反馈监督：NTP 提供曝光序列基线；WSFT 用 IPV/CVR 反馈加权 next-item likelihood；PermPO 用反馈 DCG 构造同 item 集排列偏好对，进行 pair-wise 相对排序优化。
- 广告融合：训练期引入 ad debiasing tower 单独吸收历史 eCPM 效应；在线推理移除 tower，推荐分只加当前 eCPM，保住现有 GSP 分配与定价规则。在线用多值序列检索保留 top-4 路径，由下游 evaluator 选择最终曝光。

**关键结果**：在淘宝猜你喜欢 30 天日志、两个场景（约 19.4 亿 / 2.4 亿请求）上，对比 PRM、NAR4Rec、GReF、Dual-Rerank、UniRank、DEGR，UGR 在 Scenario 1 全部六个排序指标领先，IPV NDCG 较 UniRank 提升 4.86%，IPV MAP 较 DEGR 提升 7.53%，CVR MAP 较 DEGR 提升 2.05%。在线 A/B：Core IPV +1.76%，Transaction Volume +3.29%，GMV +2.10%，Click UV +1.32%，UCTR +0.45%；广告护栏 Ad Cost +0.08%、Ad PVR -0.93%，推理延迟仅 +12ms。消融验证 WSFT、PermPO 和 ad tower 均有贡献；ad tower 使生成 logit 与 eCPM 相关性由 +0.195 转为 -0.313，表明历史广告效应被分离。

**最值得记住的一句话**：统一生成最终异构列表 + 训练期广告 debias + 在线只加当前 eCPM，是生成式排序在 GSP 拍卖约束下落地的关键组合。
