---
title: 'TraceForge: Distilling with Your Own Thinking'
title_zh: TraceForge：按学生模型家族风格生成推理轨迹的蒸馏方法
authors:
- Yan Wang
affiliations:
- Independent Researcher
arxiv_id: '2610.29680'
url: https://arxiv.org/abs/2610.29680
pdf_url: https://arxiv.org/pdf/2610.29680
published: '2026-10-20'
collected: '2026-10-22'
category: Training
direction: LLM 蒸馏 · 推理轨迹合成
tags:
- LLM distillation
- reasoning trace
- adversarial training
- style transfer
- code generation
one_liner: 提出 TraceForge，在仅有教师答案时合成学生家族原生推理轨迹用于蒸馏，代码任务提升显著
practical_value: '- 黑盒教师 API 只给答案时，不要放弃 CoT 蒸馏：可训练一个本地生成器，用 (context, answer) 自动补写学生模型家族风格的推理轨迹，再用于
  SFT 小模型；尤其适合电商 Agent 的工具调用轨迹、商品推荐理由、query 改写推理等场景。

  - 训练生成器时先用自有模型家族真实 CoT 做 SFT，再引入 critic/reward model 做对抗训练或 best-of-N 筛选；工程上相当于给合成轨迹增加真实性过滤，能显著提升下游效果，成本可控。

  - 保持 teacher answer 不变、只优化中间 reasoning trace 的思路值得复用：业务中可固定黑盒模型输出的最终标注/答案，把优化重点放在解释路径、中间步骤或工具调用序列，减少跨模型风格错配带来的性能损失。

  - 评估时把 authenticity 与 correctness 分开：需要独立 judge 打分真实性，并同时看最终任务指标；避免只追求 CoT 看起来真实但实际无益。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：闭源 frontier LLM 只返回答案或摘要，不返回推理轨迹；现有通过重放加密块恢复隐藏推理的方法违反 ToS，难以长期产品化。TraceForge 采用替代方案：只使用 context 和 teacher answer，自行生成“family-native”推理轨迹，即学生模型家族自身风格。

**方法关键点**：训练分两阶段。先监督：generator 学习从家族自身的 context+answer 重建家族真实 CoT；再对抗：critic 学习判断一条推理轨迹是否像真实轨迹。应用到教师答案时，generator 按家族风格写作；critic 可选 best-of-4。独立 judge 的真实性打分：TraceForge 平均 0.68，真实轨迹 0.66，critic 四选一后 0.82（真实性而非正确率）。

**关键结果**：在五个 benchmark 上控制变量。通用任务五种语料相近；代码任务上生成推理超过 Fable 5 自身思考内容。相同 5,000 问题与相同教师答案下，HumanEval+ 最终提升 3.7 分，MBPP+ 提升 7.1 分，且 MBPP+ 领先在每个 checkpoint 都保持。作者归因于 family-native trace 与学生在同族，吸收成本低、遗忘更小。
