---
title: 'CLEAR: Legible and Steerable Recommendation via Grounded Natural-Language
  Interests'
title_zh: 基于用户可编辑自然语言兴趣层的可读可控推荐系统 CLEAR
authors:
- Qi Guo
- Reza Mirghaderi
- Iordanis Fostiropoulos
- David Fan
- Yuchen Liu
- Shiliang Tang
- Lukasz Korycki
- Golnaz Ghasemiesfeh
- Xinzhu Bei
- Sasha Vorontsov
affiliations:
- Meta
arxiv_id: '2611.19110'
url: https://arxiv.org/abs/2611.19110
pdf_url: https://arxiv.org/pdf/2611.19110
published: '2026-11-14'
collected: '2026-11-17'
category: RecSys
direction: 自然语言用户兴趣层 · 可操控推荐
tags:
- natural language profile
- steerable recommendation
- behavioral grounding
- LLM
- deployed system
- user modeling
one_liner: 提出并部署统一自然语言兴趣身份，贯穿召回、排序、归因与曝光控制，让推荐可读且可操控
practical_value: '- 把用户显式偏好做成可编辑的自然语言“兴趣对象”，同时作为检索/排序/归因的服务地址，而不是仅做展示标签；在电商中可用“用户主动添加的品类/品牌偏好”驱动候选召回，并让同一身份贯穿排序和曝光控制。

  - 行为 grounding 思路：用历史交互事件验证生成的兴趣短语，避免暴露无支撑推断；同时这些支撑事件可作为个性化召回锚点，结合“行为近邻 + 主题匹配”做硬门控，减少全局热门但不相关的内容。

  - 冷启动声明处理：即使没有历史行为，用户新声明的兴趣立即建立 identity，通过主题检索获取候选，并在排序阶段给临时加成；等后续行为积累再转有机召回。适合电商新品/新类目偏好冷启动。

  - 曝光控制与补给解耦：用 decayed real-time per-interest 计数器监控每个兴趣的曝光，过曝时压制，衰减后触发补给；避免单个兴趣刷屏，同时保证长期兴趣得到持续交付。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现代推荐系统把用户偏好压缩成不可检查的隐向量，用户无法知道系统推断出什么，也无法确定自己的纠正是否生效。可读性（legibility）和可操控性（steerability）必须同时满足：既能展示可理解的兴趣，又能让编辑持久影响后续推荐。

### 方法关键点
- 每用户维护一个可编辑的自然语言兴趣 profile，包含推断和显式两种状态；显式增删单独存储，优先于后续推断。
- 行为 grounding：将推断兴趣投影到协同嵌入空间，逆向检索用户历史支撑事件；支撑事件过滤、去重、排序兴趣，避免暴露无依据的推断。
- 兴趣对象同时是服务地址：标签 + profile 条件改写驱动词汇检索，支撑事件种子行为召回，投影查询 ANN 索引；稳定的用户-兴趣身份贯穿排序、归因和曝光控制。
- 新声明兴趣无需历史证据即可建立身份，通过主题召回获得候选，排序临时加成和置顶保证竞争；负向抑制用相似性感知降权减少重现。
- 曝光感知控制：实时 per-interest 曝光计数，过曝时 dampen，衰减后触发补给，避免单兴趣刷屏。

### 关键结果
- 直接用户评价：393 用户、7261 条展示兴趣，88.5% 被判定准确。
- 离线生成器基准：Specialized 3B F1@10 0.3967，优于 Gemini 2.5 Pro 0.3633 和旧生成器 0.1911。
- 线上系统：新声明兴趣当天匹配交付率 79.6%；82.6% 用户声明兴趣内容占比 ≥5%；独立多模态 judge 主题相关性 87.2%。
- 五臂随机消融：候选供给贡献 13.7pp、强制置顶 11.1pp、排序加成 8.7pp，全栈增益 33.5pp。
- 补货与调控：补货 +8.34% 3s 互动兴趣响应，体积调控 flooding-days 降 15.4%。
- 效率：历史压缩减少 39.5% tokens，共享标注减少 98% 逻辑请求。

### 最值得记住的一句话
把自然语言兴趣做成一个统一的、可编辑的服务身份，贯穿召回、排序、归因和曝光控制，是同时实现推荐可读与可操控的关键；但必须分别度量“用户看到准确”和“服务确实改变”。
