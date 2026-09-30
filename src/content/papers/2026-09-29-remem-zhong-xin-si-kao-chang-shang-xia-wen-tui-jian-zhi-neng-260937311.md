---
title: 'ReMem: Rethinking Perception and Memory in Long-Context Recommendation Agents'
title_zh: ReMem：重新思考长上下文推荐智能体的感知与记忆
authors:
- Haohao Qu
- Yongcheng Jing
- Chun Hin Chan
- Shanru Lin
- Wenqi Fan
- Dacheng Tao
affiliations:
- The Hong Kong Polytechnic University
- Nanyang Technological University
arxiv_id: '2609.37311'
url: https://arxiv.org/abs/2609.37311
pdf_url: https://arxiv.org/pdf/2609.37311
published: '2026-09-29'
collected: '2026-09-30'
category: Agent
direction: 推荐 Agent 的感知与长程记忆优化
tags:
- Recommendation Agent
- OCR Perception
- Dynamic Memory
- GRPO
- Long-Context Reasoning
- User Modeling
one_liner: 用 OCR 感知与分块动态记忆重构推荐 Agent，平均相对提升 5.16%
practical_value: '- OCR 商品页感知可以替代 HTML 解析：在用户侧 Agent 中直接对商品页/App 截图做 DeepSeek-OCR，生成结构化商品卡片，平台无关且能过滤广告噪声，避免为每个站点维护
  HTML parser。

  - 分块动态记忆 TEM 很适合长用户行为序列：把历史按窗口分块，维护固定长度自然语言记忆，再基于最终记忆做推荐；不引入外部向量库或 KV cache 改动，线上实现简单、可
  debug、可用 prompt 约束记忆内容。

  - 多段独立记忆对话的 RL 训练可借鉴 Multi-Memory GRPO：把最终答案 advantage 传播到所有中间记忆 token；建议先 warm-up
  两个 epoch 再设置 λ=0.7，避免早期带偏记忆更新。

  - 长上下文不是越长越好：QwenLong-L1、向量记忆在超长上下文下仍明显衰减；电商用户行为序列建模可优先用可控的自然语言记忆压缩，而不是全量输入或纯向量检索。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
现有推荐 Agent 通常解析商品页 HTML，容易受噪声、广告、跨平台布局差异影响，且丢失多模态信息；同时长用户历史和多步交互轨迹会超出 LLM 上下文窗口，带来二次注意力成本。ReMem 从人类行为出发，重新设计 Agent 的“看”与“记”：像人一样看商品页截图，像人一样只记住演化的偏好抽象。

## 方法关键点
- **OCR 感知**：用 DeepSeek-OCR-2 将商品页截图解析为结构化自然语言商品卡片，替代 HTML 解析，平台无关且能过滤广告噪声。
- **时间演化记忆 TEM**：将用户交互历史分块，顺序读取每个 chunk，并更新固定长度自然语言记忆 m_t；最终只基于 m_T 和候选商品 OCR 结果生成答案。上下文有界，推理成本随历史长度线性增长。
- **Multi-Memory GRPO**：多段独立记忆对话无法直接用传统 token mask 做 GRPO，因此把最终答案 reward 的 group advantage 传播到所有中间记忆 token；目标为 JAns + λ JMem，并用 token-level KL 约束。

## 关键结果
在 Amazon Reviews 2023 构建的 MovieTV、Books、Games 三个数据集上，覆盖 Searching、Ranking、Judging 三类任务，以 Qwen3.5-9B 为骨干，对比 SASRec、BERT4Rec、P5、TokenRec、ToolRec、iAgent、QwenLong-L1、Mem0。ReMem 平均相对最强 baseline 提升 5.16%，例如 Books 上 HR@1 提升 14.55%，Games 上 HR@3 达到 0.5590。消融显示去掉 TEM 性能下降最大，说明动态记忆比普通长上下文更关键。

## 最值得记住的一句话
与其把长上下文硬塞进 LLM 或外挂向量记忆，不如让 Agent 在 token 空间维护固定长度、可读可编辑的动态记忆，再配合 OCR 感知商品页。
