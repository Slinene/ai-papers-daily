---
title: "OneSearch: A Preliminary Exploration of the Unified End-to-End Generative Framework for E-commerce Search"
authors: Ben Chen, Xian Guo, Siyuan Wang, Zihan Liang, Yue Lv, Chenyi Lei, Wenwu Ou, Han Li, Kun Gai, et al. (30 人)
affiliation: Kuaishou Technology
date: 2025-09
venue: arXiv
topic: gen-search
topic_name: 生成式搜索
topic_icon: 🔎
idea: |
  OneSearch 系列开山之作，也是首个工业级端到端生成式电商搜索框架(快手商城详情页 100% / 商城 50% / 主搜 20% 全流量)。三件套：① **KHQE 编码** = RQ-Kmeans 三层 hierarchical SID + OPQ 两层 残差独特属性 SID + AC 自动机关键词增强降噪；② **多视角行为序列注入** = behavior-构造 user ID + 显式 short seq + Q-Former 聚合的隐式 click/order/RSU 三类 long seq；③ **PARS** = 三阶段 SFT(语义对齐→共现同步→个性化) + 6 级行为分层 reward + Listwise DPO 两阶段 Hybrid Ranking(RM-guided→user interaction)。线上 item CTR +1.67% / Order +3.22% / Buyer +2.40%；OPEX 直降 75.40%, MFU 3.26%→27.32%(700% 相对提升)，给「单生成模型替代 MCA」首次工业证据。
