---
title: 'PriCoRec: A Privacy-Aware Cloud-Device Collaborative Framework for Ad Recommendation
  under Feature Constraints'
title_zh: PriCoRec：特征约束下隐私感知的云-端协同广告推荐框架
authors:
- Dairui Liu
- Zhongyi Lu
- Jitao Lu
- Aghiles Salah
- Mete Sertkan
- Roger Zhe Li
- Changhong Jin
- Barry Smyth
- Xingsheng Guo
- Ruihai Dong
affiliations:
- University College Dublin
- Huawei Ireland Research Center
arxiv_id: '2608.14429'
url: https://arxiv.org/abs/2608.14429
pdf_url: https://arxiv.org/pdf/2608.14429
published: '2026-08-14'
collected: '2026-08-17'
category: RecSys
direction: 隐私感知云-端协同排序
tags:
- Privacy
- Cloud-Device Collaboration
- Ad Recommendation
- CTR Prediction
- DPP Diversity
- Lightweight Ranking
one_liner: 提出隐私感知云-端协同广告推荐框架，敏感特征留在端侧，以云预排序多样性正则和云指导轻量端模型兼顾效果与效率
practical_value: '- 在隐私合规限制下无法云端使用用户画像时，可采用云-端分离级联：云端只用上下文/物品特征做粗排，端侧用完整敏感特征做精排；既满足数据不出端，又保留个性化能力。

  - 粗排候选集质量直接决定端侧精排上限。可借鉴 DPP log-det 正则，在粗排训练损失中加入多样性项，缓解因特征受限导致的候选同质化；λ 建议 1e-3~1e-2，按验证集调节，可提升
  Recall@100。

  - 端侧模型不必复现云端大模型，可将云端粗排输出的相关性 logit 作为辅助特征输入端侧模型；端侧 embedding 维度 4、两层 PNN 即可取得显著提升，配合
  FP16 存储和词表重映射能把模型控制在 7.7–29.4MB，推理延迟约 0.5–0.8ms。

  - 训练粗排模型时，1:4 随机负采样 + BPR 成对损失是稳定有效的基础配置；若业务中用户敏感特征无法上云，可先按此框架拆分粗排和精排，再迭代优化多样性正则强度。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**

隐私法规日益限制云端处理敏感用户特征（如年龄、性别），传统云端 CTR 模型面临合规与效果的两难。纯端侧部署又受算力和数据稀疏约束，而简单把排序链路切分到云-端会造成候选集质量下降、端侧推理低效。因此需要一种能在云端使用受限特征做粗排、在端侧利用敏感特征做精排的协同框架，同时解决特征不对称带来的候选质量和端侧模型轻量化问题。

**方法关键点**

- 云-端级联架构：云侧 pre-ranking 只用云可访问特征（物品特征、上下文等）将 1000 个召回候选降至 100，端侧 ranking 使用全部特征（含敏感属性）重排短列表。
- 云侧多样性正则：受 DPP 启发，计算候选物品 embedding 相似矩阵，将其 log-det 作为多样性损失，与 BPR 成对损失加权，λ 在 [1e-5,1e-2] 调参；目标是提升短列表覆盖率，避免候选同质化。
- 云指导轻量端模型：云端 pre-ranker 输出的相关性 logit 作为端侧模型辅助特征，端侧不需要复现大模型；端侧 embedding 维度仅 4（云端 32）、两层 PNN，另配合词表重映射和 FP16 存储压缩体积。
- 训练采用 1:4 随机负采样 + BPR 成对损失，云端和端侧均使用 PNN 骨干。

**关键结果数字**

在 OpenMCC、TaobaoAd、Ali-CCP 三个公开数据集上，对比 PNN、DP-SGD、DualRec、FedCAR、FedCIA。云侧预排序：PriCoRec 的 gAUC 和 R@100 均最佳，如 Ali-CCP gAUC 从 72.93 提升到 73.69，R@100 从 46.92 提升到 47.72。端侧精排：PriCoRec 在所有指标上领先，TaobaoAd R@10 从 17.38 提升到 21.74，Ali-CCP R@10 从 20.97 提升到 24.10。效率方面，TaobaoAd 总延迟 10.32ms（9.81ms 云 + 0.51ms 端）优于纯云 11.62ms；端模型体积从 7.7MB 到 29.4MB，对应 R@1 从 4.51 到 7.51。

**最值得记住的一句话**

云侧多样性正则提升候选质量 + 云端 logit 辅助端侧轻量排序，是在特征受限条件下兼顾隐私、效果和效率的有效组合。
