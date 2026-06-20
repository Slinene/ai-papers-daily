---
title: 'S-Agent: Spatial Tool-Use Elicits Reasoning for Spatial Intelligence'
title_zh: S-Agent：空间工具使用激发空间智能推理
authors:
- Yalun Dai
- Hao Li
- Shulin Tian
- Runmao Yao
- Yuhao Dong
- Fangzhou Hong
- Zhaoxi Chen
- Fangfu Liu
- Baoliang Tian
- Dingwen Zhang
affiliations:
- NTU
- THU
- ByteDance
- NWPU
- Ropedia
arxiv_id: '2606.20515'
url: https://arxiv.org/abs/2606.20515
pdf_url: https://arxiv.org/pdf/2606.20515
published: '2026-06-17'
collected: '2026-06-20'
category: Agent
direction: 空间智能 Agent 范式
tags:
- Spatial Intelligence
- Tool-Use Agent
- VLM
- Evidence Accumulation
- Memory
- SFT Distillation
one_liner: 将空间推理变为VLM规划的时空证据累积过程，配备层次化工具与双记忆，零样本提升多视图推理并可蒸馏小模型。
practical_value: '- VLM 作为规划器结合层次化空间工具（2D→3D lifting）的模式可直接复用到电商多模态商品理解，例如调用工具提取商品尺寸、方位、遮挡关系等空间属性，丰富推荐特征。

  - 双记忆设计（Scene Memory 存储场景状态 + Agent Memory 存储工具调用与推理历史）为对话式推荐 / 搜索中的多轮状态管理提供参考，能持续累积用户意图与工具反馈，避免孤立轮次。

  - 推理时增强 + 轨迹蒸馏方法论（S-300K → S-Agent-8B）可借鉴到业务轻量模型升级：收集 LLM/VLM 的工具调用轨迹，微调小模型，在成本限制下获得复杂推理能力。

  - 时空证据累积而非单帧预测的思路，对视频推荐或动态场景理解有价值，例如从用户浏览视频多帧中逐步累积兴趣证据，提升长期偏好建模的准确性。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有 VLM 及工具增强 Agent 大多仅处理静态、孤立图像，无法在连续多视图或视频中进行状态化空间推理，丢失了场景演化和时序证据。

**方法关键点**：
- 将 VLM 重新定位为语义规划器，动态决定需要何种空间证据，而非直接预测答案。
- 层次化空间工具链：2D 目标定位 → 3D 几何 lifting → 聚合为高层空间知识（计数、测量、方位、相对位置）。
- 双记忆系统：Scene Memory 维护动态场景状态，Agent Memory 累积工具调用与推理上下文，实现跨帧与跨步骤的时空证据积累。
- 训练自由增强：无需微调即提升多种 VLM 零样本性能；通过收集 S-Agent 推理轨迹构建 S-300K 数据集，监督微调出 S-Agent-8B。

**关键结果**：
- 在多视图与视频空间推理基准（MMSI-Bench 等）上，零样本分别提升开源 VLM 最高 10.5%、闭源 Gemini-3-Pro 达 1.2%。
- S-Agent-8B 大幅超越同尺寸 Qwen3-VL-8B，并达到与 GPT-5.4、Gemini 3 等先进闭源模型可比的性能。
