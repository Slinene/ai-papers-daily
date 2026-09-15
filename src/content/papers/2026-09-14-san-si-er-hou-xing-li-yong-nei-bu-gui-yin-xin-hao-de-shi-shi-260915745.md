---
title: 'Look Before You Leap: Factual Decoding with Internal Attribution Signals'
title_zh: 三思而后行：利用内部归因信号的事实性解码
authors:
- Hayeong Ryu
- JungMin Yun
- Byeonggeuk Lim
- Sunhee Jo
- YoungBin Kim
affiliations:
- Chung-Ang University, Department of Artificial Intelligence
- Chung-Ang University, Graduate School of Advanced Imaging Sciences, Multimedia and
  Film
arxiv_id: '2609.15745'
url: https://arxiv.org/abs/2609.15745
pdf_url: https://arxiv.org/pdf/2609.15745
published: '2026-09-14'
collected: '2026-09-15'
category: LLM
direction: LLM 事实性解码 · 内部归因信号
tags:
- Hallucination
- Factual Decoding
- Internal Attribution
- Inference-time Intervention
- Probe
- LLM
one_liner: 提出 DescaPE，在推理时用内部归因信号对候选续写打分，抑制幻觉易发路径，提升事实性
practical_value: '- 推理时轻量探针监控内部归因信号，可集成到电商商品文案、搜索回答或推荐理由生成中，在 beam search / top-p
  解码时对候选打分，实时过滤容易出错的属性、价格、活动规则等事实错误，无需重训大模型。

  - 滑动窗口 MLP 消融定位事实显著层的方法可复用：业务中可对自有 LLM 做类似层重要性扫描，找出监控事实性的关键层作为线上干预点，降低全量 probing
  成本。

  - 探针只需单次前向传播近似信号，延迟仅 1.10×，适合在线生成场景；可结合业务知识库构建正负样本训练领域定制探针，与 RAG 互补，防止检索到错误信息后继续编造。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

动机：LLM 早期事实错误会在自回归生成中形成雪球效应，事后纠错或权重级干预难以在推理中提前阻断。

方法：DescaPE 通过滑动窗口 MLP 消融定位事实显著层 span，该 span 派生的内部归因信号对事实 token 选择性升高，在幻觉易发步骤出现异常尖峰。随后训练轻量探针，只需单次前向传播即可近似该信号，并将其集成到候选打分中，惩罚高风险续写、奖励事实一致的续写。探针不依赖外部检索或额外训练大模型权重，可与常规解码流程结合。

结果：在 3 个 LLM、5 个事实性基准上，相比解码时基线在多个设置下取得事实性提升，效率评估中仅增加 1.10× 延迟。代码开源。
