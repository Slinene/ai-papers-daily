---
title: 'The Riddle Riddle: Testing Flexible Reasoning in Large Language Models and
  Humans'
title_zh: 谜中谜：测试大语言模型与人类的灵活推理
authors:
- Bella Fascendini
- Kathryn McGregor
- Max D. Gupta
- Thomas L. Griffiths
affiliations:
- Princeton University
arxiv_id: '2606.27103'
url: https://arxiv.org/abs/2606.27103
pdf_url: https://arxiv.org/pdf/2606.27103
published: '2026-06-25'
collected: '2026-06-27'
category: Reasoning
direction: LLM 推理 vs 模式匹配评估
tags:
- flexible reasoning
- LLM evaluation
- riddle
- pattern matching
- cognitive bias
- strategy selection
one_liner: 用“谜中谜”范式揭示LLM擅长模式匹配而非灵活推理，在需字面理解时仍过度使用创意策略
practical_value: '- 在构建需要灵活推理的 Agent（如电商导购机器人）时，LLM 可能因输入表面形式（如比喻、对仗）而错误触发“创意模式”，可仿照“谜中谜”构造对抗测试集，评估
  Agent 能否根据内容切换推理策略。

  - 当用 LLM 做查询理解或推荐文案生成时，若输入带有谜语式结构，模型可能过度解读，建议在 prompt 中明确要求按字面理解，或提供 few-shot 示例引导正确推理。

  - 该范式提示：评估 LLM 推理能力不能只看标准基准，应设计能区分记忆检索与灵活推理的测试，对依赖 LLM 做决策的推荐系统尤为重要。

  - 人类倾向字面解读，LLM 倾向过度创意，可在人机协作中结合两者优势，如让 LLM 生成候选，人类过滤过度创意结果，提升推理准确性。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：人类能根据问题需求灵活调整推理策略，但大语言模型（LLM）在众多推理任务上的出色表现，究竟是源于灵活推理还是训练数据中的模式匹配，尚不清晰。为此，论文提出“谜中谜”（riddle riddle）范式：将经典谜题改写，使其答案只需字面理解，但保留谜语般的形式。如果 LLM 依赖于表面特征（如形式），会继续使用创意推理，而无法根据内容灵活切换策略。

**方法**：在两项实验中，测试了9个先进 LLM（如 GPT‑4、Claude 等）和100名人类被试。材料包含50个经典谜题（需要创意推理）和50个谜中谜（只需字面理解，但形式酷似谜题）。核心指标是在两类题目上的准确率和错误类型（过度创意 vs. 过度字面）。

**关键结果**：LLM 在经典谜题上准确率高达84.9%，但在谜中谜上骤降至50.7%；人类则相反，谜中谜准确率80.5%，经典谜题仅50.5%。错误分析表明，LLM 在谜中谜上的错误中90.8%是由于不当使用创意推理，而人类在经典谜题上的错误只有57.6%是因过度字面推理。这说明 LLM 的强纠错更多源于对谜语结构表层的记忆检索，而非真正的策略选择。论文警示：若无专门设计，很容易将 LLM 看似推理的输出等同于真正的推理。
