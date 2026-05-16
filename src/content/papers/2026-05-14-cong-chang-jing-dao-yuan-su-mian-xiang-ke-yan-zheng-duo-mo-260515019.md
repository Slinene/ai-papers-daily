---
title: 'From Scenes to Elements: Multi-Granularity Evidence Retrieval for Verifiable
  Multimodal RAG'
title_zh: 从场景到元素：面向可验证多模态 RAG 的多粒度证据检索
authors:
- Guanhua Chen
- Chuyue Huang
- Yutong Yao
- Shudong Liu
- Xueqing Song
- Lidia S. Chao
- Derek F. Wong
affiliations:
- University of Macau
arxiv_id: '2605.15019'
url: https://arxiv.org/abs/2605.15019
pdf_url: https://arxiv.org/pdf/2605.15019
published: '2026-05-14'
collected: '2026-05-16'
category: Multimodal
tags:
- Multimodal RAG
- Element-level Grounding
- Benchmark
- Attribution
- Open-vocabulary Detection
one_liner: 提出元素级多模态 RAG 框架 GranuRAG 与基准 GranuVistaVQA，通过检测-匹配-生成实现透明归因与大幅性能提升
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**  
当前多模态 RAG 系统以整图或整场景为检索单元，与细粒度用户查询之间存在粒度不匹配，且无法对失败进行归因——检测错误、检索错误与生成幻觉混为一团。为解开这一黑箱，需要将视觉元素作为一等检索目标，构建从元素检测、知识匹配到归因生成的透明流水线。现有基准缺乏元素级监督，尤其忽略真实场景中因视角变化导致的“部分可见”挑战。  

**方法关键点**  
- **GranuVistaVQA 基准**：包含 71 处地标、1422 张多视角图像，为每张图像人工标注可见元素集合（平均仅覆盖地标总元素的 34%），并提供元素到专业描述的结构化知识。  
- **GranuRAG 框架**：三阶段可归因推理——① 使用开放词汇检测器 YOLO-World 定位候选视觉区域，经重叠过滤去冗余；② 以知识库中元素的视觉描述为指导，利用 MLLM 将每个裁剪区域匹配至具体元素，得到置信可见元素集合；③ 仅基于匹配元素及其描述与全局上下文进行归因约束生成，确保每项事实声明可追溯到视觉区域与检索片段。  
- **错误可拆分诊断**：流水线天然分离“是否检测到正确元素→是否正确检索知识→生成是否忠实”，使归因评价成为可能。  

**关键实验**  
- 在 GranuVistaVQA 上评估 6 个 MLLM（Qwen3-VL、GPT-4o、Claude-3.5-Sonnet 等），下，GranuRAG（仅提供验证后的元素子集）相比基线（全量候选元素）和 CoT 均取得一致且显著提升：最佳模型 Qwen-VL-Max 的 LLM Score 从 54.70 升至 83.90，小型模型 Qwen3-VL-8B 也由 52.90 升至 65.00；fine-tuned 版本达到 70.24。消融表明，检测+元素过滤是关键，优于纯 LLM 提取或 CLIP 检索；注意力可视化证实模型将焦点重定向到知识相关区域。人类评估中 GranuRAG 对 GPT-4o 和 Qwen-VL-Max 的胜率分别达 82.22% 和 91.11%。  

**一句话最值得记住**  
“将视觉元素显式接地为检索单元，而非依赖粗粒度隐式注意力，是多模态可验证推理的关键转折，带来了 29.2% 的性能跃升并让错误可追溯。”
