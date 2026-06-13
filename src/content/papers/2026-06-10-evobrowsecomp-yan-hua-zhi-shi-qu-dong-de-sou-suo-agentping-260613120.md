---
title: 'EvoBrowseComp: Benchmarking Search Agents on Evolving Knowledge'
title_zh: EvoBrowseComp：演化知识驱动的搜索Agent评测基准
authors:
- Yunhan Wang
- Jiaan Wang
- Lianzhe Huang
- Xianfeng Zeng
- Fandong Meng
affiliations:
- Northeastern University, China
- Weixin AI, Tencent Inc, China
arxiv_id: '2606.13120'
url: https://arxiv.org/abs/2606.13120
pdf_url: https://arxiv.org/pdf/2606.13120
published: '2026-06-10'
collected: '2026-06-13'
category: Eval
direction: 搜索Agent评测基准 · 动态知识演化
tags:
- search agent
- benchmark
- evolving knowledge
- multi-agent synthesis
- contamination-free
one_liner: 提出自动更新的复杂问答基准EvoBrowseComp，利用三Agent协同从实时网络中合成无污染题目，评估搜索Agent的真实浏览能力。
practical_value: '- 借鉴多Agent协作流水线（QA合成、信息过滤、高层推理图构建）自动生成评测数据，可迁移到电商推荐场景，动态生成需要实时检索的商品对比、政策更新等复杂查询，防止模型依赖过时记忆。

  - 信息过滤Agent通过可信度和流行度双筛阻断参数快捷方式，这一思路可用于构建推荐系统的抗泄漏测试集，确保模型真正理解上下文而非记忆热门模式。

  - 推理Graph形式化减少逻辑冗余，可启发我们将用户多条件查询（如“性价比高、适合油皮、2025新款粉底液”）解析为结构化约束，生成更鲁棒的Agent评测用例。

  - 定期自动更新的基准设计，适合作为线上搜索Agent持续监控的探针，及时检测模型在面对新鲜知识时的退化，类似推荐系统中的概念漂移检测。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有搜索Agent基准（如BrowseComp）依赖静态知识，易遭遇测试集污染和参数记忆，导致模型靠事实回忆而非真正检索得分，掩盖真实浏览能力的不足。

**方法**：提出EvoBrowseComp，一个可自动更新的高难度复杂问答基准，包含400个英文和400个中文问题，全部从实时网络信息中合成。核心设计了三Agent协同框架：（1）QA合成 Agent 从网络中检索最新知识生成问答对；（2）信息过滤 Agent 按可信度和流行度筛选知识，阻断模型利用参数记忆的捷径；（3）高层指导 Agent 将问题形式化为推理Graph，消除逻辑冗余和潜在捷径。整个过程全自动化，支持定期更新以抵御数据污染和保持时效。

**结果**：实验表明该基准难度极高，要求Agent进行广泛的水平搜索和深度推理，现有搜索Agent得分普遍较低，彰显了其评估真实浏览能力的有效性，确立了一种可扩展的自动演化基准范式。
