---
title: 'Deeper is Not Always Better: Mitigating the Alignment Tax via Confident Layer
  Decoding'
title_zh: 更深未必更好：通过自信层解码缓解对齐税
authors:
- Xuanming Zhang
- Sining Zhoubian
- Yuxuan Chen
- Tianyi Tang
- An Yang
- Sean Du
- Chujie Zheng
- Fei Huang
- Dayiheng Liu
- Gao Huang
affiliations:
- Qwen Team, Alibaba Inc.
- Tsinghua University
- Nanyang Technological University
arxiv_id: '2606.21906'
url: https://arxiv.org/abs/2606.21906
pdf_url: https://arxiv.org/pdf/2606.21906
published: '2026-06-19'
collected: '2026-06-24'
category: Reasoning
direction: LLM推理解码优化·动态层选择
tags:
- Confident Decoding
- Alignment Tax
- Entropy Valley
- Layer Selection
- Decoding Strategy
- Reasoning
one_liner: 发现LLM最终层会引入对齐扰动，提出训练无关的熵指导层选择解码策略，在推理任务上稳定提升性能且零额外内存开销
practical_value: '- **生成式推荐的解码去偏置**：在生成式推荐（如Semantic ID生成）中，若模型经过用户偏好对齐，最后层可能高概率输出安全、通用的ID或文本，丢失个性化与多样性。可借鉴Confident
  Decoding，在生成每个token时动态回溯到预测熵最低的层，恢复精细化、领域相关的推荐词，提升推荐独特性和准确性。

  - **Agent推理时的保守性缓解**：AI Agent在执行复杂规划或搜索推荐策略时，LLM的最终层对齐可能导致过度谨慎（如拒绝合理但非常规行动），使用熵谷层解码可在不破坏整体安全护栏的前提下，解锁更富有创造性的推理路径，增强Agent在开放环境中的探索能力。

  - **近乎零成本的推理增强**：该方法无需修改模型权重、无需额外训练，仅动态切换采样层，额外延迟<2%、无KV缓存开销，可快速集成到现有的LLM推理引擎（如vLLM）中，非常适合在生产环境中对已有模型进行无痛部署，立即提升推荐/搜索/问答等复杂任务的性能。

  - **推理任务难易自适应的介入机制**：实验表明对高难度推理任务（如复杂数学）提升极大，对简单任务几乎无影响。在推荐场景中，可根据请求复杂性自动选择是否启用，避免不必要的计算，实现自适应解码策略。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：LLM推理通常约定从最后一层解码，假设中间层表示逐步精化，最终层最可靠。但本文通过层贡献范数和残差余弦相似度分析，发现前向传播呈现“猜测-精炼-扰动”三阶段：最终层由于RLHF/DPO等对齐训练，会引入背离推理语义的扰动，使预测偏向通用、安全的token，损害复杂推理性能（对齐税）。因此，需要一种动态方法，在不改变模型和增加开销的情况下，绕过最终层扰动，提取精炼阶段的最优预测。

**方法关键点**：
- **层动态建模**：量化各层的相对贡献范数和残差IO余弦相似度，将正向传播划分为Phase I（猜测）、Phase II（精炼）、Phase III（扰动），发现最终层会使残差方向大幅偏转，置信度下降。
- **自信解码策略**：在每个token解码时，从前向传播得到的候选层集合（最后M层）中，反向扫描寻找预测熵首次停止下降的局部最小值层（熵谷），将其logits送入采样器；整体计算仅增加少量未嵌入投影和熵计算，完整保留KV缓存和模型前向。
- **理论保证**：将层选择形式化为最优停止问题，证明保守反向扫描能在有界投影噪声下过滤对齐扰动，保证所选层在精炼窗口内，且损失小于可忽略边界。
- **系统实现**：在vLLM推理引擎内实现，保证图编译兼容、连续批处理下的正确性，额外延迟<2%，无内存开销。

**关键结果**：
- 在GPQA-Diamond、HLE、Omni-MATH、LiveCodeBench等6个高难度基准上，对Qwen3.5、gpt-oss、Gemma-4等多架构模型，自信解码相比贪婪解码取得一致提升，例如Qwen3.5-35B-A3B在GPQA-D上+6.5%，在LCB-v6上+4.3%；大规模MoE模型gpt-oss-120B在GPQA-D上+4.5%。
- 在安全性基准Air-Bench和创意写作WritingBench上性能持平或小幅提升，证明未破坏安全对齐。
- 对比基模与指令微调模型，指令模型增益明显更大（+2.8% vs +1.7%），证实了对齐税的存在。
- 按任务难度分层，困难题目增益显著（如Omni-MATH Level 4从1.1%提升至23.5%），而简单任务几乎不变，体现了方法的自适应特性。
- 额外计算开销极低：实际平均仅增加0.116次额外未嵌入投影，总FLOPs增加<1%，端到端延迟增加<2%，KV缓存零增长。

**最值得记住的一句话**：语言模型的最终层对齐扰动会损害复杂推理链，通过动态回溯到预测熵最低的中间层解码，可以在不训练、不增加显存的前提下显著恢复被隐藏的推理能力，且安全护栏不受影响。
