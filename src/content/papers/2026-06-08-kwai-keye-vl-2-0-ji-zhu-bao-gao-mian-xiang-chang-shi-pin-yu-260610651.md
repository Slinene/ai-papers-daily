---
title: Kwai Keye-VL-2.0 Technical Report
title_zh: Kwai Keye-VL-2.0 技术报告：面向长视频与智能体的多模态基础模型
authors:
- Kwai Keye Team
- Bin Wen
- Changyi Liu
- Chengru Song
- Chongling Rao
- Guowang Zhang
- Han Li
- Haonan Fan
- Hengrui Ju
- Jiankang Chen
affiliations:
- Kuaishou Group
arxiv_id: '2606.10651'
url: https://arxiv.org/abs/2606.10651
pdf_url: https://arxiv.org/pdf/2606.10651
published: '2026-06-08'
collected: '2026-06-11'
category: Multimodal
direction: 多模态大模型 · 长视频理解与智能体
tags:
- Multimodal LLM
- Sparse Attention
- Long Video Understanding
- Agent
- MoE
- On-Policy Distillation
one_liner: 首个在GQA架构上实现DeepSeek稀疏注意力以无损处理256K上下文，并通过跨模态多教师在线蒸馏解决多任务遗忘的多模态模型
practical_value: '- **稀疏注意力用于长序列推荐**：DSA 通过 MQA 式索引 + GQA 分组聚合将注意力复杂度从 O(L²) 降至 O(Lk)，这个思路可以直接迁移到用户行为序列建模（如百万级行为
  token 的推荐模型），在减少 KV cache 的同时保持关键信息捕获。

  - **多教师在线蒸馏解决多任务冲突**：MOPD 动态路由 13 个领域专家、按 token 类别缩放优势值的方法，可借鉴到多目标推荐模型训练，避免不同业务目标（点击率、转化率、时长）之间的梯度干扰。

  - **视频时序定位能力复用**：论文中构建的 TVG、帧级感知、场景密集描述等数据与训练流水线，可迁移到电商直播场景——精确截取商品讲解片段、自动生成直播看点，提升内容分发效率。

  - **合成数据 RL 的设计范式**：基于可控编辑图像对+规则可验证 reward 的 RL 方法，可用于商品图片差异检测、属性变更验证等场景，低成本获得精准监督信号。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
长视频理解面临三个核心矛盾：超长上下文导致 KV 缓存膨胀不可控；视频帧采样丢失时序连续性；多任务注入（视觉、推理、Agent）容易引发灾难性遗忘。Keye-VL-2.0 旨在用一个 30B MoE、激活仅 3B 参数的模型，同时突破上下文可扩展性与能力隔离这两大瓶颈。

**方法关键点**  
- **架构**：在 GQA 架构的 LLM 解码器上首次适配 DeepSeek 稀疏注意力（DSA），通过 MQA 式 Lightning Indexer 计算全局词元重要性并选取 Top-k，然后各 query 头在共享的稀疏索引集上做分组 GQA 聚合，将 256K 上下文的注意力复杂度削减为线性。训练采用先稠密预热再稀疏适配的两阶段策略。  
- **视觉编码**：继承 Keye-VL-1.5 的 ViT，引入原生分辨率、2D RoPE 与 Patch n' Pack，统一图像与视频的动态分辨率编码，用自然语言时间戳注入帧间时序信息。  
- **预训练**：四阶段课程——投影器初始化、32K 通用对齐、64K 多任务注入（OCR、STEM、GUI、Grounding、Coding 等）、256K 长上下文扩展，视频时长从 15 秒逐步增加到 2 小时。  
- **后训练**：SFT 阶段混合 40% 纯文本数据防止语言能力退化，并构建合成思维链数据；RL 阶段引入合成数据 RL（差异图像识别）、通用 RL（GSPO）、领域专家 RL（接地、空间、数学、计数、OCR）和视频 RL；最后通过**跨模态多教师在线策略蒸馏（MOPD）**将 13 个领域教师的有标记反馈蒸馏回学生模型，用 top-k 重叠估计和 token 类别敏感优势缩放抑制遗忘。

**关键实验**  
- **长视频理解**：在 Video-MME-v2 上以 512 帧采样取得 42.4（Non-Lin 分数 52.4），LongVideoBench 上 2fps 采样达到 81.1，远超同规模开源模型（Qwen3.5-35B-A3B 仅 28.5/36.8）。  
- **时序定位**：TimeLens 框架下的 ActivityNet/QVHighlights/Charades 上 mIoU 分别达 70.1/65.7/74.1，大幅领先 Gemini-3-Flash。  
- **效率**：DSA 使预填充成本降至全注意力的 0.32 倍，解码成本降至 0.2 倍，并在 128K tokens 时保持恒定开销。  
- **Agent 能力**：支持代码、工具、搜索等多步交互，通过环境可验证奖励实现稳定训练。

**最值得记住的一句话**  
“将 DSA 植入 GQA 解码器，用稠密预热+稀疏适应实现 256K 无损视频理解，再用在线蒸馏让 13 个领域教师的能力无冲突地收敛到一个 3B 激活参数的 MoE 中，这是长上下文多模态模型走向实用的关键突破。”
