---
title: 'TRAPSBench: Vision-Language Models Encode but Fail to Express Epistemic Restraint'
title_zh: TRAPSBench：视觉语言模型编码了认知克制却无法表达
authors:
- Fnu Pramono
- John Cai
- Sourabh Kulkarni
affiliations:
- Meta Superintelligence Labs
arxiv_id: '2608.13167'
url: https://arxiv.org/abs/2608.13167
pdf_url: https://arxiv.org/pdf/2608.13167
published: '2026-08-13'
collected: '2026-08-16'
category: Multimodal
direction: 多模态 VLM 视觉不确定性下的克制与评估
tags:
- VLM
- abstention
- epistemic uncertainty
- benchmark
- probing
- steering
one_liner: VLM 内部能识别证据不足但输出不克制；提出 TRAPSBench 和 PECS，定位表达瓶颈
practical_value: '- 在电商/广告的视觉智能体（商品图审核、直播切片理解、图文问答）中，模型对图像遮挡/模糊常过度自信；不要只靠 prompt 或
  logit 置信度，可在 hidden states 上训轻量 probe 识别“不可判定”，作为路由/兜底信号。

  - 评估不能只看准确率：可借鉴 PECS 构造 matched pairs（同一 case 只改一个关键帧/遮挡物/文字），要求可判定时答对、不可判定时弃权；在线上可把拒答率与人工差评率、客诉率挂钩。

  - 文本不确定性比视觉不确定性更易被识别；若 Agent 含多模态输入，视觉分支应单独做 epistemic gate，避免文本线索足够时掩盖视觉证据缺失。

  - 工程化干预放在 output stage 更划算（单层 steering / refusal head / adapter），因为模型内部已有可解码的答案性信息，无需从头训练大模型；这对搜索推荐中的多模态生成式模型做安全拒答也可复用。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：视觉证据被遮挡或混乱时，VLM 应选择性弃权；但现有物理推理基准不评估证据不足下的克制能力，导致模型对“何时不知道”缺乏测试。

**方法**：构建 TRAPSBench，包含 1,404 组成对视频物理题，单处改动使结果从可判定变为不可判定；提出惩罚型认知校准分数 PECS，要求可判定时答对、不可判定时弃权，惩罚不适当回答。在 16 个 VLM（5 个家族）上评估；用 linear probe 从 hidden states 解码可回答性；通过单层 void direction 做 steering，观察弃权是否被因果诱导或抑制。

**结果**：自发克制差，最佳 PECS 仅 0.292；但 linear probe 对可答性的 AUROC 高达 0.91，说明感知不是瓶颈，瓶颈在表达；单层 steering 能因果改变弃权行为；在 Qwen、Gemma、LLaVA 三个开源家族复现；模型对文本不可能性的识别约为视觉证据缺失的 4 倍。结论指向输出阶段干预。
