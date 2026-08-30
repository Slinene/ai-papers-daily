---
title: 'Prediction of Prediction (PoP): Inter-Layer Activation Fusion for Single-Pass
  Hallucination Detection in Large Language Models'
title_zh: 预测之预测：层间激活融合实现LLM单遍幻觉检测
authors:
- Himal Badu
arxiv_id: '2608.27165'
url: https://arxiv.org/abs/2608.27165
pdf_url: https://arxiv.org/pdf/2608.27165
published: '2026-08-27'
collected: '2026-08-30'
category: LLM
direction: LLM幻觉检测·隐藏层动态
tags:
- hallucination detection
- hidden states
- layer dynamics
- uncertainty estimation
- efficient inference
one_liner: 提出PoP机制，融合跨层隐藏状态捕获层转移不确定性，在单次前向中检测LLM事实错误
practical_value: '- 对LLM生成的推荐文案、商品描述、搜索query等文本，可在单次前向中提取跨层隐藏状态作为事实置信度信号，用于低成本过滤或风险分级，弥补输出token概率的不足。

  - PoP的<1.2%延迟开销适合在线生成式推荐系统，可在不增加额外采样的情况下对生成结果做实时健康度评估，触发人工审核或降级。

  - 该机制在TruthfulQA上AUROC仅75.5%，且缺乏跨域验证，在电商场景落地前需用自有业务数据验证检测精度与阈值稳定性。

  - 层间转移不确定性可作为特征加入现有质量/风控模型，特别针对商品属性、价格、活动规则等事实性易错点。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**  
LLM在生成事实性错误时往往仍保持高解码置信度，输出层不确定性指标（如token熵、序列困惑度）无法可靠识别幻觉，而多样本验证带来显著内存和延迟开销。  

**方法**  
提出Prediction of Prediction (PoP)，在单次前向传播中捕获层间激活转移的不确定性，通过跨深度融合中间隐藏表示构建事实错误信号，无需额外生成pass，不改变模型架构。  

**结果**  
在TruthfulQA基准上，PoP对事实正确性分类取得75.5% AUROC，运行时延迟增加小于1.2%，且零额外解码调用。实验基于自回归Transformer骨干网络，结果来自作者验证的实现。
