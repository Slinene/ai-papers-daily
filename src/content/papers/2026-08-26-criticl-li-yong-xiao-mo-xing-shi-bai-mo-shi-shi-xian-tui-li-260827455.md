---
title: 'CritICL: Inference-Time Weak-to-Strong Generalization from Small Language
  Model Failure Modes'
title_zh: CritICL：利用小模型失败模式实现推理时弱到强泛化
authors:
- Yufan Wu
- Yinghui He
- Zhengyi Hu
- Lang Wei
- Ruichen Li
- Qifan Yang
- Ting Zhu
affiliations:
- The Ohio State University
- Princeton University
arxiv_id: '2608.27455'
url: https://arxiv.org/abs/2608.27455
pdf_url: https://arxiv.org/pdf/2608.27455
published: '2026-08-26'
collected: '2026-08-29'
category: Reasoning
direction: 推理时弱到强泛化 · 失败模式检索
tags:
- Weak-to-Strong Generalization
- In-Context Learning
- Failure Mode
- Test-Time Scaling
- Mathematical Reasoning
- LLM
one_liner: 用同家族弱模型失败模式构建离线批判库，推理时按失败模式检索注入大模型，单次生成匹配多次采样性能
practical_value: '- 建立业务侧“失败模式 CritBank”：用较小/便宜的模型或线上历史 badcase 生成错误响应，由强 LLM 离线标注失败类型和纠正说明；在
  query 理解、商品属性抽取、推荐理由生成等任务中，把失败模式预测或静态画像作为检索键，从库中取示例注入 prompt，减少在线多路采样成本。

  - 检索键从语义相似度改为失败模式/错误类型：实验显示比随机、固定、语义相似度检索高 4-6 个点；推荐场景可先预测用户/物品/请求的易错标签，再召回对应纠错示例，比只找相似
  case 更直接规避模型系统性错误。

  - 同模型家族多尺度失败分布稳定（Spearman 0.88-0.91），聚合多个弱模型比单一弱模型更贴近大模型；在模型升级或蒸馏时，可以用同架构旧小模型收集错误，指导新大模型上线前的
  prompt 防御性设计或 few-shot 示例库构建。

  - CritICL-static 只需单次生成即可达到 Consistency@5 效果，总 token 远低于 self-reflection 和 LLM-as-judge；适合线上延迟敏感、需要快速推理的
  Agent 链路，也说明离线构建错误知识库比在线多路验证更划算。'
score: 8
source: huggingface-daily
depth: full_pdf
---

动机：推理时扩展（如 self-consistency、self-reflection、LLM-as-judge）提升 LLM 推理，但依赖多次生成或外部验证，成本高；弱到强方法虽利用弱模型在线监督，仍增加推理开销且未充分利用失败的系统性。观察到同家族模型失败模式分布跨尺度一致（Qwen 聚合 Spearman 0.91，Llama 0.88），因此将小模型错误当作可复用信号，而不是一次性噪声。

方法关键点：
- CritBank 构建：从 GSM8K+MATH 抽取 15k 训练问题，用 Qwen2.5-1.5B/3B/7B 或 Llama 小模型 CoT 生成 5 条响应；保留错误响应，由 GPT-4o-mini 生成最多 5 个失败模式标签并聚类为细粒度分类，同时生成自然语言 critique。
- 推理时两种变体：CritICL-dynamic 让目标模型先预测输入最可能的失败模式（≤5），据此从 CritBank 检索相关 critique；CritICL-static 基于同家族弱模型聚合的全局失败模式画像，检索主导失败模式对应的示例，输入无关且更稳定。
- 检索键是失败模式，不是语义相似度；最多检索 5 个示例注入 prompt。

实验结果：
- Qwen2.5-72B 上 CritICL-static overall 59.2%，超过 Consistency@5 59.0% 和 LLM-as-Judge 58.5%；Qwen2.5-32B 上 49.8% 超过 Consistency@7 49.5%。
- 推理成本：CritICL-static 仅 1 次生成，MATH 平均总 token 3768，显著低于 Consistency@5 4814、LLM-as-Judge 6465、Self-Reflection 7533。
- 消融：失败模式检索比随机/固定/语义检索在 AMC23/AIME 提升 4-6 点；标注稳定性 GPT-4o-mini 与人类 F1 0.82，接近人-人 0.86。
- 扩展：在化学/生物领域有效；同家族迁移强于跨家族，跨域也有一定迁移。

最值得记住的一句话：弱模型的失败模式是可离线复用、跨尺度稳定的推理先验，按失败模式检索纠错示例，能在单次生成内逼近多次采样精度。
