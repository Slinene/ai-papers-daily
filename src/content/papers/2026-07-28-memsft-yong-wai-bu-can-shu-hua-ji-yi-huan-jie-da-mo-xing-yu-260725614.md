---
title: 'MemSFT: Mitigating Alignment Tax with an External Parametric Memory'
title_zh: MemSFT：用外部参数化记忆缓解大模型领域微调的对齐税
authors:
- Jiarui Wang
- Xiang Shi
- Jiaqi Cao
- Rubin Wei
- Xiquan Wang
- Hao Sun
- Jingzhi Wang
- Zhiqi Yang
- Qipeng Guo
- Bowen Zhou
affiliations:
- Shanghai Jiao Tong University
- Shanghai AI Laboratory
- Tsinghua University
arxiv_id: '2607.25614'
url: https://arxiv.org/abs/2607.25614
pdf_url: https://arxiv.org/pdf/2607.25614
published: '2026-07-28'
collected: '2026-07-29'
category: LLM
direction: 领域专精 · 外部参数化记忆
tags:
- Parametric Memory
- Alignment Tax
- Catastrophic Forgetting
- Domain Specialization
- Token-level Routing
- LLM Adaptation
one_liner: 通过外部参数化记忆和token级动态路由器，在不修改基座模型参数的前提下注入领域知识，完全避免通用能力遗忘
practical_value: '- **记忆训练范式**：利用领域数据构建 kNN 检索的 soft label 作为教师分布，结合 KL 散度和交叉熵训练一个独立的
  Memory LM，避免直接微调基座模型，可向电商搜索/推荐 LLM 注入商品、规则等新知识而不损害通用对话与推理能力。

  - **动态路由器设计**：轻量两层 MLP 以基座和记忆的隐藏状态及输出置信度/熵为特征，预测 token 级融合权重；训练时混合领域与通用数据并加入符号正则，自动学习何时依赖记忆，适用于生成推荐理由、推送文案等需要专业性与通用性平滑拼接的场景。

  - **记忆复用**：同一记忆模块可在共享 tokenizer 的不同规模基座模型上即插即用，无需重训；在电商多模型矩阵中，可一次训练商品知识记忆，供多款 LLM
  部署使用，显著降低维护成本。

  - **工程成本**：训练一个 8B 记忆和路由器的 FLOPs 仅占全量 SFT 的一小部分（如四个基座模型总成本仅 0.22 倍），适合快速迭代注入新业务线知识。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**  
大模型在垂直领域 SFT 虽能大幅提升领域性能，但会带来“对齐税”（alignment tax），即严重遗忘数学推理、指令遵循等通用能力。LoRA 等参数高效方法只能减缓，仍无法消除性能‑保留的权衡。为此，MemSFT 提出将领域知识存入外部参数化记忆，彻底解耦基座模型参数更新。

**方法关键点**  
1. **检索教师构建**：在领域 SFT 数据上建立 token 级 kNN 数据存储，对每个答案位置检索近邻并生成非参数教师分布（soft label），提供更丰富的领域监督信号。  
2. **记忆训练**：训练一个独立的 Memory LM（与基座同 tokenizer），通过 KL 散度和交叉熵损失模仿教师分布，从而内部化领域知识。  
3. **路由器训练**：冻结基座和记忆后，训练一个两层 MLP 路由器，输入两模型的隐藏状态和输出分布特征，预测 token 级融合权重 λ，最终分布为 (1‑λ)·p_base + λ·p_memory；训练目标为融合分布的 CE 损失，并加入符号正则（领域 token 倾向增大 λ，通用 token 减小 λ）。  
4. **推理**：基座与记忆并行前向，路由器动态输出 λ，实现 token 级混合。

**关键实验与结果**  
- 在生物学（BioIns）、地球科学（OpenSWI）和法律（LawBench）三个领域，使用 Qwen3‑8B 至 235B 及 Llama2‑13B 骨架。  
- BioIns：MemSFT 将平均分从 5‑6 提升至 42+（+37 以上），通用平均分变化 <0.6，而 SFT 和 LoRA 分别导致通用分下降 13.5 和 17 分。  
- OpenSWI：8B 模型 RMSE 从 103 降至 0.47，通用能力无损失。  
- 法律：LawBench 提升 6.6 分，通用性能持平。  
- 同一 8B 记忆可跨 8B‑235B 模型复用，适配四个模型的总 FLOPs 仅为全量 SFT 的 0.22 倍。  
- 路由器行为：自动区分功能词（λ≈0.2）、领域术语（λ≈0.43）、数值 profile token（λ≈0.99），无需人工规则。
