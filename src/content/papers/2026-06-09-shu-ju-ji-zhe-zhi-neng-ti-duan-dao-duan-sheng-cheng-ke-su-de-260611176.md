---
title: 'Data Journalist Agent: Transforming Data into Verifiable Multimodal Stories'
title_zh: 数据记者智能体：端到端生成可溯源的交互式数据报道
authors:
- Kevin Qinghong Lin
- Batu EI
- Yuhong Shi
- Pan Lu
- Philip Torr
- James Zou
affiliations:
- University of Oxford
- Stanford University
arxiv_id: '2606.11176'
url: https://arxiv.org/abs/2606.11176
pdf_url: https://arxiv.org/pdf/2606.11176
published: '2026-06-09'
collected: '2026-06-11'
category: MultiAgent
direction: Agent · 多智能体协作与可验证内容生成
tags:
- Multi-Agent
- Verifiability
- Multimodal Generation
- Auditability
- Data Journalism
- Agent-as-Judge
one_liner: 提出七角色虚拟新闻室与 Inspector 证据链机制，将原始数据转化为可验证的多模态互动文章
practical_value: '- **可溯源的 Agent 输出设计**：Inspector 将最终页面的每个声明（数值、图表、引用）绑定到上游的代码行或源
  URL。在电商 Agent（如导购、客服、报告生成）中可借鉴这一模式，对每一条生成的内容附加证据指针，实现“可审计的推荐理由”或“可核查的 AIGC 描述”。

  - **多角色协作的工作流编排**：Detective-Analyst-Editor-Designer-Programmer 的分工清晰，尤其适合需要外部搜索、数据分析、叙事构建的复杂流程。在电商场景下，可以把市场洞察
  Agent、商品知识库、文案撰写 Agent 和交互式落地页生成串联，提升从数据到营销内容的自动化程度。

  - **多模态生成与受众适配**：Designer 根据数据主题和读者偏好动态选择交互形式（地图、音频、可玩 demo），而非强制静态图表。在推荐解释或商品展示中，可以借鉴“先理解读者/场景，再生成最适配的媒体形态”的思路，例如对地理相关的生鲜推荐使用交互地图，对音乐类商品嵌入音频试听。

  - **用计算机使用 Agent 做低成本评估**：采用 browser-use agent 对交互式页面进行自动化评审，与人类评分排名有 0.44 的 Spearman
  相关，可用作快速迭代期的排序性评估，节省人工费。在生成式推荐首页、导购页面等交互产出上，该思路可用于回归测试或候选排序。'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

**动机**  
一篇高质量的数据新闻需记者团队花费数周完成背景调研、统计分析、叙事构思与视觉设计，而现有 AI 工具仅在单一环节（如数据分析或图表生成）有用，缺乏端到端能力，更缺乏对产出内容的可验证性保障。语言 agent 的幻觉问题使读者无法信任文中的数字和图表是否真正来自数据。因此，亟需一个能自动将原始数据转化为可信、可交互报道的 agent 系统。

**方法关键点**  
Data Journalist Agent (Data2Story) 构建了一个由七个专门角色组成的虚拟新闻室：
- **Detective**：联网搜索为数据补充背景信息和参考媒体，产出带源 URL 的上下文集合。
- **Analyst**：用代码全方位分析数据集，生成带脚本行号的结果（每个统计值都有可执行溯源）。
- **Editor**：从分析结果中挑选优先项，编排叙事角度和段落级大纲，输出带上游引用的讲述方案。
- **Designer**：根据段落内容和读者可能想看的东西，调用文本到图像/视频/音频等工具，创作匹配的多模态资产。
- **Programmer**：将 Editor 的叙事和 Designer 的资产组装成交互式 HTML 网页，支持 Auditor 反馈后的修改。
- **Auditor**：检查页面视觉缺陷（如元素重叠、图表失效），向 Programmer 提供修改建议。
- **Inspector**（核心创新）：将最终页面中的每个元素（句子、图表、交互组件）绑定到上游证据——代码证据指向产生数字的具体脚本和行号，引用证据指向外部 URL。这使得全文的声称都具备可审计的溯源链。

**关键实验与结果**  
在 18 组数据-人类记者原文对（来自 The Economist、The Pudding、TidyTuesday）上进行四轴评估：
- **角度覆盖**：agent 覆盖了人类文章 50.4% 的声称（对 Economist 简短报道达 73%），但反向仅 35.1%，表明 agent 能复现可预测的分析角度，但难以捕捉长文中的独家编辑视角。
- **人工评价**（53 人盲评，1–7 分）：Data2Story 平均 4.21 vs 人类 3.38，尤其在“数据与方法透明度”领先 1.49 分（Inspector 的贡献），整体偏好 74% 选择 agent 文章。但在以创意设计著称的 Pudding 上打成平手。
- **计算机使用 agent 评审**：browser-use agent 自动导航页面评分，与人类排名 Spearman ρ=0.44，可作低成本排序替代。开启 Inspector 使透明度分提升 +1.67。
- **可验证性**：agent 文章中 93% 的声明可被代码或引用源审计，而人类文章因缺少可执行代码，该比率仅 25%，体现了 agent 在审计性上的结构性优势。

**核心结论**  
Data2Story 不旨在取代记者，而是作为协作工具，输出“自带审计链”的多模态初稿，让报道更透明、更经得起核查；它在分析覆盖和透明度上领先，但编辑创意、交互设计深度仍逊于人类特稿。
