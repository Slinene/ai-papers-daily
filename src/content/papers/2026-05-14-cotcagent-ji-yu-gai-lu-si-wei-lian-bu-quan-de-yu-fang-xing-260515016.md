---
title: 'COTCAgent: Preventive Consultation via Probabilistic Chain-of-Thought Completion'
title_zh: COTCAgent：基于概率思维链补全的预防性咨询系统
authors:
- Zihan Deng
- Xiaozhen Zhong
- Chuanzhi Xu
affiliations:
- The University of Hong Kong
- University of Electronic Science and Technology of China
- The University of Sydney
arxiv_id: '2605.15016'
url: https://arxiv.org/abs/2605.15016
pdf_url: https://arxiv.org/pdf/2605.15016
published: '2026-05-14'
collected: '2026-05-16'
category: Agent
tags:
- EHR
- Agent
- Clinical Reasoning
- Knowledge Base
- Probabilistic Scoring
- Chain-of-Thought
one_liner: 通过解耦可执行趋势统计、IDF 加权知识库评分和有界对话补全，COTCAgent 实现纵向 EHR 的可审计疾病排序。
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

## 动机
纵向电子健康记录（EHR）为临床诊断提供关键时序证据，但现有大语言模型（LLM）在此场景下存在两大缺陷：一是缺乏细粒度统计推理，常因文本隐含的定量信息产生趋势和指标幻觉，导致诊断偏倚；二是非均匀时间序列和标签稀缺使模型难以捕获长程依赖，制约可靠临床推理。因此，需要一种能将统计计算、知识匹配与语言生成解耦的框架，以保障可审计性和推理可靠性。

## 方法关键点
COTCAgent 是一个层次化推理框架，由三个核心模块构成：
- **Temporal-Statistics Adapter (TSA)**：将自然语言查询映射为统计分析方案并生成可执行代码，输出类型化趋势谓词（如斜率、变点后验质量等），完全避免 LLM 自行生成数值声称；内置路由器按意图分派统计方法（混合效应模型、贝叶斯变点检测等），失败时自动降级并标记不确定性。
- **Chain-of-Thought Completion (COTC)**：基于一个覆盖 9,948 种疾病的症状‑趋势‑疾病知识库（KB），引入逆疾病频率（IDF）加权。疾病评分采用 Gibbs 能量形式：正症状贡献 `log w_IDF + log φ`，缺失症状施加惩罚 `log(1-γ·w_IDF)`，再经 softmax 归一化为排名概率。通过能量门限 `T` 和概率门限 `θ` 控制确认终止。
- **有界补全模块**：迭代识别信息缺口，生成模板式澄清问题，并将用户回复解析为离散证据重新计算评分，直至排名概率超出阈值或熵降至指定水平。整个流程的每一步都锚定在 KB 条目或对话轮次，实现全程可追溯。

## 关键结果
在自建的纵向病历数据集上，COTCAgent 结合 Baichuan-M2 取得 Top‑1 准确率 90.47%、F1 86.74%，大幅超越 TimeCAP（80.47%）、DirPred（88.27%）、KARE（83.76%）等现有医疗智能体，以及 GPT‑4o、Claude 3.7 Sonnet 等前沿模型。在 HealthBench 基准上达到 70.41% 准确率，同样领先其它方法。KB 边缘消融显示，仅保留 25% 边缘时准确率下降 11.3 个百分点，表明框架在 KB 稀疏时仍有较好鲁棒性；轮次归因实验表明约 70% 的交互增益来自第一轮提问。表示探针进一步证实，添加 TSA 与 COTC 后编码器状态的时间连贯性和语义分离度显著提升。

> **核心启示**：将统计计算、符号匹配与自然语言生成显式分层，使纵向 EHR 推理的每一个决策都能回溯到可执行的代码或知识库行，是走向透明、可信临床智能的关键一步。
