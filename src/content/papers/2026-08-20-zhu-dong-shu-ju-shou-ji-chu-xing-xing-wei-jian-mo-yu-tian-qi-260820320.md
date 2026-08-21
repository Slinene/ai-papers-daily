---
title: An Agentic Approach for Active Data Collection, Travel Behavior Modeling, and
  Weather-Sensitive Demand Prediction
title_zh: 主动数据收集、出行行为建模与天气敏感需求预测的智能体方法
authors:
- Narges Ahmadi
- Yubo Jiao
- Jônatas Augusto Manzolli
- Jiangbo Yu
- Luis Miranda-Moreno
affiliations:
- Department of Civil Engineering, McGill University
arxiv_id: '2608.20320'
url: https://arxiv.org/abs/2608.20320
pdf_url: https://arxiv.org/pdf/2608.20320
published: '2026-08-20'
collected: '2026-08-21'
category: Agent
direction: LLM 行为预测 · 多 Agent 工作流
tags:
- agentic workflow
- LLM prediction
- multimodal
- prompt engineering
- behavior modeling
- active data collection
one_liner: 三 Agent 工作流整合对话式调查、数据处理与 LLM 出行预测，多模态最佳达 71.5% 准确率
practical_value: '- 行为预测/用户偏好建模：将“习惯性历史信息”类比用户历史点击/购买序列，加入 prompt 可稳定提升准确率；在生成式推荐或排序中优先注入用户行为特征，而非仅依赖
  persona 或角色描述。

  - Prompt 策略：采用“专家”角色描述优于一般“角色扮演”；persona 只在缺少行为历史时收益更大；few-shot 仅需少量示例即可提升，示例过多边际收益递减，适合线上
  prompt 成本控制。

  - 多模态信号：用用户实际看到的图像（商品图、场景图）作为视觉上下文，可使 LLM 预测提升（最佳 71.5%），建议在多模态商品推荐或内容理解中复用同一视觉输入。

  - Agent 工作流可审计性：将数据收集、结构化、预测拆分为三个 agent，便于追踪数据版本和模型决策，适合在电商/广告场景构建数据飞轮与离线评估管线。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

动机：旅行行为研究中数据收集与预测建模常被割裂，难以形成可审计的闭环；需要一种将对话式调查、结构化处理与行为预测统一协调的智能体工作流。

方法关键点：设计三阶段 Agent 流水线——聊天机器人通过图像增强的 SP 调查收集 92 名学生通勤者在 5 种天气场景下的 454 条出行方式选择；随后进行结构化数据处理；最终将多类出行方式预测建模为 5 分类任务。使用 MNL、Logistic Regression、Random Forest 作为经典基线；同时评测 9 个本地 LLM（2B-35B）在 4 种 zero-shot prompt 条件下的表现，并扩展到 persona、few-shot、vision 配置。

关键结果：Random Forest 达到 69.6% 5 类准确率；最佳纯文本 zero-shot LLM 达到 69.9%，无需任务特定拟合。习惯出行信息带来最一致的提升；Expert framing 总体优于 Role-Play；persona 信息在缺少习惯出行信息时最有用；few-shot 对多个模型有效且少量示例后提升趋于稳定。使用与受访者相同的天气图像，最佳 vision 配置达到 71.5% 的 5 类准确率，表明视觉上下文可为部分模型提供额外预测信息。
