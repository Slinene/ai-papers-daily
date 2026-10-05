---
title: 'When History Misleads: Asymmetric Margin Supervision for Instruction-Guided
  LLM Generative Recommendation'
title_zh: 当历史误导：指令引导LLM生成式推荐的非对称边际监督
authors:
- Ming Yin
- Yuhan Yang
- Chen Chen
- Xinyu Lin
- Wentao Shi
- Fangcong Yin
- Chaofei Yang
- Chao Yang
- Jiyan Yang
- Hui Zhang
affiliations:
- Duke University
- Meta
arxiv_id: '2610.02600'
url: https://arxiv.org/abs/2610.02600
pdf_url: https://arxiv.org/pdf/2610.02600
published: '2026-10-01'
collected: '2026-10-05'
category: GenRec
direction: 生成式推荐 · 指令跟随与历史纠偏
tags:
- LLM Generative Recommendation
- Instruction-Guided
- Counterfactual Margin
- History Bias
- Semantic ID
- Asymmetric Loss
one_liner: 提出AIMS，把单条历史删除效应转化为请求特定的反事实排序边际目标，用非对称辅助损失在完整历史上训练
practical_value: '- 在电商/搜索的指令引导生成式推荐中，用户当前 query 与历史行为冲突常见（如“素食快手菜” vs 历史“红烧肉”）。可以离线用冻结模型评估删除单个历史事件对目标物品分数和
  target–competitor margin 的影响，只保留同时提升两者的删除，把对应 margin 作为训练目标；训练仍用完整历史，推理零额外开销，适合大规模工业系统。

  - 非对称梯度路由值得借鉴：辅助排序损失中把目标物品分数 detach，梯度只回传竞争者分数。这避免与 CE 对目标分数的直接监督冲突，能更干净地压低边界竞争者而不损害目标，可复用到
  pairwise/ranking loss 设计。

  - 做历史去噪或特征归因时，不能只看 influence 或 target uplift。本文证明无标签的 prediction sensitivity 与目标
  support 几乎不相关，且 target uplift 高可能 competitor uplift 更高。实际应使用有标签的离线 margin 校验筛选干预，而不是仅依赖敏感度或单边
  uplift。

  - 简单 history dropout 不能复现 AIMS 的收益，说明“忽略冲突历史”不是把历史随机丢掉的等价做法。在冲突请求上增益更大，且 AIMS 选择的删除优先移除违反当前约束的历史事件，这提示可以显式构造约束冲突样本并用
  margin 监督来纠正。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
指令引导的 LLM 生成式推荐需要同时响应当前请求和利用交互历史。当两者冲突时，历史事件可能覆盖请求，例如用户要“快手素食晚餐”，但历史中的慢炖牛肉视频使模型排高了三小时牛肉炖菜。现有方法通过编辑历史、反事实训练或偏好优化来缓解，但直接编辑可能丢失个性化信息。本文指出两个障碍：一，历史事件对预测的影响大小（influence）与它对目标物品的有符号支持（utility）不一致，称为 Influence–Utility Misalignment；二，删除误导事件可能提高目标分数，但同时提高边界竞争者分数更多，因此目标分数上涨不保证排序改善。

**方法关键点**  
提出 AIMS（Asymmetric Intervention-Guided Margin Supervision）。离线阶段，冻结的 SFT 参考模型对每个初始 top-R 正确的训练请求，逐条删除历史事件（默认 K=1），计算目标分数 uplift 和 target–competitor margin gain，只有两者都超过阈值 τ 才接受该删除，并缓存最大的 margin gain，得到请求特定的反事实边际 mcf = m0 + g。训练阶段，学生模型仍输入完整历史，损失 = CE + λ ACS。ACS 为 hinge 损失：`[mcf_i - ε - sg(sθ(y_i)) + sθ(c_i)]_+`，其中目标分数被 detach，梯度只通过竞争者分数（asymmetric competitor suppression）。推理不变，无删除搜索。

**关键结果**  
在工业数据集和 Qilin、KuaiSearch-Lite 两个公开基准上，使用 Llama-3.1-8B/70B、Gemma-3-4B/12B、Qwen3-8B/14B 六个 backbone，AIMS 全面取得最佳 Recall@10 和 NDCG@10，相对 Continued CE 的 Recall@10 相对提升 4.0–10.9%。消融表明：请求特定 margin 目标、基于 margin 的删除选择、完整历史训练、非对称梯度路由均关键；冲突请求上增益更大，且 AIMS 选择的删除优先移除违反当前请求约束的历史事件。

最值得记住的一句话：**历史事件的删除效应应作为排序边际的监督信号，而不是直接编辑输入；用非对称梯度只压边界竞争者，可以在保留完整历史的同时纠正指令-历史冲突。**
