---
title: 'From Layers to Submodules: Rethinking Granularity in Replacement-Based LLM
  Compression'
title_zh: 从层级到子模块：重思替换式LLM压缩的粒度
authors:
- Elia Cunegatti
- Marcus Vukojevic
- Erik Nielsen
- Giovanni Iacca
affiliations:
- University of Trento
arxiv_id: '2606.02559'
url: https://arxiv.org/abs/2606.02559
pdf_url: https://arxiv.org/pdf/2606.02559
published: '2026-06-01'
collected: '2026-06-02'
category: LLM
direction: 后训练压缩 · 子模块级残差替换
tags:
- LLM Compression
- Submodule Replacement
- Residual Bypass
- Post-training
- Structured Pruning
one_liner: 提出子模块级非连续替换方法 SUBFIT，利用残差旁路拟合，在困惑度与准确率折衷上显著优于层级替换基线。
practical_value: '- 对 LLM 部署中的推理加速有直接帮助：25% 稀疏度下可实现 1.12×~1.17× 的解码加速和 25% 的 KV 缓存节省，适合电商应用中需要低延迟、高并发的
  agent 或推荐服务。

  - 子模块级非连续选择策略可推广到其他模型的细粒度压缩，例如在生成式推荐或 agent 的多组件 Transformer 中，可独立对 Attention/FFN
  进行按需裁剪，而非粗暴删除整个层。

  - 闭式残差旁路拟合（利用特征协方差和低秩近似）仅需数千条校准样本，无需反向传播，这可以作为一种“剪枝后快速恢复”的手段嵌入到现有的 post-training
  流水线中，降低压缩成本。

  - 共享 FFN 输入基的设计在保持质量的同时大幅减少额外参数（约为原 FFN 参数的 1/10），类似 LoRA 的思路但应用于压缩，可参考其跨层参数共享方式以降低多任务或大模型的部署显存。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

## 动机
后训练压缩是缩小 LLM 部署成本的主要途径，已有的替换式方法（如 Streamline、ReplaceMe）都在**层粒度**上移除连续的 Transformer 层，并用轻量模块替换。作者指出这种设计过于僵化：预训练 Transformer 中的冗余并不局限于连续区域，Attention 与 FFN 子模块的冗余分布也不同，因此不同子模块类型应使用不同的近似策略，且可移除的子模块无需聚集在连续深度上。

## 方法关键点
- **子模块级替换**：SUBFIT 在 **Attention 和 FFN 子模块**粒度上做非连续选择，独立决定每个子模块的去留，不再要求整层或连续块。
- **顺序评分与选择**：先计算 Attention 子模块的“影响度得分”（结合残差旋转幅值与大小时评估），选最低分的模块移除；再在部分压缩后的模型上，对 FFN 采用“替换感知得分”（基座模型）或仅依赖余弦相似度（指令微调模型）。
- **统一残差旁路结构**：对每个移除的子模块，拟合一个同形式的轻量旁路 `g⊙x + b + (x-μ)U`，其中 `U` 为低秩矩阵。Attention 的旁路 U 为每个子模块独立；FFN 则共享一个低秩输入基 `V`，仅保留层特定的投影 `Wℓ` 和仿射项，大幅减少参数。
- **闭式解拟合**：旁路参数通过校准数据的统计量直接解出，无需梯度优化：仿射项由经验均值确定，门控系数由岭回归得到，低秩基取输入协方差的 top-r 特征向量，输出系数再用岭回归求解。

## 关键结果
- 在 5 个基座模型、5 个指令微调模型、5 个稀疏度（12.5% 至 37.5%）上对比 Streamline 和 ReplaceMe 的四种变体，SUBFIT 在 **困惑度–准确率折衷上整体最优**：25% 稀疏度时，平均保留 84.6% 的下游准确率，而最强基线仅 81.6%；PPL 劣化因子 2.42× vs 4.34×。
- 压缩越激进优势越大：37.5% 稀疏度下 PPL 劣化 5.76×，远低于基线（22.28×–339.31×）。
- 推理加速：25% 稀疏度下 TTFT 加速 1.18~1.40×，解码加速 1.12~1.17×，KV 缓存使用按比例下降（如 DeepSeek-7B 从 240MB 降至 176MB）。
- 消融表明：FFN 补偿对稳定性起主导作用，Attention 旁路仅需极低秩（256），而 FFN 需要更高秩（4096）；替换感知选择优于纯掩码评分；共享 FFN 基与逐层基质量接近，但参数大幅减少。
