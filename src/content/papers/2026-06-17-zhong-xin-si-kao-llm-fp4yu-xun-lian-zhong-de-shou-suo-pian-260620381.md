---
title: 'Rethinking Shrinkage Bias in LLM FP4 Pretraining: Geometric Origin, Systemic
  Impact, and UFP4 Recipe'
title_zh: 重新思考LLM FP4预训练中的收缩偏置：几何根源与UFP4方案
authors:
- Qian Zhao
- Kunlong Chen
- Changxin Tian
- Zhonghui Jiang
- Haitao Zhang
- Chaofan Yu
- Peijie Jiang
- Mingliang Gong
- Jia Liu
- Ziqi Liu
affiliations:
- Ant Group
arxiv_id: '2606.20381'
url: https://arxiv.org/abs/2606.20381
pdf_url: https://arxiv.org/pdf/2606.20381
published: '2026-06-17'
collected: '2026-06-20'
category: Training
direction: 低精度训练 · FP4均匀网格
tags:
- FP4
- Quantization
- Shrinkage Bias
- Uniform Grid
- Random Hadamard Transform
- LLM Pretraining
one_liner: 指出非均匀E2M1格式固有的收缩偏置被RHT放大导致训练不稳定，提出基于均匀E1M2网格与全RHT相结合的UFP4训练配方
practical_value: '- 当对推荐模型做低比特量化或采用类似RHT的旋转预处理时，优先选用均匀网格（INT4/E1M2），因为非均匀格式（E2M1）的舍入偏置会在深层网络积累，而均匀网格不存在该问题。

  - 若使用FP4训练LLM-based推荐模型，可借鉴UFP4的配方：将RHT扩展到前向、数据梯度、权重梯度三个GEMM，仅对dY使用随机舍入；该设计在1.5B~124B的实验中稳定降低了与BF16的loss差距。

  - 收缩偏置是一个容易被忽视的几何缺陷：当量化区块不对称时，即使是零均值的分布也会产生系统性负误差，造成信号衰减；在自研或选用量化方案时，应检查舍入bin的对称性，而非只关注动态范围。

  - 在只有E2M1硬件的场景下，试图通过限制最大可表示值来模拟均匀网格效果不佳，未来若能为推荐训练引入FP4加速，应争取支持均匀4-bit格式作为第一等训练原语。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
FP4训练有望大幅降低LLM预训练的内存与算力开销，但现有的E2M1配方（如NVFP4）在结合随机Hadamard变换（RHT）后仍出现训练不稳定和相对于BF16的明显损失上升。论文从量化网格几何角度揭示了一个根本原因：E2M1的非均匀代表值导致RTNE舍入产生系统性的负误差——收缩偏置（Shrinkage Bias），该偏置在深层网络中逐层衰减信号，且被RHT加剧，因为RHT将张量主要质量推入最不对称的舍入区间。相反，均匀网格（E1M2/INT4）舍入bin对称，天然消除这一偏置。  

**方法关键点**  
- **收缩偏置的几何形式**：对非均匀量化等级，RTNE舍入区间左右不对称时，在局部均匀密度假设下，期望舍入误差为负值，导致张量幅值系统性缩小。  
- **RHT对格式偏好的翻转**：RHT将异常值能量分散，使张量从动态范围受限转为局部分辨率受限，此时均匀网格能更好利用桶利用率，而非均匀E2M1因分辨率不足而SQNR下降。  
- **UFP4配方**：基于E1M2均匀网格，将RHT应用到全部三个训练GEMM（前向FPROP、数据梯度DGRAD、权重梯度WGRAD），并仅对dY使用随机舍入（SR）以保留梯度期望，其余RTNE。  
- **与E2M1方案对比**：保持block size、scale层次等一致，仅切换网格类型与RHT范围，直接比较收缩偏置的影响。  

**关键实验与结果**  
- 在Dense 1.5B、MoE 7.9B和MoE 124B长流程预训练中，UFP4将BF16相对loss误差从E2M1的1.26%→0.97%、2.36%→1.85%、1.73%→1.39%。  
- 消融实验表明：全RHT覆盖相比无RHT降低loss 0.011，dY-only SR再降低0.005；限制E2M1最大幅值来模拟均匀网格反而使loss恶化。  
- 缩放律分析显示E1M2的优势在不同模型规模下保持，且FP4与BF16的差距不随计算量扩大。  
- 融合RHT与量化仅带来6-7%额外延迟，工程开销可控。  

**一句话记住**  
"4-bit训练应当将均匀网格作为一等格式——非均匀格式的几何偏置是深层不稳定之源，RHT放大了这一缺陷。"
