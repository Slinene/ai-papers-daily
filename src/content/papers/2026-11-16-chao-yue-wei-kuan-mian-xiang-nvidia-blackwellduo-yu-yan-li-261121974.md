---
title: 'Beyond Bitwidth: Deployment-Constrained Mixed-Precision Quantization for Multilingual
  LLM Inference on NVIDIA Blackwell'
title_zh: 超越位宽：面向NVIDIA Blackwell多语言LLM推理的部署约束混合精度量化
authors:
- Hyojung Han
affiliations:
- ThakiCloud
arxiv_id: '2611.21974'
url: https://arxiv.org/abs/2611.21974
pdf_url: https://arxiv.org/pdf/2611.21974
published: '2026-11-16'
collected: '2026-11-18'
category: LLM
direction: LLM 推理混合精度量化部署
tags:
- mixed-precision quantization
- NVFP4
- INT8
- vLLM
- Qwen3-8B
- LLM serving
one_liner: 在NVIDIA B200上系统验证Qwen3-8B量化，给出通过多语言门控的5.917 GiB混合精度配置
practical_value: '- 部署生成式推荐/Agent LLM时，除了精度指标，应设置服务相关门控（内存、TPOT、多语言准确率），并用未接触的 FINAL
  集做独立验证，避免选择集过拟合；实验显示开发集 +3.4pp 到独立集只剩 +1.4pp。

  - 混合精度保护模块的选择不能只看单模块恢复效果——模块间效应强非加性，且韩语与推理敏感度排序不一致；若业务需同时保证多语言和推理，建议分别评测并全局迭代分配。

  - 在 vLLM + Blackwell 环境，可优先验证 NVFP4 W4A4 与 INT8 混合的 kernel 可行性；该工作表明 16-bit 激活相对
  W4A4 的增益可能比 INT8 保护更大，工程上可先改激活精度。

  - 若业务模型需覆盖韩语等非英语场景，不要只优化英语或通用指标；文中韩语 teacher-correct retention 是独立门控，类似地可为各关键语言设置最低通过线。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

动机：低比特量化虽能降内存与成本，但部署可行性还受 GPU kernel 支持、实际内存/延迟限制和多语言精度保持约束；单纯追求位宽降低可能在真实服务中失效。

方法：以 Qwen3-8B 在 NVIDIA B200 + vLLM 为平台，测试 INT2/INT3、GPTQ、NVFP4 及多种混合精度配置；验证全部 144 个 fused linear 模块的 packed 执行与精度；预设服务门控（权重内存 5.98 GiB、韩语 teacher-correct retention ≥0.90、TPOT 比率）并在未接触的 FINAL-81 集（5,168 items）上评估韩语、英语、数值与推理能力。

结果：packed INT2/INT3 可执行，但 7 种 INT2 grid 生成全部退化；孤立模块恢复效应强非加性，韩语与推理敏感度排序不一致；开发集表现好的 INT4/INT8 候选未通过独立评估。最终通过门控的配置为 16-bit 激活 + 98 个 NVFP4 weight-only 模块 + 46 个 INT8 模块 + INT8 输出头：权重内存 5.917 GiB，韩语保留 0.904，TPOT 比 0.939（相对 BF16）；相比 NVFP4 W4A4 提升 +1.4pp（Bonferroni-adjusted 区间 [+0.2, +2.6]），开发集提升为 +3.4pp。探索性分析提示激活精度变化贡献更大，但隔离分配效应未确立；最终 checkpoint 未保留，bitwise 重建可复现性未验证。
