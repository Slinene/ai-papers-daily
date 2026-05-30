---
title: How LoRA Remembers? A Parametric Memory Law for LLM Finetuning
title_zh: LoRA的参数记忆定律：量化LLM微调中的精确记忆容量
authors:
- Ziwen Xu
- Haiwen Hong
- Linsong Yu
- Benglei Cui
- Longtao Huang
- Hui Xue
- Ningyu Zhang
affiliations:
- Zhejiang University
- Alibaba Group
arxiv_id: '2605.30260'
url: https://arxiv.org/abs/2605.30260
pdf_url: https://arxiv.org/pdf/2605.30260
published: '2026-05-28'
collected: '2026-05-30'
category: LLM
direction: 参数记忆 · 幂律缩放与相变
tags:
- Parametric Memory
- LoRA
- Power Law
- MemFT
- Phase Transition
- Fine-tuning
one_liner: 发现LoRA的记忆增益遵循幂律定律，并利用p>0.5的相变阈值设计MemFT优化精准回忆。
practical_value: '- **LoRA作为记忆插件**：在电商/Agent场景中，需精确记住配置、规则或用户凭证时，可用LoRA模块存储，MemFT方法能在有限秩下显著提升准确率，避免关键token错误。

  - **容量预估公式**：幂律定律∆L=C·r^α·ℓ^{-β}可帮助在资源受限时快速估算所需的最小秩r，避免盲目分配参数。例如，给定序列长度ℓ，可计算达到目标损失所需的秩。

  - **关注关键token**：业务中生成式推荐或Agent输出常因个别token错误导致整句失效，借鉴p>0.5的相变思想，在微调时动态分配梯度给低概率token，而不过度优化已掌握的token，可提升整体生成质量。

  - **MemFT的训练策略**：滑动窗口（MemFT-SW）聚焦首次错误位置的上下文，课程学习逐步增加困难样本，这些技巧可直接迁移到其他需要精确生成的任务（如广告文案、商品描述）的LoRA微调中。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**
大模型部署后需要持续吸收新知识（如更新的事实、用户偏好），LoRA作为参数效率的微调方法常被用作“记忆插件”，但其精确记忆（verbatim memorization）的容量边界和底层机制仍不清晰。现有评估依赖下游任务（如问答）混杂了理解与推理，难以独立量化记忆容量。

**方法关键点**
1. **精确记忆任务**：给定key-value对，仅通过LoRA参数存储value，要求模型根据key完整复现value，彻底解耦记忆与理解。
2. **参数记忆定律**：扫描LoRA秩r和序列长度ℓ，发现损失减少量∆L与r、ℓ服从幂律：`∆L(r,ℓ)=C·r^α·ℓ^{-β}+b`，对8B模型拟合R²>0.98。α与β分别表征容量与长度惩罚。
3. **确定性相变**：Token级别分析显示，平均损失低不代表记忆成功；贪婪解码下，目标token预测概率p>0.5是正确回忆的充分条件（对应损失临界值ln2≈0.693）。低于此阈值的顽固token（stubborn tokens）会引发自回归级联崩溃。
4. **MemFT方法**：基于相变阈值重新分配梯度，仅对p<0.5的token加权优化。MemFT-OT使用硬阈值掩码，MemFT-SW进一步引入滑动窗口（聚焦首次错误位置的上下文）和课时课程（由易到难安排batch）。

**关键实验**
在Qwen3-8B和Llama3.1-8B上进行长期记忆压力测试（长序列随机token）和PhoneBook（短key-value）基准。SFT在低秩时记忆失败，而MemFT显著提升：例如Llama3.1-8B的r=1时，MemFT-SW将token级准确率从27.4%提至32.5%；高秩时MemFT-OT可达100%完美记忆。PhoneBook上MemFT-SW最早达到100%精确匹配率。额外实验显示，MemFT在规则学习任务上的泛化能力也优于SFT（提升7-15%）
