---
title: 'MemUse: Moving Memory Evaluation from Direct QA to Natural Integration in
  Long-Term Human-AI Conversation'
title_zh: 长期人机对话记忆评估：从直接追问到自然整合的 MemUse
authors:
- Ryuichi Sumida
- Koji Inoue
- Tatsuya Kawahara
affiliations:
- Graduate School of Informatics, Kyoto University
arxiv_id: '2608.24189'
url: https://arxiv.org/abs/2608.24189
pdf_url: https://arxiv.org/pdf/2608.24189
published: '2026-08-24'
collected: '2026-08-27'
category: Eval
direction: LLM 长期对话记忆评估
tags:
- Memory
- LLM
- Evaluation
- Natural Integration
- Conversational AI
- User Satisfaction
one_liner: 发现直接问答记忆准确率与用户满意度无关，提出自然整合评估基准 MemUse，揭示 71 点巨大差距
practical_value: '- 在电商导购/客服 Agent 中，长期记忆评估不要只看「直接提问能否答对」（Direct QA），这类指标与用户满意度可能无相关；应在真实对话流中挖掘「记忆时刻」，评估模型是否在自然回复中主动且恰当地融入历史信息。

  - 建立集成感知的自动化评估：对每个记忆时刻，用 LLM-as-judge 检查回复是否自然引用了相关历史事实（而不是仅仅能否回答事实问题）；该指标与满意度相关性更强，可用于回归测试。

  - 检索增强记忆系统往往只优化 top-k 准确率，但可能存在高检索准确、低实际使用的问题；可通过「引用率」等下游指标暴露该 gap，指导改进方向：不仅提升检索命中，还要提升相关性检测和上下文融合能力。

  - 直接 QA 准确率从 19.7% 到 70.1% 变化，但满意度无显著差异，提示团队在迭代记忆模块时不要过度依赖离线 QA 基准，要做用户满意度 A/B 测试或应用内行为指标。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**  
长期对话 LLM 的记忆评估通常采用直接事实问答（Direct QA），即考察模型能否从历史对话中回忆出某个事实。但该假设未经检验：召回能力是否能代表真实对话中的记忆使用？

**方法关键点**  
在 4 个月、40 名用户、1872 个会话、7 种记忆条件下的真实部署中，测量 Direct QA 准确率与用户满意度；引入 MemUse，从真实用户触发的记忆时刻（memory moments）构建评测集，采用自然整合（Natural Integration）视角评分：不只是能否答对，而是能否在自然对话中检测相关性并恰当地融入历史信息。

**关键结果数字**  
Direct QA 准确率在 7 种条件间从 19.7% 到 70.1% 变化，但用户满意度没有显著差异；固定模型和上下文，Direct QA 78.8% 的系统在对话中仅引用了 7.9% 的事实，差距 71 点；在这些真实记忆时刻中，自然整合与满意度相关，而 Direct QA 不相关。语料和评测集已开源。
