---
title: 'Pass the Baton: Trajectory-Relayed On-Policy Distillation'
title_zh: 传递接力棒：轨迹接力的On-Policy蒸馏
authors:
- Haolei Xu
- Xiaowen Xu
- Haiwen Hong
- Zixuan Ni
- Hongxing Li
- Yiwen Qiu
- Weiming Lu
- Yongliang Shen
affiliations:
- Zhejiang University
- Yuvion Team, Alibaba Group
arxiv_id: '2607.26057'
url: https://arxiv.org/abs/2607.26057
pdf_url: https://arxiv.org/pdf/2607.26057
published: '2026-07-28'
collected: '2026-07-29'
category: Training
direction: On-policy 蒸馏 · 接力轨迹
tags:
- On-Policy Distillation
- Knowledge Distillation
- Mathematical Reasoning
- Relay Trajectory
- LLM Training
- Prefix Failure
one_liner: 通过检测前缀失败并让教师短暂接管生成修正轨迹，将错误前缀转化为有效蒸馏信号，显著提升小模型数学推理性能
practical_value: '- **前缀失败的无标签检测**：利用教师和学生预测分布差异（如相同位置token概率差）作为接力触发信号，无需额外标注，可直接用于对话Agent的推理步骤监控，在发现错误倾向时自动引入更强模型纠正。

  - **接力蒸馏减轻训练浪费**：电商场景中，如果推荐理由生成或查询改写模型产生错误前缀，可用更大模型局部修正后继续，既能保留学生探索，又能提供正确梯度，比全丢弃重采样更高效。

  - **接力预算控制成本**：限制最大接力步数和干预次数，将修正集中在关键早期位置，平衡干预收益与计算开销，适合在线学习或大规模分布式训练。

  - **思路可迁移至多步推理Agent**：当Agent进行多步骤决策（如购物决策、多轮对话）时，若某步走错，可让教师模型介入修正后再交还，最终全程轨迹用于优化学生，提升整体成功率。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：On-policy distillation (OPD) 让学生从自身采样轨迹中学习，但一旦生成初期犯错（前缀失败），后续所有token都建立在错误方向上，既浪费计算又产生无效监督信号。

**方法关键点**：
- 发现**教师-学生延续不对称性**：面对失败前缀，教师倾向于重定向，学生却继续原有方向。
- 提出 **Relay-OPD**：训练时，根据学生和教师分布差异自动检测触发点（无标签），教师短暂接管生成一段“教师腿”，再交还学生继续生成，形成接力轨迹，并以此轨迹优化学生。
- 引入**有限接力预算**：限制总接力步数和单次最大步数，确保干预集中在早期关键位置且不过度偏离学生策略。

**关键结果**：
- 在Qwen3-4B教师、Qwen3-0.6B/1.7B学生上测试8个数学推理基准，1.7B模型较标准OPD平均提高**+5.73%**，较最强基线FastOPD提高**+1.49%**，所有基准均获最优或次优；0.6B模型同样一致提升。
- 训练轨迹长度减少超过**50%**，大幅提升训练效率。
