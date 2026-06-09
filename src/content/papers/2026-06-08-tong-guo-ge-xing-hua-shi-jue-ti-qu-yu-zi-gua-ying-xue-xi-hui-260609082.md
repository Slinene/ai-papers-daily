---
title: Teach Multimodal Recommendation Model to See via Personalized Visual Extraction
  and Adaptive Learning
title_zh: 通过个性化视觉提取与自适应学习教会多模态推荐模型“看见”
authors:
- Yutong Li
- Xinyi Zhang
- Ziyi Ye
- Daoguo Dong
- Yu-gang Jiang
affiliations:
- Fudan University
- Imperial College London
arxiv_id: '2606.09082'
url: https://arxiv.org/abs/2606.09082
pdf_url: https://arxiv.org/pdf/2606.09082
published: '2026-06-08'
collected: '2026-06-09'
category: RecSys
direction: 多模态序列推荐 · 视觉信号增强
tags:
- Multimodal Sequential Recommendation
- Visual Feature Learning
- Modality Imbalance
- Prompt Optimization
- VLM
- Gradient Reweighting
one_liner: 提出即插即用框架REVEAL，通过反馈引导视觉提取和自适应视觉学习提升多模态序列推荐中视觉信号的利用率。
practical_value: '- **视觉特征增强可复用**：当业务中视觉内容（商品图、短视频封面）对CTR/CVR贡献不足时，可借鉴FVE思路——用任务反馈（如最终推荐
  loss）迭代优化视觉提示词，无需微调VLM，将静态通用视觉特征转为用户偏好对齐的表示。

  - **缓解模态不平衡的轻量方案**：AVL通过计算单模态损失差距动态缩放视觉梯度，无需额外监督、不改变骨干结构。电商推荐中文本信息（标题、属性）常过强，可引入类似机制让模型更公平地学习图像、音频等弱模态。

  - **即插即用与零推理开销**：REVEAL仅在训练阶段生效，推理完全还原原始管道，非常适合业务已上线的模型做低成本升级。

  - **提示词工程与反馈循环设计**：FVE中利用VLM基于推荐错误分析优化提示词的范式，可迁移至生成式推荐（例如用LLM生成商品描述或创意文案时，以最终转化指标反馈迭代提示模板）。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：多模态序列推荐（MSR）虽同时使用文本和图像，但大量消融实验表明视觉模态贡献极小，往往只带来微弱增益甚至无增益。作者分析得出两个核心瓶颈：(1) 预训练视觉编码器（如CLIP）提取的是通用视觉特征，无法捕捉与用户偏好相关的细节（如图中复杂背景或装饰），导致视觉表示缺乏推荐任务所需的判别力；(2) 文本模态信息密度高、易学习，训练过程中占主导，严重抑制了视觉信号的有效优化。

**方法**：提出REVEAL，包含两个即插即用模块。
- **反馈引导视觉提取（FVE）**：用可学习的提示词控制冻结的VLM（如Qwen2.5-VL）提取图像特征。提示词模板结合商品元数据与用户评论高频词来实例化。训练时交替进行“视觉编码→推荐→错误分析→提示词优化”循环：固定提示词下训练推荐模型至收敛，然后用VLM根据真实交互与推荐结果生成批评文本，再依据批评文本更新提示词，从而逐步引导VLM关注用户偏好的视觉属性。整个过程VLM参数冻结，仅更新提示词文本。
- **自适应视觉学习（AVL）**：在训练推荐主网络时，每步计算纯视觉与纯文本单模态损失（通过屏蔽另一模态的零向量推理得到），定义视觉与文本损失差Δ，并用指数函数映射为缩放因子r。为了平滑，维护历史累积损失计算长期差距r̄。最终的梯度缩放系数K由当前r与历史r̄的偏差决定，若当前视觉差距大于历史平均值则放大视觉相关参数的梯度，反之缩小。该机制仅改变视觉参数梯度，不改变原推荐损失函数，也无额外监督。

**实验**：在Amazon Home、Beauty、Sports及Yelp四个数据集上实验，与SASRec、LightGCN、STOSA等传统模型以及VBPR、UniSRec、MMSR、HM4SR等SOTA多模态模型对比。以MISSRec、M3SRec、HM4SR为骨干时，REVEAL在所有数据集和指标上一致提升，例如Home上HM4SR的NDCG@10从0.0188升至0.0205（+9.04%），Sports上MISSRec的NDCG@10提升8.15%。消融实验证明FVE与AVL互补，视觉-Only条件下提升更为显著。分析显示REVEAL使视觉注意力集中于与偏好相关的区域，且未引入额外推理开销。

**一句话**：用推荐任务反馈迭代优化视觉提示词，并动态加权视觉梯度，能以零推理成本系统性提升多模态推荐中的视觉特征利用效率。
