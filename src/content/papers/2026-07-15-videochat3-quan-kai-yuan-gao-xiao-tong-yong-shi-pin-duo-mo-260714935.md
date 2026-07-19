---
title: 'VideoChat3: Fully Open Video MLLM for Efficient and Generalist Video Understanding'
title_zh: VideoChat3：全开源高效通用视频多模态大模型
authors:
- Xinhao Li
- Yuhan Zhu
- Xiangyu Zeng
- Yuhao Dong
- Haoning Wu
- Zhiqiu Zhang
- Yuandong Yang
- Changlian Ma
- Qingyu Zhang
- Yansong Shi
affiliations:
- Nanjing University
- Shanghai AI Laboratory
- Nanyang Technological University
- Peking University
arxiv_id: '2607.14935'
url: https://arxiv.org/abs/2607.14935
pdf_url: https://arxiv.org/pdf/2607.14935
published: '2026-07-15'
collected: '2026-07-19'
category: Multimodal
direction: 高效通用视频多模态大模型
tags:
- Video MLLM
- Efficiency
- Data Synthesis
- I3D-ViT
- Streaming
- Open Source
one_liner: 提出膨胀3D ViT与自适应帧分辨率，结合三阶段合成数据，4B参数即超越更大模型，实现高效通用视频理解。
practical_value: '- **视频特征提取效率**：I3D-ViT 将 2D ViT 权重直接膨胀到 3D，无需重新训练时空融合模块，可直接迁移到商品视频表征、直播切片理解等场景，大幅降低训练成本。

  - **流式处理设计**：自适应帧分辨率（Adaptive Frame Resolution）根据视频动态调整抽帧策略，适合电商直播实时分析、监控流式视频中的行为事件，提升吞吐且保持精度。

  - **多领域数据合成流水线**：通过结构化提示合成多样视频问答对（通用、长视频、流式），可借鉴为推荐系统生成多模态训练数据，例如为商品视频生成属性描述、使用教程等指令微调数据，缓解标注稀缺。

  - **全开放生态**：模型权重、代码、数据全开源的策略，方便团队快速复现并适配垂直业务，降低自研视频理解模型的门槛，尤其适合需要定制化视觉问答或视频审核的电商场景。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有视频多模态大模型在领域泛化性、计算效率与开源性上均存在短板，阻碍社区迭代与真实应用落地。

**方法关键点**：
- **效率设计**：提出 **I3D-ViT**，用简单的权重膨胀将预训练 2D ViT 迁移到时空建模，避免昂贵的 3D 预训练；配合 **自适应帧分辨率** 策略，根据视频内容动态分配分辨率与抽帧密度，显著降低计算量。
- **数据引擎**：构建可扩展的合成数据流水线，产出三套高质量指令数据：**VideoChat3-Academic2M**（通用视频问答）、**VideoChat3-LV116K**（长视频理解）、**VideoChat3-OL617K**（流式交互），覆盖不同场景需求。
- **模型与训练**：基于 Qwen2-4B 语言骨干，整合 I3D-ViT 编码器并通过多阶段训练（对齐、预训练、指令微调）注入庞大多样视频知识。

**关键结果**：VideoChat3-4B 在通用（MVBench、Video-MME）、长视频（LongVideoBench、MLVU）及流式（StreamingBench、Ego4D）基准上，全面超越同等或更大参数的开源模型（如 VideoLLaMA2、MiniCPM-V 2.6），且训练/推理效率更高，证明全开源路线的竞争力。
