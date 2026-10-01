---
title: 'MemLife: Curating and Reasoning over Long-Term Egocentric Video Memories'
title_zh: 长期自我中心视频记忆的构建与推理：MemLife与MemOpt
authors:
- Guangzhi Xiong
- Xinyuan Zhang
- Xiao Yang
- Hyokun Yun
- Kai Zhang
- Shiun-Zu Kuo
- Hyeonjeong Ha
- Xilun Chen
- Kai Sun
- Lucas Liang
affiliations:
- Meta Reality Labs
- University of Virginia
- University of Illinois Urbana-Champaign
arxiv_id: '2609.40195'
url: https://arxiv.org/abs/2609.40195
pdf_url: https://arxiv.org/pdf/2609.40195
published: '2026-09-30'
collected: '2026-10-01'
category: Agent
direction: 长期视频记忆 Agent 与 RL 训练 writer
tags:
- Memory
- Egocentric Video QA
- Agentic Retrieval
- Reinforcement Learning
- Multimodal
one_liner: 提出MemLife多模态记忆系统与MemOpt强化学习框架，只训练记忆写入器即显著提升长期视频QA
practical_value: '- 记忆写入与读取解耦：将非结构化多模态行为流（观看/会话/操作）离线压缩成时间戳+实体锚定的文本条目，线上只做检索与推理，可大幅降低长期用户行为记忆的存储与查询成本。在电商场景可对用户历史生成第一人称摘要（“我上周浏览过某商品”），对齐自然语言问询。

  - 时间索引 + 语义搜索：检索时先用时间区间过滤再做 embedding 相似度排序，并按时间顺序组织证据，能缓解长历史中相似事件的检索竞争。迁移到搜索推荐可处理“上个月看过的那双鞋”等时间敏感查询，先缩小候选集再匹配。

  - RL仅训练记忆写入器而非端到端答案：奖励分解为 Faithfulness / Informativeness / Retrievability，避免 reader
  执行噪声干扰，训练稳定且跨 backbone 泛化。可以对用户行为摘要或商品描述生成模块采用类似分解奖励，将“信息量”和“可检索性”纳入优化目标。

  - 可检索性离线评估：用固定 reader 缓存 actions 重放判断候选记忆是否会被检索到，无需每次生成新推理轨迹，显著降低训练开销。在推荐/搜索中评估历史摘要或商品描述的召回效果时，可用固定策略重放，快速离线筛选高质量候选。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

动机：长时间跨度自我中心视频会积累数百小时，每次查询都重处理原始视频不可行。文本压缩是可行路径，但激进压缩会丢失未来问题所需证据，保守压缩则引入大量噪声稀释检索信号，且写入模型可能产生幻觉。因此需要一种能忠实、信息充分且易于检索的记忆表示。

方法关键点：
- MemLife 系统：写入器独立处理每个30秒视频段，融合视觉帧与语音转录，输出时间锚定、实体接地（将口语指代与视觉实体对齐）、第一人称叙述的文本片段；不依赖前文上下文，保持线性扩展。
- Agentic Reader：支持 Rewrite / SearchMemory / FetchMemory / FetchVideo / Answer 动作，可进行语义搜索与时间区间限定，并按时间顺序排列证据后回答。
- MemOpt 训练框架：只优化记忆写入器，保持读取器冻结。提出 FIRM 奖励：Faithfulness（token级忠实度，检查生成内容是否被源视频支持）、Informativeness（提取关键事实并判断候选记忆是否蕴含）、Retrievability（固定读取器动作重放，检查候选记忆是否被检索到）。采用 GRPO，token级优势归一化，乘性聚合奖励。

关键实验：在 SuperMemory-VQA、EgoLifeQA、SuperMemory-LVQA、EgoLife-EQA 四个基准上，MemLife 在无训练情况下比最强无训练基线提升 4.6–12.0% 准确率；MemOpt 进一步带来 2.7–5.0% 提升。MemLife+MemOpt 在 SuperMemory-VQA 准确率 60.35%，超过 TaskMem (50.88%)、M3-Agent (53.93%) 等训练基线。消融验证实体接地、第一人称叙述、时间锚定、时间排序以及 FIRM 各分量的贡献；优化后的写入器跨 Qwen3.5-9B / Qwen3.6-27B 和 EgoRAG 等异构读取器均有效。

最值得记住的一句话：学习“写什么”本身就是长期记忆问答的有力杠杆，只优化 memory writer 就能稳定提升检索与回答质量。
