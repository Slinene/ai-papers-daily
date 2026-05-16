---
title: 'From Text to Voice: A Reproducible and Verifiable Framework for Evaluating
  Tool Calling LLM Agents'
title_zh: 从文本到语音：可复现且可验证的工具调用 LLM 智能体评估框架
authors:
- Md Tahmid Rahman Laskar
- Xue-Yong Fu
- Seyyed Saeed Sarfjoo
- Quinten McNamara
- Jonas Robertson
- Shashi Bhushan TN
affiliations:
- Dialpad Inc.
arxiv_id: '2605.15104'
url: https://arxiv.org/abs/2605.15104
pdf_url: https://arxiv.org/pdf/2605.15104
published: '2026-05-14'
collected: '2026-05-16'
category: Eval
tags:
- Tool Calling
- LLM
- Audio
- Evaluation
- TTS
- Omni-modal
one_liner: 提出将文本工具调用基准转化为受控音频评估的框架，保留原始标注，实现配对文本-音频对比，发现语音性能损失高度依赖模型与任务
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**
当前语音智能体需从语音输入可靠调用工具，但主流工具调用基准（如 Confetti、When2Call）均为文本形式，无法直接评估端到端全模态模型在语音场景下的表现。企业若自行从头构建音频基准，需重新标注工具模式和金标准标签，成本高昂。因此，迫切需要一种低成本、可复现的方式，将已验证的文本基准快速转换为受控语音评估，同时保留原始标注与评分协议，以支持级联与端到端架构的早期诊断。

**方法关键点**
- **TTS 转换流水线**：利用 Gemni‑2.5‑Flash‑TTS、Pro‑TTS 和 GPT‑4o‑Mini‑TTS 将原始文本查询合成语音，覆盖多种性别与音色，并注入 DEMAND 环境噪声（SNR 5‑20 dB）。
- **配对实例保留标注**：每一条语音均来自原始文本，完全继承工具模式、金标准标签和现有评分协议，实现受控的文本‑音频对比。
- **多模态模型评估**：在音频版本的 Confetti 与 When2Call 上评测七款全模态模型，包括 GPT‑4o/1.5/Mini‑Realtime、Gemini‑2.5/3.1‑Flash‑Live、Qwen3‑Omni 和 Phi‑4‑Multimodal，并与干净文本、ASR→文本级联两种设定对比。
- **配对错误分解**：利用相同实例的文本‑音频对，将失败归因于决策错误、工具选择错误、参数模式错误和参数值错误四类。
- **参考自由 LLM 裁判**：引入 GPT‑5 与 Gemini‑2.5‑Pro 裁判进行无参考评估，并验证开源 Qwen3 裁判与专有裁判的一致性。

**关键结果数字**
- Confetti 上 Gemini‑3.1‑Flash‑Live 准确率达 **70.4%**，When2Call 上 GPT‑Realtime‑1.5 F1 达 **71.9%**。
- 文本到语音准确率下降幅度显著模型依赖：Qwen3‑Omni 仅下降 **1.8 点**，GPT‑Realtime‑1.5 下降 **4.8 点**。
- 错误分析表明，参数值理解错误占大多数（Gemini‑3.1‑Flash‑Live 为 57.2%，GPT‑Realtime‑1.5 为 54.3%），表明模型常保留工具调用框架但听错具体值。
- Qwen3 裁判在 **8B** 以上参数规模与专有裁判一致性超过 **80%**，提供隐私友好评估路径。
- 模糊查询重构压力测试下，Qwen3‑Omni 文本准确率从 62.2% 暴跌至 37.6%（‑24.6 点），提示任务表述也能成为性能瓶颈。

**核心洞见**
语音工具调用性能无法仅凭架构判断优劣，级联与端到端的相对优势取决于具体模型和任务上的文本‑语音能力差距。该框架为企业在自有数据上做出级联 vs. 全模态诊断提供了低门槛、可复现的首阶段工具。
