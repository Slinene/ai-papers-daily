---
title: 'Role-Break in Attention Heads: Understanding and Detecting Hallucinations
  in VLMs'
title_zh: 注意力头角色断裂：理解与检测VLM幻觉
authors:
- Mingyu Wang
- Weilin Jin
- Wenbo Li
- Haoyang Huang
- Nan Duan
- Tong Jia
- Chaoran Luo
- Ying Li
affiliations:
- Peking University
- Joy Future Academy
arxiv_id: '2607.29412'
url: https://arxiv.org/abs/2607.29412
pdf_url: https://arxiv.org/pdf/2607.29412
published: '2026-07-31'
collected: '2026-08-03'
category: Multimodal
direction: 视觉语言模型幻觉检测
tags:
- VLM
- Hallucination
- Attention Heads
- Detection
- Role-Break
one_liner: 发现幻觉使注意力头偏离忠实上下文行为（角色断裂），基于此构建轻量线性检测器，AUROC 达 93.23%
practical_value: '- 在电商多模态推荐（如商品图生成描述/问答）中，可借鉴 Role-Break 信号构建轻量线性检测器（特征维度<5000），无需微调
  VLM 即可识别幻觉输出，提升生成内容可信度。

  - 检测器基于注意力头行为的局部偏离，具备线性可读性和可解释性，适合作为实时监控或过滤模块，拦截不可靠的生成文本。

  - 若 Agent 工作流中调用 VLM 进行图像理解，可将此检测器后置，对高幻觉 token 直接干预（屏蔽/重生成），降低下游决策风险。

  - 该方法不依赖单一幻觉模式，跨模型/任务稳定性强，可用于多模态推荐系统的质量保障。'
score: 7
source: arxiv-cs.CV
depth: abstract
---

**动机**：视觉语言模型(VLM)在生成描述、问答时易产生幻觉，现有检测方法多针对单一模式（如视觉-文本失衡），难以跨模型和任务稳定。

**方法**：从注意力头视角统一观察，发现幻觉导致局部注意力头偏离其“忠实上下文行为”，形成系统性的“角色断裂”(Role-Break)。这种偏离在头、上下文来源、偏离方向上组织有序，且保留头身份后信号线性可分。基于此，构建轻量线性检测器，特征维度低于5000，无需对VLM微调。

**结果**：在6个VLM、4个基准上平均AUROC 93.23%；小规模干预实验表明，检测到的幻觉token在判别式设置下可直接处理。
