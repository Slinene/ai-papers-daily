---
title: 'TimeLogic Challenge @ CVPR 2026: Strong MLLMs Meet Evidence-Seeking Agents
  for Temporal-Logic Video Question Answering'
title_zh: 时序逻辑视频问答：主动证据搜寻代理方案
authors:
- Zhaoyang Xu
- Xusheng He
- Wei Liu
- Zhenyang Li
- Jianlong Wu
affiliations:
- Harbin Institute of Technology (Shenzhen)
- HKUST
arxiv_id: '2606.01631'
url: https://arxiv.org/abs/2606.01631
pdf_url: https://arxiv.org/pdf/2606.01631
published: '2026-06-01'
collected: '2026-06-06'
category: Agent
direction: 多模态代理 · 时序视频理解
tags:
- Temporal-Logic VideoQA
- Evidence-Seeking Agent
- ReAct
- Multi-Granular Sampling
- Gemini 3.1 Pro
- Training-Free
one_liner: 提出训练无关的 ReAct 代理，通过多粒度时间戳采样与问题类型感知策略，在 TimeLogic 上取得 77.13 平均准确率。
practical_value: '- 在商品视频或直播片段中，可借鉴 **multi-granular toolkit** 思路：先全局粗览，再对关键时段精细扫描，替代均匀抽帧，降低推理成本的同时捕捉关键动作边界。

  - **问题类型感知的策略路由** (question-type-aware exploration) 可直接迁移到多模态 Agent 的 prompt 工程：根据输入语义类别动态选择工具、迭代深度与思维预算，避免“一刀切”的策略浪费。

  - **时间戳与帧交错注入** (frame–timestamp interleaving) 可让 VLM 将时间关系转化为数值比较，这是一种轻量的时间推理增强
  trick，适合处理带有时间戳的商品描述或用户行为序列。

  - **语料感知的预算分配** (corpus-adaptive budgeting) 对异构数据源（如店铺直播 vs. 商品讲解视频）自动调节帧数/步数，适合工程中需要处理不同长度、密度视频的场景。'
score: 8
source: arxiv-cs.MM
depth: full_pdf
---

## 动机
时序逻辑视频问答要求模型理解事件之间的先后、重叠、持续等关系，而标准 VLM 的一次性均匀采样极难捕捉局部证据，尤其在多事件链的长视频中。现有方法缺乏主动定位关键片段的机制。

## 方法关键点
- **ReAct 证据搜寻代理**：将推理转化为 Think–Act–Observe 循环，代理可反复请求新的时间戳帧，积累观测历史再作答。
- **多粒度采样工具包**：提供 overview、temporal scan（分段扫描）、skim、focus 四种工具，所有返回帧均绑定绝对时间戳，使时间关系简化为数值比较。
- **问题类型感知策略**：基于规则分类器将问题映射到时序类别，为每类预设初始工具、迭代深度、帧预算和专属提示（如“before”形式定义、常见陷阱提醒），长链问题强制生成 timeline-first 的显式时间线再回答。
- **语料自适应预算**：根据视频来源（CrossTask 有音频，STAR/AGQA/Breakfast 纯视觉）及剪辑长度与动作密度，动态分配帧数与步骤，短视频直接密集采样，长视频迭代探索。
- **训练无关**：仅使用 Gemini 3.1 Pro 作为推理骨架，通过 prompt 与工具调用实现，无任何微调。

## 关键结果
在 TimeLogic 官方测试集（3000 问题 / 1850 视频，含四种来源与多种时序类别）上，AvgAcc 达到 77.13，验证了主动证据搜寻对时序推理的有效性。该系统为挑战赛提交方案，未与其他方法比较，但展示了不依赖于训练的代理框架的可行性。

## 一句话总结
给 VLM 装上「搜索能力」和多粒度时钟，远比一次性塞入所有帧更能解决需要精确定位时间边界的视频理解任务。
