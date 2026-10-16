---
title: 'EdgeWise: Bringing Long-Horizon Agents to the Edge via Selective Cloud Delegation'
title_zh: EdgeWise：通过选择性云委托将长程智能体带到边缘
authors:
- Zeru Shi
- Jindong Jiang
- Ryo Hachiuma
- Yonggan Fu
- Byung-Kwan Lee
- Peter Belcak
- Saurav Muralidharan
- Ayush Agarwal
- Ruixiang Tang
- Ambrish Dantrey
affiliations:
- NVIDIA
- Rutgers University
arxiv_id: '2610.17560'
url: https://arxiv.org/abs/2610.17560
pdf_url: https://arxiv.org/pdf/2610.17560
published: '2026-10-12'
collected: '2026-10-16'
category: Agent
direction: 边缘-云端 Agent 协作与选择性模型路由
tags:
- Edge-Cloud Collaboration
- Model Routing
- Long-Horizon Agents
- RL Fine-Tuning
- SLM-LLM Collaboration
- Cost Reduction
one_liner: 提出EdgeWise框架，让本地SLM作为主求解器，仅在关键步骤选择性委托云LLM，显著降低成本且保持性能
practical_value: '- 在电商/广告等长链路 Agent 工作流（选品、文案生成、数据分析）中，识别关键决策步骤（类似 Write/Edit）并仅对这部分调用大模型，其余用轻量模型处理，可显著降低大模型
  API 成本。

  - 借鉴 self-delegation 的 RL 训练方式：用轨迹级奖励 + 步骤级 credit assignment，让 SLM 自主学习何时调用大模型，无需额外路由模型；可以用一个轻量
  critic 模型提供细粒度优势信号。

  - 跨模型协作时，上下文传递不要盲目压缩：全量历史性能最好但成本高，可尝试去掉轻量模型的内部推理只保留执行历史，在性能和成本间取得折中。

  - 将路由判断改为连续分数 + 阈值控制，可以灵活调整大模型调用频率，适合业务中根据预算动态平衡成本与效果。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
长程 Agent 任务通常全程依赖云端大模型，推理成本高昂，但并非每一步都需要同等模型能力。先前工作多聚焦单查询路由或依赖额外模型池，缺乏对真实长程任务（如代码、深度研究）的评估。本文在边缘-云场景下，让本地 SLM 作为主求解器，仅在关键步骤选择性调用云 LLM，以大幅降低推理成本。

**方法关键点**
- 随机委托实验发现：仅约 40% 步骤使用 LLM 即可达到与全程 LLM 相近性能，但委托位置至关重要。
- 分析 2.4k 条轨迹，识别出 Write/Edit 动作与任务成功相关性最强（r=0.200），据此设计关键步骤感知委托。
- 两种委托机制：外部 judge（GPT-5.4-mini 判断是否委托）和 self-delegation（SFT + RL 训练 SLM 自主决策）。
- RL 阶段引入 step-level credit assignment：用 critic 模型评估每个委托决策，奖励包含任务正确性和云调用惩罚；轨迹级优势 + 步骤级优势加权。
- 上下文传递研究：对 LLM 全量历史最佳；对 judge 全量历史最佳，但去除 SLM 推理可降低推理成本且性能接近。
- 阈值控制：将 judge 输出扩展为连续分数，通过阈值调节委托频率，实现预算可调。

**关键实验**
以 Qwen3.5-9B 为 SLM，GPT-5.5 或 Opus4.8 为 LLM，在 Terminal-Bench 2.1 和 SWE-ReBench 上评估。Self-delegation 相比纯 LLM：SWE-ReBench Pass@3 成本降低 53%（GPT-5.5）和 63%（Opus4.8），性能持平或略高；Terminal-Bench 降低 35%/33%。平均成本降低 46%。在 DGX Spark 边缘设备上验证，成本节省约 50%。

**最值得记住的一句话**
大模型能力应集中在少数关键步骤（如 Write/Edit），而非均匀分配；通过 RL 让 SLM 学会选择性委托，是边缘-云协作实现成本与性能平衡的有效路径。
