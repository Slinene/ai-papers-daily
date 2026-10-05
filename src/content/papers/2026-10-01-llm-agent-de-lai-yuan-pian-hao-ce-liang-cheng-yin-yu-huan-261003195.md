---
title: 'Source Preference in the Wild: How LLM Agents Favor Items by Source, and How
  to Reduce It'
title_zh: LLM Agent 的来源偏好：测量、成因与缓解
authors:
- Jonghyun Song
- Haewon Park
- Jeonghoon Shim
- Woojung Song
- Yohan Jo
affiliations:
- Graduate School of Data Science, Seoul National University
arxiv_id: '2610.03195'
url: https://arxiv.org/abs/2610.03195
pdf_url: https://arxiv.org/pdf/2610.03195
published: '2026-10-01'
collected: '2026-10-05'
category: Agent
direction: Agent 端到端搜索中的来源偏好测量与缓解
tags:
- Source Preference
- LLM Agents
- End-to-End Search
- DPO
- Bias Mitigation
- E-commerce
one_liner: LLM Agent 在端到端搜索中因来源域名产生选择偏差，即使内容一致也偏好特定站点，且可通过平衡训练与缺失信息干预缓解
practical_value: '- 在电商/Agent 评估中引入 requirement-matched pair + Bradley-Terry 方法监控来源偏差；用
  inversion rate 衡量来源偏好是否压倒 item 质量，可作为线上选品 Agent 的公平性指标。

  - 工程上，URL/域名是来源偏好的主要信息载体；隐藏文本中的来源名作用小，因此做盲评或上线时可考虑对 Agent 屏蔽 URL 或标准化来源展示，减少域名对决策的影响。

  - 精调 LLM 选择模型时，DPO/偏好数据中 source 与 preferred label 的相关性会学习成 shortcut；把 source 与 label
  的配对比例平衡到 50% 可将已有来源偏好拉回中性，避免某个电商平台/供应商被系统性偏袒。

  - 当商品属性缺失时（如价格），Agent 会用来源先验脑补；补充缺失属性或 prompt 中明确“来源与属性无关/指定某来源通常低价”可显著降低偏好，尤其后者对线上
  prompt 工程成本低，但需知道哪个来源被歧视。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
LLM agent 在真实搜索中替用户选商品、住宿、论文，来源（站点/域名）偏好可能让用户只能看到少数来源，甚至弃优选劣。以往研究未在端到端检索中控制 item 内容差异与位置，本工作量化并定位来源偏好。

## 方法关键点
- 在 WebShop、HotelQuEST、ScholarGym 三个域上用 12 个模型跑 ReAct 搜索；用 source-blind LLM judge 打需求满足标签，做 requirement-matched pair 匹配，并通过 cyclic rotation 控制展示位置；拟合 Bradley-Terry 模型得到来源偏好 τ_s，bootstrap+FDR 分类 SOURCE+/-/0。
- 控制实验：HIDDEN/URL-ONLY/ORIGINAL 三种显式来源信息，以及 swap source 标签固定内容。
- 训练实验：用 DPO 和 fake source，设置 target source 与 preferred response 的关联比例 50%/80%/20%（Balanced/Aligned/Reversed）；再用 Amazon 对比 eBay/Etsy/AliExpress 检验重新平衡能否缓解已有偏好。
- 推理实验：针对缺失价格，补同一价格、General 指令（URL 与价格无关）、Designate 指令（指定 SOURCE− 通常低价）。

## 关键结果
- 所有 12 个模型在每个域都有来源偏好，110/144 个显著组合，中位数偏好 +15/-18 pp。
- preferred source 的较差 item 在 68% 情况下被选，反过来只有 2%，中性 baseline 19%。
- 隐藏来源信息减弱偏好，恢复 URL 导致大部分差异；swap 同一内容为 preferred source 使选择率显著上升。
- DPO Aligned 让 fake source 选择率从 50% 升至 70-75%，Reversed 降至 24-28%；Amazon 已有偏好可被 Balanced 拉回 50%，Reversed 降到 18-25%。
- 补缺失价格使 SOURCE+ 选择率最多降 28.3 pp；Designate prompt 最多降 22.5 pp，General 几乎无效。

## 最值得记住的一句话
LLM Agent 把来源域名作为需求满足的 shortcut，能压倒真实 item 质量；平衡训练关联、补齐缺失信息或针对性 prompt 可有效减少这一偏差。
