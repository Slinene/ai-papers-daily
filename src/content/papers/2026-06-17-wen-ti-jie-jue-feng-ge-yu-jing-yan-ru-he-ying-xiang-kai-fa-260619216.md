---
title: 'No Two Developers Think Alike: How Problem-Solving Styles and Experience Shape
  Needs in Conversational Interaction with Copilot'
title_zh: 问题解决风格与经验如何影响开发者与 Copilot 对话的需求
authors:
- Jonan Richards
- Bruno Alves de Oliveira
- Iury Oliveira
- Igor Wiese
- Mairieli Wessel
affiliations:
- Radboud University
- Federal University of Technology – Paraná
- Microsoft
arxiv_id: '2606.19216'
url: https://arxiv.org/abs/2606.19216
pdf_url: https://arxiv.org/pdf/2606.19216
published: '2026-06-17'
collected: '2026-06-21'
category: Other
direction: 对话式助手交互的认知多样性研究
tags:
- cognitive diversity
- programming assistants
- interaction modes
- developer needs
- user study
- GitHub Copilot
one_liner: 通过有声思维研究识别开发者与编程助手对话的 5 种交互模式和 10 种需求，揭示认知多样性的影响
practical_value: " - 在对话式推荐助手（如购物导购、广告客服）中，可参照此研究设计用户意图识别模块，根据用户的提问风格（如探索型 vs. 聚焦型）动态调整推荐策略，提供更个性化的交互体验。\n\
  \ - 为不同经验水平的用户提供差异化引导：新手可能需要逐步解释和示例，而专家偏好简洁快速的意图理解，可在对话流中设置自适应路径。\n - 对用户交互日志进行模式聚类，类似文中识别的5种模式，可用于监控用户行为并触发主动帮助（如识别“挣扎”模式时推送提示）。\n\
  \ - 在评估对话式搜索/推荐系统时，引入认知多样性变量（如问题解决风格量表），更全面地解释不同用户群的满意度差异，避免“一刀切”的评估指标。"
score: 6
source: arxiv-cs.HC
depth: abstract
---

**动机**：基于 LLM 的编程助手（如 GitHub Copilot Chat）虽被广泛使用，但现有研究显示开发者需求存在显著个体差异，部分特定群体面临独特挑战。现有工具设计多为“通用型”，未考虑认知多样性如何影响交互。

**方法**：采用混合方法有声思维研究，招募 27 名专业开发者与学生，在真实编程环境中使用 Copilot Chat，通过出声思维、即时追问和事后问卷，收集交互行为与主观反馈。分析阶段结合定性编码与定量聚类，归纳出 5 种典型交互模式、10 项核心需求，并关联开发者的问题解决风格（Kirton Adaption–Innovation Inventory）与经验水平。

**关键结果**：
- 识别出 5 种交互模式：主动型、被动型、实验型、挣扎型、避开型，每种模式对应不同的需求组合。
- 提炼出 10 项需求，如“理解建议生成逻辑”“控制对话节奏”“获得解释而非代码”等，高频需求包括“保持上下文”和“获得多样化建议”。
- 问题解决风格（适应型 vs. 创新型）显著影响交互模式：适应型开发者更倾向结构化、逐步的交互，创新型开发者喜欢跳跃式探索。经验水平也会影响对提示精确性和解释深度的需求。

**贡献**：构建了编程助手交互的概念模型，揭示了认知多样性对交互的塑造作用，为个性化编程助手设计提供了实证依据。
