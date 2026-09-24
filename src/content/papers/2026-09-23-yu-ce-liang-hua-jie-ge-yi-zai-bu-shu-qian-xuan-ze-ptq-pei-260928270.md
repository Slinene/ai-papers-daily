---
title: Predicting Quantization Price for Selecting PTQ Configurations Before Deployment
title_zh: 预测量化价格以在部署前选择 PTQ 配置
authors:
- Junbin Qiu
- Jian Mu
- Weitong Zhang
- Yao Shu
affiliations:
- HKUST-GZ
arxiv_id: '2609.28270'
url: https://arxiv.org/abs/2609.28270
pdf_url: https://arxiv.org/pdf/2609.28270
published: '2026-09-23'
collected: '2026-09-24'
category: Other
direction: LLM 权重 PTQ 配置选择与价格预测
tags:
- PTQ
- Quantization Price
- Configuration Selection
- Forward KL
- LLM Compression
- Mixed-Precision
one_liner: 用 forward KL 诱导的二次价格统一比较位宽、粒度、变换等 PTQ 配置，实现预算约束下的部署前选择
practical_value: '- 部署 LLM 推荐/Agent 模型时，可用校准时价格表快速筛选量化配置（位宽、粒度、预量化变换），避免反复构建完整量化模型，节省大量实验时间。

  - 把量化配置视为统一候选，用输出侧曲率加权误差协方差（而非仅重建误差或输入对角线统计）排序，能更贴近下游任务效果，适合对线上精度敏感的生成式推荐/Agent
  场景。

  - 在成本受限的部署（如端侧推理）中，引入部署成本约束做 budgeted search，显式权衡精度与资源，对工程实现有直接参考价值。

  - 实现上只需 Hutchinson 估计曲率迹和扰动矩，不需要完整 Hessian，可作为轻量校准步骤嵌入现有 PTQ 流程。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

## 动机

权重 PTQ 必须在部署前决定每层的格式、粒度、量化器族、变换和位宽，但完整模型的输出分布漂移只有在所有选择组合完成后才可见。现有方法通常在固定几何后做重建误差或 Hessian 敏感度评分，或者只在单一配置家族内部比较，缺乏跨位宽、粒度、码本、变换和硬件成本的统一预部署分数。

## 方法关键点

- 将权重 PTQ 建模为预算约束下的配置选择问题，候选层配置 αₗ 诱导层输出误差协方差 Σₗ(αₗ) 并携带部署成本 κₗ(αₗ)。
- 从 full-precision→quantized 的 forward KL 出发做 Taylor 展开，线性项在参考模型处消失，保留二次量化价格：ρₗ(αₗ) = ½ Tr(Hₗ Σₗ(αₗ))，其中 Hₗ 是全精度参考模型的下游曲率，Σₗ 由候选扰动和输入协方差构成。
- 重建误差和输入对角分数只是该价格的缩减代理：重建误差令 H→I，对角分数进一步丢掉跨通道输入协方差，仅在对应因子近似不变时才保序。
- 对候选族统一：有限格式/码本改变扰动矩，等价变换改变扰动生成坐标和输入度量但保持输出侧价格固定；在近似各向同性下可简化为 trace 价格 ½ σ² ω Tr(H)，形成校准时间价格表。
- 预算搜索 α* = arg min Σ ρ̂ₗ(αₗ) s.t. Σ κₗ(αₗ)≤B，固定几何位宽分配退化为特例。

## 关键实验

- 在 OPT-125M 和 Qwen3-0.6B 上，控制扰动下实现价格(8)与 KL drift 的对数相关性分别为 0.9470 和 0.9249；简化 trace 价格(18)也达 0.9483 和 0.9438，验证预测链有效。
- 在 Llama-3.2-1B 上测试三类配置选择：位宽分配（[2,3,4] 平均 3bit），相比 HIGGS 时间从 813s 降到 579s，PPL 12.22 vs 12.50，平均下游任务分 51.24 vs 50.57；相比 AMQ 虽 PPL 略高（12.22 vs 11.05）但选择时间从 11635s 大幅降至 579s，平均任务分更高（51.24 vs 50.13）。
- 变换选择：PPL 11.53 vs CALM-CKA 12.80，随机 22.68；粒度选择：PPL 11.39 vs 固定 group-128 12.71，随机 23313。

## 最值得记住的一句话

PTQ 不是固定几何下的位宽分配，而是用 forward KL 诱导的二次价格（误差协方差 × 下游曲率）统一比较所有可部署配置，在部署前完成预算约束选择。
