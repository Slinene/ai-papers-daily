---
title: 'SpectrumQuant: Spectrum Alignment for LLM Quantization'
title_zh: SpectrumQuant：面向LLM量化的谱对齐旋转方法
authors:
- Dwaipayan Haldar
- Indranil Patra
- Azhar Yousuf
- Chandra Sekhar Seelamantula
affiliations:
- Indian Institute of Science
arxiv_id: '2610.20303'
url: https://arxiv.org/abs/2610.20303
pdf_url: https://arxiv.org/pdf/2610.20303
published: '2026-10-14'
collected: '2026-10-15'
category: LLM
direction: LLM 量化 · 正交旋转
tags:
- LLM Quantization
- Orthogonal Transform
- Spectrum Alignment
- Post-Training Quantization
- Hadamard
- Butterfly
one_liner: 通过协方差最大化推导出闭式数据感知正交变换，大幅降低LLM量化校准成本
practical_value: '- **数据感知旋转替代固定 Hadamard**：在电商/搜索推荐场景部署 LLM 时，若采用旋转量化（如 QuaRot、SpinQuant），可直接用激活协方差特征向量作为对齐组件
  U，再与 Hadamard/Butterfly 混合，无需迭代优化即可获得与学得旋转相当的精度，适合快速适配领域数据（如电商 query、商品描述）。

  - **闭式解大幅降低校准成本**：SpectrumQuant 仅需估计激活协方差并做特征分解，70B 模型校准仅 43 分钟（单 A6000 GPU），内存占用
  22 GiB，相比 SpinQuant 加速 21 倍、省 9.8 倍内存，且支持 CPU 校准，适合资源受限的线上服务或边缘部署。

  - **旋转可完全吸收进权重，零推理开销**：正交旋转矩阵可合并到相邻权重中，实测 MacBook 上推理吞吐与无旋转基线一致，不影响在线延迟，适合对实时性要求高的搜索推荐/Agent
  系统。

  - **Butterfly 矩阵作为高效混合组件**：理论证明满足 |v_{ki}|=1/√d 的正交矩阵（Hadamard、特定角度 Butterfly）均为最优混合组件，Butterfly
  乘法 O(d log d) 可进一步降低在线计算，替换 R3/R4 中的 Hadamard 不影响精度。'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

**动机**  
LLM 激活异常值严重阻碍低比特量化，旋转方法通过正交变换分散异常值幅度，但现有方案存在权衡：固定 Hadamard 数据无关，学得旋转（如 SpinQuant、DartQuant）成本高昂且缺乏理论保证。需要一种数据感知且闭式的旋转设计。

**方法关键点**  
- 从协方差最大化目标出发，等价于最小化变换后协方差对角线平方和，证明最优旋转需使各维方差相等（等于平均特征值）。  
- 解的形式为 Q = U V：U 是激活协方差的特征向量（对齐组件，KL 变换），V 是满足 |v_{ki}|=1/√d 的正交矩阵（混合组件），如 Hadamard 矩阵或角度在 {π/4, 3π/4, 5π/4, 7π/4} 的 Butterfly 矩阵。  
- 该闭式解统一了数据无关旋转与数据感知对齐，理论上证明了在共享尺度量化下，该旋转最小化总量化误差。  
- 实际校准：用 Welford 算法在线估计激活协方差（128 个 WikiText2 样本），得到 Q=UH 或 Q=UB。旋转 R1、R2 用 SpectrumQuant，R3、R4 保持随机 Hadamard/Butterfly。

**关键实验**  
- 在 Llama-2 7B/13B/70B、Llama-3 8B、Mistral 7B v0.3 上做 W4A4KV4 量化，与 QuaRot、SpinQuant、DartQuant 对比。  
- 精度：SpectrumQuant 与 DartQuant 统计相当（如 Llama-2 7B 平均 PPL 21.5 vs 20.5，0-shot 60.1 vs 61.0），优于 QuaRot 和 SpinQuant。  
- 校准成本：70B 模型单 A6000 GPU 校准 43 分钟，内存 22.4 GiB，相比 SpinQuant 加速 21 倍、内存节省 9.8 倍；DartQuant 内存 128 GiB。  
- 推理开销：MacBook Air M4 实测解码吞吐与无旋转基线一致，旋转吸收进权重后零额外开销。  
- 消融：对校准数据集（WikiText2/PTB/C4）和样本数（64~256）不敏感；替换 R3/R4 为随机 Butterfly 无显著差异。

**最值得记住的一句话**  
闭式协方差对齐旋转（Q=UV）以小于 1/10 的校准内存和 1/21 的时间，取得与学得旋转相当的量化精度，为 LLM 部署提供了轻量且理论坚实的旋转选择。
