---
title: Who Pays the Price? Stakeholder-Centric Prompt Injection Benchmarking for Real-world
  Web Agents
title_zh: 谁来买单？面向真实 Web Agent 的利益相关者中心化提示注入基准测试
authors:
- Zihao Wang
- Yiming Li
- Yutong Wu
- Zheyu Liu
- Kangjie Chen
- Fok Kar Wai
- Pin-Yu Chen
- Vrizlynn L. L. Thing
- Bo Li
- Dacheng Tao
affiliations:
- Nanyang Technological University, Singapore
- ST Engineering, Singapore
- IBM Research, USA
- University of Illinois Urbana-Champaign, USA
arxiv_id: '2606.13385'
url: https://arxiv.org/abs/2606.13385
pdf_url: https://arxiv.org/pdf/2606.13385
published: '2026-06-11'
collected: '2026-06-12'
category: Eval
direction: Agent 安全性评估 · 利益相关者建模
tags:
- prompt injection
- web agents
- benchmark
- security
- stakeholder-centric
one_liner: 提出以利益相关者（用户、卖家、平台）为核心的提示注入安全基准，揭示危害的不对称性和异质失败模式。
practical_value: '- 在电商推荐 Agent 安全评估中引入利益相关者视角，区分对用户、卖家、平台的损害，不仅看攻击成功率，还要联合任务偏离度（TDR）和行为异常率（BIR），全面捕捉隐蔽操纵（如卖家偏向）和平台扰乱。

  - 利用 ASR-TDR 矩阵识别“Stealthy Parasitism”等失败模式：高 ASR 低 TDR 的攻击可在不破坏用户体验的情况下实现对抗目标（如商品推荐偏向），需特别关注。

  - 注意注入内容与用户意图的语义对齐度：相似度越高，越容易在任务不被察觉的情况下成功，防御时可尝试降低攻击目标的语义对齐程度或引入不一致的环境线索。

  - 多模态注入（产品图片）能影响 Agent 决策，且评分信号不能完全消除视觉影响，需考虑视觉通道的鲁棒性。'
score: 8
source: arxiv-cs.MM
depth: full_pdf
---

**动机：** 基于 LLM 的 Web 智能体在电商等场景中自主执行搜索、比价、交易，但它们极易受到提示注入攻击——隐蔽在网页内容（如评论、评分）中的恶意指令可操纵其行为。现有安全基准多从攻击者角度评估技术可行性，忽略了受害者的异质性：同一攻击对用户、卖家、平台造成的伤害可能截然不同，并且失败模式也存在多种形态。因此亟需一个以利益相关者为中心的评估框架，真实反映部署中的风险。

**方法关键点：**
- 提出 **StakeBench**，围绕受伤害的实体（用户、第三方卖家、平台）组织攻击分类：定义 12 种具体攻击目标，涵盖强制购买、泄露信息、评价操纵、订单膨胀、工作流绕过等。
- 构建 22 个可复用的攻击模板（9 个直接注入、13 个间接注入），在电商环境 OneStopMarket（VisualWebArena 的一部分）中实例化为 264 个可执行测试用例，覆盖 12 个产品类别。
- 设计 **多维评估指标**：攻击成功率（ASR）、任务偏离度（TDR）、行为异常率（BIR）。ASR 与 TDR 联合定义四种失败状态：复合失败（高 ASR + 高 TDR）、隐蔽寄生（高 ASR + 低 TDR）、错位中断（低 ASR + 高 TDR）、鲁棒行为（低 ASR + 低 TDR）。
- 严格限制攻击者能力：仅能控制评论、评分、元数据等现实可接触的渠道，不能篡改系统提示或平台基础结构。

**关键实验：**
- 评估在两个代表性 Web Agent 系统（NanoBrowser、BrowserUse）和两个 LLM 骨干（GPT-5、Gemini-2.5-Flash）上进行，3,168 次攻击记录。
- 间接注入下，所有配置均无法完全抵抗任何一个攻击目标；平均 ASR 在 41.67% 至 68.16% 之间。
- 卖家目标攻击 ASR 最高（约 60%），用户目标 TDR 最低（隐蔽性强），平台目标 BIR 更高（执行不稳定）。
- 注入目标与用户意图语义高度相似时，ASR 高达 70–79% 且 TDR 低，呈现隐蔽寄生；语义偏离越远，越易转向错位中断。
- 周边线索（如评分与恶意评论不一致）可在某些骨干下大幅降低攻击成功率（GPT-5 从 55.56% 降至 19.44%）。
- 视觉操纵初步实验：仅修改产品图片就能显著影响 Agent 的选择，且评分信号不能完全抵消。

**最值得记住的一句话：** 提示注入对 Web Agent 的危害不是单一标量，而是受受害者身份、注入目标与用户任务的语义对齐、以及 Agent 架构共同作用的分布化风险，必须用多维指标和利益相关者视角才能全面揭示。
