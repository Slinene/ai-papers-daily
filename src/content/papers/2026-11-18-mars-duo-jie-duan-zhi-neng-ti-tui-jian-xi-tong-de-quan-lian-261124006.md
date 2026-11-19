---
title: MARS Technical Report
title_zh: MARS：多阶段智能体推荐系统的全链路个性化编排
authors:
- Tong Liu
- Chaoqun Hou
- Longxiang Xiong
- Junhong Lou
- Jiaqi Zheng
- Qixin Li
- Zixin Zhao
- Yong Duan
- Xiannian Hu
- Fengze Jiang
affiliations:
- Taobao
arxiv_id: '2611.24006'
url: https://arxiv.org/abs/2611.24006
pdf_url: https://arxiv.org/pdf/2611.24006
published: '2026-11-18'
collected: '2026-11-19'
category: RecSys
direction: LLM Agent 全链路推荐编排
tags:
- LLM Agent
- Recommender Systems
- Multi-stage Pipeline
- Post-training
- GRPO
- ActionMask
one_liner: 用近线微调 Qwen3-0.6B Agent 生成用户级七维推荐编排配置，三阶段训练上线后最高 +7.34% GMV、+5.22% V2P
practical_value: '- 近线生成 + 版本化缓存 + 双重校验 + 兜底回退：LLM 异步生成配置，在线只读缓存，绝不阻塞关键路径。这套架构可直接迁移到任何用
  LLM 调整推荐参数的场景，如动态召回配额、融合权重、模型选择、push 策略等。

  - 把连续参数离散成围绕生产默认值的网格（±20% 配额、13 级权重），并在 system prompt 注入专家规则（行为/意图 → 调权方向）。消融显示无专家知识时
  V2P/GMV 大幅为负，说明 domain-informed prompting 是落地关键，不要裸用 LLM 生成参数。

  - FAPO 的 ActionMask 只对 action 字段的 token 位置计算偏好损失，避免结构 token 稀释，同时保留完整 generation
  loss 防止格式崩塌；配合 posterior V2P 权重缓解稀疏购买反馈。这套偏好学习方案可复用到任何“LLM 输出结构化决策”的任务。

  - GRPO 阶段用 Sandbox 快照回放 + frozen learned reward model（CTR/CVR heads，给出 dense 分数）做
  on-policy 探索，避免用户暴露。工程上可借鉴 diversity filtering 选多样样本、asymmetric clipping 防熵塌缩，以及
  Wilson lower bound 选取 SFT 正样本抑制小样本高胜率。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：工业级推荐系统是多阶段级联（retrieval → pre-rank → rank → re-rank），每个阶段有模型，但通道激活、候选配额、模型选择、分数融合等 pipeline 级决策仍由工程师统一配置，所有用户共享，无法适应个体意图、价格敏感度和行为模式。静态编排导致三类 mismatch：不同用户上下文需求不同；同一用户最优配置随会话位置、时间、促销日历变化；配置空间组合爆炸且反馈延迟多天、噪声大，A/B 探索不可行。

**方法关键点**：
- 近线 Agent：fine-tuned Qwen3-0.6B 生成七维配置（pipeline mode Full/Streamline/Minimal、retrieval channel subset 及 per-channel quotas ±20%、CTR/CVR 模型选择、融合权重 13 级 grid、reranker 设置），异步验证后原子写入 iGraph 版本缓存；在线只读缓存，LLM 延迟不进入服务路径，并有 schema 校验、latest-valid fallback、master kill switch。
- 提示设计：特征用 XGBoost/FSCD 重要性筛选控制 token 预算；system prompt 注入专家知识（生产默认配置、参数离散化边界、基于行为/意图的调权指南）。无专家知识消融 V2P -5.44%/-27.00%、GMV +0.39%/-21.23%，有专家知识全部转正。
- 三阶段训练：1) Confidence-aware SFT 用 Qwen3.6-Max teacher 蒸馏 schema-valid 生成，再用 Wilson lower bound 选执行高效样本，格式有效率 1.0%→99.8%；2) FAPO 用 ActionMask 只对 action 字段 token 位置比较偏好，保留生成 loss 锚定格式，并用 posterior V2P 权重缓解稀疏反馈；3) GRPO 用 Sandbox 快照回放 + frozen learned reward model（CTR/CVR heads，AUC 0.76/0.81）做 on-policy 探索，diversity filtering + asymmetric clipping 保持探索。

**关键实验结果**：五场景两周 A/B，超一千万 DAU，各场景关键指标 positive point estimates；最大 +5.22% V2P、+7.34% GMV，两个点击面 CTR 正；约 20% 请求路由到 Minimal 模式，在线 serving latency 降低 12ms；系统连续运行三个月，有效缓存覆盖 85%–95%。

**最值得记住的一句话**：个性化不只发生在单阶段打分，更应扩展到整个推荐流水线的编排，而近线 LLM Agent + 版本化缓存 + 结构化后训练是一条可落地的路径。
