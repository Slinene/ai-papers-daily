---
title: Detecting LLM-Generated Tokens in Human--LLM Coauthored Text
title_zh: 检测人-LLM合作文本中的LLM生成Token
authors:
- Yangjun Lu
- Hongyi Zhou
- Fabian Spill
- Kai Ye
- Chengchun Shi
- Jin Zhu
affiliations:
- University of Birmingham
- Shanghai University of Finance and Economics
- London School of Economics and Political Science
arxiv_id: '2607.21458'
url: https://arxiv.org/abs/2607.21458
pdf_url: https://arxiv.org/pdf/2607.21458
published: '2026-07-23'
collected: '2026-07-25'
category: Other
direction: 细粒度LLM生成文本定位与检测
tags:
- token-level detection
- LLM-generated text
- kernel smoothing
- Lepski's method
- human-AI coauthoring
one_liner: 提出基于自适应带宽核平滑的token级检测方法，无需标注数据即可定位LLM生成片段。
practical_value: '- 在电商评论、客服对话等场景中，可基于现有token级生成概率分数，结合局部平滑算法定位LLM生成内容，无需额外标注数据，快速部署。

  - 自适应带宽选择策略（Lepski规则）能根据局部作者变化动态调整平滑程度，可迁移到其他需要局部自适应的检测任务，如点击序列异常检测。

  - 方法简单，可直接替代固定阈值或全局分类，适用于自动化内容审核、欺诈评论识别等场景，降低人工审核成本。

  - 开源实现和网页工具便于快速实验，可作为业务中检测混合作者文本的基线方法。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

**动机**：人类与大语言模型协同写作日益普遍，但现有检测方法多为文档级分类，无法细粒度定位文本中哪些部分由LLM生成，这限制了内容透明性和真实性验证。

**方法**：本文在已有token级检测分数的基础上，提出一种无需标注数据的后处理方法。核心思路是对相邻token的检测分数进行核平滑以降低变异性，同时引入Lepski型自适应规则自动选择平滑带宽，使其根据局部作者结构动态调整。该方法无需训练，可直接应用于任何token级生成概率输出。理论上，作者分析了估计量的均方误差特性，并证明了其在捕捉底层作者信号方面的优势。

**结果**：在合成数据集和真实人-LLM合著数据集上进行评估，与多种基线方法（包括固定阈值、文档级分类器）相比，所提方法在token级检测准确率和F1分数上均有显著提升，尤其在局部平滑效果上表现稳健。作者还公开了在线演示工具。
