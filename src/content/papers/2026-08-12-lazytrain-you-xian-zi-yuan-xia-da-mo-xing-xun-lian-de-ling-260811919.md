---
title: 'LazyTrain: Limited-resource Allocation toward Zero-waste Yield Optimization
  in Large Language Model Training'
title_zh: LazyTrain：有限资源下大模型训练的零浪费产出优化
authors:
- Xiaojun Wu
- Cehao Yang
- Honghao Liu
- Xueyuan Lin
- Xuhui Jiang
- Chengjin Xu
- Jia Li
- Jian Guo
affiliations:
- IDEA Research
- The Hong Kong University of Science and Technology (Guangzhou)
- DataArcTech Ltd.
arxiv_id: '2608.11919'
url: https://arxiv.org/abs/2608.11919
pdf_url: https://arxiv.org/pdf/2608.11919
published: '2026-08-12'
collected: '2026-08-13'
category: Training
direction: LLM 训练资源调度优化
tags:
- LLM Training
- Offloading
- Scheduling
- Memory Optimization
- 8-bit Optimizer
- Layer Streaming
one_liner: 将checkpoint选择、激活放置、重计算与CPU-GPU-NVMe通信重叠建模为混合整数调度，并耦合混合8-bit算子提升单卡训练效率
practical_value: '- 层流式执行器上将 checkpoint 选择、激活 offload、重计算与 PCIe/NVMe 传输显式建模为混合整数调度问题，避免通信暴露在关键路径；自研微调平台或单卡多卡调度时可把“何时
  offload/重计算”做成可求解策略而非硬编码规则。

  - 8-bit 优化器状态与快速梯度裁剪耦合为混合算子，压缩优化器状态省显存，同时用快速裁剪掩盖 CPU 端更新延迟；适合 LoRA/QLoRA 或全参微调中优化器状态占显存大、需单卡大
  batch 的场景。

  - 消费级 GPU（RTX 3090）上最大可行 batch size 各模型规模可增加 1，能直接服务推荐/CTR/CVR 模型 LLM backbone 的对比学习、多任务微调，降低单卡试错成本。

  - 离线求解调度策略、训练时执行的思想可迁移到推荐系统训练中，把 embedding offload、参数服务器通信、数据搬运也显式建模为调度问题，提升 GPU
  利用率。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

动机：单卡或有限硬件上训练大型 LLM 时，GPU 显存、主机内存、PCIe 和存储带宽的调度成为核心瓶颈；已有 offloading 系统如 MegaTrain 虽支持层流式执行，但固定 checkpoint 和放置启发式使通信暴露在关键路径。

方法关键点：LazyTrain 在层流式执行器之上添加优化层，将 checkpoint 选择、激活放置、重计算和 CPU-GPU-NVMe 通信重叠形式化为混合整数调度问题，并执行求解后的策略。进一步把 8-bit 优化器状态压缩与快速梯度裁剪耦合成 Hybrid 8-bit 算子，既降低优化器状态内存，又抵消 CPU 端更新带来的额外开销。

关键结果：H800 上从 Qwen2.5-3B 到 Qwen3.6-27B，LazyTrain 持续 TFLOPS 相比匹配基线提升约 1.24×；RTX 3090 上各模型规模最大可行 batch size 增加 1。Qwen3.6-27B MetaMathQA 训练达到 219.95 TFLOPS、1361 tokens/s（batch size 72），GPU 峰值内存 68.84GB，全评估集 exact-match 准确率 95.42%。