paperUrl: https://arxiv.org/abs/2509.03236
codeUrl: null
tags:
- Generative Search
- KHQE
- RQ-OPQ
- Multi-view Behavior
- E-commerce Search
unverified: false
detail:
  contribution: |
    首个工业级端到端生成式电商搜索框架(对标 OneRec 在 E-commerce Search 领域的 first-mover)，四大贡献：

    1. 提出 **KHQE**(Keyword-enhanced Hierarchical Quantization Encoding)，把 RQ-Kmeans + OPQ + AC 自动机抽核心关键词组合，hierarchical 语义与 lateral 独特属性双保留，并显式解决电商 item 描述「冗长无序+卖家塞无关词」的低密度噪声；
    2. 设计 **Multi-view Behavior Sequence Injection**，behavior-constructed user ID(替 Tiger 的 hashing uid) + 显式 short seq + Q-Former 聚合 click/order/RSU 三类隐式 long seq，三路径分工注入；
    3. 提出 **PARS**(Preference Aware Reward System)，三阶段 SFT(语义→共现→个性化) + 6 级行为分层 reward + Listwise DPO + Hybrid Ranking 两阶段(RM-guided→user interaction)，把强相关约束与个性化排序统一处理；
    4. 大规模 A/B + 工业级部署：MFU 3.26%→27.32%、OPEX -75.40%、详情页 100% + 商城 50% + 主搜 20% 流量上线，首次给出「单生成模型替代 MCA」的工业证据。
  background: |
    传统电商搜索是多级级联架构 MCA：recall(~10⁹) → pre-rank(~10⁴) → rank(~10²)，逐级漏斗权衡延迟与精度。两大顽疾：① **fragmented compute**(资源大头去做通信/存储而非数值计算)；② **objective collision**(各阶段独立训练目标互打架，intent item 一旦早期被砍后期再准也救不回来)。

    近两年生成式检索(GR) Tiger / LC-REC / OneRec / EGA / OneSug 把召回当 seq-to-seq 生成，但绝大多数只能当 recall 补丁。电商搜索三独特门槛挡住 GR 落地：

    1. item 信息(title/属性/详情/OCR)冗长无序、卖家塞无关词造噪声，普通 SID 易丢核心属性；
    2. query 与 item 强相关约束(2-3 词短 query 属性错一个就翻车)，共享 SID 易丢关键匹配；
    3. 短 query/新品类下需要把行为画像合理融入挖隐式意图。

    OneSearch 要在快手详情页/商城/主搜真实流量下一次解掉这三个门槛，把 GR 从「recall 补丁」推到「替代 MCA 全栈」。
  method: |
    **(1) KHQE 编码**

    - *Aligned Rep* 用同 family 的 query/item embedding model + QwenVL 抽图；
    - *Core Keyword Enhancement* 用 Aho-Corasick 自动机匹配关键词字典(品牌/类目/属性)，命中关键词显式拼到 embedding 端降噪；
    - *RQ-Kmeans* 三层 codebook (4096-1024-512)，**不能做全层 balanced k-means**(实验证明早期层 hierarchical clustering collapse，CUR 从 48.95% 跌到 1.64%)，只在 L3 做 balanced；
    - *OPQ 残差量化* 在 RQ-Kmeans 之后把残差 embedding 再用 OPQ(256-256)量化两层，补回独特属性，SID 总长 5 token。

    **RQ-OPQ(2/256) 是最优配置**，继续往深加(4/256、4×2/256、4×4/256)反而崩 —— 残差量化深不得是工业 GR 硬规则。

    **(2) Multi-view Behavior Sequence Injection**

    - *behavior-constructed User ID* — 用 short seq 的 SID softmax-scaled exp(√i) 加权 + long seq 的 SID 加权 拼成 10-token uid，替 Tiger 的 hashing uid 大幅降 SID 碰撞；
    - *Explicit Short Seq* — 把最近点击的 query/item SID 直接拼 prompt，slide window 数据增强；
    - *Implicit Long Seq + Q-Former* — click/order/RSU 三类长 seq(长度可达 10³)，每个 item 取 RQ-Kmeans 三层 cluster centroid 聚合，再 Q-Former 压成固定 token 注入(R^(N_M×768))，建短期意图同时建长期 profile，资源占用受控。

    **(3) Unified Encoder-Decoder Architecture**

    默认 BART-base(对 decoder-only Qwen3 也兼容)；输入 `[BOS] uid q SID_q Seq_q Seq_short Seq_long_emb U [EOS]`，输出 item SID 列表；beam size 512；支持 constrained / unconstrained beam search。

    **(4) PARS**

    - *三阶段 SFT* —— S1 语义对齐(query/item↔SID, query/item→category)、S2 共现同步(query↔item, SID_q↔SID_i, 不带用户特征纯学协同)、S3 用户个性化(uid + q + SID_q + Seq_q + Seq_short + Seq_long_emb → item SID)；
    - *6 级行为分层 reward* —— 搜索购买 2.0 > 推荐同类购 1.5 > 点击 1.0 > 曝光未点 0.5 > 同类未曝 0.2 > 随机其他 0.0，并用 log(Cnt_T) 校准 CTR/CVR 偏置防新品 100%CTR 噪声；
    - *Reward Model* SIM 三塔(CTR/CVR/CTCVR + 加权 10× S_Rel)对生成结果重排，选 ranking 变动样本做 Listwise DPO；
    - *Hybrid Ranking 两阶段* Phase1 RM-guided(初期对齐 MCA)→ Phase2 user interaction(突破在线分布天花板)；
    - 训练节奏：SFT+RM 周更，RM-guided 日更，user interaction 流式准实时。
  experiments: |
    **数据**：快手商城搜索 2025-05~08 的 ~1B PV，前 90 天训练 + 末 1 天测试；各 30k click/order pair 评测。

    **Offline 主结果(Table 5)**：onlineMCA HR@350 order=51.74% click=64.40%，MRR@350=19.26%/16.89%；OneSearch(RQ-OPQ(2/256)+Adaptive RS) HR=**66.46% / 71.06%** (+14.72pp/+6.66pp)，MRR=18.38%/16.33% 与 MCA 打平；「MCA w/o ranking」HR 高但 MRR 暴跌(75.75%/4.19%)——反证 MCA ranking 是关键，OneSearch 单模型同时做到了召回+排序。

    **Ablation Tokenization(Table 2)**：codebook size (1024,1024,1024)→(4096,1024,512) HR/MRR 单调上涨；+keywords HR@350 order 从 59.58→62.38%；+L3 balanced 到 63.16%；+Adaptive RS 到 64.33%；+RQ-OPQ(2/256) 顶配 66.46%。

    **OPQ 配置(Table 7)**：RQ-OPQ(2/256) 最佳；(4/256) HR@10 -2.36%/MRR -1.77%；(4×2/256) HR -10.20%；(4×4/256) HR -24.18% —— 残差量化越深越崩。

    **行为序列(Table 6)**：去 Seq_short HR@350 -3.43%、去 User SIDs -0.94%、去 Seq_long -2.26%、去 sliding window -1.95%。

    **Codebook 稳定性(Figure 6)**：8.18 大促前后 RQ-Kmeans CUR -1.11%，RQ-OPQ 仅 -0.43% —— 抗新品冲击强。

    **线上 A/B (Table 8) 快手商城**：

    - MCA w/o ranking 全线大跌(item CTR -9.97%, Order -39.14%) —— 反证 ranking 不可或缺；
    - OneSearch¹(无 long seq) item CTR -1.10%，+RM 后 +1.40%；
    - OneSearch²(全量优化) item CTR +1.45% / PV CTR +1.40%；
    - **OneSearch²+RM 全显著**：item CTR +1.67% / PV CTR +3.14% / PV CVR +1.78% / Buyer +2.40% / Order +3.22% (全 p<0.05)。

    **MFU/OPEX(Figure 7)**：onlineMCA MFU 3.26% → OneSearch 27.32%(+700%)；OPEX -75.40%。

    **细分**：Top 30 行业 28/30 CTR 正向(均值 +2.49%)；query 三档流行度全部正向(top +1.25%/middle +2.27%/long-tail +1.33%)；冷启 item CTR +3.31%、冷用户 +2.50%(都比热的强)；Manual page good +1.03% / item quality +2.12% / Q-I relevance +1.87%。

    **部署**：详情页 search 全流量 + 商城 50% + 主搜 20%，日 PV 千万级。
  pros: |
    1. **工业首发**：第一个端到端 GR 在电商搜索全流量落地，不是 recall 补丁；线上 +1.67% CTR / +3.22% Order / MFU +700% / OPEX -75.40% 全部 p<0.05，量级足以撬动决策；
    2. **KHQE 完整方案**：RQ-Kmeans 解 hierarchical 语义 + OPQ 解 lateral 独特属性 + 关键词增强解噪声，三路径分工明确，ablation 干净；
    3. **多视角行为注入设计实用**：behavior-constructed uid + 显式 short + Q-Former 聚合 long(三类 click/order/RSU)，对冷启动用户 CTR 比热的还高 2.50%，工业落地极关键；
    4. **PARS 训练管线工程化好**：三阶段 SFT 解耦语义/共现/个性化、6 级行为分层 reward + CTR/CVR 偏置校准很务实；Hybrid Ranking 两阶段(先对齐 MCA 再突破天花板)解决「在线分布天花板」问题；
    5. **MFU/OPEX 当指标**汇报很高级 —— 纯转化卷不动了，加成本端会让决策者更易批准上线；
    6. 行业/流行度/冷启动多维细分实验充分，长尾+冷启动正向是另一类业务铁证。
  cons: |
    1. **召回赢 MCA 但 MRR 没赢**(66.46% vs 51.74% / 18.38% vs 19.26%) —— 生成式靠召回端发力，排序端只是打平 MCA 千特征模型，靠 RM 重排才补齐排序差距；
    2. **强依赖手工 keyword 字典 + AC 自动机抽取 pipeline**，搬到其他平台需重做基建(后续 OneRetrieval 扩到 108 万词，说明这块成本高)；
    3. **强依赖 Bart-base + beam=512**，未与更大 backbone / decoder-only 路线(Qwen3 等)系统对比；
    4. **reward 系统含独立 RM**，OneSearch-V2 已用 TPMA-GRPO 干掉它，说明 V1 这条路线本身有迭代必要；
    5. **可编辑性弱**：大促新词/新品牌进不来要重训(OneRetrieval 后续正好补这条)；
    6. 实验仅在快手单平台单时段(91 天)，无跨平台/跨品类外推；
    7. "end-to-end" 实际仍是检索阶段统一(召回+排序合并)，并非真正端到端从 query 到曝光全链路。
  inspiration: |
    对电商/广告/搜索推荐的借鉴：

    1. **SID 设计应是「层级 + 残差」组合体**：单一 RQ 量化在电商 item 下会丢独特属性，KHQE(RQ-Kmeans + OPQ + 关键词)的三件套范式值得抄，尤其 OPQ 残差只做 2 层、继续加深反而崩——是工业 GR 一条硬规则；
    2. **行为序列要分路径注入**(uid 嵌入 + 显式 short + 隐式 long w/ Q-Former)，不要塞一锅，冷启动/热用户都覆盖，推荐/广告同样适用；
    3. **强相关性约束场景下，reward 必须把相关性显式放大**(10× S_Rel) —— GR 不像推荐，搜索 reward 不显式加约束就会让相关性掉到地板；
    4. **Hybrid Ranking 两阶段(Phase1 RM-guided 对齐 MCA → Phase2 user interaction 突破天花板)** 是聪明的「先对齐再超越」工程范式，可迁到任何想替换在线系统的生成式方案；
    5. **MFU/OPEX 当指标**是工业 GR 落地汇报的高级武器，纯转化指标卷不动时把成本端推到业务面前更易拿到上线许可；
    6. OneSearch 与 OneRec/OneSug/OneRetrieval/OneSearch-V2 构成「Kuaishou One系」，是字节内做电商生成式搜推必须长期跟踪的对手范式；
    7. V1 的三条局限正好是 V2(加潜在推理+自蒸馏解 query 理解)和 OneRetrieval(加可编辑码本解新词)的发力点，三篇对照读可以看到一条工业 GR 范式如何迭代成熟。
  takeaway: |
    OneSearch 是第一个工业级、端到端、上电商搜索全流量(快手详情页 100% + 商城 50% + 主搜 20%)的生成式检索框架，核心价值在于 KHQE 编码 + 多视角行为注入 + PARS 三件套给出了一条「单生成模型替代 MCA」的可复现工业路径，且把 OPEX 直接砍掉 75.40% / MFU 翻 7 倍，把节流也当硬指标推到业务面前；主要局限是排序端仅与 MCA 打平(无显著超越)且依赖手工关键词字典 + 独立 RM 重排 + 不可编辑码本——这些限制正好是 OneSearch-V2 / OneRetrieval 后续两篇要继续解的题。本文是工业电商生成式搜索范式的奠基级里程碑，也是读这条线必须读的第一篇。
