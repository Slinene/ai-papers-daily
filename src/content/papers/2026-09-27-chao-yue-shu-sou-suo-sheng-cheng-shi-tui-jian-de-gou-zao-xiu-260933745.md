---
title: 'Beyond the Beam: Constructive Repair and Candidate Completion for Generative
  Recommendation'
title_zh: 超越束搜索：生成式推荐的构造性修复与候选补全
authors:
- Zijun Zhao
- Peng Zhang
- Gang Zhang
- Yuanchi Ma
- Hui He
- Zhendong Niu
affiliations:
- Beijing Institute of Technology
- China Meteorological Administration
- Tsinghua University
- Singapore Management University
arxiv_id: '2609.33745'
url: https://arxiv.org/abs/2609.33745
pdf_url: https://arxiv.org/pdf/2609.33745
published: '2026-09-27'
collected: '2026-09-29'
category: GenRec
direction: 生成式推荐 · Semantic ID 修复与候选补全
tags:
- Generative Recommendation
- Semantic ID
- Beam Search
- Assignment Repair
- Candidate Completion
- Catalog Update
one_liner: 用可行性区间刻画identifier分配修复，结合最小叶子替换与候选补全提升生成式推荐新item召回
practical_value: '- 目录扩容时不要只依赖 beam rerank：用保留前缀上界 `U_i=已评估前缀 logprob + item correction`
  和 item-level 协同预测器对 beam 外物品做候选补全，预算控制在 20/80 个额外评估即可显著提升 Recall/NDCG。

  - 旧 Semantic ID 不一定要推翻重训：先按 Theorem 1 的区间条件判断 assignment repair 可行性，再用 integral
  min-cost flow 求最小叶子替换，保留旧 ID 的同时让新 item 进入 Top-K，降低重训与历史兼容性风险。

  - 合并生成概率与协同分数为单一排序得分，并对新 item 做校准（λ、γ、b 控制 scale/shift），避免冷启动新 item 被生成分数压制；校准参数在验证集上选。

  - 停止条件 `t_K > max U_i` 可给出全局 Top-K 证书；线上可做成本自适应：预算内满足才输出证书，否则返回已评估最高分。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

生成式推荐通过生成 Semantic ID 返回商品，但目录扩容后，新 item 可能具备有效 ID 和强协同信号，却因 beam search 未覆盖而无法被 rerank 找回。已有方法多聚焦于选择某个 assignment 并测量效果，缺少对可行分配家族的完整刻画，推理阶段也缺少超越初始 beam 的系统机制。

**方法关键点**：
- 理论：固定 generator 和输入编码、保留旧 item ID。先给出 output-invariance certificate，识别所有合法分配下输出不变的 query。在 common effective prefix 下，Theorem 1 给出目标 item 可被 Top-K 恢复的充要条件：`a_S(y)+g_S(y)<K` 且 `r_S+δ_S(y)≤m≤C_S−max{0,R_S(y)−K}`，分别约束排序竞争、前缀支持和容量上界。
- 构造：对可行 (S,y)，用 integral min-cost flow 求解最小叶子替换，保留旧 ID；将局部修复组合为共享映射，用固定 warm-up generator 在训练集上按 NDCG@10 选择最优共享映射，再固定映射微调生成器。
- 推理：合并生成似然 `s_θ(i|h)` 与 item-level ridge predictor 的校准 correction `d_i` 为最终得分 `F`。利用已评估前缀的上界 `U_i=u_i+d_i` 对 beam 外候选做 bounded candidate completion；当 `t_K > max U_i` 时输出带全局 Top-K 证书的结果。

**关键实验**：
在 Amazon Beauty/Tools/Toys 上，用 T5 和 decoder-only LC-Rec 两种 backbone、3 个随机种子。BB 在全部数据集上 Recall@10、NDCG@10 领先；相比每个数据集最好的生成 baseline，Recall@10 提升 15.5–46.3%，NDCG@10 提升 15.2–44.4%。有限目录穷举验证中，完整构造在 1,816 个可行 count/cutoff 条件全部成功，删除 support 或计数边界会产生假可行性。消融显示合并评分与候选补全在所有数据集上提升 NDCG@10；shared construction 在 Beauty/Toys 上提高新 target NDCG@10 3.82/9.56%，并将 Top-20 认证率提升 3.54/9.87 个百分点、额外评估减少 2.86/7.90%。

最值得记住的一句话：生成式推荐的新 item 召回不能只靠换 ID 或重训；用可行性区间+最小叶子替换修复分配，再用前缀上界补全 beam 外候选，是低成本的系统性解法。
