---
title: DiffusionGemma Technical Report
title_zh: DiffusionGemma：基于 Gemma 4 微调的离散扩散高速文本生成模型
authors:
- DiffusionGemma Team
- Adrien Ali Taïga
- James Assiene
- Daniele Calandriello
- Rahma Chaabouni
- João Gante
- Tamara von Glehn
- Nate Keating
- Chris Knutsen
- Martin Kukla
affiliations:
- Google DeepMind
arxiv_id: '2608.00146'
url: https://arxiv.org/abs/2608.00146
pdf_url: https://arxiv.org/pdf/2608.00146
published: '2026-07-30'
collected: '2026-08-05'
category: LLM
direction: 文本扩散模型 · 高速块生成
tags:
- discrete diffusion
- text generation
- MoE
- RL+distillation
- inference optimization
- adaptive stopping
one_liner: 通过微调 AR 模型结合 RL 与采样器蒸馏，实现离散扩散文本生成，速度达 ~1500 TPS，远超自回归模型
practical_value: '- **块级并行生成降低延迟**：在需要实时响应的对话或文案生成场景中，可直接借鉴 DiffusionGemma 的块扩散范式，采用
  256 token 并行去噪的方式代替逐 token 解码，大幅降低单用户服务延迟，尤其适合低并发、低批量的推理场景。

  - **RL 与采样器蒸馏联合训练可压缩推理步数**：对生成式推荐或搜索改写等系统，可设计类似的在线训练流程（SD·RL），将奖励最大化与推理步数压缩作为联合目标，使模型在保持生成质量的同时大幅减少前向次数，提升吞吐。

  - **自适应停止机制动态节省算力**：对于不同复杂度的任务（如简单商品描述 vs. 复杂推荐理由），可以引入基于预测熵的自适应停止策略，对简单任务早期停止去噪，避免固定步数浪费计算，实现“按需计算”。

  - **保留 AR 能力实现混合解码**：在 Agent 系统中，可根据延迟要求和任务复杂度动态切换扩散模式或 AR 模式，或混合使用两者，平衡生成速度与质量，为请求路由策略提供新的自由度。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
当前大型语言模型普遍采用自回归（AR）逐 token 生成，在低并发服务时存在严重的内存带宽瓶颈，导致解码速度受限。离散扩散模型通过并行生成整个 token 块，有望从根本上突破这一瓶颈，但现有扩散模型要么速度不足，要么智能程度不够，且多为闭源。本研究旨在提供一个开放权重的高性能文本扩散模型，在不牺牲智能水平的前提下大幅提升生成速度。

## 方法关键点
- **模型初始化**：以 Gemma 4 26B A4B（MoE 架构）的公开权重为起点，共享 Transformer 结构，保留其多模态、长下文和 think 能力。
- **两阶段训练**：
  - **SFT**：利用离散多项式扩散过程，将模型从单向注意力改造为双向注意力，在 256 token 的画布上去噪，学习从噪声预测干净 token。
  - **SD·RL（采样器蒸馏 & 强化学习）**：在线联合优化生成质量（RL 奖励）与推理效率（压缩去噪步数），通过自适应停止和温度退火引导模型在极少步骤内产出高质量结果。
- **采样策略**：使用 entropy-bounded sampler，按熵从小到大接受 token 并重噪声其他位置；温度从 0.8 线性退火到 0.4；自适应停止条件为平均熵 < 0.005 且连续两步预测相同。
- **推理优化**：在 H100 GPU 上利用 FlashAttention-4、异步调度、因果注意力 flag 等，单个去噪步耗时约 13.56ms。

## 关键结果
- **速度指标**：在思考模式下，平均Tokens Per Forward (TPF) 达 19.74，输出吞吐约 1479 TPS（H100，FP8），约为同规模 Gemma 4 AR 模型的7.1×，带 MTP 的 4.8×。
- **质量对比**：在推理/知识、编程、指令遵循与 agent 三大类 benchmark 上，DiffusionGemma 大幅超越现有开源扩散模型（LLaDA 2.1 Flash、Nemotron Diffusion），与闭源 Mercury 2 接近，但吞吐为其 2.5×。
- **训练效率**：总训练 token 量不足原 AR 模型的 10%，SD·RL 进一步将有效去噪步数从 SFT 的较高值压缩至约 12 步。
- **双模能力**：微调后仍能进行 AR 解码，性能衰减有限，为混合解码提供基础。

## 核心启示
“用少数量块并行去噪代替 token-by-token 生成，并通过联合优化质量与步数，可以将大模型带入超低延迟的新帕累托前沿。”
