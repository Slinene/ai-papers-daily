---
title: 'Kimi K3: Open Frontier Intelligence'
title_zh: Kimi K3：开源前沿智能体——2.8T参数MoE模型与强化学习实践
authors:
- Kimi Team
- Tongtong Bai
- Yifan Bai
- Yiping Bao
- M. C.
- Jianfeng Cai
- Xinyuan Cai
- Peizhou Cao
- Yuxuan Cao
- Ziwei Chai
affiliations:
- Moonshot AI
arxiv_id: '2607.24653'
url: https://arxiv.org/abs/2607.24653
pdf_url: https://arxiv.org/pdf/2607.24653
published: '2026-07-26'
collected: '2026-07-28'
category: LLM
direction: 大规模 MoE 模型前沿训练与强化学习
tags:
- Mixture-of-Experts
- Reinforcement Learning
- Long Context
- Test-Time Scaling
- Agent
- Open-Source
one_liner: 开源2.8T参数MoE模型，融合KDA、AttnRes和Stable LatentMoE架构，通过多领域多推理努力强化学习达到封闭前沿水平
practical_value: '- **强化学习训练范式**：部分回滚（partial rollout）方案允许长周期任务跨迭代训练，对搜索 / 推荐系统中基于用户长期反馈的强化学习优化具有直接借鉴意义。

  - **多教师在线蒸馏（MOPD）**：将多个领域、不同推理努力水平的专家策略融合为单一模型的技术，可应用于合并不同排序目标的推荐模型（如点击率、转化率、多样性等）。

  - **推理部署优化**：全后训练阶段集成的量化感知训练（QAT）及 EAGLE-3 投机解码微调，可降低大模型推荐 / 搜索推理成本，对线上部署有实际工程价值。

  - **长上下文架构设计**：KDA 与 Attention Residuals 的混合注意力可高效处理超长序列，可迁移至用户行为序列建模，支持更长行为记忆和更精准的长期兴趣提取。'
score: 9
source: huggingface-daily
depth: full_pdf
---

**动机**  
开源模型在前沿预训练规模上长期停滞于 1T 参数级别，而闭源系统已通过扩大基座和强化学习（RL）持续拉大差距。Kimi K3 旨在同时扩展预训练与 RL 测试时计算，以开源方式逼近最强封闭模型。

**方法关键点**  
- **架构创新**：混合注意力（3 层 Kimi Delta Attention + 1 层 Gated MLA 每块）实现高效长上下文建模；Attention Residuals 让每层可选择性关注前序所有层输出；Stable LatentMoE 将路由专家数扩至 896、激活 16，配合 SiTU-GLU 与分位数平衡（QB）保证极端稀疏下的稳定训练。  
- **预训练**：2.8T 总参、104B 激活、1M 上下文；多模态数据从零训练视觉编码器 MoonViT-V2；余弦退火学习率、Per-Head Muon 优化器；上下文长度从 8K 渐进扩展到 1M，整体训练效率较 Kimi K2 提升约 2.5 倍。  
- **后训练 RL**：在通用、通用 Agent、编程三个领域各自训练低/高/最大推理努力共 9 个专家；采用部分回滚的同步 RL 框架支持超长 Agent 轨迹；通过多教师在线策略蒸馏（MOPD）统一为单一模型；全程量化感知训练（QAT）及 EAGLE-3 投机解码微调以降低部署成本。

**关键结果**  
在 DeepSWE（73.0）、FrontierSWE（42.0）、SWE-Marathon（86.6）、BrowseComp（91.2）等编程与 Agent 基准上，Kimi K3 均大幅领先其他开源模型，综合性能仅次于 Claude Fable 5 和 GPT-5.6 Sol；同时实现了 2.5× 的预训练缩放效率增益。
