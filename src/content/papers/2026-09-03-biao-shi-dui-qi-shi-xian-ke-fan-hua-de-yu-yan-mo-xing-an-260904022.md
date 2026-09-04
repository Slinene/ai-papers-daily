---
title: Representational alignment yields generalizable safety in language models
title_zh: 表示对齐实现可泛化的语言模型安全
authors:
- Lingyu Li
- Yan Teng
- Yingchun Wang
- Xia Hu
affiliations:
- Shanghai Artificial Intelligence Laboratory
arxiv_id: '2609.04022'
url: https://arxiv.org/abs/2609.04022
pdf_url: https://arxiv.org/pdf/2609.04022
published: '2026-09-03'
collected: '2026-09-04'
category: Training
direction: LLM 表示级安全对齐
tags:
- Representational Alignment
- Safety
- Jailbreak Robustness
- ReSO
- Moral Categorization
- DPO
one_liner: 提出 ReSO，直接对齐 LLM 潜在表示与人类道德分类结构，在不监督响应的情况下提升对抗鲁棒性
practical_value: '- 在内容安全/合规审核中，不要只做输出层微调（如 DPO），可对物品/内容/query 的表示与安全分类结构做表示级对齐，增强对对抗改写、隐晦违规的泛化。具体可用
  triplet 排序损失拉近同类安全内容表示、拉远危险表示。

  - 若已有安全分类标签/人工判断，可构造 graded category vector（严重度×置信度），用 Bradley-Terry 目标对 latent
  相似度排序进行优化，不需要生成标签，适合标签稀疏或冷启动场景。

  - 监控训练过程中验证 RSA 与攻击成功率（ASR）的相关性，作为早停/剂量指标；在 ReSO 中观察到后期 RSA 回归伴随 ASR 上升，避免过拟合。

  - 对 Agent 系统，若依赖 LLM 做安全决策，可考虑对状态/动作表示做类似对齐，提升对未见对抗输入的鲁棒性，而不是仅依赖 prompt 或输出过滤。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**  
现有 LLM 安全对齐主要优化可观测响应（DPO/RLHF），但模型在相同有害意图被改写为陌生或对抗形式时仍易被越狱。人类通过原型分类对道德概念进行泛化，而 LLM 主要基于语言统计压缩，可能未保留这种类别结构。问题：行为对齐能否改变内部表示？表示对齐能否带来可泛化的安全？  

**方法关键点**  
- 从 Social-Chemistry-101 提取 251,334 条单标注道德判断，基于 Moral Foundations Theory 五个对立维度（care-harm 等）构造十维 graded morality vector，幅值编码 confidence-weighted typicality。  
- 分析 23 个 open-weight LLM（0.6B–235B，base/instruct/safeguard），发现对立道德类别原型重叠、typicality 梯度弱（峰值 Spearman <0.55）、线性探测 R² 峰值仅 0.34，安全对齐未显著改变内部表示。  
- ReSO：对每层残差流表示做 RSA，构造三元组，用 Bradley-Terry 损失对齐模型相似度与人类 similarity 排序，每层独立并平均；增加 preservation KL 散度（对 frozen ref）保持能力。不监督生成 token。  
- 对比 DPO（同数据构造偏好对）和 shuffled-label 控制。  

**关键实验与结果**  
在 Qwen3-8B/14B/32B 和 gpt-oss-20b 上训练。DPO 快速提升道德判断准确率（约 0.69–0.78）但 RSA 几乎不变；ReSO 提升验证 RSA（0.05→0.24–0.28），判断准确率仅小幅上升。9 个 OOD 基准测试：ReSO 在 HarmBench 上 ASR 从 26.17%→14.72%（8B）、22.48%→13.33%（14B）、19.00%→13.67%（32B）；DeceptionBench 分别降低 21.67、13.22、12.11 个百分点；27 种 OpenRT 攻击中有 23/23/19 种 ASR 降低。DPO 反而升高 ASR。gpt-oss-20b 上 HarmBench ASR 从 3.33%→1.33%。Qwen3-8B 训练轨迹中 RSA 解释 ASR 变化 86%。  

**最值得记住的一句话**  
模型可以学会表面合规的输出策略却不具备支撑泛化的概念组织；直接优化表示关系能同时提升安全与减少过度拒答。
