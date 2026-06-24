---
title: "OneRetrieval: Unifying Multi-Branch E-commerce Retrieval with an Editable Generative Model"
authors: Xuxin Zhang, Ben Chen, Yue Lv, Chenyi Lei, Wenwu Ou, Kun Gai, et al. (17 人)
affiliation: Kuaishou (快手)
date: 2026-06
venue: arXiv
topic: gen-search
topic_name: 生成式搜索
topic_icon: 🔎
idea: 第一个可实时编辑的生成式检索框架：用 Keyword-Aligned Encoding(KAE) 把 item/query 编码成由「关键属性词」(而非量化 embedding)构成的 6-token 语义 ID，并预留一批 codebook 槽位，让运营像改倒排索引一样几小时内、不重训模型就注入新词/新品牌，从而有潜力用单个生成模型替换整个多路召回。深召回 HR@350 与最强生成基线 OneSearch 打平，干预命中率高一个数量级以上；线上替倒排分支订单 +0.71%。
paperUrl: https://arxiv.org/abs/2606.13533
codeUrl: https://github.com/xuxinzhang/oneretrieval
tags:
- Generative Retrieval
- Keyword-Aligned Encoding
- Editable Codebook
- E-commerce Search
- Real-Time Intervention
unverified: false
detail:
  contribution: |
    提出 OneRetrieval——第一个把「实时可编辑性」做成结构属性的生成式检索框架，开辟「可扩展码本」第三条标识符路线(区别于闭码本 SID 与开放词表)。三大贡献：① KAE 把每个 SID token 锚定到可读的关键属性词而非量化 embedding；② 信息论把 18 类属性合并成 6 组(信息损失曲线拐点)+ 密度感知非均匀容量分配，每位预留 10 槽(共 60)供部署后绑新词；③ 属性锚定的四阶段 SFT 把召回质量与可编辑性用近似不相交的阶段联合保住。首次让单生成模型有潜力接管几乎整个在线召回阶段。
  background: |
    工业电商搜索召回是倒排(词面)+向量(语义)+协同三路并联，手工调融合、无法联合优化。生成式检索想用单模型收口，但卡在「可编辑性悖论」：倒排分支转化率低于均值却删不掉，因为它是唯一能让运营几小时内注入新词/爆款品牌(如 LABUBU)而不重训模型的分支——它活着不是因为召回好，而是因为可编辑。现有 GR 结构性不可编辑：闭码本(TIGER/DSI/OneSearch)每槽绑训练时固定的量化 embedding，新词进不来要重训；开放词表(SEAL/GRAM)生成自由片段，新词能否路由全靠模型泛化，运营无显式绑定机制。
  method: |
    **KAE**：用 Aho-Corasick 把 item(标题/结构化属性/详情/图 OCR)与 query 对 108 万词生产属性字典做确定性匹配(在线零神经推理)，18 类属性按信息论合并成 6 组，一组多词时用「主体优先(LLM 离线判定)+行为后验(PV/CTR)」选代表，拼成 6-token SID，每 token 直接是一个属性词。**可扩展码本**：每位含 cluster 槽(k-means 质心)+solo 槽(高频头词)+10 个 reserved 预留槽；预留槽训练时不绑词、部署后才绑。**L6-D3 配置**：密集头 3 组各 2048、轻尾 3 组各 1024(核心码本 9216+预留 60)。**四阶段 SFT(BART-base)**：S0 属性词↔SID 对齐；S1 内容对齐(召回质量主力)；S2 协同共现 query-SID→item-SID 路由(可编辑性主力)；S3 个性化检索+预留槽自路由监督。**可编辑性靠三性质**：P1 句法可达(beam 任意位发任意码)、P2 词无关身份路由(S3 用 prefix→prefix 自路由教成恒等路由器)、P3 编码端确定性(字典查表把新词定映到预留槽)。运营改字典+在 SID-to-item 查表 T 里绑目标商品，几小时生效、不动模型。
  experiments: |
    数据：快手电商搜索 31 天，500 万训练请求+约 3 万 click/order 测试，7.6M query/20M item/1.08M 属性词。基线：BM25/docT5query/DPR + TIGER/DSI/LTRGR/LC-Rec/OneSearch(自家前作)。**RQ1**：HR@350 order 0.5482/click 0.6055，与最强 OneSearch(0.5550/0.6007)深召回打平(click 反超)，但 MRR 远低(0.0880 vs 0.1333)——定位深召回非精排。**RQ3(KAE vs 量化)**：total IHR@350 KAE 0.0806 vs RQ-VAE/kmeans/OPQ 0.0021~0.0030，高一个数量级以上，且召回也最好。**对比 BM25**：IAR@350 0.553 vs 0.761(约 3/4)，但召回翻倍(0.5482 vs 0.2215)。**RQ4 SFT 留一**：去 S2→IHR 从 0.1340 崩到 0.0030(可编辑性=S2)，去 S1→召回掉(质量=S1)。**RQ5 线上 A/B**：替倒排分支→Order +0.710%(显著)/CTR +0.074%/Buyer +0.450%；替倒排+向量→CTR +0.821%(显著)/Order +0.255%(不显著)；16/20 行业 CTR 正向(均值 +1.00%)；人工 GSB 三轴全胜。已部署快手外搜，日数亿 PV。
  pros: |
    ① 概念创新：提出「可编辑性悖论」并确立为统一召回的真门槛，开辟可扩展码本路线，是对 GR 范式的认知贡献；② KAE 用属性词当 SID token，可读/可控/可编辑且召回不输量化码；③ 可编辑性沉到上游字典+预留槽，运营操作与倒排同构(改字典+绑表几小时生效)，在线编码纯查表零神经推理；④ 自造 IHR/IAR 量化可编辑性；⑤ offline+线上 A/B+人工 GSB 三层证据，非层级码本等消融干净，结论可被别的工业 GR 直接复用。
  cons: |
    ① 召回质量相对 OneSearch 并无提升(打平)，卖点全在可编辑性；② 强依赖 108 万词的生产属性字典+抽取 pipeline，无此基建难复用；③ IAR 仍只有倒排 3/4，激活能力未追平；④ 「替换全部」时 Order/Buyer 不显著，「一个模型干掉全部召回」差临门一脚，且窗口仅 11 天单平台；⑤ 干预测试用 LLM 造 2000 词模拟，非真实运营干预分布；⑥ 骨干仅 BART-base 一种，未测更大 backbone。
  inspiration: |
    对电商/广告/搜索推荐的借鉴：① 「可编辑性」是 SID/生成式召回落地的隐形门槛——做 Semantic ID/生成式检索别只看 Recall，要把「运营能否几小时注入新词/新品/活动词」当一等公民，解法是把可编辑性沉到上游字典+预留槽而非塞进模型，这个解耦极可迁移；② KAE 用属性词当 SID token，比 RQ-VAE 量化码可读可控，且能规避 RecLoop 里量化码本(尤其 CID)的热度偏置/结构茧房问题，是另一条编码路线值得对照；③ 非层级+全局共享码本+密度感知非均匀分配是可直接抄的工业 GR 配置结论；④ Kuaishou 线上系统(OneRec/OneSearch/OneRetrieval 一脉)，与字节 OneRec 系直接对标，跟踪价值高。
  takeaway: |
    OneRetrieval 的核心价值在于第一个让生成式检索具备倒排级「实时可编辑性」(KAE+预留槽，把可编辑性沉到上游字典)，证明单生成模型有望保住召回质量同时接管多路召回；主要局限是召回精度本身不超 OneSearch、强依赖生产属性字典基建、且「替换全部」的转化收益尚不显著——是电商生成式检索工业落地方向上问题精准、范式有原创性、线上已验证但尚未完全收口的重要进展。
---
