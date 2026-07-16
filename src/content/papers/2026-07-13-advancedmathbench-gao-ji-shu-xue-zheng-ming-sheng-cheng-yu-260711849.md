---
title: 'AdvancedMathBench: A Benchmark Suite for Advanced Mathematical Proof Generation
  and Verification'
title_zh: AdvancedMathBench：高级数学证明生成与验证基准套件
authors:
- Lingkai Kong
- Zijian Wu
- Yuzhe Gu
- Haiteng Zhao
- Wenyong Huang
- Shuang Sun
- Zhicheng Xiong
- Xiaotian Zhang
- Shuya Zhao
- Yan Wang
affiliations:
- Shanghai AI Laboratory
- Shanghai Jiao Tong University
- MMLab, The Chinese University of Hong Kong
- Great Bay University
arxiv_id: '2607.11849'
url: https://arxiv.org/abs/2607.11849
pdf_url: https://arxiv.org/pdf/2607.11849
published: '2026-07-13'
collected: '2026-07-16'
category: Other
direction: 数学推理基准与自动验证
tags:
- mathematical reasoning
- proof generation
- proof verification
- automatic evaluation
- LLM benchmark
one_liner: 构建首个面向高级数学证明的生成-验证双任务基准，揭示前沿LLM在严谨推理上的严重瓶颈
practical_value: '- 主要在数学推理领域有学术贡献，对电商、推荐、Agent等业务场景的可直接借鉴点有限。

  - 自动验证管道的设计思路（结合细粒度错误判定与人类标注对齐）可迁移至任意需评估模型推理质量的场景，例如推荐解释生成的可信度自动评价、Agent规划步骤的正确性校验。

  - 论文揭示的“错误检测能力弱”在推荐Agent中同样关键：当模型在长链任务中自行纠错时，细粒度判定逻辑可下沉为CoT过程的在线校验器。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：当前LLM在高中奥数级别数学上表现强劲，但在高级数学（本科至博士资格考试水平）上的能力未知。已有基准存在学科覆盖面窄、评估仅依赖最终答案正确性或粗糙判断，无法评价证明过程的严谨性。

**方法**：提出了AdvancedMathBench，核心包含两个子基准：
- **ProverBench**：包含296道本科和博士资格考试级别数学问题，用于评估证明生成能力。
- 配套的**自动验证管道**：在大规模专家标注上训练，输出正确性判定和细粒度错误类型评估，与人类专家具有高一致性。
- **VerifierBench**：888条模型生成的证明轨迹，附有专家真实标签，评估模型判断证明有效性的能力及验证理由的合理性。

**结果**：前沿模型仍面临巨大挑战。证明生成：最好模型GPT-5.5-xhigh在本科子集（UGD）上仅达75.8%，博士资格考试子集（QE）上仅66.1%。证明验证：最佳模型Balanced F1仅65.1，且真阴率普遍偏低，表明关键错误检测是主要瓶颈。
