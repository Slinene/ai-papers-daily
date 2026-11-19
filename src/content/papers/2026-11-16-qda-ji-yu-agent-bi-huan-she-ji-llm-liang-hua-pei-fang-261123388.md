---
title: 'QDA: Closed-Loop LLM Quantization Design with Agents'
title_zh: QDA：基于 Agent 闭环设计 LLM 量化配方
authors:
- Xingyang Li
- Tianlang Zhao
- Song Han
- Ligeng Zhu
affiliations:
- MIT
- NVIDIA
arxiv_id: '2611.23388'
url: https://arxiv.org/abs/2611.23388
pdf_url: https://arxiv.org/pdf/2611.23388
published: '2026-11-16'
collected: '2026-11-19'
category: Agent
direction: Agent 闭环优化 LLM 量化配方
tags:
- LLM Quantization
- PTQ
- Agent
- KL Divergence
- AutoML
- Serving
one_liner: LLM agent 闭环搜索量化配方，以 KL 为廉价代理指标，跨模型/精度平均提升 0.9–2.2 个点
practical_value: '- 借鉴「廉价代理指标 + 最终全量评测」的闭环：在 Agent 搜索优化模型压缩、超参或 serving 配置时，不要直接对昂贵业务指标（线上
  A/B、长 CoT 推理准确率）评分。可缓存原始模型输出的 top-k token 分布/参考轨迹，用 KL 等分钟级指标排序候选，仅对少量 promising
  候选做长文本生成检查，最后才用测试集/业务集验收。

  - 隔离评估器，防止 Agent 过拟合：让参考轨迹和最终测试 benchmark 对 agent 不可见，所有 GPU 作业通过队列调度，工具调用可审计；避免
  Agent 通过校准数据或 prompt 直接刷高分。这是做自动化 ML 搜索/AutoML 的通用工程原则。

  - 构建可组合方法库：把 PTQ 方法统一为「checkpoint → checkpoint」接口，自动从模型结构推导层间关系，降低新架构适配成本；MoE expert
  批量求解加速 GPTQ。多模型/多架构的量化部署可直接复用该工具链思路。

  - 如果要在电商/搜索/推荐系统中部署 LLM（如生成式推荐、query 改写、Agent 推理），该论文的量化配方搜索可直接降低 serving 成本，并验证了在多种
  reasoning model 上能超过公开 vendor checkpoint，且不增加推理开销。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
PTQ 是低成本 serving LLM 的标配，但最优量化配方因模型和精度而异；专家手工为每个新模型重写配方（如 ModelOpt 为 28 个模型维护 28 份手写配方），无法应对快速发布的大量 open-weight 模型。完整评测一个量化 reasoning 模型需 23–86 GPU-hours，而组合不同 codebase 的 PTQ 方法还需手工移植，导致候选评估和构建都极其昂贵。

## 方法关键点
- 由 coding agent 闭环搜索：每轮提出 recipe → 库构建 checkpoint → 用 KL 打分 → 少量候选做长答案生成检查。
- 廉价代理指标：在 agent 不可见的 reference traces 上，缓存原始模型 top-128 token 分布，只跑量化模型计算 next-token KL；比全评测便宜 350–990×，且能捕捉 serving kernel 引入的误差。
- 可组合库：21 种 PTQ 方法统一为「checkpoint → checkpoint」接口，可任意堆叠；自动从模型结构推导层映射，新架构如 GLM-5.3-Flash 仅需 72 行适配；MoE 的 GPTQ 按 expert 批量求解，从约 16 GPU-hours 降到 0.42。
- Harness 隔离：agent 无 GPU/无外网，只能通过 qda/kl/qsched/handin 四个命令访问系统；测试 benchmark 和 reference traces 对 agent 不可见，防止刷分；调度器共享 8 GPU 并保证预算。

## 关键结果
在 4 个 reasoning 模型（dense / Gated DeltaNet / MoE）上，QDA 相对最强公开配方平均提升 0.9 (W4A16)、1.4 (W4A8)、2.2 (W3A16) 个百分点，每次搜索仅 64 GPU-hours。
320B MoE GLM-5.3-Flash 的 NVFP4 W4A4 搜索中，QDA 恢复 FP8 98.3% 精度，优于 NVIDIA 的 96.9% 和 Red Hat 的 96.3%，且 checkpoint 更小。
同 agent 配 ModelOpt 工具落后 0.5–1.3 个点；替换为 greedy/ASHA 或去掉自研基础设施也下降。
所有 checkpoint 运行在现有 vLLM kernel 上，无推理开销。

最值得记住的一句话：用「缓存原始模型 top-k 分布的分钟级 KL + agent 不可见的评测器 + 可组合方法库」做闭环搜索，能以 64 GPU-hours 自动找到优于人工配方的量化配方。
