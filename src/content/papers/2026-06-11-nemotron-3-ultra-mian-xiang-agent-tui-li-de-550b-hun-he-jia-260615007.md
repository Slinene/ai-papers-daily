---
title: 'Nemotron 3 Ultra: Open, Efficient Mixture-of-Experts Hybrid Mamba-Transformer
  Model for Agentic Reasoning'
title_zh: Nemotron 3 Ultra：面向 Agent 推理的 550B 混合专家 Mamba-Attention 开源模型
authors:
- NVIDIA
- Aaron Blakeman
- Aaron Thomas
- Aastha Jhunjhunwala
- Abhibha Gupta
- Abhinav Khattar
- Adam Rajfer
- Adi Renduchintala
- Adil Asif
- Aditya Vavre
affiliations:
- NVIDIA
arxiv_id: '2606.15007'
url: https://arxiv.org/abs/2606.15007
pdf_url: https://arxiv.org/pdf/2606.15007
published: '2026-06-11'
collected: '2026-06-16'
category: Agent
direction: Agent 专用大模型 · 混合 Mamba-Attention MoE
tags:
- Mixture-of-Experts
- Hybrid Mamba-Attention
- NVFP4
- Multi-Token Prediction
- Agentic Reasoning
- Speculative Decoding
one_liner: 总参数 550B、活跃 55B 的混合 Mamba-Attention MoE 模型，在 Agent 推理上精度对齐且推理吞吐量最高达同规模模型的
  5.9 倍
practical_value: '- **长上下文高效推理架构可迁移到推荐 Agent 中**：Hybrid Mamba‑Attention + MoE 大幅降低
  KV cache 与注意力成本，适合需要维持超长对话历史或文档上下文的推荐/搜索 Agent；可在电商客服、导购助手等场景落地类似模式，平衡推理延迟与能力。

  - **Multi‑Token Prediction 头可直接加速自回归生成**：训练时加入共享权重的 MTP 头，上线后通过投机解码（speculative
  decoding）提升吞吐，对需要高并发生成回复的推荐理由、搜索词改写等场景有直接工程价值。

  - **后训练中的多教师 On‑Policy 蒸馏（MOPD）可借鉴到工业 Agent 对齐**：用领域专家 teacher 在 student 的 rollouts
  上进行 token 级蒸馏，能在保持推理效率的同时注入多任务 Agent 能力（如工具使用、纠错），适合业务定制化 Agent 构建。

  - **推理预算控制（reasoning effort control）可用于动态服务质量调节**：允许在推理时根据负载动态调整思考深度，平衡效果与成本，可应用于推荐
  Agent 的实时适配。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
LLM 从短对话转向长时间自主执行复杂任务的 Agent（代码编写、研究、多步操作）对推理吞吐和长上下文提出了极高要求。现有大型开源模型在 Agent 基准上虽有竞争力，但推理速度往往成为瓶颈。Nemotron 3 Ultra 旨在用混合 Mamba-Attention 与 MoE 架构突破精度‑吞吐边界，提供适合长期运行 Agent 的高效模型。

## 方法关键点
- **架构**：Hybrid Mamba‑Attention + Mixture‑of‑Experts。每 token 活跃参数 55B（总 550B），用 LatentMoE 实现稀疏激活。交替排列 Mamba‑2 层与 Attention 层，减少 KV cache 压力和注意力计算量。
- **NVFP4 预训练**：首次在 550B 规模上稳定使用 4‑位浮点预训练，保留最后 15% 层为高精度，训练损失与 BF16 的差距 <0.4%。
- **Multi‑Token Prediction (MTP)**：两个共享权重的 MTP 头用于预训练，损失系数 0.1；推理时通过投机解码加速，无需额外模型。
- **长上下文扩展**：继续预训练阶段加入 1M 长度数据（含 QA 与 SFT 式数据），保持短上下文指标不下降，RULER 1M 得分 76.8。
- **后训练堆栈**：SFT → 统一 RLVR → Multi‑teacher On‑Policy Distillation (MOPD)。RLVR 融合推理、Agent、代码、安全、长上下文等多环境奖励。MOPD 将十多个领域专家 teacher 的知识通过 student 自生成轨迹进行 dense token‑level 蒸馏，并支持推理预算控制。
- **数据**：预训练数据 20T tokens，分两阶段（先多样性后高质量）；新增代码刷新、法律、道德场景等合成数据；后训练数据涵盖终端操作、软件修复、搜索工具、多语言安全等，总规模约 500K+ 条多轮轨迹。

## 关键结果
- **Agent 与推理精度**：在 Terminal Bench 2.1、SWE‑Bench Verified、TauBench V3、GPQA 等 Agent/推理基准上与 GLM‑5.1、Kimi‑K2、Qwen‑3.5 等持平或接近，且在长上下文 RULER（1M）取得 76.8 分。
- **推理吞吐**：8K 输入/64K 输出设置下，NVFP4 推理吞吐分别为 GLM‑5.1‑754B‑A40B 的 5.9 倍、Kimi‑K2.6‑1T‑A32B 的 4.8 倍、Qwen‑3.5‑397B‑17B 的 1.6 倍（均取各自最佳配置，Nemotron 用 TRT‑LLM，对比模型用 vLLM）。
- **预训练基准**：Base 模型在 MMLU、GPQA、代码、长上下文等全面优于 DeepSeek‑V3.2‑Exp、Mistral Large 3 等公开基座。
- **开源**：模型、数据、训练配方全部开放，包括 BF16 与 NVFP4 量化版本。
