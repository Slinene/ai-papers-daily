---
title: 'Data Turnstile: A Scalable Open Framework for Function-Calling Data Generation'
title_zh: Data Turnstile：面向函数调用的可扩展数据合成开放框架
authors:
- Goutham Ramakrishnan
- Megha Sharma
affiliations:
- Amazon AGI
arxiv_id: '2607.29250'
url: https://arxiv.org/abs/2607.29250
pdf_url: https://arxiv.org/pdf/2607.29250
published: '2026-07-31'
collected: '2026-08-03'
category: Training
direction: 小模型工具调用数据合成
tags:
- Function Calling
- Synthetic Data Generation
- Small Language Models
- Multi-turn Agent
- Data Quality
- Open-source Framework
one_liner: 将多轮工具调用交互分解为逐角色生成与验证，用高质量合成数据让 0.6B SLM 无需 CoT 即超越 4B 基座。
practical_value: '- **自定义域数据生成**：电商 Agent、搜索助手等场景下，只需提供自有 API 定义与策略文档，即可用 Turnstile
  合成高质量多轮对话数据，训练轻量工具调用模型，降低推理延迟和部署成本。

  - **模板化验证提升质量**：借鉴逐角色生成+结构 / 语义验证+错误重试的流水线，可在内部数据生产中避免一次性生成导致的 API 幻觉、格式错误等；动态注入“无关
  API 拒绝”训练样本，解决模型盲目录入调用问题。

  - **无 CoT 加速推理**：经 Turnstile 数据微调的 SLM 在单轮简单任务上无需 CoT 即可超越带思考的基座，适合对延迟敏感的线上服务；但多轮复杂任务仍需保留
  CoT，可依据任务复杂度灵活选择推理模式。

  - **多样性控制方法**：模板分布、参数组合采样和动态扰动（如模拟 API 执行失败、用户不配合）能显式控制数据多样性，优于仅靠温度采样的方式，适合构造覆盖长尾与异常情况的稳健训练集。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**：小型语言模型（SLM）在边缘部署中有低延迟、低成本、高隐私优势，但工具调用能力弱，主要瓶颈是训练数据质量。现有合成方法要么一次性生成整个对话导致质量失控，要么需要真实 API 执行环境，限制使用范围。

**方法关键点**：
- **交互模板 DAG**：将多轮工具调用分解为 USER、THINKING、API CALL、API OBS、ASSISTANT 五种角色，按有向无环图逐步生成，每步生成后执行**结构与语义验证**，失败时提供错误反馈并重试。
- **多样性提升**：通过模板权重控制不同交互结构比例，结合 API 库、用户画像等参数采样，并引入**动态扰动**（API 执行失败、信息不完整等）生成鲁棒性更强的数据。
- **执行无关验证**：不依赖真实后端，仅需 API schema，利用 LLM-as-Judge 在每步检查参数是否合法、观察值是否合理。

**关键结果**：
- 在 BFCL 单轮基准上，Qwen3-0.6B 经 Turnstile 数据微调后，**不启用 CoT 即达 75.9%**，超越基座带思考的 67.4%，接近 7 倍大的 Qwen3-4B（79.9%）。相比使用相同 API 的原始开源数据，Turnstile 带来 **+15.3pp** 绝对提升。
- 在 τ²-bench 多轮 Telecom 任务上，Turnstile 微调的 Qwen3-1.7B 达到 **31.1% pass¹**，超过 19 倍大的 Qwen2.5-32B 的 27.4%；0.6B 模型从 3.5% 提升到 24.6%，提升约 7 倍。
- 消融显示：多轮任务中 CoT 至关重要（无 CoT 性能暴跌 11‑22pp），但单轮任务中 CoT 反而导致不相关调用合理化，提出参数过度解读；工具调用 token 加权 SFT 带来小幅增益。
- 开源框架及包含 1K+ API、100K+ 交互的合成数据集。
