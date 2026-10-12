---
title: 'Orthros: Phase-Aware Heterogeneous Attention for Efficient Transformers'
title_zh: Orthros：相位感知异构注意力，高效 Transformer
authors:
- Yuhong Chou
- Zehao Liu
- Yuqi Pan
- Qian Liu
- Xianwei Chen
- Zhongzhu Zhou
- Jibin Wu
affiliations:
- The Hong Kong Polytechnic University
- University of Chinese Academy of Sciences
- Independent Researcher
- University of Sydney
arxiv_id: '2610.13735'
url: https://arxiv.org/abs/2610.13735
pdf_url: https://arxiv.org/pdf/2610.13735
published: '2026-10-09'
collected: '2026-10-12'
category: LLM
direction: 高效 Transformer 注意力架构
tags:
- Efficient Attention
- Sliding Window Attention
- Long Context
- Inference Acceleration
- Transformer Architecture
one_liner: Orthros 注意力按预填充/解码相位解耦：线性复杂度预填充加全注意力解码，长上下文召回近无损并大幅加速推理
practical_value: '- 对于推荐/搜索/Agent 中长 prompt、短输出的场景（如基于大段用户行为序列生成推荐理由、商品描述改写），这类相位解耦注意力可将
  TTFT 降低数倍，适合在线低延迟要求；若输出很短，收益尤其明显。

  - 现有 LLM（如 Qwen3、Llama3.1）可通过 80B token 级继续训练转换为 Orthros 结构，且性能不降，业务方可在已有模型上低成本验证和部署；转换时注意保留窗口大小
  128 的设置。

  - 双流设计（滑动窗口 + 全注意力）通过复制输出 token 实现全局召回，可复用到需要长上下文记忆的对话式推荐、个性化解释生成等任务，避免线性注意力带来的召回损失。

  - 工程落地需注意：当前实现基于 FLA/SGLang，解码时额外 token 会增加 FLOPs，但在 I/O bound 解码阶段可被掩盖；若使用 MoE
  或需要 KV cache 压缩，需要定制路由和缓存策略。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

**动机**  
长上下文 LLM 在推理时面临预填充算力瓶颈。线性/滑动窗口注意力虽降复杂度但损害上下文召回；混合架构（如 Jamba）仍受全注意力瓶颈限制，无法实现真正的线性加速。需要一种在预填充阶段线性、在解码阶段保持全局注意力的机制。

**方法关键点**  
- Orthros 按生成阶段解耦：对全部 token 做滑动窗口注意力（窗口 128）以线性复杂度处理输入；对输出位置的 token 额外执行 full cross-attention，查询全局 KV cache。  
- 训练时复制输出 token 为“base token”和“output-specific token”，分别生成滑动窗口 query 和 cross query，用可学习 scale-offset 区分，不增加参数和 I/O 负担。  
- 同一层内统一两种注意力，无需改变宏观架构，支持预训练、SFT、预填充、解码四种模式，训练推理严格一致。  
- 复杂度：当输出长度 Tout 远小于输入长度 T（长上下文/高输入低输出场景），复杂度为 O(Tout T d)，接近线性；输出极短时退化为严格线性；只有预训练时输出长度接近输入才回到二次。

**关键实验与结果**  
- 1.3B 模型从零训练 100B tokens，常识推理平均分 53.98，优于 Transformer（53.41）及 GDN/GLA/RetNet/SWA。  
- 将 Llama3.1-8B 和 Qwen3-8B 转换为 Orthros 并用 80B tokens 继续训练，平均分分别 67.26 vs 65.47（原模型）和 67.00（同数据继续训练 Transformer），Qwen3 转换同样优于 baseline。  
- 128K needle-in-a-haystack 近乎满分；长上下文召回任务平均分 34.4，与 Transformer 34.4 持平，超过其他高效注意力。  
- 预填充 8B 模型在 1M tokens 时相对 Qwen3 最高加速 21.9×；128K 输入/128 输出端到端 TTFT 从 77.2s 降至 17.0s，E2E 从 84.9s 降至 24.6s；解码吞吐与 Transformer 相当（额外计算被 I/O bound 掩盖）。

**最值得记住的一句话**  
将 Transformer 的效率优化从“结构混合”转向“相位解耦”，是兼顾长上下文召回与推理加速的关键。
