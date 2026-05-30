---
title: Toward User Preference Alignment in LLM Recommendation via Explicit Context
  Feedback
title_zh: 通过显式上下文反馈实现LLM推荐中的用户偏好对齐
authors:
- Weizhi Zhang
- Wooseong Yang
- Yuxin Cui
- Zhaohui Guo
- Hins Hu
- Liangwei Yang
- Henry Peng Zou
- Qifei Wang
- Hanqing Zeng
- Jiayi Liu
affiliations:
- University of Illinois Chicago
- Meta
arxiv_id: '2605.29141'
url: https://arxiv.org/abs/2605.29141
pdf_url: https://arxiv.org/pdf/2605.29141
published: '2026-05-27'
collected: '2026-05-30'
category: RecSys
direction: LLM推荐 · 显式反馈整合
tags:
- LLM
- Recommendation
- Explicit Feedback
- Preference Alignment
- Context-Aware
- User Profile
one_liner: 论证将评论文本等显式反馈深度融入LLM推荐流程，以实现细粒度偏好对齐、提升多样性与可解释性
practical_value: '- **评论驱动标签系统**：从用户评论中抽取出结构化偏好标签（如 #LightWeightPhone、#NoJumpScares），作为召回过滤信号或重排特征。电商场景下可将标签异步生成并接入实时排序管线，低延迟融合语义理解。

  - **负面信号图谱构建**：将用户明确批评的属性构造成负面偏好图，避免推荐触发用户厌恶的商品（如“电池差”“太甜”），既能减少无效曝光，又能提升信任度。

  - **用户属性跨域复用**：利用用户自述的身份标签（素食主义者、专业摄影师）在不同业务线间传递稳定的偏好约束，实现从商品推荐到内容推荐的跨域对齐。

  - **可解释性提升**：在推荐理由中引用用户的原话或提炼的偏好点（如“因为您提到不喜欢跳跃惊吓，我们避免推荐此类影片”），增强推荐透明度和用户控制感。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
传统推荐系统几乎完全依赖点击、购买等隐式反馈，忽略了用户用文字明确表达的偏好（评论、吐槽、反馈）。这种缺失导致系统难以理解用户行为的真实原因，容易强化过滤气泡。LLM虽然具备极强的自然语言理解能力，但目前的LLM推荐仍然以物品元数据或交互序列为主，没有充分挖掘用户自己写出的上下文反馈。本文正是针对这一空白，倡导将显式上下文反馈作为下一代LLM推荐的核心信号。

## 方法关键点
- **四类显式反馈分类**：将用户文本反馈划分为正面偏好、负面约束、用户属性、物品级评论，每类提供不同的对齐信号。
- **多阶段整合框架**：① 用LLM从评论中提取用户画像和动态知识图谱，直接编码“为什么”的偏好；② 上下文感知检索，利用推理嵌入捕捉动机（如“喜欢科幻是因为哲学主题而非太空打斗”）并进行跨域兴趣发现；③ 重排序阶段引入个性化规则，对硬约束（过敏）和软偏好（减少咖啡因）做差异化处理；④ 异步标签对齐，后端用LLM生成语义标签和亲和度分数，前端检索和排序直接使用预计算标签，兼顾深度理解和实时性。
- **新基准和指标**：提出需要构建附带实时用户文本反馈的连续序列推荐数据集，并设计“不喜欢规避率”“偏好满足分”等对齐指标。

## 关键结果
本文为前瞻性愿景文章，未给出定量实验。其核心主张是：将用户自己的语言作为一级信号，可实现比只看行为更高精度的偏好对齐、更丰富的多样性和更强的可解释性。
