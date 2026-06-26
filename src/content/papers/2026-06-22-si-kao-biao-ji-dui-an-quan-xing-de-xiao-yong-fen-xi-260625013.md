---
title: Do Thinking Tokens Help with Safety?
title_zh: 思考标记对安全性的效用分析
authors:
- Narutatsu Ri
- Abhishek Panigrahi
- Sanjeev Arora
affiliations:
- Princeton Language and Intelligence, Princeton University
arxiv_id: '2606.25013'
url: https://arxiv.org/abs/2606.25013
pdf_url: https://arxiv.org/pdf/2606.25013
published: '2026-06-22'
collected: '2026-06-26'
category: Reasoning
direction: 推理安全行为的早期锁定与过度拒绝
tags:
- reasoning models
- safety alignment
- thinking tokens
- deliberation
- over-refusal
- AUROC prediction
one_liner: 推理模型的安全决策在思维链早期即已锁定，首token隐藏状态可高精度预测最终拒绝/合规，现有干预导致过度拒绝
practical_value: '- 在推荐/Agent系统中引入推理模型做安全决策时，不要默认思维链能提供“深思熟虑”的安全保障；早期隐藏状态即能高准确率预测最终行为，可用轻量探头做实时安全兜底。

  - 现有安全干预（推理时干预或训练）易导致过度拒绝，在商品推荐、广告文案等场景中会降低用户体验；需重新评估拒绝边界，避免安全机制伤害业务指标。

  - 如果需要显式安全推理，可探索在推理中期加入forced rethinking或deliberation诱导机制，而不是依赖模型自发生成的思维链。

  - 从工程上看，若需对生成结果做安全过滤，基于首token表示的分类器（AUROC 0.84-0.95）可作为低延迟分流器，减少全链推理的资源消耗。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：主流推理模型通过思维链（thinking tokens）提升能力，并被认为能通过“深思熟虑”改善安全对齐。本文质疑该直觉，指出安全结果在思维早期即已确定，思维过程更像是前缀补全而非审慎修正。
**方法**：在GPT-OSS、Qwen、Olmo、Phi等开源推理模型上，分析安全相关请求的思维链。训练线性探头基于**首token隐藏状态**预测最终拒绝/合规，并研究思维过程中结果翻转的时机。同时评估推理时和训练型安全干预（如安全提示、偏好调优）对思维模式和过拒绝的影响。
**关键结果**：首token探头AUROC达0.84–0.95，平衡准确率约88%，表明最终行为在可见思维前已可预测；仅在前~20%思维内出现少量翻转，之后极少改变；文本表面74%的“深思熟虑”发生在输出分布已锁定时；现有干预方法普遍加剧过拒绝，并抑制本已稀缺的真实审慎信号。结论：当前推理模型的安全行为远非真正审慎，需设计诱导真实安全考量的方法。
