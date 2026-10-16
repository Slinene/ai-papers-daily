---
title: 'CleanRM: Reward Modeling from Noisy Feedback with a Few Clean Feedback for
  RLHF'
title_zh: CleanRM：用少量干净反馈对 RLHF 做样本级噪声奖励建模
authors:
- Licheng Pan
- Haocheng Yang
- Yuzhou Chen
- Yichen Sun
- Yuan Lu
- Yunfei Teng
- Jiajun Fan
- Guangyi Liu
- Zhixuan Chu
- Hao Wang
affiliations:
- Zhejiang University
- Xiaohongshu Inc
- National University of Singapore
- New York University
- University of Illinois at Urbana-Champaign
arxiv_id: '2610.21138'
url: https://arxiv.org/abs/2610.21138
pdf_url: https://arxiv.org/pdf/2610.21138
published: '2026-10-15'
collected: '2026-10-16'
category: Training
direction: RLHF 奖励建模 · 样本级噪声校正
tags:
- reward modeling
- RLHF
- label noise
- optimal transport
- denoising
- sample-wise noise
one_liner: 用少量干净反馈经最优传输校准样本级噪声率，并构造无偏代理损失提升奖励建模与 RLHF
practical_value: '- 点击、点赞、评分等 point-wise 反馈噪声天然是样本级的，不应沿用全局噪声率假设；可抽样少量高质量人工/专家复核样本作为
  clean set，训练一个轻量样本级噪声率估计器，再做损失校正。

  - 把 CleanRM 的两阶段思路迁移到 CTR/CVR 或推荐 reward 建模：先学样本级翻转概率 μ(x)、ν(x)，再用无偏 surrogate loss
  训练主模型；相比全局 IPS 或 forward correction，更贴合业务中不同 item/query 的噪声异质性。

  - 最优传输对齐 clean set 和 noisy set 的联合 (embedding, preference) 分布，工程上只需 backbone 输出的
  embedding 和少量干净标签，不需要大规模标注；可复用于 LLM-as-judge 的评分去偏，尤其当业务依赖模型打分构建训练信号时。

  - 下游策略优化对 reward model 的噪声高度敏感；在电商/Agent 场景如果要用 reward model 驱动策略或排序，先做样本级去噪能直接放大下游收益，论文中
  FFT 安全分数相对 naive 提升 79.5% 可作为收益量级参考。'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

**动机**  
偏好数据中的反馈噪声普遍存在，来源包括人类主观判断、标注错误和 imperfect LLM judge。标准 reward model 直接在噪声反馈上训练，会对 clean risk 产生有偏估计。经典去噪方法通常假设全局统一噪声率，但偏好噪声本质上是样本级的：例如明确指令遵循错误几乎无争议，而两个都合理但侧重不同的回答容易出现标注分歧。因此需要样本级噪声建模。

**方法关键点**  
- 假设能获得少量干净反馈 D_clean（可通过专家审计或重复标注得到），用它校准样本级噪声率。  
- 训练一个双头噪声率估计器 p_φ(x) 输出 μ(x) 和 ν(x)，分别表示正偏好翻转为负、负偏好翻转为正的概率。  
- 通过反演二元转移方程，用 μ(x)、ν(x) 从噪声反馈 r 恢复估计的真实偏好 r̂*_φ(x)。  
- 用 Wasserstein optimal transport 对齐恢复后的 noisy 联合分布与 clean 联合分布；联合代价由 preference 预测损失与输入 embedding 距离加权组成，从而驱动条件偏好分布对齐。  
- 用估计出的样本级噪声率构造 noise-corrected surrogate loss：使期望损失等于 clean loss 的唯一线性组合，理论证明该代理损失对 clean risk 无偏。  

**关键实验**  
在 HelpSteer、UltraFeedback、PKU-SafeRLHF 三个偏好数据集上模拟样本级噪声，保留 5% 干净反馈。CleanRM 在 R² 和 MSE 上全面超过 20 多个基线；相比最强基线 TrainRef，R² 分别提升 +0.052、+0.013、+0.032。消融显示样本级噪声率估计贡献最大，surrogate loss 提供互补增益。跨 Qwen3-8B/32B 和 LLaMA3.1-8B/70B 均稳定有效。下游 GRPO 对齐实验中，Qwen3-8B 在 FFT 安全分数上比 naive 高 79.5%，比最强基线 TrainRef 再高 16.3%。

**最值得记住的一句话**  
反馈噪声是样本级的，用少量干净反馈经最优传输校准样本级翻转概率，再训练无偏代理损失，是提升 reward model 和下游 RLHF 对齐的有效路径。
