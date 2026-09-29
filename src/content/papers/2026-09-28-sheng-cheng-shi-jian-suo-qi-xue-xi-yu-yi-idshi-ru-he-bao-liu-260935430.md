---
title: Can Generative Retrievers Learn Semantic IDs Without Forgetting How to Speak?
title_zh: 生成式检索器学习语义ID时如何保留语言生成能力
authors:
- Junchen Fu
- Kleomenis Katevas
- Vandana Rajan
- Sofía Celi
- Hamed Haddadi
affiliations:
- University of Glasgow
- Brave
arxiv_id: '2609.35430'
url: https://arxiv.org/abs/2609.35430
pdf_url: https://arxiv.org/pdf/2609.35430
published: '2026-09-28'
collected: '2026-09-29'
category: RecSys
direction: 生成式检索的语义ID防遗忘训练
tags:
- Generative Retrieval
- Semantic ID
- Language Drift
- Knowledge Distillation
- On-policy Distillation
- LLM
one_liner: SpeakGR用on-policy蒸馏的正向KL正则，在SID检索微调中保留LLM文本分布，语言drift降低81-94%且检索不降
practical_value: '- 在电商/搜索的生成式召回（如物品Semantic ID或文档SID）中，仅用SID CE微调会让LLM的对话/解释能力迅速崩溃：PPL从31.69涨到53966，Top-1一致性从100%掉到0.13%。因此如果系统还需要模型回答追问、解释结果或澄清query，必须在SID阶段加语言保持损失。

  - 可复用轻量正则：准备一个prompt池（WikiText自然前缀 + 指令/QA类），每步约6条；学生以文本-only rollout生成前缀（mask SID
  logits，temperature 0.8/top-p 0.9/top-k 20），冻结base模型给出同前缀next-token分布，最小化正向KL（重新归一化到原始词表）。比offline
  replay更稳定，几乎不增加额外模型。

  - 三阶段训练（doc→SID、伪query→SID、真实query→SID）里，语言正则可在Stage1用λ0=0.1并逐步加强；若不想手动调权，可用Adaptive
  SpeakGR：对preservation KL做EMA，λ按clip(K/ε−1)乘性更新，ε取0.5–2较稳，过严的ε反而双输。

  - 工程上要单独统计SID mass：SFT-only在文本上下文里有4–26%概率分配给SID token，而SpeakGR可降到0.2–0.6%；保持前向KL的同时需mask
  SID logits，避免评估语言时SID泄漏。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
生成式检索（GR）让一个LLM通过自回归生成文档的Semantic ID来完成召回，这吸引人的是同一个模型既能检索又能生成自然语言回答、澄清问题。但标准SID微调只优化identifier生成，会剧烈扭曲LLM的文本预测分布：Qwen3-0.6B在MS MARCO上仅25步PPL就从31.69涨到6956；全文实验中SFT-only让WikiText forward KL达到5.5–13.0，Top-1一致性降到0.13–16.5%。如果一个检索器在完成召回后还要解释、追问或总结，这种语言遗忘是不可接受的。

**方法关键点**
- 提出SpeakGR，双目标联合训练：L = L_ret + L_Speak。L_ret是level-restricted CE，只在每步合法的SID token上计算；L_Speak是语言保持正则。
- L_Speak采用on-policy蒸馏：从4,096条prompt池（WikiText自然前缀 + 指令/QA）中采样，学生以纯文本方式rollout生成前缀（mask掉全部SID logits），冻结的base模型在同一前缀上给出完整词表分布，然后用正向KL匹配；梯度只回传到学生。
- 与offline replay不同，它不需要缓存固定回答；与ORBIT式的参数融合不同，它在函数空间直接约束文本分布。
- Adaptive SpeakGR只动态调整保持系数λ：对训练流上的preservation KL做EMA，按K/ε相对偏离进行乘性更新，ε为参考KL水平，含死区和clip。

**关键实验**
在MS MARCO和NQ上，用Qwen3-0.6B/1.7B和Gemma-3-1B-IT三个backbone，SID用5个256-size codebook的RQ-VAE。对比SFT-only、SpeakGR、Adaptive SpeakGR、Offline Replay和ORBIT。
- SpeakGR相比SFT-only将WikiText forward KL降低：MS MARCO 81.3–93.8%，NQ 81.2–85.2%；PPL从数千/数万回落到34.66–105.86。
- 检索基本保持或更好：Qwen3-1.7B MS MARCO上Adaptive SpeakGR R@10 0.6745，高于SFT-only 0.6696，同时FKL从11.222降到1.841；Gemma-3-1B-IT上R@10从0.6337升到0.6399而FKL从13.005降到0.775。
- Offline Replay在MS MARCO上FKL仍高达8.672，R@10仅0.5903；ORBIT强约束τ=0.007虽把FKL压到0.273但R@10崩到0.198，表明SpeakGR提供了更优的检索-保持平衡。
- Adaptive对ε不敏感：ε 0.5–2.0之间R@10 0.6324–0.6584且FKL 1.533–1.728；但ε=0.25反而双输。

**一句话**
想让LLM-based生成式检索/推荐既有SID召回又能正常说话，别只做SID CE，加上on-policy正向KL语言保持是最直接有效的做法。
