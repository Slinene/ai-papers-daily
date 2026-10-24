---
title: 'DIAL: Steerable Language Models with Distilled Instruction-Adherence Levels'
title_zh: DIAL：蒸馏指令遵循等级的可操控语言模型
authors:
- Thanh Q. Tran
- John Russell Himawan
- Arun Verma
- Kiwan Wong
- Wei Xiao
- Daniela Rus
- Bryan Kian Hsiang Low
affiliations:
- School of Computing, National University of Singapore, Singapore
- Singapore-MIT Alliance for Research and Technology Centre, Singapore
- CSAIL, Massachusetts Institute of Technology, USA
- School of Electrical and Electronic Engineering, Nanyang Technological University,
  Singapore
arxiv_id: '2610.31438'
url: https://arxiv.org/abs/2610.31438
pdf_url: https://arxiv.org/pdf/2610.31438
published: '2026-10-22'
collected: '2026-10-24'
category: LLM
direction: 语言模型细粒度指令遵循控制
tags:
- instruction following
- classifier-free guidance
- steering adapter
- distillation
- controllable text generation
one_liner: 轻量steering adapter+CFG蒸馏实现LLM指令遵循程度细粒度控制，并保持高吞吐与跨指令泛化
practical_value: '- 在电商导购/客服 LLM 中，可用 DIAL 式的 steering adapter 对“回复长度/促销语气/品牌人设”做连续数值控制，避免仅靠
  prompt 导致过短或过啰嗦；同一 base LLM 可部署多档风格服务不同场景，例如售前简短答疑与售后详细说明。

  - 对 Agent 工具调用、商品属性抽取等可验证约束，可借鉴其“结合 prompting 提升 verifiable instruction following”：把价格、材质、适用人群等作为
  verifiable 约束，在生成时动态加强遵守，降低后校验和拒识成本。

  - 共享 text-conditioned classifier 的设计使得新增指令/风格无需重新拟合 adapter，便于在推荐文案、搜索广告标题、push
  文案等多任务上用一个模型快速扩展；离线训练只需 instruction+request 文本，省去大量标注 response。

  - 其 closed-form steering edit 推理开销极小，吞吐保持 96–99%，适合推荐/搜索/广告在线高 QPS 场景；可在流量侧按用户特征或场景动态选择
  adherence level，实现个性化响应风格。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

现有用户/应用对指令遵循程度有不同需求，但仅靠 prompting 无法可靠细粒度控制。DIAL 通过三方面解决：1) 细粒度控制：使用 frozen LLM 做 classifier-free guidance 生成训练信号，对 instruction adherence 不同 level 做 on-policy distillation；2) 效率：设计轻量 steering adapter，在 LLM hidden states 上训练 classifier 计算 closed-form steering edit，逐 token 依据目标 level 调整幅度，并利用 hidden state 几何保持连贯性；3) 可扩展：classifier 是 text-conditioned，共享 adapter 支持新指令，训练只需 instruction 和 request 文本，无需标注 response、外部 generator 或 judge。评估覆盖多个 LLM 家族，DIAL 在 concept expression 与 response fluency 间取得竞争平衡，concept score 随 adherence level 单调上升。还发布 SteerIF 数据集，含 98,625 条 concept、persona、verifiable、descriptive 指令；在 SteerIF 上训练后，DIAL 可细粒度控制 persona，并与 prompting 结合提升 verifiable instruction following；推理吞吐保持 base LLM 的 96–99%。