---

## 核心思路

传统电商搜索靠多级级联架构(MCA): recall(~10⁹) → pre-rank(~10⁴) → rank(~10²)，逐级漏斗权衡延迟与精度。但 MCA 有两大顽疾：**fragmented compute**(资源大头给通信/存储而非数值计算)与 **objective collision**(各阶段独立训练目标互打架，intent item 早期被砍后期救不回)。生成式检索(GR)用单模型 seq-to-seq 收口理论上能解，但电商搜索三个独特门槛挡住 GR 落地：item 信息冗长无序+卖家塞无关词噪声、query↔item 强相关约束、短 query/新品类下隐式意图挖掘。

**OneSearch** 是首个把这三道门槛一次解掉、并在 Kuaishou 电商搜索详情页全流量、商城 50%、主搜 20% 流量上落地的端到端生成式框架。核心三件套：

1. **KHQE**(Keyword-enhanced Hierarchical Quantization Encoding) —— RQ-Kmeans 三层 hierarchical SID + OPQ 两层残差独特属性 SID + AC 自动机抽核心关键词降噪；
2. **Multi-view Behavior Sequence Injection** —— behavior-constructed user ID + 显式 short seq + Q-Former 聚合 click/order/RSU 三类隐式 long seq；
3. **PARS**(Preference Aware Reward System) —— 三阶段 SFT(语义对齐→共现同步→个性化) + 6 级行为分层 reward + Listwise DPO + Hybrid Ranking 两阶段(RM-guided→user interaction)。

