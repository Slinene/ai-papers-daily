---
title: Language Models for Page-Level Layout Decisions in E-commerce Search
title_zh: 电商搜索页面级布局决策的语言模型评估：Prompt 与表征方法对比
authors:
- Varun Joshi
- Eva C. Song
- ChengXiang Zhai
affiliations:
- Walmart Global Tech
- University of Illinois at Urbana-Champaign
arxiv_id: '2610.10920'
url: https://arxiv.org/abs/2610.10920
pdf_url: https://arxiv.org/pdf/2610.10920
published: '2026-10-07'
collected: '2026-10-09'
category: Eval
direction: LLM as judge · 页面布局离线评估
tags:
- LLM-as-judge
- page layout
- representation learning
- e-commerce search
- offline evaluation
- secondary stack
one_liner: 首次系统对比 Prompt 与表征方法离线评估电商搜索中次级堆叠布局，表征方法 AUC 0.853 显著更优
practical_value: '- 页面布局评估不要直接用 LLM-as-judge：DP 几乎全预测 1，PDJ 虽有分解但仍等权结合，不可靠；改用轻量预训练编码器（如
  ModernBERT）embedding + 浅层分类器，AUC 可从 0.67 提升到 0.85，且推理成本更低。

  - 标签构造采用 top-to-bottom scroll model：只保留用户实际滚动到次级堆叠位置以下的会话，避免将未看见模块的会话误标为正/负，可显著降低标签噪声，适合电商搜索行为数据。

  - 显式结构化特征（stack type、插入位置、重复商品数等）在 prompt 推理中容易被损失，但 representation 方法能自动编码这些信号；如果要用
  prompt 派生特征，务必把关键显式特征重新拼回分类器输入。

  - 对 Agent/LLM 驱动的 UI 决策，优先考虑用 embedding 作为状态表示，再用小型分类器做最终判断，而不是让 LLM 直接输出最终决策，可减少方差并提升离线可评估性。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
电商搜索页面越来越多地插入推荐模块（如 secondary stack）来展示备选商品，但布局决策（是否插入、插入位置）直接影响用户浏览流畅度和主结果效果。传统排序评估方法（interleaving）难以扩展到页面级布局，在线 A/B 测试成本高，历史日志只能覆盖已上线布局，无法评估未见过布局。因此需要语言模型作为可扩展的离线评估器。

**方法关键点**
- 问题形式化：给定 query q、主商品列表 P 和候选 secondary stack S，比较在位置 i 插入 S 与不插入 S 两种布局，输出二分类标签（插入更好=1），以加购（ATC）为正信号。
- 标签方案：从搜索日志提取包含一次 secondary stack 的会话，采用 top-to-bottom scroll model——只考虑 secondary stack 位置及以下的 ATC 事件；若用户对 stack 本身加购则标 1，若跳过 stack 但对下方主结果加购则标 0，否则丢弃。
- 三类方法：DP（Mistral-7B-Instruct-v0.3 直接 prompt 输出判断）；PDJ（prompt 分解为 6 个标准评分再输出判断）；PFC（PDJ 分解分数 + 显式特征 + 线性/XGB/浅层神经网络分类器）；REC（ModernBERT 对同一 prompt 文本做 embedding + 32 神经元浅层网络分类）。
- 数据：Walmart.com 一周搜索日志，11k 条请求，80/20 划分，正负样本平衡。

**关键结果**
REC-Snn 全面领先：ROC-AUC 0.853、AP 0.873、Accuracy 0.768、F1 0.765；DP 最差（AUC 0.596），且几乎把所有样本都预测为 1，输出分数集中在 0.7-0.8；PDJ 提升到 0.673，但仍受等权结合限制；PFC-Xgb 达到 0.734，仍低于 REC。消融显示：PFC 移除显式特征后 AUC 下降 0.02-0.05，而 REC 增加显式特征仅提升 0.002，说明 ModernBERT embedding 已经编码了 stack 类型、位置等结构化信号。

**最值得记住的一句话**：在页面级布局评估中，轻量级语义表示（ModernBERT embedding）比 LLM-as-judge 更可靠、更轻量，是离线评估的实用基础。
