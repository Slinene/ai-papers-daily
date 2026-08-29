---
title: 'Video-IFBench: Evaluating Instruction Following of Multimodal LLMs in Video
  Understanding Scenarios'
title_zh: 视频场景下多模态大模型指令遵循能力的评估基准
authors:
- Hongbo Liu
- Peixian Chen
- Sihan Liu
- Peiyuan Zhang
- Kai Zou
- Dian Zheng
- Xiaoxing Hu
- Yuhao Dong
- Mengdan Zhang
- Yunhang Shen
affiliations:
- Tencent Youtu Lab
- Tencent Hunyuan
- TJU
- SJTU
- CUHK
arxiv_id: '2608.25529'
url: https://arxiv.org/abs/2608.25529
pdf_url: https://arxiv.org/pdf/2608.25529
published: '2026-08-25'
collected: '2026-08-29'
category: Eval
direction: 多模态LLM指令遵循评估
tags:
- MLLMs
- Instruction Following
- Video Understanding
- Benchmark
- Evaluation
one_liner: 提出Video-IFBench，系统评估视频理解中MLLMs的指令遵循能力，含1500样本和39类约束
practical_value: '- **约束分类体系可复用**：电商视频场景中用户指令常含多个视觉/音频约束（如“找出视频中穿红色衣服且位于画面左侧的人”），可借鉴其39类约束设计评估或训练数据，提升模型对复杂query的遵循能力。

  - **半自动数据构造流水线**：结合MLLM生成、程序化处理和人工验证，可低成本构建领域专用的指令遵循数据集，适合业务迭代。

  - **评估发现的启示**：当前模型在复杂条件分支和语义约束上表现差，提示在Agent系统中需增加指令解析模块或结构化输出约束，避免直接依赖端到端生成。

  - **多模态推荐借鉴**：视频推荐/搜索中用户query可能包含条件选择（如“如果出现A则返回B，否则C”），可参考其嵌套指令模板设计更严格的评测集。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：多模态大模型（MLLMs）在视频理解上表现提升，但现有评测主要关注任务准确率，忽略模型对用户指令中具体约束的遵循能力。真实场景中用户指令常包含视觉、音频、格式等多重约束，指令遵循不足会严重影响实用性。

**方法**：构建Video-IFBench，设计指令分类体系，包含单任务、多任务、选择、嵌套4种模板，覆盖32类任务和39类约束（语义与格式），例如“找出穿红色上衣的人并统计数量，若超过两个则只输出数量否则描述外观”。数据构建采用半自动流水线：MLLM生成候选 + 程序化验证 + 人工复核，得到1.5K高质量样本。

**结果**：对20+近期MLLMs评估发现，指令遵循在视频场景下仍是挑战。模型在约束数量多、语义约束密集、需要条件分支选择正确路径时性能显著下降，尤其在嵌套和选择类指令中表现差，表明当前模型的指令解析和执行能力不足，未来需加强结构化推理与显式约束建模。
