---
title: The Dynamic Verifiable Multi-Agent Human Agentic Loyalty Loop (DVM-HALL) Model
  and the Net Human-Agent Score (NHAS) in Autonomous Commerce
title_zh: 自治商务中的动态可验证多智体人类代理忠诚循环（DVM-HALL）模型与净人类-代理评分（NHAS）
authors:
- Sai Srikanth Madugula
- Peplluis Esteva de la Rosa
- Daya Shankar
affiliations:
- School of Technology, Woxsen University, Hyderabad, Telangana 502345, India
- Universitat de Girona, 17004 Girona, Spain
arxiv_id: '2607.13998'
url: https://arxiv.org/abs/2607.13998
pdf_url: https://arxiv.org/pdf/2607.13998
published: '2026-07-15'
collected: '2026-07-16'
category: MultiAgent
direction: 多智体协作 · 自治商务忠诚度模型
tags:
- Multi-Agent
- Autonomous Commerce
- Loyalty
- Human-Agent Alignment
- Trust Calibration
- Blockchain
one_liner: 提出多智体忠诚模型与可审计指标，将人类情绪、机器效用、信任、委托与链上执行风险联合建模品牌选择
practical_value: '- 在构建面向代理执行的推荐或广告系统时，可将品牌选择拆解为人类情绪效用（情感资产、满意度、价值感知）与代理机器效用（API可用性、延迟、交付可靠度）的加权融合，通过动态信任和委托系数控制代理自主权。

  - 对涉及链上交易或可验证执行的场景，可引入 gas 成本、滑点、MEV 暴露、预言机风险、智能合约漏洞等变量作为代理偏好的负向预测因子，量化执行风险对最终选择的影响。

  - NHAS 可以作为在线评估人与代理对齐程度的审计指标：组合偏好对齐、经济效率、执行可靠性和解释质量，结合用户反馈与执行日志，用于代理行为的 post-hoc
  监控或奖励信号，区分微小次优决策与关键失败（如超支）。

  - 动态信任更新公式（基于对齐、执行质量、解释质量、损失等递归更新）可直接部署于代理系统，实现“过度信任→惩罚→降低委托”的自动校准，避免代理失控。'
score: 10
source: arxiv-cs.AI
depth: full_pdf
---

## 动机
传统客户忠诚度模型（如 NPS）建立在“人直接执行购买”的假设上。随着 AI 代理从被动推荐转向可自主执行交易的目标驱动 Agent，品牌选择变成人、代理与品牌三方博弈：人的情绪偏好不再直接驱动交易，代理的机器体验和可验证执行风险成为新变量。现有模型无法解释这种“算法有限理性”与“构建出的自主权”，亟需一个能同时建模人类情感、代理效用、信任校准与委托程度的动态框架。

## 方法关键点
- **DVM-HALL 选择模型**：品牌选择概率由组合效用 softmax 决定。组合效用 = (1-δ) × 人类效用 + δ × 信任系数 × 代理效用 - 政策惩罚项。人类效用含情绪资产、满意度、感知价值、规范匹配；代理效用含机器体验特征（API 可用性、延迟等）减去执行风险（gas 费、滑点、MEV、预言机风险、合约风险等）。
- **动态信任与委托更新**：信任通过递归公式更新，输入包含对齐度、执行质量、解释质量、损失、硬约束违反；委托系数基于修订后的信任、NHAS、任务风险和控制水平自适应调整，保证代理行为收敛。
- **NHAS 审计指标**：每笔交互用偏好对齐、经济效率、执行可靠性、解释质量加权得分，经风险加权（对金融损失、隐私泄漏、合规失败施加惩罚）后取均值，得到 -100～100 的对称评分，作为代理对齐程度的可审计信号。
- **验证计划**：提出三个阶段的实证设计——控制人-代理购物实验、多代理市场仿真、DeFi/代币化忠诚度测试床，但论文本身只给出了理论推导与 Python 模拟（附仓库）。

## 关键结果（模拟）
- NHAS 期望值边界为 E[NHAS] = 70 - 170h，其中 h 为代理幻觉率；当 h≥0.45 时 NHAS 变负，触发委托系数 δ 归零，系统退化为传统人工搜索模式。
- 在高委托、高信任场景下，机器体验和链上风险变量完全主导品牌概率，情绪资产仅通过用户约束间接作用。
- 模拟市场冲击显示：系统性预言机/API 故障使 NHAS 快速降至负值，验证了模型的动态风险感知能力。
