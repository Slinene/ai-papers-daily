---
title: BitNet Text Embeddings
title_zh: BitNet文本嵌入：极端低比特LLM语义表示
authors:
- Zhen Li
- Xin Huang
- Liang Wang
- Nan Yang
- Ting Song
- Yan Xia
- Xun Wu
- Shaohan Huang
- Huishuai Zhang
- Furu Wei
affiliations:
- Peking University
- Microsoft Research
arxiv_id: '2606.25674'
url: https://arxiv.org/abs/2606.25674
pdf_url: https://arxiv.org/pdf/2606.25674
published: '2026-06-24'
collected: '2026-06-25'
category: Training
direction: 极端低比特嵌入模型的量化训练与多精度存储
tags:
- Text Embedding
- BitNet
- Quantization
- Distillation
- Multi-precision
- LLM
one_liner: 将LLM转换为1.58位BitNet嵌入器，配合对比预训练与蒸馏，实现接近全精度性能并支持多精度存储
practical_value: '- 线上推理加速：将LLM嵌入骨干量化为1.58位三值权重与8位激活，CPU吞吐量提升约2倍，适合电商搜索/推荐场景的实时查询编码。

  - 多精度向量索引：单个模型可输出1/2/4/8/16位嵌入，按存储预算灵活选择精度而不需重新训练，大幅降低向量数据库成本。

  - 蒸馏策略可复用：相似度分布蒸馏（KL散度对齐批内候选分布）与注意力关系蒸馏（单层多头自注意力关系对齐）能有效补偿量化损失，可迁移至其他模型压缩任务。

  - 工程稳定技巧：在每层Transformer内插入子层归一化 (SubLN)，缓解量化带来的激活尺度漂移，使极端低比特训练更稳定。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
LLM文本嵌入质量优异，但大骨干导致推理耗时，高维全精度向量存储成本巨大。BitNet风格模型（1.58位三值权重+8位激活）能显著降低推理开销，但尚未被引入文本嵌入领域。本文首次系统探索将预训练LLM转化为极端低比特嵌入器，同时缓解量化带来的语义表征丢失。

**方法关键点**  
- **骨干量化**：将LLM线性层权重量化为{−Δ, 0, Δ}的三值，激活做逐token 8位量化，同时在每个Transformer块内插入子层归一化 (SubLN) 稳定训练。  
- **持续对比预训练**：在10亿级文本对上用InfoNCE损失重建量化模型的语义空间，弥补极端量化造成的表征扭曲。  
- **蒸馏微调**：用全精度教师模型指导监督微调，结合两个蒸馏损失：①相似度分布蒸馏——对齐师生对候选集的余弦相似度分布（KL散度）；②注意力关系蒸馏——对齐单层多头自注意力的token间关系分布。  
- **多精度输出嵌入**：训练时对每个嵌入维度模拟1/2/4/8/16比特量化，优化平均损失，使单一模型支持不同存储精度。

**关键实验**  
在MMTEB (eng, v2)上评测，骨干为Qwen3-0.6B和Gemma3-270M。BITEMBED取得67.60（教师67.95）和66.10（教师66.71）的平均分，CPU吞吐量分别从364→831 tokens/s、1181→2055 tokens/s，提升约2倍。输出嵌入4/8位几乎无损，1位仍保留可用性能。消融显示去除SubLN、蒸馏或持续预训练均导致明显下降。
