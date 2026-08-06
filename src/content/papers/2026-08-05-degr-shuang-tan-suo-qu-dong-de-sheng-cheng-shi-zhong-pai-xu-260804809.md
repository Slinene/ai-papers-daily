---
title: 'DEGR: Dual Exploration-Driven Generative Re-Ranking for Adaptive Cross-Request
  Context Bridging'
title_zh: DEGR：双探索驱动的生成式重排序实现自适应跨请求上下文桥接
authors:
- Binglei Zhao
- Xuanhua Yang
- Xiwei Zhao
- Sulong Xu
affiliations:
- JD.com
arxiv_id: '2608.04809'
url: https://arxiv.org/abs/2608.04809
pdf_url: https://arxiv.org/pdf/2608.04809
published: '2026-08-05'
collected: '2026-08-06'
category: GenRec
direction: 生成式重排序 · 探索性奖励模型
tags:
- Generative Re-Ranking
- Dual Exploration
- Exploratory Reward
- RL
- Multi-Head Decoding
- E-commerce
one_liner: 提出双探索生成式重排序，通过混合监督-强化学习与探索性奖励模型自适应平衡即时与探索价值，提升电商推荐效果
practical_value: '- **探索性奖励模型设计**：将“序列探索价值”量化为可学习奖励，结合上游 pCTR 动态调整权重，在低质量候选集时自动优先保留浏览潜力，可直接迁移到搜索推荐的重排阶段，尤其适用于冷启动或召回质量波动场景。

  - **混合优化范式（SL + EDC + AR-ORPO）**：监督学习保持在线分布稳定性，探索多样性约束（EDC）缓解并行解码头的语义坍缩，AR-ORPO
  利用奖励值作为软权重建构偏好列表替代硬排名，比标准 ORPO/DPO 更鲁棒，适合生成式推荐或 Agent 策略优化中的对齐训练。

  - **并行解码与高效采样**：多头并行生成 + 群组束搜索/启发式混合采样，将序列生成复杂度从 O(M) 降至 O(M/K)，线上 TP99 仅增加 3.2ms，可直接用于低延迟的实时重排或对话式推荐生成。

  - **跨请求上下文桥接思路**：显式建模当前请求的探索行为对未来点击/浏览的影响，可在精排或重排阶段加入类似“未来请求增益”辅助任务，提升长期用户活跃度。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：工业推荐重排受限于上游固定供给，当候选集整体低质时，传统即时收益优化（CTR/CVR）陷入局部最优，忽视浏览沉淀带来的后续转化机会。该工作提出重排应主动平衡即时价值与探索价值，在低质供给下优先保留探索性曝光，为后续请求创造上下文桥接。

**方法关键点**
- **探索性奖励模型**：采用 DIN+自注意力+MMoE 架构，同时预测项目级即时奖励和序列级探索奖励；探索奖励通过五级未来行为标签（终止、无效探索、潜在兴趣、即时匹配、深度探索）建模，并根据上游最大 pCTR 动态调整样本权重，在低 pCTR 时鼓励探索，高 pCTR 时侧重即时收益。
- **高效生成器**：编码器-解码器结构，解码器使用多头并行生成（K=6）减少推理步数，同时施加探索多样性约束（EDC）惩罚同批次头的嵌入余弦相似度，防止生成项过度同质。
- **混合探索与优化范式**：三个损失联合训练——监督交叉熵保持在线分布，EDC 保持多样性，自适应奖励加权 ORPO（AR-ORPO）将采样序列按奖励量化排序并构造软权重，最大化高奖励序列概率。
- **多机制采样**：融合群组束搜索（Gumbel 噪声+组内去重）与启发式加权扰动采样，生成丰富轨迹以强化 RL 探索。

**关键结果**
- 离线：在 Taobao 和 JD 数据集上，DEGR 全面超越 PRM、PIER、GRN、CMR、NAR4Rec、MG-E、GReF 等基线，京东 GAUC 从 0.6403 提升至 0.6486，MAP@2 提升 0.5pp。
- 在线 A/B（JD 首页）：UCTR 提升 1.22%，PV 提升 0.20%；低 pCTR 区间 NER（下刷率）和 NCR（下游点击率）均有显著提升，验证了跨请求上下文桥接效果。
- 消融与效率：探索奖励移除、EDC 去除、ORPO 替换后指标下降明显；并行解码使推理时间提升约 18%，线上 TP99 仅增 3.2ms，可满足工业实时性要求。
