---
title: 'Breaking News Out of the Filter Bubble: Generative AI Search Diversifies Collective
  Attention and Raises Shared Information Consumption'
title_zh: 生成式AI搜索打破信息茧房：多样化集体注意力并提升共享信息消费
authors:
- Heeseung Andrew Lee
- Dokyun Lee
- Gwanhoo Lee
- Dongwon Lee
affiliations:
- University of Texas at Dallas, Richardson, TX 75080, USA
- Boston University, Boston, MA 02215, USA
- Faculty of Computing & Data Sciences, Boston University, Boston, MA 02215, USA
- American University, Washington, DC 20016, USA
- Hong Kong University of Science and Technology, Hong Kong SAR
arxiv_id: '2609.38946'
url: https://arxiv.org/abs/2609.38946
pdf_url: https://arxiv.org/pdf/2609.38946
published: '2026-09-30'
collected: '2026-10-03'
category: Other
direction: 生成式AI搜索与集体注意力多样化
tags:
- generative AI search
- AI overview
- filter bubble
- news consumption
- field experiment
- RAG
one_liner: 随机田野实验显示，生成式AI搜索能扩大热门话题触达、增加读者间话题重叠，同时把消费推向冷门话题
practical_value: '- 生成式AI搜索/推荐顶部放置带引用的AI摘要，会改变点击和流量分布：在处理组中，读者从传统结果点击转向引用文章和后续搜索，且引用文章推动冷门消费；电商/广告搜索可以借鉴这一机制，通过有选择地引用长尾商品或新品，调节头部集中度、扶持冷门供给。

  - 评估AI搜索/推荐功能时不能只看单次点击或CTR：该实验发现，虽然单次搜索的文章消费下降，但更频繁的搜索抵消了这一下降，带来每人文章消费小幅增加、每分钟信息消费上升。业务上应结合搜索频率、总消费时长、曝光消费等指标综合评估，否则可能误判为负向。

  - AI答案可直接满足信息需求，大部分共享信息增长不需要点击文章；在电商场景中，生成式摘要可能降低商品点击，但提升用户信息获取效率和整体互动，需要区分“展示消费”与“点击消费”来度量真实价值。

  - 随机田野实验设计值得迁移：两组共用同一底层档案，实验组仅额外获得AI答案，可干净识别AI功能的因果效应；类似方法可用于评估推荐卡片、AI摘要、搜索改版对用户行为和平台生态的净影响。'
score: 7
source: arxiv-cs.MM
depth: abstract
---

**动机**  
生成式AI搜索和AI overview正在改变信息获取方式，但引发担忧：读者可能接触更窄的话题范围、共同信息更少，加剧过滤气泡。该研究通过《华盛顿邮报》37,561名读者的随机田野实验，检验生成式AI搜索对新闻消费多样性及共享信息的影响。

**方法关键点**  
两组读者搜索同一新闻档案，处理组在传统结果上方额外展示带文章引用的AI答案。研究同时测量“展示的答案”和“打开的文章”两类消费，覆盖曝光和点击行为。AI答案基于RAG生成，摘要综合多篇检索文章并提供引用链接。

**关键结果**  
AI搜索扩大了热门话题的触达范围，并增加读者之间话题消费的重叠，即共同信息上升。同时，消费集中度下降：无论是个体内部还是全体受众层面，都明显向冷门话题转移。AI答案贡献了大部分共享信息增长，且无需点击文章即可传递信息；引用文章进一步推动冷门话题消费。读者从传统结果点击和浏览转向引用文章和后续搜索。虽然单次搜索的文章消费下降，但更频繁的搜索弥补了这一下降，带来每人文章消费的小幅增长，每分钟总信息消费也上升。结论：生成式AI搜索可以在强化读者共有信息的同时，多样化集体注意力，并非简单加剧同质化。
