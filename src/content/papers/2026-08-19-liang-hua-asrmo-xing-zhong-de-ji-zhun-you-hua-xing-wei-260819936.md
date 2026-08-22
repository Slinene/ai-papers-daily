---
title: Towards Quantifying Benchmark Optimization in ASR Models
title_zh: 量化ASR模型中的基准优化行为
authors:
- Theo Lebryk
- David Ayllon
- Alice Baird
- Jakub Piotr Cłapa
- Jens Madsen
- Panagiotis Tzirakis
affiliations:
- Hume AI Research
arxiv_id: '2608.19936'
url: https://arxiv.org/abs/2608.19936
pdf_url: https://arxiv.org/pdf/2608.19936
published: '2026-08-19'
collected: '2026-08-22'
category: Eval
direction: 基准过拟合评估 · 行为探针
tags:
- benchmark overfitting
- evaluation
- probing
- causal intervention
- ASR
- shortcut learning
one_liner: 用三类行为探针发现高分开源ASR模型在音频欠定时仍输出基准参考文本，可通过低秩引导操控
practical_value: '- 在搜索推荐场景中，公开评测集同样存在被离线指标过拟合的风险。可直接借鉴其三类探针思路：构造用户意图/行为欠定的样本（如历史稀疏、上下文矛盾、文本模糊），检查模型是否偏向输出头部商品、高频query或模板文案，而不是忠实于可用信号

  - 用机制探针验证模型是否依赖窄特征（如位置、曝光次数、特定品牌词）来提升离线指标，若存在可通过低秩线性引导（类似activation steering）或对输入追加简单信号进行因果操纵，说明模型学到的是捷径而非可泛化能力

  - 对LLM Agent或生成式推荐做上线前评估时，加入参考不一致、掩码关键信息、拼写/表述切换等对抗性探针，量化模型在信息不确定时是否“背答案”，可作为离线A/B前的诊断关卡

  - 结论提醒：WER/AUC等指标提升可能来自对特定评测分布的条件化行为，而非真实能力提升。业务迭代中应定期注入分布外或反事实测试集，防止基准优化误导模型选型'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：公开基准的指标提升可能来自对基准特定偏差的利用，而非真实泛化能力，导致基准性能与真实场景表现持续脱节。需要定量识别“benchmark optimization”现象。

**方法**：聚焦音频欠定参考转录的场景，设计三类行为探针：① reference disagreement——音频与参考文本矛盾；② masked-number recovery——数字被掩蔽；③ orthographic switching——拼写/写法切换。观察模型是否仍输出基准参考文本中的精确片段。再使用多种机制探针分析模型内部激活，定位其是否响应窄声学线索而覆盖忠实音频表征。进一步通过低秩线性引导或在片段末尾简单拼接音频进行因果操纵。

**关键结果**：得分最高的开源ASR模型在音频矛盾、掩蔽或模糊时，仍会逐字输出基准参考文本区间；机制探针显示模型采用基准优化策略而非忠实转写；该行为可通过低秩线性引导或简单追加音频被因果操控。结论表明，高分数模型的基准表现被基准条件行为抬高，并不反映通用转写能力的提升。
