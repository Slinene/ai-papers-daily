---
title: User Preference Induction with LLMs for Offline Top-N Recommendation Evaluation
title_zh: 利用 LLM 诱导用户偏好以改善离线 Top-N 推荐评估
authors:
- David Otero
- Javier Parapar
affiliations:
- Information Retrieval Lab, CITIC, Universidade da Coruña
arxiv_id: '2607.11354'
url: https://arxiv.org/abs/2607.11354
pdf_url: https://arxiv.org/pdf/2607.11354
published: '2026-07-13'
collected: '2026-07-15'
category: RecSys
direction: 评估方法与流行度偏差缓解
tags:
- offline-evaluation
- LLM-as-a-judge
- popularity-bias
- preference-induction
- pooling
- top-N-recommendation
one_liner: 两阶段 LLM 先归纳用户偏好再补充缺失判断，降低评估中的流行度偏差
practical_value: '- 在电商/广告推荐离线评估中，可利用 LLM 为每位用户生成偏好摘要（类似购物画像），再对多路召回融合后的 top-N 候选池中未被点击/购买的物品进行相关性补充标注，减少假阴性。

  - 采用池化思想：只对多个推荐算法输出的并集进行 LLM 打分，避免全量评定，成本可控且聚焦评价关键区。

  - 提示设计上，用“偏好叙述 + 判断指令”比直接给历史交互序列更能降低判定中的流行度先验；在实际业务中可先让 LLM 总结用户浏览/购买历史，再基于摘要评估新商品的契合度。

  - 注意适用条件：若候选池本身已被热门商品主导（如仅评估头部的精排结果），补充标注可能反而强化流行度偏差，需配合多样性控制或长尾增强策略一同使用。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
离线 Top‑N 推荐评估通常将未观测到的交互默认为不相关，这种“缺失即负例”的假设会低估系统对长尾相关物品的推荐能力，并系统性地偏向推崇热门物品的算法，导致评估失真。  

**方法关键点**  
- **两阶段 LLM 框架**：第一阶段，基于用户的历史交互和物品元数据，让 LLM 生成一个紧凑的 **诱导偏好画像（IPP）**，包含偏好叙述和判断指令；第二阶段，以该 IPP（或结合原始交互）作为上下文，让同一个 LLM 对池化候选集中无真实标签的用户‑物品对进行 **个性化相关性判断**。  
- **池化策略**：对 31 种推荐算法的 top‑N 输出取并集构建候选池，仅对池内缺失标注的样本进行 LLM 补充评判，降低计算成本并聚焦评价关键区。  
- **三种上下文方案**：仅 IPP、仅原始历史画像、IPP + 历史画像，对比不同证据对判断稳定性和流行度偏差的影响。  

**关键实验与结果**  
- 数据集：MovieLens 32M 与 Goodbooks‑10k，抽样 500 用户以保证实验效率与统计一致性。  
- 在 MovieLens 上，**IPP+Profile 方案** 使系统有效性排名与物品流行度排名的 Kendall τ 相比人类标注基线 **下降约 0.20**（Δτ = –0.2000），明确缓解了流行度偏差；同时 LLM 判断的系统级别排名与实际人类标注的排名保持高度一致（τ 最高达 1.000）。  
- 实例级 MAE 在 0.62–1.11 之间，虽非完美，但系统级排序稳定，表明 LLM 判断可作为实用的扩充信号。  
- 在 Goodbooks 上，因物品目录本身全为头部书，补充标注未降低反而增加了流行度耦合（Δτ 多为正值），验证了方法效果依赖于候选池的流行度分布。  

**核心发现**  
LLM 基于用户偏好归纳的补充判断能够在长尾物品有机会进入候选池时有效削弱流行度偏差，提升离线评估的公平性；但在纯头部流量场景下可能适得其反，提示该方法需与候选池的多样性控制结合使用。
