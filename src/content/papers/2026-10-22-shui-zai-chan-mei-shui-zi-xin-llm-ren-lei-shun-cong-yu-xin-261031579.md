---
title: Who Is Sycophantic to Whom? Confident LLMs, Human Deference, and the Collapse
  of Trust Calibration
title_zh: 谁在谄媚谁？自信 LLM、人类顺从与信任校准崩溃
authors:
- Deepthika S
- Pawni Yadav
- B. Sankar
affiliations:
- Amrita Vishwa Vidyapeetham
- Netaji Subhas University of Technology
- Indian Institute of Science (IISc)
arxiv_id: '2610.31579'
url: https://arxiv.org/abs/2610.31579
pdf_url: https://arxiv.org/pdf/2610.31579
published: '2026-10-22'
collected: '2026-10-25'
category: LLM
direction: 人机交互 · 信任校准与反向谄媚评估
tags:
- sycophancy
- trust calibration
- human-AI interaction
- misinformation
- confidence calibration
- automation bias
one_liner: 当 LLM 自信且一致地犯错后，人类会反向顺从：虚假事实被采纳约65%，置信校准从0.70降至随机
practical_value: '- 电商导购/客服 Agent 不能只评估模型是否迎合用户；应同步统计用户是否反向顺从错误答案。可仿照 Human Deference
  Index，在会话日志中标记用户是否采纳 LLM 输出的商品属性、政策解释或推荐理由，并与真实值比对，重点关注错误采纳率。

  - RAG / 商品事实问答中，仅靠 LLM 自信表达无法阻止错误被吸收，且用户事后信任几乎不下降。应把“高置信但无依据”的内容做逐条可信度标注、来源展示或要求用户确认，不能寄希望于用户自行校准。

  - 搜索推荐 Agent 生成的候选 query、推荐理由或商品描述，避免所有输出都用肯定语气。对低可靠性字段加不确定性提示、可核验来源或二次确认，尤其要防止高置信错误被直接采纳。

  - 用户回看/互动多不等于系统更可靠：本实验中更差的助手反而导致更多回看，但回看伴随更多错误吸收。工程上不要把 session 回看次数当作质量正向指标，应结合正确性结果或任务完成度。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

动机：以往 LLM 谄媚研究关心模型是否迎合用户；这里反向考察用户是否对自信、一致但错误的 LLM 产生顺从，进而导致信任校准失效。

方法关键点：32 名被试内实验，与五个基于 GPT-5-mini 的助手对话学习科学主题；五个助手的事实错误率分别为 0、25%、50%、75%、100%，但均以完全自信表达。每主题后突袭测验，包含正确事实、植入错误项和两个干扰项，并要求回答置信度。

关键结果：104 次测验、1040 个答案中，得分从 7.4/10 降至 2.9/10；虚假教学项上植入错误被选择 60%，正确教学项仅 11%，OR=12.5。错误陈述被采纳率约 65%，且与错误注入比例无关；被吸收错误置信度高达 8.4/10，信心对正确性的 AUROC 从 0.70 降至随机，事后信任评分几乎不变。更差的助手导致更多回看，但回看与更多错误吸收相关；30% 回合把测验问题粘贴回被检查的来源。助手自身几乎不谄媚，面对质疑也不让步。引入基线校正的 Human Deference Index 量化人类侧谄媚，指出可信度是人机配对属性，可靠性应逐条可见。
