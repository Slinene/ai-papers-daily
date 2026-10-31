---
title: 'Youtu-Parsing-Omni: One Encoder, One Schema, All Modalities'
title_zh: Youtu-Parsing-Omni：单编码器、统一模式的全模态解析
authors:
- Yunhang Shen
- Zhangquan Chen
- Xiaotian Li
- Zhongpeng Cai
- Qing Zhou
- Zekai Zhang
- Kun Zhang
- Zezhong Wu
- Jian Hu
- Haihan Gao
affiliations:
- Tencent Youtu
arxiv_id: '2610.39301'
url: https://arxiv.org/abs/2610.39301
pdf_url: https://arxiv.org/pdf/2610.39301
published: '2026-10-28'
collected: '2026-10-31'
category: Multimodal
direction: 全模态文档解析 · 统一 schema 与自进化训练
tags:
- Multimodal Parsing
- Unified Schema
- Self-Evolving Training
- Agent Perception
- OCR
one_liner: 提出一个编码器与统一 schema 的全模态解析器，将文档、图像、音频、视频解析为带时空定位的结构化记录
practical_value: '- **统一 token-role schema 可减少多任务解析头**：在电商内容理解中，商品主图、详情页、短视频封面、直播切片往往需要多套解析模型。将不同任务输出统一为带角色标签的
  token 序列（如文本、坐标、时间戳），能让 Agent 直接读取并定位证据，降低格式转换和后期拼装成本。

  - **OSAD 自进化蒸馏适合标注稀缺场景**：电商属性抽取、广告素材审核等场景标注成本高、数据漂移快。可先用少量种子数据训练，再用自身 rollout 与参考条件副本做
  token 级蒸馏，迭代刷新参考模型，形成“模型生成—自我蒸馏—权重刷新”闭环，减少对新增人工标注的依赖。

  - **用预训练 LLM 初始化编码器并共享权重**：对于强文本感知需求的任务，如海报 OCR、商品标题识别、价格标签读取，LLM 初始化的编码器能显著提升文本阅读能力。可将现有多模态编码器的文本分支替换为
  LLM 初始化，并让各模态共享权重以压缩参数量。

  - **视频帧关注并发音频的融合层**：在直播切片或口播视频理解中，将音频作为并发信号引入帧特征融合，能改善时序定位和证据引用。对于商品讲解视频，可更准确地定位口播内容对应的画面片段，为后续推荐理由生成或广告素材自动剪辑提供结构化输入。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：文档、图像、音频、视频解析长期分散在不同模型和任务头中，输出格式不统一，难以直接作为 Agent 的感知层，无法在空间和时间上进行跨模态证据定位与引用。

**方法关键点**：
- **Youtu-Omni-Encoder**：从预训练语言模型初始化以加强文本阅读，用共享权重编码所有模态，并统一到同一空间-时间坐标系；少量融合层让视频帧关注并发音频，使跨模态融合和时间对齐进入感知本身。
- **OmniSchema**：将十种解析任务的输出统一为基于 token 角色的 schema，避免任务专用输出头。
- **OSAD（OmniSchema-Aware On-Policy Distillation）**：自进化后训练流程，每轮用模型自身 rollout 与参考条件副本的 token 级目标进行蒸馏，然后把训练后的权重刷新给参考副本，使解析器和监督信号共同进化。

**关键结果**：单个 5B 参数 checkpoint 在 OmniDocBench v1.6 上以 96.96 Overall 达到 SOTA，超过 TeleOCR（96.91）等系统；在 OmniParsingBench 上以 75.08 领先所有开放权重模型；图表解析得分 95.02 为最佳；化学指纹精确匹配最高；在排版乐谱字符级转录上与专用光学音乐模型相当，远超通用系统。
