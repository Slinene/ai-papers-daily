---
title: Emotion Understanding in Streaming Video with Trajectory-Aware Reliability
title_zh: 流式视频情感理解的轨迹感知可靠性框架
authors:
- Qingsong Wang
- Qigong Lei
- Zitong Wang
- Bohan Yu
- Zhiang Dong
- Jian liu
- Weiqiang Wang
- Chang Yao
- Jingyuan Chen
affiliations:
- Zhejiang University
- Ant Group
- School of Software Technology (Ningbo), Zhejiang University
arxiv_id: '2608.26786'
url: https://arxiv.org/abs/2608.26786
pdf_url: https://arxiv.org/pdf/2608.26786
published: '2026-08-27'
collected: '2026-08-30'
category: Multimodal
direction: 流式多模态情感计算 · 可靠性门控
tags:
- Streaming Video
- Emotion Understanding
- Trajectory-Aware Reliability
- Multimodal
- Selective Inference
one_liner: 提出轨迹感知可靠性框架 TRACE，基于流式信念的稳定性与切换模式选择性调用多模态重推理，优化在线情感理解的准确率-成本权衡
practical_value: '- 在线推荐/排序场景中，用户行为流式到达，可借鉴 TRACE 的轨迹稳定性信号：不仅看当前预测置信度，还监控近期预测分布的熵、类切换频率，当轨迹不稳定时触发重排或调用更重模型。

  - 将系统拆成低延迟主路径与高成本上下文重推理路径，通过可靠性分数做门控，能有效平衡实时性与准确性，适合广告/搜索中延迟敏感但需质量保障的模块。

  - 对 LLM Agent 或 RAG 流程，在对话/推理中间步骤记录 belief 轨迹（如生成候选答案的分布），若检测到频繁切换则触发工具调用、检索或重新推理，避免过早
  commit。

  - 可靠性估计不必依赖额外标签，可从置信度、熵、稳定性等无监督信号合成，落地成本低，适合快速实验。'
score: 6
source: arxiv-cs.MM
depth: abstract
---

**动机**：
- 现有视频情感理解多为离线分类，实时交互需从流式不完整证据做在线决策。
- 单一高置信度前缀预测仍可能不可靠，若底层情感信念轨迹不稳定或频繁类切换。

**方法关键点**：
- 提出 TRACE 框架，从流式音频前缀构建低延迟情感信念。
- 可靠性估计融合置信度、熵、稳定性与类切换模式。
- 选择性调用视觉、文本和邻接话语进行上下文信念重解释；稳定案例走低延迟在线路径，不确定案例升级到多模态推理。

**关键结果**：
- 在 StreamMER、MELD、MER2024 上验证，提升准确率-成本权衡，保留大部分全上下文增益同时大幅减少不必要的上下文推理。
