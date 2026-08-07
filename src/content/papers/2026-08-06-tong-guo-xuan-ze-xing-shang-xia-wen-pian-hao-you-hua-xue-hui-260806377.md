---
title: Learning When to Trust via Selective Context Preference Optimization
title_zh: 通过选择性上下文偏好优化学会何时信任
authors:
- Xian Sun
- Wei Chow
- Yingshuo Wang
- Junhao Liu
- Wei Gao
- Qing Wu
- Lingdong Kong
affiliations:
- Duke University
- National University of Singapore
- UC Berkeley
- UC Irvine
- Northeastern University
arxiv_id: '2608.06377'
url: https://arxiv.org/abs/2608.06377
pdf_url: https://arxiv.org/pdf/2608.06377
published: '2026-08-06'
collected: '2026-08-07'
category: Training
direction: 选择性信任训练 · DPO偏好优化
tags:
- Selective Trust
- DPO
- MIST
- SC2W
- Context Robustness
- LLM Training
one_liner: 提出选择性信任基准 MIST 与平衡 DPO 训练 SCOPE，使 LLM 在利用上下文时抵御误导信号
practical_value: '- **构建多条件评估集**：在 Agent 或 RAG 流程中，可借鉴 MIST 的四条件（干净、误导、正确上下文、无关上下文）设计验证集，评估模型对检索/注入上下文的「选择性信任」能力，避免只测鲁棒性或只测利用率。

  - **DPO 训练数据构造**：利用 clean-correct/misleading-wrong 失败案例构造偏好对，且平衡四种条件（而非仅误导样本），可改善模型在不牺牲正确上下文利用率的前提下降低误导敏感度，适用于微调客服对话、搜索总结等易受噪声上下文影响的
  Agent。

  - **SC2W 指标应用**：在推荐解释生成或购物助手场景，可用 SC2W（干净正确被误导翻转为错误的比率）作为核心监控指标，重点检测模型在面对错误产品描述、误导性评论时是否保持正确。

  - **工程实现轻量**：SCOPE 仅需标准 DPO 训练，无需额外模型结构或强化学习，可直接在现有微调流程中应用，适合业务快速实验。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：LLM 常依据外部上下文回答问题，但单条误导信号就可能将原本正确的答案翻转错误。单纯训练模型抵抗误导会导致忽略所有上下文，无法利用可信信息。现有基准只测单一上下文，无法评估模型的选择性信任能力。

**方法关键点**：
- 提出 **MIST 基准**：人工标注推理题，每条题在四种匹配条件下呈现（无上下文、误导上下文、正确上下文、无关上下文），并引入成对指标 **SC2W**（干净正确→误导后错误的翻转率）。
- 提出 **SCOPE 训练**：挖掘干净-正确/误导-错误的失败样本构建偏好对，在四种条件上均衡采样，用标准 DPO 优化，而非仅在误导样本上训练。
- 平衡目标：降低 SC2W，同时保持正确上下文下的准确率不降。

**关键结果**：在多个开源模型上，SCOPE 大幅降低 SC2W（例如 Llama-3-8B 的 SC2W 从 28.7% 降至 10.3%），并在正确上下文和无关上下文下保持甚至提升准确率。相比之下，仅用误导数据训练（抗干扰）虽降低 SC2W 但损害正常利用率。
