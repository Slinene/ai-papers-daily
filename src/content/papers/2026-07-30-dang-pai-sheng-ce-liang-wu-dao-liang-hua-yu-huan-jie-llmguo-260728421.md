---
title: 'When Derived Measurements Mislead: Quantifying and Mitigating LLM Over-Trust
  with Privileged-Modality Reliability Evidence'
title_zh: 当派生测量误导：量化与缓解LLM过度信任的可靠性框架
authors:
- Zongheng Guo
- Tao Chen
- Tianli Li
- Mingzhe Cui
- Yang Jiao
- Lei Xie
- Yi Pan
- Xiao Hu
- Manuela Ferrario
affiliations:
- Politecnico di Milano
- Zhejiang University
- Chinese Academy of Sciences
- Emory University
- China-Japan Friendship Hospital
arxiv_id: '2607.28421'
url: https://arxiv.org/abs/2607.28421
pdf_url: https://arxiv.org/pdf/2607.28421
published: '2026-07-30'
collected: '2026-08-02'
category: LLM
direction: LLM过度信任评估与缓解
tags:
- DFOT
- Privileged Distillation
- LLM Over-Trust
- Reliability
- Evaluation
one_liner: 定义衍生特征过度信任(DFOT)问题，提出特权模态蒸馏缓解LLM错误信任，在医学时序数据上修复误差率提升1.82-6.69个百分点
practical_value: '- 推荐系统中派生特征（预估CTR、用户标签）进入LLM决策时，可借鉴DFOT框架设计冲突检测与可靠性声明生成，监控COTR/CIR

  - 利用离线高能特征（如真实转化标签）作为特权信息蒸馏到在线可靠性模型，校准LLM对派生特征的信任度

  - 构建类似D1/D2的逻辑测试集，检验LLM在矛盾噪声上下文下是否会错误接受/拒绝推荐理由

  - 对Agent工具调用返回的派生数据，可引入证据特定修复边界(ESRM)评估，防止错误向上传播'
score: 6
source: arxiv-cs.AI
depth: abstract
---

**动机**：LLM正越来越多地将派生测量（如预估分数、传感器衍生指标）直接作为事实使用，但这些测量的有效性高度依赖实例，LLM容易赋予其不当的确定度，即衍生特征过度信任（DFOT）。

**方法关键点**：
- 以生理信号（PPG心率估计）为实例，定义两个测试场景：D1测试LLM在ECG（金标准）矛盾下是否仍相信派生测量，D2测试LLM在误导性病史下拒绝原本可靠的派生测量。
- 提出五个评估指标：冲突过度信任率(COTR)、上下文诱导错误率(CIR)、正确修复率(CRR)、证据特定修复边界(ESRM)、效用损害率(UHR)。
- 缓解方案：利用特权模态蒸馏，用ECG（推理时不可见）训练可靠性生成器，蒸馏到仅用PPG的模型，生成可靠性证据引导LLM校准信任。

**关键结果**：在50,000对训练、187名患者测试集上，基线蒸馏方法在四个修复与特异性指标上提升1.82–6.69个百分点（所有配对置信区间排除0），UHR轻微上升0.67个百分点（95% CI [-0.4, +1.7]），表明总体纠错收益显著，过度验证代价可控。
