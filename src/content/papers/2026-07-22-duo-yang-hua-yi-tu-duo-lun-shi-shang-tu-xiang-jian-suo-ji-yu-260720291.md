---
title: Diverse-Intent Multi-Turn Fashion Image Retrieval
title_zh: 多样化意图多轮时尚图像检索基准与 MLLM-VLP 对齐框架
authors:
- Mingqiang Tang
- Haokun Wen
- Meng Liu
- Yupeng Hu
- Weili Guan
- Xuemeng Song
affiliations:
- Southern University of Science and Technology
- Harbin Institute of Technology (Shenzhen)
- Shandong University
- Shenzhen Loop Area Institute
arxiv_id: '2607.20291'
url: https://arxiv.org/abs/2607.20291
pdf_url: https://arxiv.org/pdf/2607.20291
published: '2026-07-22'
collected: '2026-07-23'
category: RecSys
direction: 多轮多意图图像检索基准与 MLLM-VLP 对齐框架
tags:
- Multi-turn Retrieval
- Fashion
- MLLM
- Vision-Language Alignment
- Diverse Intents
- DIM-Fashion
one_liner: 提出支持多意图切换与回溯的多轮时尚检索基准 DIM-Fashion，并设计三阶段 MLLM-VLP 框架 FashionAM 避免文本化瓶颈
practical_value: '- **多意图多轮交互建模**：电商搜索中用户常混合文字、图片、草图等查询，且可能突然“回到之前某轮结果再修改”，可借鉴 DIM-Fashion
  的会话构造方式，合成带 rollback 的多样化多轮训练数据，提升对话式检索鲁棒性。

  - **避免文本化瓶颈**：现有 LLM 检索多将多模态查询转为文本再检索，丢失视觉细节。FashionAM 直接用可学习 query tokens 将多模态上下文对齐到冻结的商品图像嵌入空间，可迁移到以图搜图、多模态商品搜索等任务。

  - **三阶段训练管线**：Stage1 背景去除对齐使图库编码器关注物品本体；Stage2 用 MLLM 生成的背景去除图描述进行图像-文本对齐，仅微调最后两层，保持物品中心表示。该策略可低成本适配
  CLIP 类模型到电商商品检索，降低背景干扰。

  - **多源数据桥接**：通过余弦相似度桥接不同数据集中的视觉相似物品，构造跨任务多轮 pair，可用于推荐系统中冷启动 item 的跨场景数据扩充或多任务统一建模。'
score: 9
source: arxiv-cs.CV
depth: full_pdf
---

**动机**：现有时尚多轮图像检索假设每轮都是对前一轮图像的属性编辑，忽略了真实搜索中意图可能跳变（如从草图搜图切换到找同款、搭配推荐），且用户会回溯到历史状态。同时，普遍采用的“多模态→文本→检索”管线丢失细粒度视觉信息，在图像中心任务上表现差。为此，该工作首次形式化多样化意图多轮检索问题，并构建大规模基准 DIM-Fashion 与直接对齐的多模态框架 FashionAM。

**方法关键点**：
- **DIM-Fashion 基准**：融合 13 个数据集（7 种检索任务），包含 26,748 个会话、110,841 个轮次，支持回顾（rollback）和异质查询（图文、草图、多图等）。构建三步：1）跨数据集视觉相似桥接（余弦相似度阈值 0.8）；2）受约束随机游走生成多轮会话，加入 rollback 机制；3）MLLM（Qwen3.6-35B）细化意图注释与文本初始查询，并进行质量验证。
- **FashionAM 模型**：三阶段管线。Stage1 用背景去除图像对齐 CLIP 图像编码器，学习背景无关的商品中心特征。Stage2 利用 MLLM 对去除背景图像生成的描述，进行图像-文本对齐，仅微调 CLIP 图像编码器最后两层。Stage3 冻结图像编码器，以 LoRA 微调 MLLM 编码器（Qwen3.5-4B），将多轮多模态上下文映射到统一查询嵌入，直接与图库向量做对比学习，避免中间文本化。

**关键结果**：
- 在 DIM-Fashion 上，FashionAM 总 R@5 达 51.0%，优于 MAI（42.2%）和 ImageScope（44.0%）；在图像中心任务（Street2Shop、Sketch2Img）提升巨大，分别达 58.1% 和 20.5%（ImageScope 仅 13.8% 和 0.6%）。
- 在 MT-FashionIQ 标准多轮属性编辑基准上，FashionAM R@5 56.3% 超越所有对比方法，验证了泛化性。
- 消融实验证实去掉任一阶段或直接使用原始 CLIP 均导致性能下降，证明三阶段对齐的必要性。

**一句话总结**：用跨数据集桥接构造多意图多轮检索数据，以“直接视觉对齐”替代“文本化”，是提升多模态图像检索的关键路径。
