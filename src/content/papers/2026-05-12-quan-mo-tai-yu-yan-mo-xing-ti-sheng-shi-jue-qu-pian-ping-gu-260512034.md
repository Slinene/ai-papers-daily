---
title: 'Boosting Omni-Modal Language Models: Staged Post-Training with Visually Debiased
  Evaluation'
title_zh: 全模态语言模型提升：视觉去偏评估下的分阶段后训练
authors:
- Che Liu
- Lichao Ma
- Xiangyu Tony Zhang
- Yuxin Zhang
- Haoyang Zhang
- Xuerui Yang
- Fei Tian
arxiv_id: '2605.12034'
url: https://arxiv.org/abs/2605.12034
pdf_url: https://arxiv.org/pdf/2605.12034
published: '2026-05-12'
collected: '2026-05-17'
category: Multimodal
direction: 全模态模型训练优化与视觉去偏评估
tags:
- Omni-modal
- Post-training
- Visual Shortcut
- Self-distillation
- RLVR
- Evaluation
one_liner: 通过视觉去偏基准OmniClean与三阶段后训练，3B全模态模型无需强教师即可匹敌30B模型
practical_value: '- **消除评估中的模态泄漏**：在电商多模态搜索或推荐评估中，检查图像是否单独能给出答案（如商品图直接暴露属性），构建去偏测试集，避免模型走视觉捷径，暴露真实跨模态理解能力。

  - **三阶段后训练策略复用**：先做模态平衡的SFT打底，再用RLVR统一提升跨模态对齐，最后利用自蒸馏（self-distillation）精调，这套流程可复用到多模态Agent或生成式推荐模型的微调中，逐步压榨小模型性能。

  - **小模型无强教师自蒸馏**：用模型自身生成高质量的"全模态查询 + 响应"对进行监督学习，无需更大教师模型，适合资源受限的电商场景（如端侧多模态助手），可降低推理成本。

  - **审计现有基准以指导训练**：电商中常有多模态评测集（如商品图文问答），可以先做只输入图像的探测，识别并剔除可纯视觉求解的样本，使训练反馈更干净，优化方向更明确。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**  
当前全模态基准测试存在视觉泄漏：大量查询仅靠视觉就能正确回答，导致模型分数虚高，无法反映真实的音-视-语言联合理解能力。  

**方法关键点**  
1. 构建OmniClean：对9个全模态基准进行视觉-only探测，去除视觉可解样本，保留8511条需真正跨模态整合的查询，获得干净评估集。  
2. 提出OmniBoost三阶段后训练（基于Qwen2.5-Omni-3B）：  
   - 第一阶段：**平衡双模态SFT**，混合视觉、视频、音频-语言数据，避免单模态过拟合。  
   - 第二阶段：**混合模态RLVR**，用强化学习奖励统一优化跨模态表现。  
   - 第三阶段：**自蒸馏SFT**，用模型自身生成的"全模态查询+高质量响应"对再做监督微调，重塑能力分布。  

**关键结果**  
- 平衡SFT带来有限且不均衡的提升；RLVR首次广泛提升所有任务；自蒸馏最终将性能推至接近并略超Qwen3-Omni-30B-A3B-Instruct，无需强教师。  
- 在OmniClean上，3B模型通过分阶段训练实现与30B级模型相当的整体表现，验证了去偏评估下训练的有效性。
