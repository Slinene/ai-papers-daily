---
title: 'HumanTracker: Towards Comprehensive and Human-Aligned Motion Tracking Benchmark'
title_zh: HumanTracker：迈向全面且与人类对齐的运动跟踪基准
authors:
- Dairu Liu
- Zekun Qi
- Jiayu Zeng
- Ruixi Yu
- Yu Guan
- Yintianrun Zhang
- Xuchuan Chen
- Sikai Liang
- Zekai Li
- Chenghuai Lin
affiliations:
- Nankai University
- Tsinghua University
- Galbot
- Shanghai Jiao Tong University
- Peking University
arxiv_id: '2608.13555'
url: https://arxiv.org/abs/2608.13555
pdf_url: https://arxiv.org/pdf/2608.13555
published: '2026-08-13'
collected: '2026-08-15'
category: Eval
direction: 人形运动跟踪基准与偏好对齐评估
tags:
- Humanoid Motion Tracking
- Preference Alignment
- Benchmark
- Reward Model
- Evaluation Metric
- Temporal Transformer
one_liner: 构建153小时运动跟踪基准与偏好对齐的HumanScore指标，更符合人类感知并揭示接触/稳定性故障
practical_value: '- 离线评估别再只看 log-likelihood：用成对偏好数据训练 reward model 作为生成式推荐/搜索改写/文案生成的自动评估指标，尤其要加入业务约束违规信号（相关性、时效、价格带等）。

  - 构建诊断型 benchmark 时按场景/意图分层（类似论文四个 motion families），例如按导购、比价、冲动消费分层统计，便于定位 Agent
  决策在哪些场景崩。

  - 使用时序 Transformer 对整段 session/轨迹打分，而不是逐 item 独立打分：在会话推荐或 Agent 多步工具调用评估里，直接输出 session
  级 reward，可捕捉上下文一致性和长期目标达成。

  - 物理/业务约束显式建模：在生成式选品或文案生成后增加 constraint checker（如库存、毛利、合规），与 reward model 联合过滤，避免只看
  soft metric。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

动机：人形机器人运动跟踪评估常用运动学误差逐帧平均位姿差，但常与人类视频感知不一致，忽略足部滑动、接触时机错误等物理伪影；现有测试集规模小、多样性不足，难以压力测试接触密集、长时程行为。

方法关键点：构建 HumanTracker 基准，约153小时光学运动轨迹，来自多位专业表演者，分为四个运动家族（日常任务、高动态、交互、地面动作）并带文本标签，支持细粒度诊断。提出 HumanScore 偏好对齐指标，在12K运动对（24K运动）上训练，使用时序 Transformer 将观察序列映射为标量分数，作为奖励模型。

关键结果：在多个代表性 SOTA 跟踪器上，HumanScore 比运动学指标更好地预测人类偏好，并能暴露接触与稳定性失败，而这些失败常被运动学指标遗漏。
