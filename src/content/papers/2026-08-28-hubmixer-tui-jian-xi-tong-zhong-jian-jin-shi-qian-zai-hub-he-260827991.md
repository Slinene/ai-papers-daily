---
title: 'HubMixer: Progressive Latent Hub Mixing for Parameter-Efficient Feature Interaction
  in Recommendation'
title_zh: HubMixer：推荐系统中渐进式潜在 Hub 混合的参数高效特征交互
authors:
- Jie Zhou
- Zixian Gong
- Wenhao Li
- Chang Liu
- Enzhao Shen
- Bo Liu
- Xu Guo
- Fei Pan
- Peng Jiang
affiliations:
- Kuaishou Technology
- Tsinghua University
arxiv_id: '2608.27991'
url: https://arxiv.org/abs/2608.27991
pdf_url: https://arxiv.org/pdf/2608.27991
published: '2026-08-28'
collected: '2026-08-31'
category: RecSys
direction: 参数高效特征交互 · 潜在 Hub 混合
tags:
- Feature Interaction
- Token Mixing
- Latent Hubs
- Parameter Efficient
- CTR Prediction
- Industrial RecSys
one_liner: 用少量可学习 latent hubs 组织异构特征交互，参数更少、AUC 更高
practical_value: '- 在已 token 化的精排模型里，若不想对全量 token 做 O(T^2) 交互，可引入 H 个可学习 hubs（H<<T）做
  induction→hub self-attention→token readout，计算降到 O(TH)，适合电商/广告 ranking 做参数受控升级。

  - 保留 token 级 field identity：不要将交互后的 hubs 池化成全局向量广播；用 token-conditioned cross-attention
  readout + LayerScale 残差写回，多任务各目标能按需取不同交互语义，避免全局坍缩。

  - 静态 learnable hubs 加一个由 mean-pool token 生成的输入条件残差，成本低但能让 hub 随样本软路由；T=32 时 H=16
  是精度/参数甜点，再多收益饱和，可作为默认配置参考。

  - cross-attention 在 H<<T 时是小矩阵计算，批处理友好、便于 kernel fusion，适合在已有 token-mixing 排序模型上做轻量替换并上线验证深度转化目标。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
工业推荐精排模型通常把用户画像、行为序列、item 属性、上下文、统计特征等异构 token 展平后直接做特征交互。但推荐 token 来自不同语义空间，有效交互稀疏且依赖样本，直接做全量 token 混合会让模型浪费容量在大量无用交互上。HubMixer 提出：先把异构 token 归纳到少量 latent hubs，在干净的 hub 空间做高阶交互，再按 token 条件写回，从而提升参数效率。

**方法关键点**
- Tokenization：按语义 group 组织成 token，不做无结构 flatten。
- Latent hub 初始化：维护 H 个可学习 base hubs（H<<T），并用 mean-pool token 经两层 MLP 生成输入条件残差，使 hub 随样本自适应。
- Hub induction：以 hubs 为 query、tokens 为 KV 做 cross-attention，把异构 token 信息归纳进 compact hub。
- Hub interaction：在 hub 空间做 self-attention，建模高阶 hub 依赖，计算量远小于 token 全量交互。
- Token-conditioned readout：每个原始 token 作为 query，从交互后的 hubs 中检索自己需要的全局交互信号，经 LayerScale 残差写回，保留 field identity。
- 多任务预测：最终 token 拼接后接多任务 head，HubMixer 与 MTL 解耦。

**关键实验**
在快手短视频招聘业务 1B 样本上验证，覆盖用户画像、行为序列、职位/短视频/上下文/统计特征，优化 plc_click、effective_view、interact、resume_submit 四个目标。对比 DCN、DCNv2、AutoInt、Wukong、RankMixer、TokenMixer。HubMixer 平均 AUC 0.8256，优于 TokenMixer 0.8241、RankMixer 0.8238，且参数仅 142.4M，低于 RankMixer 155.1M、TokenMixer 156.9M。消融显示去掉 hub interaction 平均 AUC 降至 0.8232，池化读回降至 0.8247，证明 selective readout 有必要。H=16 为甜点，H=32 收益饱和。线上 A/B 7 天覆盖 7.2% 流量，简历提交转化率提升 5.48%，已全量部署。

**最值得记住的一句话**
把异构特征先归纳到少量可学习 latent hubs，在 hub 空间做高阶交互，再通过 token 条件读回，比直接在原始 token 空间做全量混合更参数高效。
