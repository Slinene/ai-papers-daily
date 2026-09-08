---
title: 'How Perturbations Propagate: A Multi-Level Analysis of Robustness in Large
  Language Models'
title_zh: 扰动如何在大型语言模型中传播：鲁棒性的多层分析
authors:
- Dun Li Chan
- Emily Liu
- Niyathi Allu
- Christian Hoang
affiliations:
- INTI International College Penang
- Independent Researcher
- FPT University
arxiv_id: '2609.03322'
url: https://arxiv.org/abs/2609.03322
pdf_url: https://arxiv.org/pdf/2609.03322
published: '2026-09-03'
collected: '2026-09-08'
category: Eval
direction: LLM 鲁棒性多层评估
tags:
- robustness
- perturbation
- CKA
- intrinsic dimension
- attention heads
- HotFlip
one_liner: 在六个模型上从行为、隐状态几何和注意力头三层揭示输入扰动传播异质性，证明单指标鲁棒性评估不充分
practical_value: '- 在电商搜索/QueryRec 的 LLM 链路（query rewriting、产品匹配、生成式 item ID 等）中，不要只看最终准确率：对拼写错误、OCR
  扰动、词序打乱等输入，建议同时监控 hidden-state CKA、intrinsic dimension 或关键 attention head 的激活漂移，否则轻微行为变化可能掩盖内部计算崩溃。

  - 对抗性 HotFlip 扰动比同比例随机 token 替换造成更强的行为与表示破坏，且行为影响跨 GPT-2/Qwen2.5 一致；若将 LLM 用于用户输入理解或
  prompt 约束较弱的 Agent 规划，应优先做梯度引导攻击的鲁棒性测试，并考虑对抗样本增强。

  - Copying score 与 token 替换/打乱下 activation patching 恢复高度相关，可在线上输入异常检测中把拷贝型 attention
  head 的响应作为鲁棒性代理指标，快速定位长尾扰动导致的失败。

  - 模型版本升级或 prompt 修改时，用多层指标做回归比对，而不是只跑 benchmark 分数，避免“输出分数没变但表示已经漂移”的隐患。'
score: 6
source: arxiv-stat.ML
depth: abstract
---

**动机**：真实输入中的拼写错误、OCR 损坏、词序打乱等会让 LLM 行为退化，但只看输出无法判断扰动如何改变模型内部计算。  
**方法**：选取六种自然/合成扰动（token 替换、打乱、HotFlip 等），在 4 个 GPT-2 与 2 个 Qwen2.5 checkpoint 上，从三个层级评估：输出行为、隐状态几何（CKA 与 intrinsic dimension）、注意力头功能（GPT-2 activation patching / copying score）。  
**关键结果**：不同扰动产生可区分的多层指标画像，输出指标不能完全捕捉这些差异，且画像跨 checkpoint 只有部分一致。Copying score 与 token 替换/打乱下 activation-patching 恢复高度相关。梯度引导的 HotFlip 在 GPT-2 中比 rate-matched 随机替换造成更强的行为与表示破坏，其行为影响在全部 6 个 checkpoint 上一致。结论是单指标鲁棒性结论可能误导，需要多层评估。
