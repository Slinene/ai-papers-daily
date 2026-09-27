---
title: 'RLVR landscapes for iterated multiplications can be benign: Insights from
  spin-glass theory'
title_zh: 迭代乘法的 RLVR 景观可良性：自旋玻璃理论的启示
authors:
- Noa Rubin
- Zohar Ringel
affiliations:
- Racah Institute of Physics, The Hebrew University of Jerusalem
arxiv_id: '2609.28625'
url: https://arxiv.org/abs/2609.28625
pdf_url: https://arxiv.org/pdf/2609.28625
published: '2026-09-23'
collected: '2026-09-27'
category: Reasoning
direction: RLVR 优化景观与推理训练
tags:
- RLVR
- spin-glass
- optimization landscape
- chain-of-thought
- policy gradient
- reasoning
one_liner: 用自旋玻璃证明 RLVR 算法任务景观无局部极小，困难在扩散障碍与梯度误差；transformer 仅末 token 奖励可学算法思维链
practical_value: '- RLVR 训练卡住时先别归因于景观 rugged：在无关联输入的算法任务中景观通常无局部极小，应优先排查梯度估计噪声与 credit
  assignment，用更大 batch、动态采样或更稳的 baseline。

  - 熵正则项选择是关键：调节 entropy regularizer 可缓解扩散障碍，帮助策略穿过平坦/高熵区域；在 LLM 推理 RLVR 可尝试调高熵系数，避免过早收敛到次优确定性策略。

  - 只用 last-token reward 从零训练 transformer 也能学到非交换群乘法的算法 CoT，说明验证奖励加长序列生成可在无中间奖励下学会推理，值得在可自动验证的业务任务（如规则链推理、订单状态预测）尝试。

  - 注意理论假设是 tabular/myopic/uncorrelated inputs，直接迁移到真实电商 Agent 需谨慎；但对 RLVR 训练调参和故障排查有方向性参考。'
score: 7
source: arxiv-stat.ML
depth: abstract
---

动机：RLVR 是 LLM 推理能力提升的主要工具，但它能否学到新推理、优化景观是否 rugged 仍存争议，尤其 credit assignment 与噪声梯度带来开放问题。

方法：将熵正则化、myopic tabular policy 的 RLVR 映射到 deterministic policies 上的自旋玻璃能量模型；该映射给出 RLVR 性能上界，并允许严格刻画景观。研究对象包括 iterated group/quasigroup multiplication 等算法任务。

结果：理论与实验表明，对无关联输入的广泛模型与任务类景观良性、无局部极小，不会 trap RLVR 训练；实际困难来自扩散障碍和梯度估计误差，而非景观 rugged。选择合适熵正则器可缓解这些障碍。与此一致，从零训练的 transformer 仅用 last-token reward 成功学会非交换群乘法的算法链式思维。
