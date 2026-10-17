---
title: Explaining the Roles of Experts in Mixture-of-Experts LLMs for Personalization
title_zh: 解释 MoE 大语言模型在个性化中的专家角色
authors:
- Sekh Mainul Islam
- Pepa Atanasova
- Isabelle Augenstein
affiliations:
- University of Copenhagen
arxiv_id: '2610.22127'
url: https://arxiv.org/abs/2610.22127
pdf_url: https://arxiv.org/pdf/2610.22127
published: '2026-10-14'
collected: '2026-10-17'
category: LLM
direction: MoE LLM 个性化与可解释性
tags:
- MoE
- Personalization
- Interpretability
- Crosscoder
- Sparse Routing
- Causal Intervention
one_liner: 用 MoE LLM 做个性化并通过 crosscoder 定位可解释个性化 latent 与专家路由，验证其因果作用
practical_value: '- 可尝试把个性化底座从 dense LLM 换成 MoE LLM：论文显示 MoE 个性化性能与 dense 有竞争力，但只激活一小部分参数，适合电商/广告等对推理成本敏感的场景；在线服务时稀疏路由也能降低尾部延迟。

  - 用 crosscoder 对「个性化前后模型」的成对激活学习可解释 latent，能直接定位哪些专家在编码个性化特征。业务上可以用类似方法做个性化模块审计，找出哪些专家/层负责特定用户群偏好，便于后续剪枝、蒸馏或加约束。

  - 文中通过 boosting 相关专家让非个性化模型向个性化模型靠拢，说明个性化行为有可操控的专家路由路径。可以借鉴为「可控个性化开关」：对某些用户群或场景，只强化对应专家，避免全量微调或
  prompt 注入。

  - MoE 降低 polysemanticity 的结论提示：如果线上模型需要更强的可解释性、便于合规审查（如推荐理由、广告定向），选择稀疏架构比 dense
  更容易解耦特征。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**  
LLM 个性化大多基于 dense 模型，其神经元多语义、难以定位个性化相关部件，导致理解和控制个性化困难。MoE 稀疏路由每个 token 到少数专家，可能降低多语义性，为个性化解耦提供条件。

**方法关键点**  
- 选三个开源 MoE LLM，在大规模个性化数据集上微调，得到个性化 MoE 模型。  
- 对个性化与非个性化模型成对激活训练 crosscoder，学习可解释的个性化 latents。  
- 从 latents 中识别编码不同个性化特征的专家，并与 dense 模型对比多语义程度。  
- 通过因果干预验证：直接从 latents 恢复个性化行为，以及 boosting 相关专家驱动非个性化模型向个性化模型迁移。

**关键结果数字**  
- 个性化 MoE 性能与 dense LLM 有竞争力，但仅激活一小部分参数。  
- 同等激活参数量下，MoE 的多语义性低于 dense LLM。  
- 同模型家族中，个性化 latents 与非个性化模型共享更少。  
- 因果干预显示 latents 足以恢复个性化行为；boosting 对应专家可让非个性化模型趋近个性化模型，并揭示不同个性化特征有不同路由路径。
