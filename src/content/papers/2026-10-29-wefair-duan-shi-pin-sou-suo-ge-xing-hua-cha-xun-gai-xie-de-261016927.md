---
title: 'WeFair: Fidelity-Aware Alignment from Human Feedback for Personalized Query
  Rewriting in Short-Video Search'
title_zh: WeFair：短视频搜索个性化查询改写的保真度感知对齐
authors:
- Yingtao Ren
- Aolin Li
- Cheng Cheng
- Huiyun Hu
- Huasheng Liang
- Baoxing Xie
- Jun Yuan
- Haijun Wu
- Yiwei Fu
- Chenxing Wang
affiliations:
- Weixin Group, Tencent
- East China Normal University
arxiv_id: '2610.16927'
url: https://arxiv.org/abs/2610.16927
pdf_url: https://arxiv.org/pdf/2610.16927
published: '2026-10-29'
collected: '2026-11-02'
category: QueryRec
direction: 个性化查询改写 · 保真度感知 RLHF
tags:
- query rewriting
- personalization
- RLHF
- DPO
- GRPO
- intent drift
one_liner: 用保真度分级的 SFT-DPO-GRPO 对齐人类反馈，训练紧凑个性化 query 改写模型并显著缓解意图漂移
practical_value: '- 对于 query 改写/生成式推荐，建议把真实 session 中相邻 query 改写对和“不需要改写”保留样本同时纳入
  SFT，并用 LLM 多裁判筛选，能显著提升改写决策准确率和降低 intent drift。

  - 三阶段对齐可复用：SFT 课程用低精度宽覆盖数据打底，DPO 用点击/消费偏好做相对排序，最后 GRPO 奖励只给与真实用户改写或保留完全匹配的目标；避免使用相似度/retrieval/RM
  等辅助奖励，它们会降低 advantage purity 和最终准确率。

  - 线上部署采用 direct 输出 + 用首个 token 的保留概率做 gating，决定是否只用原 query 做检索排序；这是低成本集成改写的方式。2B
  模型 7.6 tokens、0.316s 足够支撑百万级日请求。

  - 若要评估改写质量，可定义 Consistent Recall/Precision、Intent Drift Rate、Hallucination Rate
  和 Preservation Decision Recall，结合 LLM judge 与人工标注；该指标组合更适合搜索会话中的意图保真评估。'
score: 9
source: huggingface-daily
depth: full_pdf
---

**动机**  
短视频搜索 query 短且歧义，需在严格延迟下还原用户即时意图；现有 LLM 改写常靠后续消费反馈对齐，易偏向高互动内容导致 intent drift。如何用不同保真度的人类反馈训练紧凑改写模型，成为关键问题。

**方法关键点**  
- 数据构建：从搜索会话挖掘真实 query、用户改写、保留样本；规则过滤 + 三个 LLM 多数投票筛选 context-supported reformulation；形成 demonstration / preference / verification 三个监督池。
- 训练三阶段：curriculum SFT（context-to-query → CoT 推理 → 直接改写/保留）；DPO 用后续消费结果构建偏好对；GRPO 用严格 exact match 奖励（改写或保留）做最终验证，防止意图漂移。
- 部署：2B direct 输出平均 7.6 tokens，P95 模型延迟 81ms，端到端 +16ms；改写/保留通过首个 token 概率 gating 控制检索与排序。

**关键实验结果**  
离线：WeFair-2B Consistent Recall 83.95%，Overall Acc 72.81%，优于 DeepSeek/Gemini/Qwen 等大模型和 WeWrite/AWHCP；Intent Drift Rate 降至约 1/3。消融显示 SFT→GRPO 提升最大，完整序列最佳；strict verification 在 advantage purity 和准确率上优于 similarity、consumption、RM 等辅助奖励。在线 10 天 A/B：CTR +2.951%，有效观看 VV>10s +2.593%，query 改写率 -2.350%（P<0.01）。

**最值得记住的一句话**  
不同训练阶段应匹配不同保真度的监督：SFT 能容忍宽泛低精度数据，DPO 用消费偏好做相对排序，最终 GRPO 只信 exact-match 的真实改写/保留目标，可显著降低意图漂移。
