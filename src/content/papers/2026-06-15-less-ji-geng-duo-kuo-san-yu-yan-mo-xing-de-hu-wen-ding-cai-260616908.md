---
title: 'LESS Is More: Mutual-Stability Sampling for Diffusion Language Models'
title_zh: LESS 即更多：扩散语言模型的互稳定采样
authors:
- Amr Mohamed
- Guokan Shang
- Michalis Vazirgiannis
affiliations:
- MBZUAI
- Ecole Polytechnique
arxiv_id: '2606.16908'
url: https://arxiv.org/abs/2606.16908
pdf_url: https://arxiv.org/pdf/2606.16908
published: '2026-06-15'
collected: '2026-06-16'
category: LLM
direction: 扩散语言模型推理加速
tags:
- diffusion language models
- adaptive sampling
- inference efficiency
- training-free
- LLM
one_liner: 提出训练无关的自适应采样器 LESS，通过联合稳定性规则在线决定 token 揭示时机，以 72.1% 更少步骤保持精度。
practical_value: '-  若业务中尝试将扩散模型用于生成式推荐（如 Semantic ID 生成），LESS 可嵌入推理流程，自适应提前终止不稳定的
  token，直接减少 Transformer 前向次数并降低延迟。

  -  其 top-K JS 散度稳定性判据与 top-1 置信度/持久性规则可以独立迁移到其他 token 级早停（early exiting）场景，比如在序列生成中按位置动态分配计算量。

  -  该采样器无需训练、模型无关，可作为即插即用模块快速集成到现有扩散 LLM 部署中，无需重新训练或修改模型权重。

  -  本文主要学术贡献在于扩散 LM 的高效采样，若业务尚未使用扩散模型，直接可借鉴点有限；但在 Agent 系统里若用扩散模型做规划或工具调用生成，LESS
  可加速推理。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：扩散语言模型（dLLM）通过迭代去噪掩码序列实现并行更新，但现有固定步长的采样过程浪费计算在已稳定位置，且可能过早确定不稳定 token，导致低效与质量损失。

**方法**：提出训练无关的自适应采样器 LESS，将 token 确定看作在线停止问题。它只允许满足三个联合稳定性条件的位置解除掩码：(1) top-1 预测置信度高于阈值；(2) top-1 token 在最近数步内保持一致；(3) 相邻步 top-K 预测分布的 Jensen-Shannon 散度低于阈值。满足条件的 token 立即固定，其余保持掩码继续迭代，直至所有位置稳定或达到最大步数。

**结果**：在 Dream-7B、LLaDA-8B 等模型和 7 个基准上，LESS 比强训练无关采样基线平均准确率更高，同时节省 72.1% 的反向步数，直接转化为更少的 Transformer 前向、更低的实际延迟和推理计算量。
