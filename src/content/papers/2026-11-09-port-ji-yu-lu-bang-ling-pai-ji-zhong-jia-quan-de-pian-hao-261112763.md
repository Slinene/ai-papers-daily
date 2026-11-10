---
title: 'PORT: Preference Optimization via Robust Token-Level Reweighting'
title_zh: PORT：基于鲁棒令牌级重加权的偏好优化
authors:
- Ding Zhu
- Xiukun Wei
- Tian Xie
- Zhihui Zhu
- Xueru Zhang
- Mohammad Mahdi Khalili
affiliations:
- Department of Computer Science and Engineering, The Ohio State University
arxiv_id: '2611.12763'
url: https://arxiv.org/abs/2611.12763
pdf_url: https://arxiv.org/pdf/2611.12763
published: '2026-11-09'
collected: '2026-11-10'
category: Training
direction: LLM 对齐 · 鲁棒偏好优化
tags:
- Preference Optimization
- DPO
- Robustness
- Token-Level Reweighting
- LLM Alignment
- Noisy Preferences
one_liner: 在噪声偏好下，用 token log-prob 的 CDF 做前向重加权，抑制错误 token 并减少梯度偏差
practical_value: '- 推荐/搜索里用 LLM 做生成式排序或 Agent 输出对齐时，偏好对经常来自点击、转化等隐式信号，噪声比例高；可参考 PORT
  把序列级 DPO/IPO 的 loss 改成 token 级重加权，对错误 token 而不是整个样本降权。

  - 工程实现上，PORT 只需要前向 log-prob，用经验 CDF 映射成权重，不需要额外 backward 或梯度范数计算，适合在线/增量训练与大规模偏好数据清洗。

  - 遇到 rejected 样本中仍包含有效推理步骤、preferred 样本含局部错误时，不要全盘接受/拒绝；可以在 token 粒度选择性保留信息，这对搜索
  query 改写、文案生成等任务尤其有用。

  - 若业务偏好标注来自规则或弱监督，优先用 PORT 替代标准 DPO，能降低标注噪声带来的 reward hacking 和梯度偏差。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

动机：偏好优化（DPO/IPO）依赖偏好标注质量，但真实数据充满标注错误和模糊性；现有鲁棒方法多为序列级，把整个 rejected 响应当作完全错误，忽略其中有效推理步骤，也忽略 preferred 响应中的局部错误。

方法关键点：PORT 做 token 级重加权。核心是用 token log-prob 的经验累积分布函数（CDF）作为权重，近似梯度范数惩罚，仅需前向传播即可选择性抑制被噪声破坏的 token，无需额外反向传播。理论分析表明，PORT 通过最小化噪声偏好标签导致的梯度偏差上界来降低偏差。

关键结果：在多种噪声设置下，PORT 一致提升鲁棒性，并优于现有序列级基线；代码已开源。
