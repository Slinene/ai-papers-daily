---
title: 'WeVisOne-VL: Unified Visual Perception from Objects to Pixels'
title_zh: WeVisOne-VL：从物体到像素的统一视觉感知模型
authors:
- Tianming Liang
- Junyi Pan
- Yuxi Li
- Canmiao Fu
- Zhipeng Huang
- Chong Sun
- Chen Li
- Jing Lyu
affiliations:
- WeChat Vision, Tencent Inc.
arxiv_id: '2610.31329'
url: https://arxiv.org/abs/2610.31329
pdf_url: https://arxiv.org/pdf/2610.31329
published: '2026-10-21'
collected: '2026-10-24'
category: Multimodal
direction: 统一目标级与像素级视觉感知
tags:
- VLM
- object detection
- segmentation
- referring localization
- pixel decoder
- RL
one_liner: 用结构化 next-token 预测统一目标级与像素级视觉感知，支持检测、定位、分割与抠图
practical_value: '- 电商商品图片理解：可把商品主体检测、属性定位、mask 生成、OCR 统一到一个 VLM，减少多模型串联；用结构化文本输出
  boxes/masks，便于接入 Agent 工具调用。

  - <OBJ> token + 轻量 pixel decoder 的思路可迁移：在业务多模态模型中加一个特殊 token 表示实例，让 LLM 主干输出语义信息、pixel
  decoder 输出像素级结果，实现“语义理解+定位”同架构。

  - 针对缺货/不存在的对象做 robust rejection 值得借鉴：商品图或广告素材中检测用户 query 指向对象缺失时直接拒绝，可降低下游误匹配。

  - 训练上采用三阶段 curriculum SFT + mixed-task RL 的策略，适合多任务视觉-语言模型在电商场景做稳定训练。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有 VLM 在细粒度视觉感知上仍不可靠，难以同时处理目标级（检测、定位、计数、OCR）与像素级（分割、抠图）任务。

**方法关键点**：WeVisOne-VL 通过 structured next-token prediction 统一物体与像素感知；引入轻量 pixel decoder，以特殊 <OBJ> token 连接 VLM，生成实例级像素输出；支持从点、框到 mask、alpha matte 的任意用户指定粒度；训练采用三阶段课程 SFT 后接 mixed-task RL。

**关键结果**：在 30+ benchmark 上，目标级与像素级任务均取得领先，并对无目标查询保持稳健拒绝。
