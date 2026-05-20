---
title: 'Aurora: Unified Video Editing with a Tool-Using Agent'
title_zh: 极光：使用工具增强代理的统一视频编辑
authors:
- Yongsheng Yu
- Ziyun Zeng
- Zhiyuan Xiao
- Zhenghong Zhou
- Hang Hua
- Wei Xiong
- Jiebo Luo
affiliations:
- University of Rochester
- MIT-IBM Watson AI Lab
- NVIDIA
arxiv_id: '2605.18748'
url: https://arxiv.org/abs/2605.18748
pdf_url: https://arxiv.org/pdf/2605.18748
published: '2026-05-17'
collected: '2026-05-20'
category: Agent
direction: 视频编辑 · Agent 工具增强
tags:
- Video Editing
- Tool-Using Agent
- VLM
- Diffusion Transformer
- Underspecification
- AgentEdit-Bench
one_liner: 提出Aurora框架，用工具增强的VLM代理解决视频编辑中用户请求欠指定问题，将缺失条件补全后送入统一视频扩散模型。
practical_value: '- **Agent 条件构建范式**：将用户模糊请求（缺少参考图、掩码、明确指令）委托给工具增强的VLM代理，生成完整的条件元组（指令、任务类型、搜索词、掩码描述），下游生成模型只消费标准条件，该解耦模式可直接用于电商商品图生成、广告视频编辑，降低人工补全成本。

  - **偏好对齐解决边界决策**：使用DPO精细解决代理的边界案例（如误触发搜索、模糊掩码、约束丢失等），在推荐或Agent决策中可借鉴此方法，通过构建冲突对提升模型在相似但错误路径上的区分能力。

  - **工具增强与统一条件接口**：代理可调用网络搜索和分割工具，输出统一格式的参考图与掩码，屏蔽不同工具的内部差异，适合在Agent工作流中集成异构API，降低下游模型对工具强耦合。

  - **设计评测维度**：提出AgentEdit-Bench专门测量代理补全缺失条件的能力，评估指标包含实体匹配和身份保持，可启发我们为客服、推荐等场景构建需要主动补全信息的评测集。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
当前统一视频编辑模型虽然支持文本、源视频、参考图和掩码等多条件，但要求用户完整提供这些输入，而现实请求往往**欠指定**：如要求“替换为巴宝莉格纹围巾”却没有提供参考图（视觉欠指定），或指令模糊“把蓝色物品换成跑得更快的交通工具”需推理（文本欠指定）。模型本身缺乏补全条件的能力，瓶颈从生成转移到条件构造。

## 方法关键点
- **两步解耦框架 Aurora**：工具增强的 VLM 代理（LoRA 微调的 Qwen3-VL-8B）负责规划，统一视频扩散变压器（基于 Wan2.2-TI2V-5B）负责生成。代理输出四字段 JSON：改写指令、任务标签、可选的图像搜索查询、可选的掩码短语。
- **工具执行**：当有图像搜索查询时，调用 Serper API 检索候选图，再由代理选择一张；当有掩码短语时，调用 GroundingDINO 和 SAM 生成二值掩码并合成到源视频帧上，形成参考图像送入视频模型。
- **视频模型统一条件路径**：条件元组（改写指令、源视频、参考图集）通过多模态上下文编码器（冻结 Qwen3.5-4B）和潜在令牌拼接双路径注入 DiT 的交叉注意力和自注意力，同时用零时间步调制保持源帧和参考帧不受去噪影响。
- **代理训练**：先用监督微调（25K 计划数据 +10K 参考选择数据）直接教代理生成完整计划，再用 DPO 在边界案例上对齐（1.8K 对），涵盖误触发搜索、模糊掩码、约束丢失等五类边界。视频模型分两阶段用编辑数据训练，并在训练时冻结。

## 关键结果
- **AgentEdit-Bench**：构建 150 个欠指定编辑任务，Aurora 得分 87.9 分（满分百分比），比纯视频模型（74.7）提升 13.2 分，且在 IP（具名实体）替换、添加任务上提升最显著。
- **现有基准**：在 EditVerse-Bench 上取得 7.61 分（满分 10），在 OpenVE-Bench 上 3.38 分（满分 5），均为开源最佳；代理仅靠指令改写也能提升 UniVideo 和 Kiwi-Edit 的性能。
- **消融**：监督规划贡献了大部分提升（SFT 85.0），DPO 额外 +2.9；代理可迁移至冻结的其他视频编辑模型，保持增益。

最值得记住的一句话：**“由 VLM 代理负责将模糊请求翻译为完整的条件元组，让下游生成模型专注于高质量采样，是解决欠指定问题的可推广范式。”**
