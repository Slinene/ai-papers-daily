---
title: 'EAGER: Enrich-and-Align Generative Query Recommendation from Clicked Items
  in E-commerce Search'
title_zh: EAGER：电商搜索点击商品到查询的生成式推荐两阶段框架
authors:
- Shuwei Yuan
- Mingqian Ding
- Luxin Liu
- Rong Xiao
- Xiaoyi Zeng
affiliations:
- Alibaba International Digital Commerce Group
arxiv_id: '2609.07143'
url: https://arxiv.org/abs/2609.07143
pdf_url: https://arxiv.org/pdf/2609.07143
published: '2026-09-07'
collected: '2026-09-09'
category: QueryRec
direction: 生成式查询推荐 · GRPO 对齐
tags:
- EAGER
- I2Q
- GRPO
- Query Recommendation
- Preference-Aware Reward
- Curriculum Learning
one_liner: 两阶段生成式 I2Q 框架：SFT 课程+自蒸馏扩意图覆盖，GRPO 混合奖励对齐点击与业务规则
practical_value: '- 多源 intent-ordered 监督构造：把点击 query、post-click search query、LLM 扩展
  query 拼成弱有序 label，并用同一个 PARM 给 LLM query 打分排序；可复用到电商搜索、push 文案等数据稀疏但需要覆盖多意图的生成任务。

  - 课程学习拆法值得抄：I2Q → Enhanced I2Q（加 rationale）→ UI2Q → Enhanced UI2Q。论文里 rationale
  最大提升 APD（多样性），用户上下文最大提升 SoftHR@1（相关性），业务上可据此分配数据/训练资源，而不是混训。

  - GRPO hybrid reward：规则 reward 管格式、数量、流畅、重叠、安全黑名单；PARM 用生成式 yes/no 的 1-p(no) 作为点击偏好
  reward。PARM 同时用于离线数据筛选和 RL reward，保持训练一致，且 position-aware 采样去掉位置偏差；这套可直接迁移到生成式 query
  suggestion / 广告文案 RL。

  - 部署上作为第三条召回通道，与 log-based、dense retrieval 共用 ranker，长尾补覆盖、头部同台竞争；vLLM 独立多采样生成 10
  条，VRAM 压力低于 beam search。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：电商推荐流中，用户点击商品后返回 feed，系统给出查询建议承接即时搜索意图。传统 log 挖掘受限于历史 query 池，长尾/新商品会退化到头部通用词；直接调 LLM 生成流利但泛化、无个性化、不满足业务合规。核心矛盾是单一商品点击 vs 多意图查询集合，以及点击、转化、格式、多样性等多目标难以用 SFT 同时优化。

**方法**：EAGER 两阶段。阶段一 SFT 做 enrichment：构造多源意图有序监督 [q_click; Q_post; Q_llm]，其中 LLM 扩展 query 用 PARM 点击预测器打分排序消噪；设计四阶段课程 I2Q → Enhanced I2Q（teacher rationale）→ UI2Q → Enhanced UI2Q；加入 diversity regularization 和 self-distillation（高温/Top-p 采样回灌）扩生成空间。阶段二 GRPO 对齐：hybrid reward = α*规则奖励（数量、长度、流畅、重叠、多样性、安全黑名单）+ β*PARM 偏好 reward（1-p(no)）。PARM 从曝光日志 position-aware 采样训练，统一离线筛选和在线 reward。

**结果**：基于 Qwen3-1.7B，SoftHR@1 77.96、APD 72.96、Distinct-2 83.04，显著超过闭源/开源基线；课程贡献 SoftHR@1 +6.57、APD +6.97；GRPO 主要提升 Rule（9.16 vs 7.21），说明其用于合规而非相关性；PARM 与生产 ranker top-1 一致率 79.8%。9 天线上 A/B：UCTR +0.83%、PCTR +1.28%，DAC +2.98%、Pay Count +3.49%、L2P +2.38%。最值得记住：意图覆盖与部署对齐是互补目标，先离线 SFT 扩空间，再 RL 约束到可上线。
