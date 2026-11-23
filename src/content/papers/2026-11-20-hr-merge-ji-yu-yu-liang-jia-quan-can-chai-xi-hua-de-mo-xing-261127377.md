---
title: 'HR-Merge: Model Merging with Headroom-Weighted Residual Refinement'
title_zh: HR-Merge：基于余量加权残差细化的模型合并
authors:
- Jiakang Huang
- Xueyan Zhang
- Renyi Cai
- Jingcheng Niu
- Jiaru Li
- Yining Wang
- Josh Zhang
- Jiahe Jiang
- Jinman Zhao
- Gerald Penn
affiliations:
- University of British Columbia
- University of Toronto
- Technische Universität Darmstadt
- Northwestern University
- University of California, Los Angeles
arxiv_id: '2611.27377'
url: https://arxiv.org/abs/2611.27377
pdf_url: https://arxiv.org/pdf/2611.27377
published: '2026-11-20'
collected: '2026-11-23'
category: LLM
direction: 模型合并 · LoRA 多任务残差修复
tags:
- Model Merging
- LoRA
- Task Vector
- Multi-task
- Training-free
- Residual Refinement
one_liner: 训练无关包装器HR-Merge按任务验证余量加权残差并重新合并，恢复多任务合并中丢失的精度
practical_value: '- 多域/多任务 LoRA 合并部署时，可直接包装 HR-Merge：按各任务验证集掉点比例（headroom）对残差加权，再用原合并算子（TIES/DARE
  等）融合，最后在验证集上选择加回强度，无增益就回退，训练成本为零。

  - 适合解决长尾或小流量任务在合并后掉点严重的问题：先计算 task vector − merged update 的残差，用 headroom 识别值得恢复的弱任务，避免对已饱和任务过度修正。

  - 工程上风险低、可渐进上线：只需保留各任务 task vector 和少量验证样本，在已有合并 checkpoint 上做一次轻量 refine，不需要重训或梯度更新。

  - 注意不同任务的残差会互相干扰，不能简单相加，必须用同一 base merge operator 融合；否则恢复不稳定，业务实现时应沿用现有合并算子的规则。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：模型合并将多个 fine-tuned 专家组合为单一多任务模型，但现有方法对所有任务使用同一规则，导致各任务精度损失不均匀，弱任务常常被牺牲。

**方法**：作者发现丢失的精度可以从每个任务的残差（task vector 减去合并后的 update）中恢复，并定义验证 headroom 为合并损失的专家验证精度占比，用来衡量恢复收益。HR-Merge 是一个训练无关的包装器，可包裹任意合并方法：先按各任务 headroom 对残差加权，再用基础合并算子重新合并加权残差，最后以验证集选择加回强度；若没有强度带来提升，则回退到基础合并结果。

**关键结果**：在 LLaMA-3 8B 的六个 NLI LoRA adapters 上，HR-Merge 将 TIES 的归一化准确率从 93.29 提升至 94.29，超过所有测试基线，主要通过恢复最弱任务实现；在视觉领域，横跨三个 CLIP backbone、最多 20 个任务以及 LoRA 合并设置中，普遍改善或保持基础准确率，并在所有设置中取得最佳模型。
