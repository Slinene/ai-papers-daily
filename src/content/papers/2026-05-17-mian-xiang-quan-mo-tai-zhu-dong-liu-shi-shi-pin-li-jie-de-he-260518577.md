---
title: 'OmniPro: A Comprehensive Benchmark for Omni-Proactive Streaming Video Understanding'
title_zh: 面向全模态主动流式视频理解的综合基准 OmniPro
authors:
- Ruixiang Zhao
- Jie Yang
- Zijie Xin
- Tianyi Wang
- Fengyun Rao
- Jing LYU
- Xirong Li
affiliations:
- Renmin University of China
- WeChat Vision, Tencent Inc.
arxiv_id: '2605.18577'
url: https://arxiv.org/abs/2605.18577
pdf_url: https://arxiv.org/pdf/2605.18577
published: '2026-05-17'
collected: '2026-05-24'
category: Multimodal
direction: 全模态主动流式视频理解基准与评估
tags:
- benchmark
- streaming video
- proactive
- omni-modal
- audio-visual
- evaluation
one_liner: 首个统一评估全模态感知、主动响应与多任务能力的流式视频基准，揭示音频利用差异、长程退化与非语音音频薄弱
practical_value: '- 双模式评估协议（Probe/Online）可直接迁移至直播带货场景的智能客服主动干预评估：Probe 模式验证时机准确性，Online
  模式测量线上自主决策能力

  - 84% 样本依赖音频信号的发现提醒电商视频理解必须融合语音与非语音音频，避免纯视觉方案漏判用户意图

  - 长程性能退化（随时间显著下降）指向实际系统需引入记忆或状态刷新机制，以支持长达数小时的直播流

  - 非语音音频（环境音、背景声）是当前模型最弱项，电商场景中如店铺背景噪声、产品操作声可能被忽略，需针对性增强'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：全模态主动流式视频理解（omni-proactive）要求模型从连续音视频流中自主决定何时说话和说什么，但现有基准依赖视觉信号、使用轮询或固定时间戳，且任务覆盖窄，无法可靠评估和区分这类模型。

**方法**：推出 OmniPro 基准，包含 2700 个人工验证样本，覆盖 9 个子任务、3 个认知层级和 6 类基础视频理解能力；84% 样本需要音频（语音或非语音），并标注模态隔离标签以支持细粒度多模态分析。设计双模式评估协议：Probe 模式在 ground-truth 触发时刻前后查询模型以评估内容理解，Online 模式让模型在流式输入中自主决定响应时机。

**关键结果**：在 11 个代表性模型上评估发现：① 音频提供一致增益但模型间利用率差异巨大；② 性能随时间显著退化，模型长期鲁棒性差；③ 非语音音频感知是最薄弱维度。
