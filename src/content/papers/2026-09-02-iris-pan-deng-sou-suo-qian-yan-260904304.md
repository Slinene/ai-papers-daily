---
title: 'Iris: Climbing to the Search Frontier'
title_zh: Iris：攀登搜索前沿
authors:
- Ziyuan Liu
- Hengqi Liu
- Zichuan Wang
- Yang Qin
- Jiachen Liang
- Xu Chu
- Shaowei Chen
- Yuantao Gu
- Mu Chuan
affiliations:
- AllSpark Team
arxiv_id: '2609.04304'
url: https://arxiv.org/abs/2609.04304
pdf_url: https://arxiv.org/pdf/2609.04304
published: '2026-09-02'
collected: '2026-09-07'
category: Agent
direction: 搜索 Agent 训练与评估方法
tags:
- Search Agent
- RL
- SFT
- Context Management
- Data Synthesis
- Evaluation
one_liner: 通过网页超链接反向构造多跳搜索任务、双层轨迹过滤与SFT-RL迭代爬升，训练出开源同参数范围最强的搜索Agent
practical_value: '- **数据合成**：在电商/推荐的 QA、选品理由、query 改写数据中，把可搜索锚点（商品标题、类目名、品牌名）改写为描述性引用，消除字符串匹配捷径；再用双条件验证（闭卷答错
  + 给知识子图答对）筛出真正需要多跳推理的样本。

  - **轨迹过滤**：对 LLM 生成的推荐解释/搜索对话轨迹，用滑动窗口 zlib 压缩比快速检测重复和循环；turn 级 judge 从数据中归纳失败模式
  rubric，只 mask 最多 10% 差 turn，保留上下文、减少训练噪声。

  - **RL 工程**：长会话训练可用 request-level partial rollout 中断并在下步从 committed prefix 恢复，配合
  truncated importance sampling 纠正不同权重版本的 logprob 偏差；集群内部署 GenRM 与摘要器，避免外部 API 依赖。

  - **评估/上线**：将 context management 与策略能力分开报告，固定工具、上下文预算、judge，分别看无 CM 和有 CM 的结果；识别
  CM 收益来自任务是否经常耗尽上下文，高成本重试只作为上限探索，不作为默认配置。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：搜索 Agent 的价值在于处理动态环境中需要多跳证据组合的复杂问题，但现有系统性能差异常来自推理时上下文管理而非模型策略本身；因此需要一套从数据构造、训练到评估的可复现方案，并显式剥离 CM 影响。

**方法关键点**：
- 数据管线：从网页超链接图反向构造多跳问答；抽取实体图，生成至少 N 跳关系约束的问题；将所有非答案实体重写为描述性引用，消除字符串匹配捷径；仅保留参考模型闭卷答错、给实体图答对的样本。
- 轨迹过滤：强 teacher ReAct 采样后，先做轨迹级粗过滤（正确性、滑动窗口 zlib 压缩比检测重复/循环、至少 K 次工具调用），再做 turn 级细过滤：judge 从数据中归纳失败模式 rubric，最多掩码 10% 差 turn，保留上下文但排除损失。
- 训练：SFT 后接 live search RL；RL 用 request-level partial rollout 中断并复用 committed prefix，截断重要性采样纠正偏差；集群内部署 GenRM 与观测摘要器，无外部 API 依赖；观察是查询相关摘要而非原始页面。SFT-RL 迭代爬升：每轮 RL 后，从 pass rate∈(0,1/2] 的 query 中选最短成功轨迹回炉 SFT，形成自步课程。
- 评估：固定工具、上下文预算与 judge，同时报告无 CM 与 discard-all CM 两种设置。

**关键结果**：Iris-mini 35B 在 BrowseComp 82.2、BrowseComp-ZH 84.8、DeepSearchQA F1 86.9、HLE 52.3；Iris-pro 397B 为 88.6/85.1/92.9/56.4，开源同参数范围最强。无 CM 下 Iris-mini BrowseComp 64.7，超过 FORT-Searcher 55.9。CM 带来 BrowseComp +17.5（mini）/+16.0（pro），且收益与任务是否经常耗尽上下文相关。

**最值得记住的一句话**：搜索更像是一种原子能力而非垂直方向；评估必须剥离 CM 收益，并用 RL 成功轨迹回炉 SFT。
