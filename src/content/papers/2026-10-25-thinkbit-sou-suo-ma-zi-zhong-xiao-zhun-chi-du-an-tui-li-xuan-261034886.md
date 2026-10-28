---
title: 'ThinkBit: Search Codewords, Recalibrate Scales, Select by Reasoning'
title_zh: ThinkBit：搜索码字、重校准尺度、按推理选择
authors:
- Rhea Sanjay Sukthanker
- Pashmina Cameron
affiliations:
- Microsoft Applied Sciences Group
arxiv_id: '2610.34886'
url: https://arxiv.org/abs/2610.34886
pdf_url: https://arxiv.org/pdf/2610.34886
published: '2026-10-25'
collected: '2026-10-28'
category: Training
direction: LLM量化 · 标量2-bit推理保持
tags:
- Quantization
- LLM
- Reasoning
- QAT
- Scalar 2-bit
- MATH-500
one_liner: 标量2-bit量化框架，通过敏感度分配位宽、码字搜索、仅训尺度和按推理选择，在MATH-500上大幅超过同尺寸2-bit方法
practical_value: '- **线上长思维链模型压缩**：如果要在电商/Agent场景部署推理模型，可用标量2-bit格式（整数codeword × bf16
  scale，组大小128），无codebook/rotation/zero-point，dequant只需一次乘法，工程实现简单，能显著降低权重内存带宽；论文中14B模型decode从86提高到150
  tokens/s。

  - **按层敏感度混合精度**：不必全模型统一2-bit，先用KronQ敏感度（输入范数×输出梯度范数）给每层分配ternary/2-bit/3-bit，可将搜索/推荐/Agent模型的量化损失最小化；论文表明2-bit点在成本-噪声平面上不占优，多数层会分配到ternary或3-bit。

  - **低成本恢复与校准**：冻结codeword，只训练scales和RMSNorm gains（<1%参数）就能把WikiText ppl从46.9降到19.46、MATH-500从14.8拉到47.5；这适合对线上新领域数据做快速低资源校准，无需全量QAT。

  - **用业务长链路指标选checkpoint**：困惑度和多选题无法区分量化配置（差异<1.5点），但长程任务如MATH-500差异超10点；应构造业务推理样本（如商品推荐解释、Agent工具调用轨迹最终成功率）做配对sign-flip
  test来选择checkpoint，避免误选。

  - **QAT数据要加完整推理轨迹**：仅通用数据QAT会损害推理（MATH-500从47.5降到43.0），加入完整长思维链数据后同尺寸模型MATH-500从46.7跃升至73.0；业务上收集高质量Agent轨迹数据做量化后训练是划算的。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：reasoning LLM生成数千tokens，推理速度受内存带宽限制，2-bit权重可将权重内存流量降低至1/8。但常用困惑度和多选题无法反映模型是否仍能推理，甚至会误导配置选择；需要专门针对推理能力设计和评估2-bit量化方法。

**方法关键点**：
- **权重格式**：严格标量格式，每个权重是整数codeword乘以组共享的bf16 scale（组大小128），无向量codebook、旋转或zero-point，dequant仅一次乘法。
- **阶段1 Allocate**：用KronQ二阶敏感度（输入范数×输出梯度范数）求解多选择背包，为每层分配ternary/2-bit/3-bit；发现2-bit点在成本-噪声平面上不占优，常通过query/key规则保留。
- **阶段2 Search**：以GPTQ为层级起点，3-bit/ternary用Gumbel-softmax、2-bit用ReinMax，按transformer block输出目标联合搜索码字，补偿块内误差。
- **阶段3 Recalibrate**：冻结codeword，只训练scales和RMSNorm gains（<1%参数），用KL蒸馏匹配bf16模型分布；该阶段恢复大部分质量。
- **阶段4 QAT**：FP32 latent从偏向bf16权重一侧开始，用STE重分配少量codeword；1.7B仅重分配6.4%。
- **阶段5 Selection**：在313道MATH训练题上做配对sign-flip test，比较Rec和QAT checkpoint，按推理准确率而非似然选择。

**关键实验结果**：
- Qwen3-1.7B：Rec-hbf16在MATH-500 sampled上47.5，QAT后降到43.0；但加入完整推理轨迹数据QAT后，0.52GB的QAT+R-h2达到73.0，而相同数据训练的EfficientQAT仅30.0。
- 规模化：Qwen3-14B在3.74GB下MATH-500达94.8（bf16 97.5），AIME@16达57.7（bf16 73.6）；所有size上均比已发布2-bit GGUF更小且更准，如1.7B的Q2_K仅41.9。
- 消融：去掉codeword search、scale recalibration或bit allocation，7-task均值几乎不变（53.7-54.8），但sampled MATH-500从43.0掉到28.4-37.0，证明标准benchmark无法捕捉推理损失。

**最值得记住的一句话**：2-bit量化必须用长程推理任务评估与选择，冻结码字仅训练scale可用不到1%参数恢复大部分推理损失，而QAT需要完整推理轨迹才能真正提升推理性能。
