---
title: Hunyuan-A13B Technical Report
title_zh: 腾讯混元 A13B 技术报告：80B 总参、13B 激活的 MoE 高效 LLM
authors:
- Tencent Hunyuan Team
- Ao Liu
- Botong Zhou
- Can Xu
- Chayse Zhou
- ChenChen Zhang
- Chengcheng Xu
- Chenhao Wang
- Decheng Wu
- Dengpeng Wu
affiliations:
- Tencent Hunyuan Team
arxiv_id: '2609.27284'
url: https://arxiv.org/abs/2609.27284
pdf_url: https://arxiv.org/pdf/2609.27284
published: '2026-09-22'
collected: '2026-09-24'
category: LLM
direction: 高效 MoE LLM 与双模式 CoT 训练
tags:
- MoE
- Dual-Mode CoT
- RL
- Agent Tool Calling
- Long Context
- Inference Efficiency
one_liner: 开源 80B/13B 激活 MoE，通过双模式 CoT 与强化学习在推理和 Agent 任务上逼近更大模型且吞吐更高
practical_value: '- **双模式 CoT 可用于生产级 LLM 路由**：`/no think` 适合商品问答、摘要、搜索 query 理解、自动补全等高
  QPS 低复杂度场景；`/think` 适合购物导购规划、广告投放策略、深度搜索等复杂 Agent 任务。可按 query 复杂度、用户延迟预算或任务类型做策略路由，省
  token 降延迟。

  - **Agent 数据构造方法可直接迁移**：多角色合成引擎（user/planner/tool/agent/checker）+ 沙箱/MCP/合成工具 +
  30 类系统指令 + 20K 格式组合，能低成本生成多样化工具调用数据；再针对高频任务（Excel 处理、深度搜索）做增强，适合电商购物助手、广告 Agent、搜索
  Agent 的 SFT 数据 pipeline。

  - **Agent RL 奖励设计值得复用**：格式奖励（特殊标记与顺序正确给 1）+ 正确性奖励（tool/parameter/value 一致性）能稳定训练工具调用；对推荐/广告投放的
  API 调用、商品搜索参数解析等可定义可验证奖励，再叠加 sandbox 或执行反馈做 RL。

  - **MoE 推理部署配置可作为选型参考**：80B 总参、13B 激活，配 GQA、Expert Parallel、FusedMoE，支持 vLLM/SGLang/TensorRT-LLM
  与 INT8/W8A8/KV Cache FP8，batch 32 约 1982 tokens/s；对实时推荐/Agent 场景，快思考模式 + 量化可显著降低推理成本。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
大模型部署仍面临高延迟、高算力成本，尤其实时 Agent 与长上下文场景。Hunyuan-A13B 以 80B 总参数、13B 激活的细粒度 MoE 开源，目标是在不牺牲推理能力下降低部署门槛。

**方法关键点**  
- **架构**：1 个共享专家 + 64 个细粒度专家，每次激活 8 个非共享专家；采用 GQA、SwiGLU、128K 词表。  
- **预训练**：20T token，重点优化 STEM 数据，得到 250B 高质量 STEM 语料；分三阶段：基础训练 → 300B 快速退火 → NTK-aware 长上下文扩到 32K/256K。  
- **后训练四阶段**：推理 SFT → 推理 RL → 全场景 SFT → 全场景 RL。推理 RL 用 GRPO，奖励为结果验证模型 + 36 语言代码沙箱；去掉 KL 约束、on-policy、低采样温度。  
- **Agent 数据与奖励**：多角色合成引擎（user/planner/tool/agent/checker）、沙箱/MCP/合成工具、30+ 系统指令、20K 格式组合；Agent RL 采用格式奖励 + tool/parameter/value 一致性奖励。  
- **双模式 CoT**：`/no think` 为快思考，空 `<think>` 块；`/think` 为慢思考，带完整推理步骤；默认慢思考。  

**关键结果**  
Base 模型在 14 个基准中 12 个超过 Hunyuan-Large，仅 1/4 激活参数；数学、代码与 STEM 强于 Qwen2.5-72B，与 Qwen3-A22B 互有胜负。后训练慢思考模式 AIME2024 87.3、BBH 89.1、ZebraLogic 84.7，Agent 基准 BFCL-v3 78.3、ComplexFuncBench 61.2；快思考模式 ComplexFuncBench 74.0。长上下文 RULER avg 76.7，64K-128K 达 73.9，领先开源对比模型；吞吐 batch 32 约 1982 tokens/s。

**最值得记住**：细粒度 MoE + 可控双模式 CoT + 面向 Agent 的 RL 奖励设计，使 13B 激活模型在推理和工具调用上逼近甚至超过更大模型。
