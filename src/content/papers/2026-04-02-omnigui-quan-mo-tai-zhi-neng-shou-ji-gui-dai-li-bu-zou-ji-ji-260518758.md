---
title: 'OmniGUI: Benchmarking GUI Agents in Omni-Modal Smartphone Environments'
title_zh: OmniGUI：全模态智能手机 GUI 代理步骤级基准
authors:
- Felix Henry
- Xiaochen Lin
- Jiangyou Zhu
- Yangfan
- Bingqian Zhang
- Min Chen
- Shiyu Huang
affiliations:
- XPeng Motors
arxiv_id: '2605.18758'
url: https://arxiv.org/abs/2605.18758
pdf_url: https://arxiv.org/pdf/2605.18758
published: '2026-04-02'
collected: '2026-05-20'
category: Eval
direction: GUI Agent 评估 · 全模态环境基准
tags:
- GUI Agent
- Omni-modal
- Benchmark
- Smartphone
- Action Prediction
- Multimodal
one_liner: 首个在步骤级注入交错图像、音频与视频的全模态 GUI 代理基准，揭示当前模型在需要时序/听觉信号时性能大幅下降
practical_value: '- 电商或推荐场景的智能助手/自动化测试 Agent 设计时，应纳入音频、短视频等多模态输入，不应仅依赖静态截图，可参考该基准的多模态依赖标注方式。

  - 真实环境中的无关噪声会造成跨模态干扰，促使 Agent 性能下降，提示在部署中需加入模态过滤或噪声鲁棒策略，对语音购物、直播带货等场景有直接借鉴。

  - 步骤级交错输入的设计对连续交互数据采集有工程参考价值，可以迁移到对话式推荐或客服 Agent 的训练数据构建中。

  - 基准揭示了时序音频信号对动作决策的重要性，推荐系统在利用商品短视频、动态展示时，应考虑时序信息与用户操作时刻的对齐。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有 GUI 代理基准大多依赖静态截图，但真实智能手机交互经常需要处理瞬态音频提示（如通知声）和时序视频动态（如播放中的短视频），这些信号与动作执行时刻紧密耦合。缺乏对这类全模态输入的评估，导致代理在现实场景中的能力认知不足。

**方法**：提出 OmniGUI，首个步骤级全模态基准。每个动作步骤都提供交错的静态图像、同步音频和视频片段，覆盖 29 个应用、709 个专家演示片段（共 2,579 个动作步骤），并系统标注了多模态依赖级别（如是否必须依赖音频或视频才能正确决策）。选用能原生处理交错输入的全模态基础模型作为代理基线进行测试。

**关键结果**：实验表明，现有模型在纯视觉静态任务上表现尚可，但在需要同步时序或听觉信号的任务中，动作预测准确率大幅下降。消融实验进一步定位了瓶颈：任务无关的环境噪声会造成严重的跨模态干扰，导致代理性能退化。该基准为全模态 GUI 代理的优化提供了量化诊断平台。
