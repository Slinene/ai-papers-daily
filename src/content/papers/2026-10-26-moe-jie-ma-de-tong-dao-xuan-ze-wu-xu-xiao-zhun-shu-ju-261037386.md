---
title: Channel Selection for Mixture-of-Experts Decoding Needs No Calibration Data
title_zh: MoE 解码的通道选择无需校准数据
authors:
- Geunhyoung Kim
- Sung Ju Hwang
affiliations:
- KAIST
- DeepAuto.ai
arxiv_id: '2610.37386'
url: https://arxiv.org/abs/2610.37386
pdf_url: https://arxiv.org/pdf/2610.37386
published: '2026-10-26'
collected: '2026-10-29'
category: LLM
direction: MoE 推理加速 · 通道选择
tags:
- MoE
- Channel Selection
- LLM Inference
- Top-k
- Ternary Sketch
- Low-rank Recovery
one_liner: 证明 MoE 通道选择用 top-k 即可，无需离线校准阈值；并提出基于模型权重的三值草图+低秩恢复读取器，以 17.8% 读取量保持 98.1%
  精度
practical_value: '- 部署 MoE 大模型做电商/推荐场景的在线推理或 Agent 时，通道选择直接采用 top-k 分数筛选，不必维护离线校准阈值；阈值会因输入分布变化导致实际读取比例漂移（文中
  18% 预算实际仅读 12.9%），top-k 则天然固定每 token 读取预算，便于做延迟 SLO。

  - 若沿用阈值方案，需警惕生成任务中的重复循环崩溃，尤其在长文本/Agent 多轮输出中风险更高；可优先切到 top-k，并用生成类 benchmark 而非只看困惑度验证。

  - 文中 reader 完全从模型权重构造，用 ternary sketch 筛选通道 + low-rank map 恢复被跳过通道，不依赖校准集；这可作为无校准数据的稀疏化插件，适合线上数据分布频繁变化的场景。

  - Triton kernel 在 batch 1 比 vLLM 快 1.60–1.90×，大 batch 达 2.69×；如果自建 MoE 推理服务，可参照其通道读取+恢复实现，在
  interactive decoding 小 batch 场景降低 expert weight 读取带宽。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：MoE 模型在交互式解码小 batch 下，瓶颈是 routed expert 权重的内存读取；通道选择器通常用离线校准阈值决定读哪些通道，但实际读量与精度不稳定。

**方法**：作者证明通道选择不需要校准数据。校准阈值并不能固定读取预算：Prox 在 18% 预算阈值下平均只读 12.9%。相比之下，对每个 token 取 k 个最高分通道的 top-k 无需校准数据，并在相同预算下匹配或超过阈值版本：13% 和 18% 预算下 43 项比较中 40 项更好或持平，生成任务 23 项全胜；还避免了 Gemma 4 上的重复循环崩溃。进一步提出完全基于模型权重的 reader：用 ternary sketch 筛选通道，再用 low-rank map 恢复被跳过的通道。

**结果**：在三个 post-trained MoE 模型上，reader 以 17.8% 的 routed-expert 读取量保留 98.1% 全模型精度；Triton kernel 使 MoE block 比优化 vLLM 在 batch 1 快 1.60–1.90×，大 batch 最高达 2.69×。
