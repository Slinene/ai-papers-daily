---
title: 'ProVe: Proposer-Verifier Decoding'
title_zh: ProVe：提案者-验证者解码
authors:
- Ziqi Jin
- Weiwen Xu
- Jiaxi Li
- Yujie Zhong
- Qi She
- Aixin Sun
arxiv_id: '2610.27815'
url: https://arxiv.org/abs/2610.27815
pdf_url: https://arxiv.org/pdf/2610.27815
published: '2026-10-19'
collected: '2026-11-03'
category: Other
direction: LLM 推理加速 · 提案-验证解码
tags:
- Speculative Decoding
- Block Drafting
- Verification
- Throughput
- LLM Inference
one_liner: 把大模型微调为一次预测多 token 的 proposer，再以小模型或自身验证，取得 2.5–2.7× 解码加速
practical_value: '- 在延迟敏感的 LLM 在线服务（商品描述生成、query 改写、对话推荐）中，可把已有 AR checkpoint 继续微调成
  block proposer，一次 forward 生成多个后续 token，省去额外 draft head，直接降低串行 forward 次数。

  - 若业务要求输出与 greedy AR 完全一致，采用 ProVe-lossless 自验证；若允许少量精度损失换吞吐，则接一个小 verifier，这样部署时可以按
  QPS 目标动态切换档位。

  - 对 Agent 多步推理或工具调用场景，长轨迹生成可让大模型一次起草多个步骤或工具参数，再用轻量 verifier/规则引擎快速校验前缀，减少交互轮次。

  - 注意 block size 与接受前缀的关系：论文 block size 16 只有 6.6 token 平均匹配前缀，实际部署需按领域调 block size
  并监控接受率，避免无效计算。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：自回归大模型每生成一个 token 就要一次串行 forward，推理吞吐受限于串行调用。传统 speculative decoding 由小模型串行 draft、大模型并行 verify，但 draft 质量成为瓶颈。本文反转角色，让大模型负责一次生成多个 token。

方法关键点：从标准 AR checkpoint 微调大模型作为 proposer，单次 forward 预测一个长度为 k 的 token block；再用一个 forward pass 验证该 block。验证器可以是小 AR 模型，也可以是 proposer 自身。后者称为 ProVe-lossless，其 committed prefix 加上 correction token 与 greedy AR 解码逐 token 一致，因此是无损加速。每个解码周期只需两次模型调用，一次提案、一次验证。

关键结果：block size 为 16 时，在 GSM8K 上提案 block 的平均 AR 匹配前缀为 6.6 个 token。使用 32B proposer 在六个 benchmark 上测试，ProVe-lossless 平均达到 2.5× AR throughput，无需额外训练 draft head；使用 3B verifier 的 ProVe 平均达到 2.7× throughput，但六任务平均精度比 AR 低 2.6 个点，提供可调节的速度-精度权衡。
