---
title: 'The Language of the Question Selects the Market: Query Language and Exit IP
  as Separable Factors in Commercial Recommendations from a Generative Search Interface'
title_zh: 查询语言与出口IP如何分离决定生成式搜索商业推荐中的市场
authors:
- Dmitrij Żatuchin
affiliations:
- Estonian Entrepreneurship University of Applied Sciences
- Rankfor.AI OÜ
arxiv_id: '2608.30052'
url: https://arxiv.org/abs/2608.30052
pdf_url: https://arxiv.org/pdf/2608.30052
published: '2026-08-30'
collected: '2026-09-01'
category: GenRec
direction: 生成式搜索 · 语言与地理解耦
tags:
- generative search
- query language
- geo-localization
- recommendation bias
- non-determinism
- measurement validity
one_liner: 控制实验表明查询语言决定是否出现本地供应商、出口IP决定哪个市场，二者相互独立；英语测量会系统漏掉本地竞争者
practical_value: '- 做生成式搜索/LLM 的可见性测量时，必须同时记录查询语言和出口 IP；只用英语测会漏掉本地竞争对手，要用用户母语和当地 egress
  测才能反映真实市场。

  - 语言和地理位置要作为两个独立信号设计：语言决定回答语种与是否触发本地化，出口 IP 决定哪个国家市场被当作用户所在地；多市场 Agent 或生成式推荐不能只靠
  IP 或语言单一信号。

  - 生成式推荐单次答案不可靠，6 次相同 run 中 top1 变化率 4/6，浏览器和 API 同样不稳定；工程测量应重复采样（≥6，最好 20-30）并报告分布，不能截单次截图当证据。

  - 法规敏感品类（如会计、税务、合规）本地化效应远强于普通品类；电商/推荐对这类品类要显式考虑语言和地理的本地化策略，不能把项目管理类工具的结论直接迁移。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
生成式搜索界面应答商业问题时，列出的供应商名单直接决定商家曝光，但现有可见性测量大多用英语发起，且把语言和地理位置混在一起。需要拆解：查询语言和出口 IP 各自贡献什么，以及单次答案是否可靠。

**方法关键点**  
- 控制实验：234 次有效 runs，11 个 cell，4 个出口国家（德国/挪威/土耳其/爱沙尼亚），6 种查询语言，每 cell 6 次相同 run；覆盖浏览器 logged-out 和 OpenAI API `gpt-5.6-terra`，API 分 web_search 开关。  
- 会计软件 for freelancers 作为处理类别（因各国都有本地供应商），项目管理软件作为负对照；提前制定每市场供应商列表，区分本地/他国/全球，大小写敏感匹配。  
- 分别操纵：固定语言只改出口 IP；固定 IP 只改语言；同一 residential 连接交错收集三种语言。

**关键结果**  
- 单次答案不稳定：6 个 prompt 中 4 个 top1 跨 6 次相同 run 变化，浏览器与 API、开不开搜索稳定率相同，说明非确定性来自系统而非 surface。  
- 语言几乎单独决定本地供应商有无：本地语言 vs 英语，挪威 Fisher p=0.0152，德国 p=0.0606（单侧），合并 p=0.0022；土耳其和爱沙尼亚英语 0/6 本地，本地语 6/6。  
- 语言与位置解耦：土耳其语从柏林返回德国供应商（Lexware/sevdesk 5/6、5/6），从伊斯坦布尔返回土耳其供应商；俄语从爱沙尼亚返回爱沙尼亚供应商。  
- 少语中间层：爱沙尼亚连接上俄语问会计软件，本地供应商 4/6、全球 6/6，介于官方语言（6/6、1/6）与英语（0/6、6/6）之间。  
- 负对照：项目管理类别任何语言/IP 均不出现国内供应商，说明类别是否受国家法规约束（如 VAT/e-invoicing）而非是否有本地供应商起决定作用。

**最值得记住的一句话**  
用英语测量生成式推荐等于在测量另一个市场；查询语言决定是否触发本地化，出口 IP 决定哪个本地市场被选中，两者必须分开控制并重复采样。
