---
title: Multi-Agent Forensic Reasoning for Generalizable Deepfake Video Detection
title_zh: 基于多智能体法医推理的可泛化深度伪造视频检测
authors:
- Xuechao Zou
- Shun Zhang
- Kai Li
- Yi Zhou
- Xinyu Sun
- Yuhui Chen
- Zhe Wu
- Congyan Lang
- Junliang Xing
affiliations:
- Beijing Jiaotong University
- Tsinghua University
- Ant Group
arxiv_id: '2608.06865'
url: https://arxiv.org/abs/2608.06865
pdf_url: https://arxiv.org/pdf/2608.06865
published: '2026-08-06'
collected: '2026-08-11'
category: MultiAgent
direction: 多智体协同法医推理
tags:
- Multi-Agent
- Deepfake Detection
- MLLM
- Forensic Reasoning
- Generalization
one_liner: 提出多专家Agent分别分析纹理、光照、运动、物理伪造线索，以小型开源MLLM超越GPT和Gemini
practical_value: '- 多专家Agent分工架构：可借鉴到推荐系统的多信号融合——设计多个Agent分别专注商品视觉、文本描述、用户行为等不同特征，再由协调Agent融合决策，提升系统鲁棒性。

  - Judge Agent的冲突解决机制：类似推荐的多路召回融合排序，可设计一个元Agent来处理各专家意见分歧，结合置信度加权或投票策略，提高最终决策质量。

  - 小型开源MLLM的多Agent组合超越单一大模型：在资源受限的业务场景（如移动端推荐助手），可通过多个小模型协同达到不逊色于闭源大模型的性能，降低推理成本。

  - 自动化标注流水线：多模型聚合与冲突解决自动生成细粒度图文注释，可用于电商评论分析、商品描述增强等任务，提升数据标注效率。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有深度伪造检测数据集覆盖合成方法有限，缺乏细粒度文本标注；单模型或单视角方法难以捕捉微小伪造痕迹，对新兴 AI 生成方法泛化差。  
**方法**：构建大规模数据集 **FaceVid-Forensics-100K**，含 10 万视频、33 种合成方法，并自动生成视觉描述与法理解释（通过多 MLLM 聚合与冲突解决）。提出多智体框架 **ARGUS**：四个专家 Agent（纹理、光照、运动、物理）独立分析伪造线索，每个 Agent 基于小型开源 MLLM（如 InternVL2）微调；Judge Agent 整合所有报告，输出最终预测及解释。  
**关键结果**：在域外测试集上，全由小型开源 MLLM 组成的框架性能超越所有对比方法（包括 GPT-4o、Gemini），在准确率、AUC 等多个指标上排名第一，验证了多视角协同推理的泛化能力。
