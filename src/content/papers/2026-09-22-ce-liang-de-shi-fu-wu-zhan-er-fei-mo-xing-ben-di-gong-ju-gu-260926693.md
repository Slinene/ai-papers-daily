---
title: 'Measuring the Serving Stack Instead of the Model: Hidden Confounds in Local
  Tool-Use Evaluation'
title_zh: 测量的是服务栈而非模型：本地工具调用评估的隐藏混淆
authors:
- Lijuan Tang
- Yuemeng Zheng
affiliations:
- Northeastern University, Seattle
arxiv_id: '2609.26693'
url: https://arxiv.org/abs/2609.26693
pdf_url: https://arxiv.org/pdf/2609.26693
published: '2026-09-22'
collected: '2026-09-23'
category: Eval
direction: LLM 评估 · Tool-Use 服务栈混淆
tags:
- tool-call
- serving stack
- Ollama
- evaluation
- LLM Agent
one_liner: 本地 Tool-Use 评估中 serving stack 的协议差异会系统性污染模型工具调用保真度测量结果
practical_value: '- 在自建 LLM Agent 评估时，把 serving 层返回码、rejection、retry exhaustion 作为结构化字段写入轨迹；否则模型未调用与
  HTTP 400/重试耗尽会被混为 0% 工具调用保真度。

  - 对齐不同推理栈（Ollama/llama.cpp/vLLM/SGLang）对 tools= 请求的处理：先用同一批请求做 cross-stack probe，确认返回的是
  native tool_calls 还是文本，避免把服务栈行为当成模型差异。

  - 对需要文本工具列表的模型，采用“保留 native 通道 + 额外文本 tool list”的协议可能恢复测量保真度；不要对所有模型强制统一 text protocol，Llama-3.2
  等原生工具调用模型反而会下降。

  - 指标口径避免 turn-pooled 与 per-instance 混用，二者可差约 55 个点；constrained decoding 能压缩解析失败，但要监控非终止与长尾延迟。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

动机：coding agent 必须发出可解析的 tool call，harness 才能执行动作。该步骤常被模型能力评估忽略，但其测量结果可能被本地 serving stack 系统性干扰。

方法关键点：以 Ollama 默认 tools= 请求为切入点，记录不同模型的静态 template flag 门控行为：部分模型被接受并返回文本或 native tool_calls，而 Phi-3 与 Gemma-3 在推理前就被拒绝。评估 harness 未保留 rejection 与 retry exhaustion 作为结构化失败元数据，导致下游分析误判为模型未调用。实验比较了添加文本 tool list 但保留 native 通道、统一文本协议两种方式，并在 Ollama、llama.cpp、vLLM、SGLang 上做交叉探测，同时考察 constrained decoding 与 turn-pooled / per-instance 指标口径。

关键结果：被拒绝请求若未记录可导致天真地报告 0% 保真度；对已被接受的模型，额外文本 tool list 可恢复大部分保真度，但统一文本协议会使支持 native tool-call 的 Llama-3.2 下降。不同推理栈对同一请求处理不同。Constrained decoding 消除解析失败但可能诱发非终止；turn-pooled 与 per-instance 估计差异最高约 55 个点。结论是 serving behavior 应作为评估协议的一部分。
