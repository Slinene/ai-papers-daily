---
title: 'OSReward: Instituting Standardized Evaluation for Cross-Platform Computer-Use
  Reward Models'
title_zh: OSReward：建立跨平台计算机使用奖励模型的标准化评估基准
authors:
- Qiushi Sun
- Kanzhi Cheng
- Yian Wang
- Bowen Yang
- Hang Yan
- Liheng Chen
- Fangzhi Xu
- Zichen Ding
- Nuo Chen
- Jialin Cao
affiliations:
- The University of Hong Kong
- Nanjing University
- National University of Singapore
- University of Science and Technology of China
- Xi'an Jiaotong University
arxiv_id: '2607.28609'
url: https://arxiv.org/abs/2607.28609
pdf_url: https://arxiv.org/pdf/2607.28609
published: '2026-07-30'
collected: '2026-08-01'
category: Eval
direction: 计算机使用Agent奖励模型评估
tags:
- Computer-Use Agent
- Reward Model
- VLM Judge
- Benchmark
- Bias
- Open-Source
one_liner: 揭示VLM评判器普遍存在宽松偏差，并推出低成本开源奖励模型OS-Shepherd实现可靠自动化评估
practical_value: '- **警惕LLM-as-Judge中的宽松偏差**：在电商搜索、推荐系统的离线评估或RLHF reward模型中，若直接使用商业VLM作为评判器，可能系统性地将失败案例误判为成功，需通过构建类似OSReward-Hard的对抗样本集进行可靠性校准。

  - **用reasoning标注蒸馏小型评估器**：借鉴OS-Shepherd的思路，收集专家推理标注的评估数据集，训练7-9B的小模型替代GPT-4o等大模型作为评估器，实现30-60倍成本下降，同时保持高一致性，适合大规模线上监控或离线评估。

  - **多维度细粒度评分设计**：可迁移OSReward-Multi的评分框架，在推荐业务中将评估分解为效率、对齐、多样性等子维度，便于定位Agent或推荐策略的具体短板。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：计算机使用代理(CUA)的轨迹验证依赖VLM评判器，但其可靠性未经系统检验，且商业大模型成本过高，开源模型差距显著。

**方法**：构建OSReward基准，包含多平台、多代理的真实轨迹，经多阶段人工标注获得高信度标签。衍生OSReward-Hard（困难集）和OSReward-Multi（细粒度评分）。全面评测10+主流VLM，发现**系统性宽松偏差**：即使GPT-4o等顶级模型也将大量失败轨迹误判为成功，可靠模型（如Gemini-1.5-Pro）推理成本过高。为此，构建含推理注释的OS-Shepherd-100K数据集，并基于此训练开源奖励模型OS-Shepherd（9B/35B），仅需1-2张消费级GPU即可运行。

**关键结果**：OS-Shepherd-9B在OSReward上与GPT-4o准确率相当，35B版更优，成本仅为商业模型的1/30至1/60；人类一致性分析显示其与人工评判高度对齐，有效克服宽松偏差。
