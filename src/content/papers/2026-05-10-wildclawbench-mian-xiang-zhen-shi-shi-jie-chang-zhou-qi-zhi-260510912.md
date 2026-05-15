---
title: 'WildClawBench: A Benchmark for Real-World, Long-Horizon Agent Evaluation'
title_zh: WildClawBench：面向真实世界长周期智能体的基准测试
authors:
- Shuangrui Ding
- Xuanlang Dai
- Long Xing
- Shengyuan Ding
- Ziyu Liu
- Yang JingYi
- Penghui Yang
- Zhixiong Zhang
- Xilin Wei
- Xinyu Fang
affiliations:
- Shanghai AI Laboratory
- The Chinese University of Hong Kong
- Fudan University
- University of Science and Technology of China
- Shanghai Jiao Tong University
arxiv_id: '2605.10912'
url: https://arxiv.org/abs/2605.10912
pdf_url: https://arxiv.org/pdf/2605.10912
published: '2026-05-10'
collected: '2026-05-15'
category: Eval
tags:
- Benchmark
- Agent Evaluation
- CLI
- Multimodal
- Long-horizon
- Safety
one_liner: 构建60个真实长周期多模态Agent任务，揭示前沿模型在原生运行时下最高仅62.2%
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
现有 Agent 基准多依赖合成沙盒、短时任务和模拟 API，仅做最终答案校验，无法反映真实部署中长周期、多模态、跨工具协同的复杂性。亟待一个在原生运行时、真实工具条件下，对端到端轨迹和副作用进行全面审计的评估体系。

### 方法关键点
- **任务设计**：60 个人工编写的中英双语任务，涵盖生产力流程、代码智能、社交互动、搜索检索、创意合成和安全对齐六类，其中 26 个为多模态输入。
- **执行环境**：可复现的 Docker 容器，挂载真实工具（shell、浏览器、文件系统、邮件等），支持 OpenClaw、Claude Code、Codex、Hermes Agent 四种 harness，统一 API 端点，隔离评分资源以防泄漏。
- **评测方式**：混合型 grading — 确定性规则检查（文件存在、格式匹配）、环境状态审计（邮件、日历、聊天记录）及 LLM/VLM 语义法官（GPT-5.4）处理开放式输出。
- **策展流程**：作者撰写→专家参考答案构建→模型试跑与人工过滤（保留差异度≥0.2 的任务）→精炼，确保任务的可审计性和区分度。

### 关键结果
- 19 个前沿模型中，**Claude Opus 4.7 最高只得 62.2%**，其余均在 60% 以下，分数跨度 19.3%–62.2%。
- 多模态任务普遍弱于纯文本（如 GPT-5.4：40.2% vs 58.0%），同一模型在不同 harness 下得分可差 **18 分**（MiMo V2 Pro）。
- 增加技能或推理预算不一定提升——GPT-5.4 高思考模式反而因超时频发降至 45.0%。
- 工具使用风格差异显著：GPT-5.4 重文件阅读，MiniMax M2.7 重 shell 和网页调用。

### 核心洞察
在真实运行时、长周期 Agent 评估中，模型能力、harness 设计、时间预算和工具生态共同决定表现，单一维度优化远远不够。
