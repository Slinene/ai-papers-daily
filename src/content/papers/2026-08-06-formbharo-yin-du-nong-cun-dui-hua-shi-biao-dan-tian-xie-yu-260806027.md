---
title: 'FormBharo: Designing and Evaluating a Voice Agent for Conversational Form
  Filling in Rural India'
title_zh: FormBharo：印度农村对话式表单填写语音代理的设计与评估
authors:
- Aman Dalmia
- Sanskriti Midha
- Jigar Doshi
affiliations:
- Artpark
- Indian Institute of Science
arxiv_id: '2608.06027'
url: https://arxiv.org/abs/2608.06027
pdf_url: https://arxiv.org/pdf/2608.06027
published: '2026-08-06'
collected: '2026-08-09'
category: Agent
direction: 语音代理 · LLM+规则混合表单填写
tags:
- VoiceAgent
- FormFilling
- LLM
- RuleBased
- EndToEndEval
- Hindi
one_liner: 构建LLM+规则混合语音代理，发布会话表单填写基准，揭示端到端评估与多目标权衡的必要性
practical_value: '- **LLM+规则混合架构**：在电商客服或对话推荐Agent中，可借鉴生成+确定性校验的流水线，用规则兜底LLM的错误，提升低资源或高噪声场景下的鲁棒性。

  - **端到端评估优先**：组件指标（如ASR准确率、槽位提取F1）不能代替全链路表单完成率；构建推荐/查询改写Agent时，需设计覆盖真实噪声的端到端测试，避免在组件优化上浪费资源。

  - **多目标帕累托选型**：面对准确率、成本、延迟的权衡，使用加权和标量化进行模型选择，适合业务上线前的自动化配置决策。

  - **低资源语音交互基准**：发布的FormVoiceAgentBench含真实印地语音频与多轮对话，可作为多语言/方言语音Agent测试的模板，特别适合需要覆盖长尾用户语音交互的国际化电商场景。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：印度大量低识字率人群无法自行填表申领社会福利，依赖人工卫生工作者一对一登记，效率极低。亟需一个能通过电话对话自动完成表单填写的语音Agent。

**方法**：提出FormBharo，结合LLM与确定性规则。LLM负责语音转录、信息抽取和回复生成；规则引擎进行槽位验证、对话流控，确保低延迟和低成本。在ARMMAN母婴健康项目试点，面向低收入的印地语母亲。同时发布FormVoiceAgentBench基准，包含960通模拟通话、3,760次多轮测试，涵盖真实印地语音频和多种声学条件。

**关键结果**：
- 真实语音转录比参考文本导致表单完成率最高下降~41个百分点；规则控制有效恢复逐轮抽取错误，使小模型达到甚至超越大模型的完成率。
- 组件性能与端到端指标不一致：GPT-5.5在参考转录下的槽位抽取准确率99.8%最高，但表单完成度反而落后。
- 帕累托优化显示无单一模型包揽所有指标，通过加权和标量化选出一组平衡准确率、成本、延迟的部署配置。
