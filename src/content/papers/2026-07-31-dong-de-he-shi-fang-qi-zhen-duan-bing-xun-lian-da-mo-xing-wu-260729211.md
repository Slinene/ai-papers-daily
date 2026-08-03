---
title: 'Knowing When to Quit: Diagnosing and Training LLMs to Abort Futile Reasoning'
title_zh: 懂得何时放弃：诊断并训练大模型中止无效推理
authors:
- Xinyan Guan
- Jiali Zeng
- Chunlei Xin
- Yaojie Lu
- Hongyu Lin
- Xianpei Han
- Le Sun
- Fandong Meng
affiliations:
- Chinese Information Processing Laboratory, Institute of Software, Chinese Academy
  of Sciences
- University of Chinese Academy of Sciences
- Weixin AI, Tencent Inc
arxiv_id: '2607.29211'
url: https://arxiv.org/abs/2607.29211
pdf_url: https://arxiv.org/pdf/2607.29211
published: '2026-07-31'
collected: '2026-08-03'
category: Reasoning
direction: LLM推理能力对齐与无效推理抑制
tags:
- Futile Reasoning
- Capability Alignment
- Reinforcement Learning
- Refusal Training
- LLM Reasoning
one_liner: 提出CaRL框架，通过能力校准奖励与事后拒绝增强，让LLM在超出能力时学会放弃而非生成看似正确的无效推理
practical_value: '- **Agent / 推荐决策中的安全拒绝机制**：当 LLM 作为 Agent 处理复杂推荐或搜索任务（如组合优化、约束检查）超出能力时，可借鉴
  CaRL 的三级奖励（正确+1，拒绝0，错误-1）训练模型选择拒绝而非生成看似合理但错误的方案，避免误导用户。

  - **失败轨迹的样本增强**：事后拒绝增强（HRA）将失败的推理轨迹自动转化为带解释的拒绝样本，解决了拒绝数据稀缺问题；在电商对话推荐或商品组合生成中，可将用户不满意的推荐路径转化为“当前无法满足”的回复，提升安全性。

  - **降低推理计算浪费**：CaRL 使模型在察觉不可能时尽早终止，推理长度减少约33%；在高吞吐的广告查询改写或搜索推荐场景，可大幅节省 token 成本同时控制无效输出。

  - **仅靠奖励塑造不够，需要密集拒绝信号**：实验表明，缺少 HRA 时单纯校准奖励无法让模型学会拒绝（RL<sub>unk</sub> 无效推理率仍 > 95%）；提示我们在为
  LLM 加入拒识能力时，必须构造明确的拒绝演示参与训练。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**：LLM 在面对超出自身能力的推理任务时，常常生成表面上合理但实际包含错误推导的输出（称为“无效推理”），这种能力超限行为严重损害可靠性，且人类难以辨别。文中通过难度分级的 Countdown 任务系统分析了该现象，发现模型普遍存在能力超限（从不拒绝）、主要失效模式为伪推理（specious reasoning），并存在能力-行为严重失配（过度自信是过度保守的 6 倍）。因此需要一种方法让模型在推理中适时中止并明确拒绝。

**方法关键点**：
- **能力校准奖励塑造（Capability-Calibrated Reward Shaping）**：定义三级奖励——正确答案+1，有效拒绝 0，错误答案-1，激励模型在无解时选择拒绝而非硬试。
- **事后拒绝增强（Hindsight Refusal Augmentation）**：将训练中失败的推理轨迹转化为拒绝样本，保留推理过程直至最后一步，再插入拒绝前缀和简要进度总结，形成“本可拒绝”的对比学习信号，密集化原本稀疏的拒绝奖励。
- **训练流程**：结合 GRPO 算法，在 Countdown 任务上进行在线 RL；训练前模型拒绝率接近 0%，HRA 提供了必要的拒绝分布。

**关键结果**：
- 在 Qwen3-8B 上，CaRL 将无效推理率从 65.5% 降至 7.0%，同时可靠性从 0.6663 提升至 0.7915。
- 在 Qwen3-14B 上，无效推理率从 78.6% 降至 1.0%，可靠性从 0.6719 升至 0.8348。
- 在 OOD 的 Sudoku 任务上同样有效，且未出现 RFT 的灾难性坍塌。
- 通用推理基准 AIME 2024 和 GPQA 上准确率几乎无损，但推理长度减少 16%−25%，证明方法保留了基础推理能力。
- 奖励塑造单独使用无效（无效推理率仍 >95%），说明事后拒绝增强至关重要。

**一句话记忆**：CaRL 通过“错误答案惩罚+拒绝奖励中等”的奖励设计，并用失败轨迹自动生成拒绝样本，让 LLM 学会在能力边界果断喊停，有效消除看起来正确实则无效的推理。
