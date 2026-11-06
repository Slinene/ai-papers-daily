---
title: 'TAC-CoT: Tool-Empowered Implicit Chain-of-Thought via Interleaving Explicit
  Tokens'
title_zh: 工具赋能的隐式连续思维链：交错显式令牌
authors:
- Juseon Do
- Sangmin Bae
- Jeesu Jung
- Hwanjun Song
affiliations:
- KAIST
- Cluvion
arxiv_id: '2611.01926'
url: https://arxiv.org/abs/2611.01926
pdf_url: https://arxiv.org/pdf/2611.01926
published: '2026-11-01'
collected: '2026-11-06'
category: Reasoning
direction: 工具赋能的隐式连续 CoT
tags:
- Implicit CoT
- Tool Use
- Latent Reasoning
- Self-Distillation
- Adaptive Budget
- Inference Efficiency
one_liner: 将显式推理段压缩为连续隐式 token，仅保留工具调用与答案等显式文本，在 agentic math/QA 上提点并最多减少 6.8× 前向次数
practical_value: '- 在推荐/搜索 Agent 链路中，可尝试把中间推理（如用户意图解析、商品筛选理由）用连续隐式 token 表示，只保留搜索词/API
  调用参数/最终推荐理由等显式文本，降低 token 开销和第一步响应延迟。

  - 借鉴“每段隐式推理后做 action/answer 路由”的机制，根据 query 难度动态决定是否继续调用工具（如多轮检索、用户画像补全），避免所有请求都走固定深度解析。

  - 训练上，可利用现有人工 reasoning 轨迹或让强模型（如 DeepSeek-V3/GPT）合成带工具调用的数据，再用重建损失 + 显式 CE + hidden
  state 蒸馏训练小模型，适合将线上大模型能力压缩到低延迟模型。

  - 注意业务场景 API 复杂、多轮多义时还需验证；但 forward pass 减少和错误累积缓解对长程推荐 Agent 有直接迁移价值。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
显式 CoT 虽然可解释且便于工具调用，但逐字生成推理轨迹导致推理成本高、错误累积；现有隐式 CoT 使用固定连续 token，无法在中间发出工具调用，也不适应 query 难度。TAC-CoT 解决这一矛盾。

**方法关键点**  
- 将显式轨迹中每个推理段 R(i) 替换为 b 个连续 thought token，保留工具调用 u(i)、观测 o(i)、最终答案 a 为显式文本，形成交错序列。  
- 每个隐式段结束后比较工具调用与答案 logits 进行路由，决定调用工具或生成答案；总隐式预算随 query 自适应。  
- 训练数据：GSM8K 使用 GSM8K-Aug 对齐插入计算器交互；HotpotQA 用 DeepSeek-V3 合成含工具调用的轨迹，过滤到与 gold answer 匹配的 40k 条。  
- 训练目标：辅助 decoder 从隐式 token 重建对应显式推理块（reconstruction loss），显式文本用 CE；教师模型在显式轨迹上训练，蒸馏答案边界 hidden state。

**关键实验/结果**  
在 Qwen2.5-0.5B、Llama-3.2-1B、Qwen3-4B 上，数学（GSM8K/GSM-Hard/SVAMP）与 QA（HotpotQA/2Wiki/TriviaQA）基准，TAC-CoT 全面超过 Explicit-CoT agent 和 CODI/SIM-CoT/TokenSkip 等基线；数学平均+5.8 点，QA 平均+2.4 点，QA 前向次数最多减少 6.8×；AC@k 提升、ToolBench 多工具 SoWR 58.6% 显著优于；错误累积分析显示隐式推理对过长推理更鲁棒。

**最值得记住的一句话**  
在 Agent 循环中，把“思考”放进连续 latent token、把“行动/观测”留在显式文本，能在不牺牲工具接口的前提下同时获得隐式推理的效率和鲁棒性。
