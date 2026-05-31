---
title: Label Over Logic? How Source Cues Bias Human Fallacy Judgments More Than LLMs
title_zh: 来源标签如何更强烈地扭曲人类的逻辑谬误判断？LLM 更稳健
authors:
- Mahjabin Nahar
- Nafis Irtiza Tripto
- Aiping Xiong
- Ting-Hao `Kenneth' Huang
- Dongwon Lee
affiliations:
- The Pennsylvania State University
arxiv_id: '2605.29928'
url: https://arxiv.org/abs/2605.29928
pdf_url: https://arxiv.org/pdf/2605.29928
published: '2026-05-28'
collected: '2026-05-31'
category: Other
direction: 人类与LLM在来源标签偏见上的对比研究
tags:
- Source Bias
- Logical Fallacies
- Human-AI Collaboration
- Evaluation Bias
- LLM Robustness
one_liner: 来源标签（人类/AI）显著影响人类的逻辑谬误评估，而LLM评价保持相对稳定
practical_value: '- **人工评估去来源化**：在 UGC 审核、推荐理由质量评估、对话回复打分等场景，不要向评审者展示内容来源（人类/AI），避免“人类写的就更可信”的偏见

  - **LLM 做先验评判**：构建人类反馈对齐（RLHF）数据时，可先用 LLM 对候选内容进行无来源偏见的逻辑/质量评分，再让人工仅针对 LLM 标记的争议点复核，提升标注一致性

  - **推荐理由的标签策略**：若想提升用户信任，对优质推荐理由可弱化“AI 生成”标签或强调“人工润色”，对低质理由无需披露来源；反方向则可利用标签警示用户批判性看待
  AI 内容

  - **多智体协作中的信源加权**：Agent A 收到标明“人类撰写”或“AI 辅助”的信息时，可内置 LLM 仲裁器重新评估逻辑/事实，降低信源标签对后续决策的链式影响'
score: 7
source: arxiv-cs.HC
depth: abstract
---

**动机**：AI 生成与辅助内容大量涌入在线空间，附着在内容上的来源标签可能扭曲人类的推理判断，影响审核、评估与决策。LLM 是否同样受此类标签影响，直接关系到人机协作的可靠性。

**方法**：采用逻辑谬误作为受控刺激，设计线上实验（N=505）。参与者被随机分配到五种来源条件之一（人类、AI、人类辅助AI、AI辅助人类、无披露），评价含有逻辑谬误或无谬误的评论。同时让 GPT-5.2、Gemini 2.5 Flash、Claude Sonnet 4.5 在相同条件下做出判断，对比人类与 LLM 的评价差异、信任评分及置信度。

**结果**：人类评估者显著受来源标签影响——标为“人类”或“人类辅助AI”的内容获得更高信任与质量评分，即便其中包含逻辑谬误。相反，LLM 的判断在不同来源标签下保持相对稳定，虽然不同模型的表现有所差异。两者的置信度在所有条件下都维持高位，未因逻辑正确性而调整。这表明来源标签偏见主要是人类的脆弱性，LLM 能提供更不受来源干扰的评估，支持将它们作为人工判断的“校准器”，促进更稳健的人-LLM 协作。
