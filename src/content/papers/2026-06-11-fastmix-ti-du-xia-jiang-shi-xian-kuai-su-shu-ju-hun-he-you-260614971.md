---
title: 'FastMix: Fast Data Mixture Optimization via Gradient Descent'
title_zh: FastMix：梯度下降实现快速数据混合优化
authors:
- Haoru Tan
- Sitong Wu
- Yanfeng Chen
- Jun Xia
- Ruobing Xie
- Bin Xia
- Xingwu Sun
- Xiaojuan Qi
affiliations:
- University of Hong Kong
- Tencent Hunyuan LLM
- Chinese University of Hong Kong
arxiv_id: '2606.14971'
url: https://arxiv.org/abs/2606.14971
pdf_url: https://arxiv.org/pdf/2606.14971
published: '2026-06-11'
collected: '2026-06-23'
category: Training
direction: 训练数据配比优化 · 梯度下降
tags:
- data mixture
- bilevel optimization
- gradient descent
- pre-training
- post-training
one_liner: 将数据混合比例重新参数化为可微损失权重，实现单代理模型高效联合优化
practical_value: '- 推荐模型训练中常需对不同行为（点击、加购、购买）或不同频道的数据做采样配比，FastMix 提供了一种**单模型、梯度驱动的自动搜索方案**，替代手动调参或耗时的网格搜索。

  - 关键 trick：将**采样概率重参数化为损失权重**，使混合系数完全可微，可用 SGD/Adam 直接优化，仅需一个代理模型即可完成搜索，计算成本降低数百倍。

  - 为避免过拟合到验证集，可借鉴其**熵正则 + 训练损失辅助目标**的策略，提升上线后的泛化能力；工业场景可进一步用**上采样率上限**替代纯正则。

  - 代理模型不宜太小（如 <0.5B），建议采用与原模型同架构但参数减半的版本；若预训练与微调序列长度不匹配，可通过**拼接 SFT 序列**对齐长度，避免梯度失真。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：大模型预训练与后训练中，数据混合比例（如不同文本源、数学/代码/对话数据的比例）对最终能力至关重要。传统方法依赖人工试错或训练数百个代理模型（如 RegMix 需 512 个、CLIMB 需 64 个），计算成本随模型和数据规模增长变得不可承受。亟需一种仅用单个代理模型就能高效、稳定地搜索最优混合的策略。

**方法关键点**
- **可微双层优化**：将混合搜索重定义为双层优化问题。核心创新是把采样概率α转化为每源损失权重，使得 `L_train = Σᵢ αᵢ L_train(Dᵢ,w)`，在均匀采样下计算各源损失，这样α直接嵌入可微目标，支持梯度下降。
- **交替优化**：内循环用当前α更新模型参数w，外循环每隔 n₂ 步用验证损失对α求梯度并更新α。当 n₂=1 时存在闭式梯度：∂L_val/∂αᵢ ∝ -⟨∇_w L_val, ∇_w L_train(Dᵢ)⟩，即根据训练梯度与验证梯度的对齐程度自动调整权重。
- **泛化增强**：在外层损失中引入熵正则（鼓励权重均匀，防坍塌）和训练损失辅助项（平衡验证与训练信号），提升混合权重在未见任务上的迁移能力。
- **工程建议**：非可微目标可用可微代理（如 SFT loss）；长序列预训练/微调不匹配时，拼接多条微调序列对齐长度；避免用极小代理模型（<0.5B）做搜索。

**关键实验**
- **预训练**：在 Pile 的 17 个子集上搜索，仅用 1.3 GPU 小时（比 RegMix 快 550 倍，比 CLIMB 快 55 倍），得到的混合权重在 1B 模型 25B tokens 训练后，14 个基准平均 48.2 分，排名第一，其中 9 个基准最优。
- **后训练**：以 Qwen2.5-1.5B 为代理，搜索数学微调数据混合，2.2 GPU 小时完成（对比方法超 115 小时），在数学、代码、STEM 问答 4 项基准上平均 65.4 分，比 CLIMB 高 5.5 分，且展现出跨领域泛化。
