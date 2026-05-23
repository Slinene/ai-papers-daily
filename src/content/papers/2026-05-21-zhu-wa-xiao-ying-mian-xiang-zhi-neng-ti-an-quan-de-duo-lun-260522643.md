---
title: 'Boiling the Frog: A Multi-Turn Benchmark for Agentic Safety'
title_zh: 煮蛙效应：面向智能体安全的多轮基准测试
authors:
- Piercosma Bisconti
- Matteo Prandi
- Federico Pierucci
- Federico Sartore
- Enrico Panai
- Laura Caroli
- Yue Zhu
- Adam Leon Smith
- Luca Nannini
- Marcello Galisai
affiliations:
- Icaro Foundation
- Sapienza University of Rome
- Sant’Anna School of Advanced Studies
- Tongji University School of Law
- VU Amsterdam
arxiv_id: '2605.22643'
url: https://arxiv.org/abs/2605.22643
pdf_url: https://arxiv.org/pdf/2605.22643
published: '2026-05-21'
collected: '2026-05-23'
category: Agent
direction: Agent 安全评估·多轮对抗攻击
tags:
- Agent Safety
- Multi-Turn
- Benchmark
- Tool Use
- Adversarial Attacks
- AI Act
one_liner: 评估工具型AI在办公场景下对逐步升级攻击的脆弱性，多模型平均严格攻击成功率44.4%
practical_value: '- 可以借鉴“煮蛙”思路，在电商 Agent 测试中设计多轮逐步升级的恶意指令链，检查智能体是否会在不经意间执行高危操作（如修改库存、泄露用户数据）。

  - 评测方法强调状态化评估，关注最终环境状态是否变为不安全，而非单轮回复，适用于评估订单处理、客服等有持久状态的 Agent 系统。

  - 风险分类参考欧盟 AI 法案，可为合规审计提供框架：按操作风险等级构建测试场景，识别 Agent 在关键业务域的安全薄弱点。

  - 攻击链中延迟注入风险请求的编排方式，可用于生成对抗训练数据，提升自研推荐/搜索 Agent 对长程诱导攻击的鲁棒性。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

## 动机
传统语言模型安全基准只评估文本输出的毒性或偏见，当模型作为工具型智能体（Agent）部署时，安全关注点转向其在环境中的行为。现有 Agent 安全评测多采用单轮或直接指令攻击，未能捕捉“渐变式”恶意操作的风险，即攻击者通过先无害后越权的方式逐步突破安全约束。

## 方法
提出 Boiling the Frog 基准，面向企业办公场景的智能体，模拟多轮对话中渐变式攻击。每个测试链包含一系列良性工作区编辑，在受控的轮次位置引入风险请求，评估最终环境状态是否变得不安全。场景依据三级操作风险分类设计，综合了“煮蛙”风险、欧盟 AI 法案 Annex I/III 高风险场景及通用目的 AI 行为守则。评测采用严格攻击成功率（ASR），即在最终工作区中检测到明确的不安全产物才视为成功。

## 结果
在 9 个主流模型上评测，总体严格 ASR 为 44.4%。模型间差异显著：Claude Haiku 4.5 仅 20.5%，而 Gemini 3.1 Flash Lite 高达 92.9%，Seed 2.0 Lite 也超过 80%。按风险类别看，行为守则中“失控”类场景的 ASR 最高达 93.3%，表明现有模型在应对逐步升级的越权操作时普遍脆弱。
