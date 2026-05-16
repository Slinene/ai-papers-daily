---
title: 'MemLens: Benchmarking Multimodal Long-Term Memory in Large Vision-Language
  Models'
title_zh: MemLens：大视觉语言模型多模态长时记忆基准测试
authors:
- Xiyu Ren
- Zhaowei Wang
- Yiming Du
- Zhongwei Xie
- Chi Liu
- Xinlin Yang
- Haoyue Feng
- Wenjun Pan
- Tianshi Zheng
- Baixuan Xu
affiliations:
- HKUST
- CUHK
- OmniMemory
- NVIDIA
arxiv_id: '2605.14906'
url: https://arxiv.org/abs/2605.14906
pdf_url: https://arxiv.org/pdf/2605.14906
published: '2026-05-13'
collected: '2026-05-16'
category: Eval
tags:
- LVLMs
- Memory Benchmark
- Multimodal
- Long-Context
- Memory-Augmented Agents
- RAG
one_liner: 首个统一长度控制下的多模态对话记忆基准，对比长上下文与记忆增强两类方案，揭示视觉证据检索为瓶颈
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机** 大视觉语言模型（LVLMs）在多轮交互中需要持续记忆，现有方案分为长上下文 LVLMs 和记忆增强智能体两类，但缺乏在需要多模态证据的任务上对二者进行长度控制对比的基准。多数文本记忆基准忽略视觉，多模态基准常存在文本捷径，无法真正考验跨模态记忆。MemLens 正是为填补这一空白而设计。

**方法关键点**
- **五类记忆能力**：信息提取（IE）、多会话推理（MSR）、时序推理（TR）、知识更新（KU）、回答拒绝（AR），覆盖检索、聚合、更新与拒答。
- **强制跨模态依赖**：通过实体抽象（如将“金门大桥”替换为“图中这座桥”）和图像‑文本交织构造，使 80.4% 的问题必须依赖视觉证据，消融实验证明移除图像后准确率骤降至 2% 以下。
- **标准化长度构造**：每个问题在 32K/64K/128K/256K tokens 四个长度下实例化，采用跨模态 token 计数，插入与证据风格、话题相似但无关的填充会话，提高检索难度。
- **对比评估**：在同一基准上评价 27 个 LVLMs 和 7 个记忆增强智能体，后者包括纯文本和少量多模态方案，纯文本方案用图像标题替代原图。

**关键结果**
- **总体天花板至今未破**：32K 上下最高准确率仅 58.68%（Qwen3.5‑122B），128K 时降为 52.99%（Gemini‑3.1‑Pro）。
- **两类方案互补失效**：长上下文 LVLMs 短上下文表现好（直接视觉接地），但长度增长后衰退（IE 降约 20%，AR 降约 30%）；记忆智能体长度稳定，但得分普遍低于 LVLMs，尤其在 IE 和 KU 上因压缩丢失视觉细节（纯文本方案用 BLIP‑2 标题，差距依然明显）。
- **多会话推理最难**：MSR 上限仅 44%（Kimi‑K2.5），多数系统低于 30%，错误中 73% 为推理错误而非检索错误，但 oracle 检索实验表明正确提供所需会话后准确率恢复至 90%+，提示长上下文下的推理劣化源自上游检索失败。
- **视觉检索是瓶颈**：IE 和 KU 约 90% 的错误属于“视觉”类别（未找到或未正确读取证据图像），说明长上下文首先损害证据定位，而非理解能力。
- **拒答能力退化**：微调的记忆智能体（如 MemAgent‑7B、Memory‑T1、M2A）在 AR 上仅有 9‑22%，而保持骨干网络冻结的智能体（Mem0、MemOS）可达 68‑77%，显示现有记忆微调忽略了拒答信号。

**一句话记忆**：单纯缩放上下文长度或压缩记忆均不能解决多模态长时记忆，未来需融合长注意力和结构化多模态检索的混合架构，并优先提升视觉证据的保持与检索保真度。
