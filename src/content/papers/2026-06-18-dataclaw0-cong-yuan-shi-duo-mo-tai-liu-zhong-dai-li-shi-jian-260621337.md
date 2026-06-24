---
title: 'DataClaw0: Agentic Tailoring Multimodal Data from Raw Streams'
title_zh: DataClaw0：从原始多模态流中代理式剪裁数据的可学习精炼模型
authors:
- Cong Wan
- Zeyu Guo
- Zijian Cai
- Jiangyang Li
- SongLin Dong
- Lin Peng
- Xiangyang Luo
- Zhiheng Ma
- Yihong Gong
affiliations:
- Xi'an Jiaotong University
- University of Chinese Academy of Sciences
- Shenzhen University of Advanced Technology
- Tsinghua University
arxiv_id: '2606.21337'
url: https://arxiv.org/abs/2606.21337
pdf_url: https://arxiv.org/pdf/2606.21337
published: '2026-06-18'
collected: '2026-06-24'
category: Agent
direction: 代理式多模态数据精炼与合成
tags:
- Agentic Data Tailoring
- Multimodal Refinement
- GRPO
- Data Synthesis
- Factual Anchors
- Post-training
one_liner: 将数据处理从被动标注提升为可学习的代理式剪裁，用SFT+GRPO训练9B模型，生成高信息密度多模态数据以高效驱动下游任务。
practical_value: '- **电商多模态数据清洗与增强**：借鉴Factual Anchors思想，对商品视频、直播切片、详情页截图等原始流，先抽取确定性事实（如商品属性、价格、功能演示片段）作为锚点，再围绕锚点生成问答、描述、指令数据，可大幅提升推荐模型训练数据的信噪比与信息密度。

  - **Agent行为轨迹的结构化**：在广告投放决策、智能客服等场景中，Agent的操作日志冗余且混杂。可训练小型精炼模型（类似DataClaw0），自动识别关键决策点、去重、补全因果链，将原始轨迹转化为高质量的推理训练样本，用于RLHF或post-training。

  - **低成本迭代式数据精炼**：两阶段合成流水线（事实锚提取+生成式语义合成）可离线运行，不依赖昂贵人工标注；工程上可将精炼模型作为数据pipeline的微型agent，对新入库的UGC内容持续精炼，构建动态更新的高质量数据池。

  - **数据质量评估范式的迁移**：直接用下游任务（如推荐召回、CTR预估）的post-training效果来反向验证数据精炼质量，将离线质量评估与在线业务指标对齐，避免仅靠人工抽查导致的数据偏差。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：原始多模态数据流（长视频、GUI操作日志、具身轨迹等）存在极高“数据熵”，传统启发式规则或通用VLM标注成本高、信息提取浅层，无法挖掘数据中的深层过程逻辑，限制了AI后训练的数据供给。

**方法关键点**：提出**Agentic Data Tailoring**范式，将数据处理从被动标注转变为主动、可学习的剪裁与结构化能力。为训练该能力，设计**两阶段合成管道**：首先从原始流中抽取确定性事实锚点（Factual Anchors），再以这些锚点为骨架，通过生成式语义合成构建大规模、跨域（物理与数字五领域）的精细化数据。基于此，训练**DataClaw0-9B模型**，采用SFT结合Group Relative Policy Optimization（GRPO），使模型对齐复杂的精炼与剪裁意图。构建首个数据精炼专用基准**DataClaw0-val**。

**关键结果**：以《下游后训练效果》作为最终验证标准。在视频生成、真实场景VQA、GUI导航等任务上，DataClaw0生成的高信息密度剪裁数据，使下游模型在有限训练数据下快速适应新任务，性能显著优于常规数据配比方式。
