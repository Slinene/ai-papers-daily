---
title: 'CURATOR: Scalable Fine-grained Evidence Selection for Retrieval-Augmented
  Generation using Decision Models'
title_zh: CURATOR：基于决策模型的可扩展细粒度证据选择用于检索增强生成
authors:
- Shib Dasgupta
- Bandish Parikh
- Rashmi Gangadharaiah
affiliations:
- AWS AI Labs
arxiv_id: '2611.16366'
url: https://arxiv.org/abs/2611.16366
pdf_url: https://arxiv.org/pdf/2611.16366
published: '2026-11-12'
collected: '2026-11-13'
category: RAG
direction: RAG 细粒度证据选择与上下文压缩
tags:
- RAG
- Evidence Selection
- Decision Model
- LoRA
- Token Budget
- Joint Inference
one_liner: 用联合决策模型做细粒度证据选择，通过可变候选集训练和类别平衡损失提升大规模候选下的判别能力，同时保持高效联合推理
practical_value: '- **共享上下文联合打分替代逐条 rerank**：在电商搜索/推荐的多路召回后处理中，可以将候选段落拆成 sentence/span
  级别的证据单元，用一个轻量决策模型在单次推理中同时给所有候选 span 打分，避免对每个候选重复编码完整上下文；CURATOR 实测比 separate context-aware
  scoring 快 21.7×、输入 token 少 25.7×，适合线上低延迟场景。

  - **可变候选集 + 类别平衡损失训练**：业务数据里正样本（相关证据）占比通常极低，可以直接借鉴其训练策略：构造不同 K（8~128）的候选集，固定正样本数或按自然分布采样，让模型适应稀疏证据；损失按类别取平均，避免全被负样本主导，能显著提升低
  token 预算下的 recall。

  - **LoRA 只调 8 层 full-attention + decision readout**：在 4.5B 决策模型上只更新 3.8M 参数即可完成专项能力注入，几乎不增加部署成本；对于已有通用决策模型或
  reranker，可以低成本 fine-tune 到自家垂直域（商品知识、活动规则等），无需全量微调。

  - **通用任务回放防遗忘**：微调专用任务时用 40% 的通用决策样本进行 replay + 蒸馏，保证模型原有分类/打分能力不退化，适合需要同时保留通用排序和垂直证据选择的搜索/广告团队复用。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
RAG 把整段检索文本喂给 LLM，但真正有用的证据往往只有少数 span，大量无关信息既浪费 token 又干扰生成，尤其在 agentic 工作流中上下文窗口稀缺。细粒度证据选择可显著压缩输入，但逐候选独立打分缺乏上下文感知（多跳证据需要联合判断），而逐候选带全上下文打分计算成本过高。联合决策模型可以在共享推理中同时给多个候选打分，效率高，但预训练模型在候选数量增大时判别能力严重下降（图2）。

## 方法关键点
- **CURATOR 基于 pplx-decider-flash-v1.2 联合决策模型**，用 LoRA 仅微调 8 层 full-attention 的 QKV/O 投影和 decision readout，约 3.8M 参数。
- **可变候选集训练**：从 QAMPARI、HotpotQA、2WikiMultiHopQA 构造 K∈{8,16,32,64,128} 的候选 span 集，混合三种采样策略（natural / fixed-positive / gold-included），覆盖不同证据密度。
- **类别平衡联合证据监督**：损失按正负类别分别取平均，解决正样本稀疏问题；不确定标签不参与训练。
- **通用决策任务回放**：40% 训练样本来自通用分类/多选/打分任务，并用蒸馏和 CE 防止遗忘。

## 关键实验
- 在 QAMPARI（多答案 QA）上，CURATOR 证据 recall 在 B=512/1024/2048 分别达到 36.6%/54.7%/67.8%，比原联合决策模型高 17～33%，比 separate context-aware scoring 高 9～16%，且推理成本与原联合相当（快 21.7×、输入 token 少 25.7×）。
- 泛化到未见域：FEVEROUS（事实核查）、MultiHiertt（金融文档）、CUAD（法律合同）上证据 recall 和 complete-set coverage 均显著提升，且在低预算下优势更大。
- 下游 RAG：在 MuSiQue 和 MultiHiertt 上，B=128 时准确率相对最强 baseline 分别提升 20.9% 和 14.0%。
- 可伸缩性：CURATOR 在 K 从 8 增大到 256 时 AUROC 几乎不降，而原联合模型从 0.785 降至 0.683（QAMPARI）。

最值得记住的一句话：**联合决策模型能高效做细粒度证据选择，但必须用可变规模候选集和类别平衡监督专门训练，才能在大候选集上保持判别力。**
