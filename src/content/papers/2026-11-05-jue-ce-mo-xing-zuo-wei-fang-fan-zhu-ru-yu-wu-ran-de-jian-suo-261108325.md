---
title: Decision Models as Retrieval Gates Against Injection and Pollution
title_zh: 决策模型作为防范注入与污染的检索门控
authors:
- Mahdi Ghadamyari
- Reza Habibi
affiliations:
- Google
- University of California, Santa Cruz
arxiv_id: '2611.08325'
url: https://arxiv.org/abs/2611.08325
pdf_url: https://arxiv.org/pdf/2611.08325
published: '2026-11-05'
collected: '2026-11-08'
category: RAG
direction: RAG 检索安全 · 决策模型门控
tags:
- RAG
- indirect prompt injection
- decision model
- passage filtering
- web security
- open-weight
one_liner: 用开源决策模型在检索后对HTML判读，将RAG间接注入成功率从27.9%压至5.7%，污染页曝光仅0.5%。
practical_value: '- 在 RAG 线上链路里，可在检索后、prompt 构造前加一个轻量开源决策模型门控，对每个候选 passage 做安全判别；76ms/passage
  可通过批量推理压到可接受延迟，成本远低于用大模型 judge。

  - 给门控模型看原始 HTML 而不是抽出的纯文本，能保留隐藏指令、样式/脚本等攻击信号；电商/广告 UGC、商品页、论坛内容同样适用，避免纯文本清洗丢失反作弊特征。

  - 过滤要放在候选池进 top-k 之前，而不是只过滤 top-k；文中实验表明在 2/3 页面为伪造时，只滤 top-10 会剩太少页面导致回答质量下降，而滤池后
  fake exposure 从 28% 降到 0.5%，准确率保持 83%。

  - 决策模型可与已有 sanitization、Unicode normalization、citation prompting 叠加使用，攻击成功率从 13.6%
  再降到 5.7%；误报率在含人类指令的良性页上为 4/186，可作为风险预算调阈值。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

动机：RAG 从 web 检索的文本可能携带针对模型的隐藏指令，或混入为排名/误导生成的合成页；已有缓解措施仍不够。

方法要点：引入开源决策模型作为检索门控，输入每个候选页的 HTML 而非纯文本，让模型以“回答关于文本的问题”的形式判定是否安全或污染；在候选池选出 top-10 之前执行过滤。

关键结果：在 1,000 个 forum 风格网页的注入攻击 benchmark 上，攻击成功率从无防御的 27.9% 降到已有缓解措施的 13.6%，加门控后进一步降至 5.7%；门控平均耗时 76ms/passage，186 个含人类可读指令的良性页中误报 4 个，干净查询响应率仍为 85.6%→86.2%。在 200 查询污染测试中，2/3 候选页为伪造时，对候选池预过滤使 fake page 曝光率从 28% 降至 0.5%，答案准确率保持在 83%；只过滤 top-10 会导致可用页面不足。大模型 judge 的 AUROC 为 0.99，高于门控的 0.94，但成本高约 10 倍；HTML 输入比 plain text 能捕获更多攻击。所有模型均为 open-weight。
