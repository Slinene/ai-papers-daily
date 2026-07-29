---
title: Reward Guided Decoding for Generative Recommendation
title_zh: 奖励引导解码：面向生成式推荐的可控价值对齐
authors:
- Ruochen Yang
- Yusheng Huang
- Youfeng Zheng
- Shuang Wen
- Liangliang Chen
- Pengbo Xu
- Xiaoyu Zhang
- Shijun Wang
- Shuang Yang
- Zhaojie Liu
affiliations:
- Institute of Information Engineering, Chinese Academy of Sciences
- University of Chinese Academy of Sciences
- Kuaishou Technology
- Peking University
arxiv_id: '2607.25344'
url: https://arxiv.org/abs/2607.25344
pdf_url: https://arxiv.org/pdf/2607.25344
published: '2026-07-28'
collected: '2026-07-29'
category: GenRec
direction: 生成式推荐 · 奖励引导解码
tags:
- Generative Recommendation
- Reward Guided Decoding
- Semantic ID
- Beam Search
- Controllable Generation
- Industrial Deployment
one_liner: 提出RGD框架，将业务价值注入解码过程，解决生成推荐中似然与价值不匹配问题，无需重训模型
practical_value: '- **解码时注入业务价值，无需重训生成器**：RGD 将奖励模型作为测试时控制器，通过闭式解 `log P + R/β` 替换原始
  beam search 的排序方式。业务目标切换或权重调整只需更换奖励头或调整温度系数 β，生成器保持不变，显著降低维护成本。

  - **轻量级奖励模型设计可复用**：奖励头以 Bottleneck MLP 共享生成器解码器的隐藏状态，梯度隔离训练，仅增加少量参数和推理开销。这种插件式设计可直接纳入现有生成推荐服务。

  - **混合推理策略平衡效果与延迟**：在首层 SID 使用 pre-merge 扩大搜索空间，后续层改用 post-merge 减少计算量，在工业场景中实现与全量
  pre-merge 相近的效果，延迟增加可控，适合在线部署。

  - **缓解 beam search 的早期剪枝问题**：通过奖励引导，原本因低生成概率被剪枝的高价值候选项有机会存活，扩大有效搜索范围。在快手直播推荐中，CTR
  引导的 RGD 在线带来 +0.392% 页面点击率、+0.689% 观看时长。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：生成式推荐通过自回归生成语义ID，但解码过程由生成似然主导，导致高业务价值但低概率的候选项在 beam search 早期被剪枝。现有重排或训练时对齐方法介入过晚或需要频繁重训，无法灵活适配多变的业务目标。

**方法**：将价值引导解码形式化为 **KL 正则化奖励最大化问题**，推导出闭式最优解码分布 `Q*(j) ∝ P(j) exp(R(j)/β)`，即用奖励信号对生成概率做指数重加权。在此基础上提出 **RGD 框架**，包含三部分：
1. **奖励模型**：轻量级链式结构，共享生成器解码器特征（冻结），使用 Bottleneck MLP 头输出 log-odds 格式的奖励值，保持与生成 logit 的空间一致性。
2. **训练**：奖励模型与生成器联合训练但梯度隔离，支持单目标和多目标（如融合 CTR、LVTR 的 LTR 头）。
3. **推理**：提供 pre-merge、post-merge 和 hybrid 三种注入模式；hybrid 在首层 SID 做 pre-merge 扩展搜索，后续层用 post-merge 减少计算，平衡效果与延迟。

**关键结果**：
- 在 Amazon 三个子集上，RGD 的 Recall@10 与 NDCG@10 相较最强生成基线提升最高 **11.49%** 和 **8.30%**。
- 在快手工业直播推荐场景，相比 OneLive 基线，LTR 引导的 RGD 在 HitRate 上提升 **+1.09%**，多目标奖励均有明显改善，且相比 DPO/GRPO 等训练时对齐方法，RGD 在保持生成质量的同时实现业务指标提升，灵活性更高。
- 在线 A/B 测试中，CTR 引导的 RGD 带来页面点击率 **+0.392%**、观看时长 **+0.689%** 和观看次数 **+0.349%**。

**核心洞见**：RGD 提供了一种解耦、可解释、易切换的生成推荐价值对齐方案——生成器负责建模用户兴趣，奖励模型负责业务目标，通过解码时的闭式融合实现策略改进，而无需任何模型参数更新。
