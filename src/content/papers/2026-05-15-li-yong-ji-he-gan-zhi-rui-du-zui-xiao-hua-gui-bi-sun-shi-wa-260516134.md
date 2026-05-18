---
title: Navigating Potholes with Geometry-Aware Sharpness Minimization
title_zh: 利用几何感知锐度最小化规避损失坑洼
authors:
- Simon Dufort-Labbé
- Mehrab Hamidi
- Razvan Pascanu
- Ioannis Mitliagkas
- Damien Scieur
- Aristide Baratin
affiliations:
- Mila, Université de Montréal
- Samsung – SAIL Montreal
arxiv_id: '2605.16134'
url: https://arxiv.org/abs/2605.16134
pdf_url: https://arxiv.org/pdf/2605.16134
published: '2026-05-15'
collected: '2026-05-18'
category: Training
direction: 优化训练 · 二阶预条件与 SAM 协同
tags:
- Sharpness-Aware Minimization
- Preconditioner
- Second-Order Optimization
- Loss Geometry
- Flat Minima
- LLQR
one_liner: LLQR+SAM 用慢更新的二阶预条件器增强 SAM 扰动，放大局部锐利方向的逃逸信号
practical_value: '- **推荐模型泛化提升**：用慢更新预条件器捕获损失景观的低频几何，结合快速 SAM 扰动可有效跳出局部尖锐极值点，适合 CTR/CVR
  模型在大规模稀疏数据上避免过拟合。

  - **大模型微调中的曲率修正**：LLQR 的逐层线性二次型调节器预条件器可在 LoRA 等适配器微调中，以稀疏 EMA 方式注入，在不显著增加开销下改善平坦性，提升
  OOD 泛化。

  - **多任务学习与 Agent 策略优化**：在 RL 或 Multi-Agent 训练中，不同任务梯度方向冲突常形成损失坑洼，采用二时标结构（慢几何学习 +
  快曲率探测）可稳定训练，避免单个任务主导的尖锐解。

  - **工程实现 trick**：预条件器每数千步更新一次并维持 EMA，计算开销极小，适用于需长期训练的电商搜索、序列推荐模型，可与现有 SAM 变体（如 FSAM）直接插拔。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：SAM 沿高曲率方向扰动参数以寻找平坦极小值，但对所有参数方向一视同仁，忽略了损失景观的非均匀几何。尤其在大型推荐或生成模型中，某些方向整体平坦而局部尖锐（坑洼），统一扰动会削弱逃逸能力或浪费算力。

**方法关键点**：提出 LLQR+SAM，将 SAM 与从 LLQR 框架得到的可学习预条件器结合。LLQR 将最速下降重铸为逐层线性二次型调节器问题，产出逐层对角预条件矩阵，以稀疏更新（每几百步）和慢指数滑动平均维持，捕捉损失景观的低频、平滑几何。SAM 扰动在此基础上执行，快速探测曲率细节。二者形成二时间尺度：慢几何学习放大 “坑洼” 方向的 SAM 逃逸信号，而宽平坦区域保持稳定，理论证明二者互补。

**关键结果数字**：在 ImageNet (ResNet-50)、CIFAR-100、WikiText-2 (LSTM/Transformer) 等基准上，LLQR+SAM 相比单独 SAM 或 LLQR 均取得一致的误差/困惑度降低（例如 ImageNet Top-1 误差降低 1-2 个百分点），且训练时间开销与 SAM 相当，不成为瓶颈。