线上 A/B：item CTR +1.67% / Order +3.22% / Buyer +2.40%(全 p<0.05)，OPEX -75.40%、MFU 3.26%→27.32%(+700%)。本文是 Kuaishou「One系」(OneRec/OneSug/OneSearch/OneRetrieval/OneSearch-V2)在电商搜索方向的奠基级里程碑。

## 关键贡献

- 首个工业级端到端 GR 框架在电商搜索全流量落地，不再只做 recall 补丁；
- KHQE 把「hierarchical 量化 + 残差独特属性量化 + 关键词降噪」一次组合，给电商 GR 的 SID 设计立了工业基准；
- 多视角行为注入(三路径)让冷启动用户 CTR 反而高于热用户(+2.50% vs +1.11%)；
- PARS 把「在线分布天花板」工程化(Phase1 RM-guided 对齐 MCA → Phase2 user interaction 突破)，是任何想替换在线系统的生成式方案可借鉴的模板；
- MFU/OPEX 当工业指标 —— 把节流推到业务面前，决策者更易批准上线。

## 实验亮点

- HR@350 order 51.74%→66.46%(+14.72pp)，MRR 与 MCA 打平；
- RQ-OPQ(2/256) 是 sweet spot，继续往深加(4/256/4×2/4×4)反而崩；
- 线上 A/B 全显著(p<0.05)：item CTR +1.67% / PV CTR +3.14% / PV CVR +1.78% / Buyer +2.40% / Order +3.22%；
- OPEX -75.40%、MFU 翻 7 倍(3.26%→27.32%)；
- Top 30 行业 28/30 CTR 正向，长尾 query +1.33%，冷启 item +3.31% / 冷用户 +2.50%。

## 局限与延展

排序端仅打平 MCA(没赢)且依赖手工关键词字典 + 独立 RM + 不可编辑码本 —— 这三个口子正是 **OneSearch-V2**(加潜在推理+自蒸馏解 query 理解、加 TPMA-GRPO 干掉独立 RM)和 **OneRetrieval**(加可编辑码本解新词进不来)后续两篇正面解决的题。三篇对照读可以看到一条工业 GR 范式如何迭代成熟。
