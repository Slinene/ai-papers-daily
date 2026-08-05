---
title: 'Video-DeepResearch: Towards the Next-Generation Multimodal Deepresearch Agent'
title_zh: Video-DeepResearch：面向视频的多模态深度研究Agent框架
authors:
- Zhen Fang
- Yu Zeng
- Wenxuan Huang
- Yiming Zhao
- Shiting Huang
- Tianfei Ren
- Qi Lu
- Qingnan Ren
- Qisheng Su
- Lionel Z. Wang
affiliations:
- USTC
- Xiaohongshu Inc.
- CUHK
- The Hong Kong Polytechnic University
- ZJU
arxiv_id: '2608.03979'
url: https://arxiv.org/abs/2608.03979
pdf_url: https://arxiv.org/pdf/2608.03979
published: '2026-08-04'
collected: '2026-08-05'
category: Agent
direction: 视频深度研究Agent · 解耦感知探索
tags:
- Video-DR
- Multimodal Agent
- Tool Use
- GRPO
- Decoupled Perception-Exploration
- VIDEODR-BENCH
one_liner: 首个统一视频深度研究数据、训练与评估的框架，通过解耦感知-探索与GRPO纠正模态偏见，35B模型超越闭源SOTA
practical_value: '- **解耦感知-探索的两阶段流程可迁移至电商多模态搜索**：先强制对商品关键视觉特征（如logo、型号）进行裁剪搜索，再开放文本描述与评论检索，能规避模型直接依赖文本偏差。

  - **GRPO+拒绝采样训练范式适合训练Agent工具使用**：用稀疏奖励（正确/错误）结合组内相对优势，无需价值网络即可推动自主探索，可用于训练推荐Agent调用多个API（如商品查询、用户画像）。

  - **数据合成中防参数泄漏的筛选策略可直接复用**：生成问答对后，用无工具多次问答（Pass@4）过滤掉可凭记忆回答的样本，保证训练数据必须依赖工具，适用于构建需检索的推荐问答对。

  - **工具调用频率的诊断价值**：通过分析视觉/文本工具平均调用次数来识别Agent的模态偏见，可类比推广到推荐系统Agent监控不同召回通路的使用均衡性。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前深度研究Agent主要处理文本或静态图像，当扩展到视频流时，需要密集的时空定位与开放网络搜索联动。初步评测揭示两大瓶颈：（1）**严重模态偏见**：最强开源模型平均每任务仅执行0.10次视觉工具调用，严重依赖文本搜索；（2）**参数知识泄露**：GPT-5在几乎不调用工具的情况下即达57%准确率，表明现有基准可通过死记硬背刷分，无法反映真实工具使用能力。为此，论文提出Video-DeepResearch框架。

### 方法关键点
- **数据引擎**：筛选多域视频后，经CLIP关键帧提取、实体裁剪与视觉搜索，生成30K视频问答对，并通过无工具多次问答严格移除存在记忆泄漏的样本；采用**解耦感知-探索管线**构建7K条训练轨迹：先仅开放`Select_Keyframe`和`Crop_Search`强制跨帧多实体视觉定位，完成后再解锁文本搜索工具。
- **两阶段训练**：第一阶段SFT对齐解耦工作流，并混合7K纯文本问答实例增强搜索能力；第二阶段用GRPO进行强化学习，在2K中等难度样本上做组内相对优势优化，只对正确答案给予稀疏奖励，并对格式违规轨迹的梯度进行降采样。
- **基准构建**：推出VIDEODR-BENCH，200个多跳VQA实例，覆盖知识、娱乐、日常等6个域，每个问题均需视觉搜索与外部知识推理，并通过人机协同标注保证质量。

### 关键结果
- **Video-DeepResearch-35B-A3B**（基于Qwen3.5-35B-A3B）在VIDEODR-BENCH上平均准确率64.0%，超出Claude-4.5-Sonnet（59.0%）5个百分点，显著优于GPT-5（52.5%）和Gemini 2.5 Pro（57.5%）。
- **30B-A3B版本**达到59.3%，与Claude-4.5-Sonnet持平，较其基模型Qwen3-VL-30B-A3B提升+18.8个百分点。
- **工具调用行为根本转变**：视觉工具平均调用次数从基线的0.10升至2.33，文本工具从1.27升至4.24，表明训练有效注入主动多模态探索策略。
- 消融实验证实7K视觉轨迹SFT带来+12.5%涨幅，混合文本SFT再+3.8%，RL额外+2.5%，三者缺一不可。

> **一句话**：解耦感知与探索、分阶段强制使用视觉工具，再辅以GRPO自主探索，是将Agent从“记忆回测”拉向“主动验证”的关键范式。
