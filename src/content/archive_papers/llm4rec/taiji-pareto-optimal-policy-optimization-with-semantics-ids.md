---
title: 'Taiji: Pareto Optimal Policy Optimization with Semantics-IDs Trade-off for Industrial LLM-Enhanced Recommendation'
authors: Yuecheng Li, Zeyu Song, Jing Yao, …, Peng Jiang, Kun Gai (6 人)
affiliation: Kuaishou (快手)
date: 2026-06
venue: arXiv
topic: llm4rec
topic_name: LLM4Rec
topic_icon: 🛒
idea: |
  把 LLM 当推荐增强器，针对其后训练两个卡点给出系统解法：SFT 阶段用「目标物品 PPL」把开放域推荐 CoT 的质量从不可度量变成可计算标量；RL 阶段用 POPO 自适应权衡「LLM 语义奖励」与「推荐协同 ID 奖励」，达到两目标 Pareto 最优而非此消彼长。已在快手广告上线服务 4 亿+ 日活。
paperUrl: https://arxiv.org/abs/2606.03866
codeUrl: null
tags:
- LLM4Rec
- LLM-as-Enhancer
- Pareto Optimization
- GRPO
- Reward Balancing
unverified: false
detail:
  contribution: |
    把 LLM 当推荐增强器 (LLM-as-Enhancer)，针对其后训练两个卡点给出系统解法：SFT 阶段提出 RUPR (逆向工程造 CoT) + ORFT (用目标物品 PPL 做拒绝采样筛 CoT)，把「开放域推荐 CoT 质量无法度量」转成可计算标量；RL 阶段提出 POPO (Pareto 最优策略优化)，自适应权衡 LLM 语义奖励与推荐协同 ID 奖励，理论上达到两目标 Pareto 最优。已在快手广告上线服务 4 亿+ 日活。
  background: |
    LLM4Rec 分三条路线 (生成式推荐 / 排序 Scaling / LLM-as-Enhancer)，本文走第三条——LLM 不直接出结果，而是产出对用户偏好的推理表示喂给排序模型当增强特征，工程务实、不动主链路。两个卡点：(1) SFT 阶段推荐是开放域任务，一条推理链好不好难量化，以往只能靠强教师或「最终答案对错」判断，缺系统度量；(2) RL 阶段同时用 LLM 语义奖励和推荐反馈奖励，但两者一个在文本语义空间、一个在数值协同空间会冲突，现有方法固定权重加和、只对齐不权衡。论文名「太极」即隐喻两股力量动态统一、互相增益。
  method: |
    四模块。(1) RUPR 逆向工程用户偏好推理：构造蒸馏 prompt 时把用户「真实下一购买物品」作为已知条件喂给 QwQ-32B，让它倒推解释「为何买它」的 CoT，用 ground-truth 给推理上双重语义保险。(2) ORFT 开放式拒绝采样微调：核心是用「给定 CoT 时真实物品的困惑度 PPL」当 CoT 质量代理 (PPL 低=推理可靠)，每 prompt 生成 k=3 条 CoT 只留 PPL<R (R 取中位数 4.6)，再 SFT 激活 DeepSeek-R1-7B。(3) POPO：两类奖励——语义奖励 r_s (Qwen3-Emb 算预测答案与真实物品描述余弦相似度) 与协同奖励 r_id (排序模型 CTCVR 打分，min-max 归一化)；按梯度对齐指标 I(t) 自适应调权重 (梯度大且与其他目标一致就加权、冲突就降权)，可证为双层优化/镜像下降一阶解，把策略推向 Pareto 前沿。工业版 POPO-light 改用奖励组内变异系数 (std/mean) 当权重，零额外梯度计算。配离线奖励模拟环境避免每步查线上。(4) 在线排序：CoT+Item 经 Qwen-Emb 编码量化成排序特征 (Intra-User)，并检索 Top-1 相似用户的近 100 条行为做跨用户特征 (Cross-User)。
  experiments: |
    数据 111 万快手生产日志 (100 万用于 SFT)；骨干 DeepSeek-R1-7B、教师 QwQ-32B；RL 基座 GRPO。离线：ORFT 相比 7B 骨干 Category_L1 +28.97%、CTCVR +8.96% (但标题级 Hit-Rate 下降，SFT 泛化有限只学到粗粒度匹配)；POPO 相比 32B 教师 Category_L1 +23.25%/CTCVR +3.84%、相比 7B 骨干 Title_HitRate@50 +14.31%/CTCVR +11.68%。消融：POPO 相比固定权重 GRPO 让语义与偏好 Hit-Rate 同时提升 (验证 Pareto 改进)；RUPR 用真值引导显著优于直接生成。在线 A/B (10% vs 10% 跑一周)：全量 ADVV +2.83%/Revenue +3.30%，长尾用户 +5.26%/+5.32% (LLM 对稀疏用户帮助最大)。
  pros: |
    把「开放域推荐 CoT 质量无法度量」用目标物品 PPL 巧妙转成可计算标量，无需人工无需裁判模型，可迁移到其他无标准答案的 CoT 筛选场景；POPO 首次把多目标 Pareto 优化系统用于 LLM4Rec 的语义-协同权衡且有理论支撑；POPO-light、离线奖励模拟环境、CoT 量化+跨用户检索都是为 4 亿日活落地的实在工程取舍；离线+在线双验证，长尾收益尤其可信。
  cons: |
    离线主对照只有未调骨干和教师模型，未与同期 LLM-as-Enhancer 方法 (KAR/RLMRec 等) 直接对比，学术身位不明；只在快手广告单场景验证，方法地基「用户真实下一购买」在电商转化场景才清晰，泛内容推荐难复制；ORFT 有副作用 (细粒度标题能力下降)；PPL 作质量代理有根本天花板 (PPL 低≠推理因果正确，可能学到捷径)；7B LLM 近线推理的时延/成本账未充分交代。
  inspiration: |
    对话题推送/点击预测 user simulator 的直接借鉴：(1) PPL-as-CoT-quality 可用来筛「解释用户为何点击」的推理链，比 LLM 自评客观；(2) POPO 的异构奖励权衡正对应 simulator RL 阶段「语义合理性奖励 vs 真实点击对齐奖励」如何平衡，POPO-light 几乎零成本值得试；(3) 离线奖励模拟环境思路与「用真实日志做校准/评测」一脉相承，可用排序模型 CTCVR 当离线 reward 避免查线上。后续方向：更鲁棒的 CoT 质量度量 (超越 PPL)、POPO 扩展到 >2 个异构奖励、泛场景迁移。
  takeaway: |
    快手把 LLM-as-Enhancer 的 SFT (目标物品 PPL 筛 CoT) 与 RL (POPO 自适应权衡语义/协同奖励) 两个卡点同时打通，并在 4 亿日活广告系统真实落地拿到正收益；是工业 LLM4Rec 方向工程完整度高、商业验证扎实、方法有迁移价值的代表作。
---
