---
title: 'ANCHOR: Agentic Noise Creation Framework for Human Simulation and Denoising
  Recommendation'
title_zh: ANCHOR：驱动噪声生成与监督式推荐去噪的多智能体框架
authors:
- Xiangming Li
- Hua Chu
- Chengyu Feng
- Jianan Li
- Yangtao Zhou
affiliations:
- Xidian University
- Shanghai Fairyland Software Co.,Ltd.
arxiv_id: '2606.05621'
url: https://arxiv.org/abs/2606.05621
pdf_url: https://arxiv.org/pdf/2606.05621
published: '2026-06-04'
collected: '2026-06-06'
category: RecSys
direction: 推荐去噪 · Agentic 噪声生成 · 监督学习范式
tags:
- Recommendation Denoising
- Agent-based Simulation
- LLM-as-User
- Supervised Denoising
- Implicit Feedback
- Creator-Recognizer
one_liner: 将推荐去噪从无监督启发式问题重构为主动创造噪声标签并训练识别器的监督学习范式
practical_value: '- **用LLM Agent模拟噪声生成标签进行监督去噪**：在电商推荐中，点击、加购等隐式反馈经常混杂误点、从众、标题党等噪声，可以借鉴ANCHOR思路，用LLM模拟用户在这些非偏好场景下的行为，生成带标签的噪声数据，然后训练一个二分类器（如MLP）来识别真实数据中的噪声，提升训练数据质量。

  - **边界邻近噪声生成机制可作为难分负样本挖掘方案**：论文提出的对抗式迭代精炼（creator生成难分样本，recognizer反馈）可复用到电商推荐中的困难负样本生成，用于提升模型对易混淆商品的辨别能力，类似GAN但无需训练LLM参数，通过prompt和记忆即可驱动。

  - **语义+协同信号融合的识别器设计**：ANCHOR的去噪识别器同时使用协同ID嵌入和文本语义嵌入，这启示我们在设计去噪或内容理解模块时，不应只依赖行为序列，而要利用商品标题、描述等多模态特征，提升对隐蔽噪声的识别能力。

  - **可重用去噪模块降低推理成本**：训练好的识别器可离线应用，无需每次请求都调用LLM，这在工程上可行，适合在线serving前对训练数据进行清洗，提升模型鲁棒性。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：推荐系统大量依赖隐式反馈（点击、购买），但其中充满非偏好驱动的噪声（误点、好奇、标题吸引、从众、位置偏差）。现有去噪方法要么依赖昂贵的外部信息，要么基于不可靠的人工启发式规则，本质是缺标签的无监督问题，难以准确学习噪声模式。本文提出根本性转变：与其被动推断噪声，不如主动模拟噪声生成过程，为去噪任务构造监督标签，将推荐去噪从启发式过滤重塑为监督学习。

**方法**：ANCHOR实例化了一个Creation-Recognition范式，包含三部分：
1. **Agent用户模拟驱动噪声生成**：基于LLM构建用户画像，通过推荐模型提供候选列表，模拟五种典型非偏好行为——误点、好奇心驱动、标题偏差、流行偏差、位置偏差，生成带标签的“out-of-preference”噪声交互。
2. **创作者-识别者迭代边界精炼**：为生成偏好边界附近的难分噪声，设计creator（LLM）与recognizer（噪声识别器）的迭代交互：creator根据识别器反馈不断生成更具迷惑性的样本，通过prompt反思和记忆更新提升噪声难度，为识别器提供更具信息量的监督信号。
3. **可重用噪声识别器**：基于上述噪声标签训练一个结合协同信号（LightGCN产生ID嵌入）和语义表示（预训练语言模型编码用户画像与商品文本）的识别器，利用二分类交叉熵和BPR损失联合优化，最终应用于真实交互数据去噪，净化后的数据用于训练推荐模型。

**实验**：在DBbook2014、Book-Crossing、MovieLens-1M三个数据集上，以GMF和LightGCN为骨干，与T-CE、DeCA、BOD、DCF、LLaRD等SOTA去噪方法对比，ANCHOR在所有指标上显著领先。例如在LightGCN下，DBbook2014的Recall@10从0.2393提升至0.2512，MovieLens-1M上从0.1903提升至0.2015。消融实验验证了各组件（噪声生成、边界精炼、语义引导、BPR协同约束）的必要性；鲁棒性分析表明，在训练数据注入5%~20%额外噪声时，ANCHOR性能降幅明显小于baseline，显示出对高噪声环境的强鲁棒性。

**核心洞见**：*“预测噪声的最好方式是创造它。”* 通过主动模拟噪声行为并构造监督信号，ANCHOR从根本上突破了推荐去噪缺乏标签的困局，实现了数据高效且模型无关的去噪。
