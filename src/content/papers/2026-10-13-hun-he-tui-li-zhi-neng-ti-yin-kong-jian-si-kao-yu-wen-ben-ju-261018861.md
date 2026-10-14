---
title: Hybrid Reasoning Agents
title_zh: 混合推理智能体：隐空间思考与文本工具调用统一
authors:
- Jiaru Zou
- Yunzhe Qi
- Sirui Chen
- Federico Bianchi
- Shang Zhu
- Pan Lu
- Jingrui He
- James Zou
affiliations:
- Stanford University
- Together AI
- UIUC
- Meta
arxiv_id: '2610.18861'
url: https://arxiv.org/abs/2610.18861
pdf_url: https://arxiv.org/pdf/2610.18861
published: '2026-10-13'
collected: '2026-10-14'
category: Agent
direction: 混合潜在推理与工具调用的 LLM Agent
tags:
- latent reasoning
- tool use
- HybridLink
- RL
- KV cache
- LLM Agent
one_liner: HybridAgent 用轻量 HybridLink 与连续工作记忆交替进行潜在推理和文本工具调用，在 11 个基准上平均提升 10.4% 并大幅降低
  token、延迟与成本
practical_value: '- 在搜索/推荐 Agent 中，把长 CoT 的中间推理压缩为 latent steps，仅在需要调用搜索 API、商品过滤工具时切回
  text，可大幅降低 token 费用和首字延迟；适用于高并发在线服务。

  - 复用 KV cache 作为跨轮工作记忆：多轮搜索/推荐对话中保持工具结果和内部表示，避免重复编码；可参考其 persistent KV accumulation
  设计来优化多轮 Agent 服务。

  - 后训练要解决 train-inference mismatch：先用 teacher forcing 再 self-conditioned 两遍训练，是让模型学会消费自己
  latent 输出的关键；如果业务中做类似隐式状态，这个 trick 值得照搬。

  - RL 奖励只给 correctness + format + tool use，不显式控制 latent/text 比例，让模型自适应分配；在电商 Agent
  中可避免奖励设计过度约束导致行为退化。

  - 可解释性：latent pseudo-text 映射到最近 token，方便监控和 debug；适合需要审计的推荐理由生成/搜索排序 Agent，可保留可解释性同时降本。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**
现代 LLM Agent 的推理和交互都通过文本 token 进行，所有中间推理都逐 token 生成，带来高延迟、高 token 成本；同时 latent reasoning 虽然高效但缺乏工具调用和可解释性。两者割裂，需要统一。

**方法关键点**
- **HybridLink**：轻量残差 adapter，把 last-layer hidden state 映射回输入嵌入空间，使模型可进入 latent mode 进行递归快速思考，并能切回 text mode 做工具调用和外部监控。
- **动态模式切换**：用特殊 token `<latent>` 进入，用余弦相似度对齐 exit anchor `</latent>` 退出，模式长度由模型自适应决定。
- **多轮混合生成**：把 text、latent、tool observation 的 KV entries 都累积到连续工作记忆，无缝跨轮复用，避免 token 空间重构。
- **训练**：HybridSFT 两阶段：先 format activation 和 HybridLink activation，再 self-conditioned 两遍训练（teacher forcing + 自生成 latent 输入）消除训练/推理 mismatch。HybridRL：提出 hybrid policy factorization，只在 text 采样位置计算 importance ratio；exact rollout replay 重建可微图；奖励包含 correctness + format + tool use，不显式惩罚模式。
- **可解释性**：latent 模式虽无解码，但每个 latent step 映射到最近 token embedding 可读，形成 pseudo-text。

**关键实验**
11 个基准（数学、科学、医学、搜索、agentic reasoning），Qwen3-Base 4B/8B/14B，对比 frontier LLM Agents（GPT-5.6-Luna, Kimi-K3, GLM-5.3-Flash 等）、agentic frameworks（ReAct, Search-o1, WebThinker）和 latent methods（Coconut, SoftThinking, SoftCoT）。结果：平均性能提升 10.4%，token 减少 35.5%–54.7%，推理加速 1.8–2.6x，成本降低 2.7–3.7x；在 GAIA、WebWalker 等上 14B 超越最强 agentic baseline 平均 17.4%；因果干预实验证明 latent thoughts 被真实依赖；工具调用有效性和可审计性保持。

**最值得记住的一句话**
用轻量 HybridLink 把隐空间推理作为一等公民融入 LLM Agent，内部思考用连续向量省 token 和延迟，对外只暴露工具调用和关键文本步骤，同时保持可审计。
