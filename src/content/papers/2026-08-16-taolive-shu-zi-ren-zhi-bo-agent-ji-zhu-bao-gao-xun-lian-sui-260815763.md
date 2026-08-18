---
title: 'TaoLive Digital Avatar Agent Technical Report: Training Agents to Evolve with
  Their Harness'
title_zh: TaoLive 数字人直播 Agent 技术报告：训练 Agent 随 Harness 共同演化
authors:
- TaoLive AIGC LLM Team
- Yuhan Sun
- Wenhao Lin
- Yongdong Luo
- Yibo Hu
- Meiguang Jin
- Junfeng Ma
- Weihang Pan
- Jiaxin Zhao
- Zulong Chen
affiliations:
- TaoLive AIGC LLM Team
arxiv_id: '2608.15763'
url: https://arxiv.org/abs/2608.15763
pdf_url: https://arxiv.org/pdf/2608.15763
published: '2026-08-16'
collected: '2026-08-18'
category: Agent
direction: 直播电商 Agent 训练与 Harness 演化
tags:
- Harness-Aware Training
- HSA
- Agentic RL
- Live E-commerce
- Qwen3.6-35B-A3B
- GRPO-GDPO
one_liner: HAT 通过 Harness-State Augmentation 训练紧凑模型，使直播 Agent 在低延迟下随 Harness 演化并保持通用能力
practical_value: '- 把业务策略（Skills、Hooks、prompt、tool schemas）从模型权重中解耦，用可独立版本化的 Harness
  模块做诊断-编辑-评估闭环；策略更新从重训变成小时级上线，适合电商运营规则、合规要求高频变化。

  - 训练数据只覆盖单一 Harness 会让小模型记 skill 名/工具名/模板，上线后策略一改就崩；用 HSA 对 skill 名与内容、tool schema、prompt
  结构、Hook 行为做任务保持扰动，构造多种 Harness 配置让模型学会读当前指令而非背固定版本。消融显示 HSA-SFT 收益远大于 HSA-RL，优先在
  SFT 阶段做增强。

  - General OPD 以预训练基座为 teacher，在通用指令数据上做 on-policy KL 蒸馏，能找回领域 SFT 损失的通用指令能力（IFEval
  +8.5），比单纯加回通用 SFT 更贴合低延迟 agent 场景。

  - 低并发实时直播用单卡 H20 + MTP 投机解码可把 P95 压到 8.1s、吞吐提升 1.7x；但高并发下 MTP 收益递减，应预留副本而不是把它当高吞吐优化。Hooks/超时/降级路由做防御性深度，避免模型幻觉造成事实性风险。'
score: 9
source: arxiv-cs.CL
depth: full_pdf
---

**动机**
AI 数字人主播在直播电商中必须实时回答商品问题、互动并执行营销策略，要求低延迟、策略高频更新、回复准确且有效。将 Skills、Hooks、prompt、tools 从模型权重中解耦为可独立演化的 Harness，能让业务策略小时级迭代而无需重训；但这也使模型执行环境成为移动目标。固定 Harness 做 SFT 的小模型会过拟合表面形式，IFEval 掉 7.7 点；大模型零样本好但 P50 延迟超 11s，不满足实时交互。

**方法关键点**
- **HSA（Harness-State Augmentation）**：对 Skill 标识、Skill 内容、tool schema、system prompt 结构、Hook 行为做任务保持扰动，构造多样化 Harness 状态，抑制对固定名称/模板的捷径记忆。
- **三阶段 HAT**：① HSA-SFT：教师模型在不同 Harness 下生成轨迹并过滤；② General OPD：以预训练 base 为 teacher，在 Tulu3 上做 on-policy KL 蒸馏，恢复通用指令能力；③ HSA-RL：在生产级直播仿真器中做 Agentic RL，使用 GRPO 框架、GDPO 多维奖励分组优势、GSPO 序列级重要性采样，奖励含 Accuracy、Effectiveness、Tool Rationality、Skill Selection 及 CoT 长度惩罚。
- **仿真环境**：模拟多轮交互、Skill 路由、Hook 重试、工具失败注入，让模型实际经历失败恢复，而不只是模仿教师轨迹。

**关键结果**
- T1 Live-Stream QA AVG 94.8（base 80.3，最强通用 LLM 93.0）；T2 Harness-Variant QA 94.6（base 75.4）。
- IFEval 83.5/88.7，较 base +2.0/+1.0；对照 Fixed-Harness SFT 则掉 7.7/5.3。
- 单卡 H20 + MTP：P50 3.407s，P95 8.114s，100% 请求 15s 内完成；解码吞吐 271.4 tok/s（1.69×）。
- 消融：HSA-SFT 对 IFE-P 增益 +9.4，明显大于 HSA-RL 的 +1.0；HSA-RL 在原始 Harness 上仍有提升；held-out Harness 编辑测试错误降低 51.7%，远高于 Naive SFT 的 18.1%。

**最值得记住的一句话**：让模型在训练中看到 Harness 的分布而不是记住一个 Harness；SFT 阶段的 HSA 是关键，General OPD 用来保住通用能力。
