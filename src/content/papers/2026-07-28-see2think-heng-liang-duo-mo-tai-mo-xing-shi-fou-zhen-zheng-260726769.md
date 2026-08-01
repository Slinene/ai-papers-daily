---
title: 'See2Think: Do Multimodal Models Really Use Intermediate Visual States?'
title_zh: See2Think：衡量多模态模型是否真正利用了中间视觉状态
authors:
- Siyu Yan
- Zhuoran Yan
- Haiying Xu
- Panhao Zhou
- Jingyu Chen
- Chenhao Ji
- Shuo Cao
- Yongheng Zhang
- Haoze Liu
- Siyu Zhang
affiliations:
- Shanghai AI Laboratory
- The Hong Kong University of Science and Technology
- Central South University
- The Hong Kong University of Science and Technology (Guangzhou)
- University of Science and Technology of China
arxiv_id: '2607.26769'
url: https://arxiv.org/abs/2607.26769
pdf_url: https://arxiv.org/pdf/2607.26769
published: '2026-07-28'
collected: '2026-08-01'
category: Eval
direction: 多模态推理过程诊断与评估
tags:
- Multimodal
- Reasoning
- Evaluation
- Visual States
- Benchmark
- Chain-of-Thought
one_liner: 构建统一评估框架See2Think，诊断多模态推理中中间视觉状态的生成、渲染与利用瓶颈
practical_value: '- 在电商搜索、推荐解释或商品问答的Agent流程中，若引入中间草图、标注等视觉操作，可借鉴VAoT框架记录每一步的视觉动作、渲染结果与后续利用，诊断渲染失败导致的错误传播。

  - 设计多模态Agent时，避免仅依赖最终答案评估，而应分析视觉状态的忠实渲染与反馈吸收率，尤其在3D商品展示或场景理解任务中，即使模型选择正确操作，渲染瓶颈仍会大幅降低准确率。

  - 通过任务相关的损坏反馈干预，可量化模型对中间视觉状态的行为依赖性，这对于验证Agent是否真实依赖视觉信息（如商品图像局部特征）而非文本捷径具有实操价值。

  - 发现高反馈吸收率不一定转化为准确率提升，提示在Agent中盲目增加视觉反馈机制可能无效，应先确保渲染环节准确可靠。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有多模态基准要么任务覆盖窄、部分样本可被纯文本解决，要么只评估最终答案，无法诊断中间视觉状态（如草图、标注、工具输出）是否被生成、渲染并有效利用。

**方法**：提出统一评估框架See2Think，包含两个核心组件：
- See2ThinkBench：1200个开放式视觉依赖问题，覆盖2D结构、3D场景和真实世界推理共12类任务，确保无法仅靠文本求解。
- Visual Action-of-Thought (VAoT)：在四种受控推理设置下，详细记录文本思考、视觉动作、渲染状态及后续推理过程，支持细粒度过程分析。

**结果**：
- 视觉推理性能高度依赖模型和环境，没有一种设置能在所有任务上持续占优。
- 模型通常能选择相关的视觉操作，但忠实渲染是突出的瓶颈。
- 高反馈吸收率并不必然带来准确率提升，表明反馈质量比利用率更重要。
- 在3D场景中注入任务相关的损坏反馈后，准确率下降超过10个百分点，证实模型行为依赖中间视觉状态的正确性。
