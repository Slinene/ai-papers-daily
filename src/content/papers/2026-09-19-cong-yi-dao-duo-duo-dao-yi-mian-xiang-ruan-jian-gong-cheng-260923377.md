---
title: 'One to More, More to One: Category-Aware Iterative Expert Training for Software
  Engineering Agents'
title_zh: 从一到多，多到一：面向软件工程 Agent 的类别感知迭代专家训练
authors:
- Jie Zhao
- Ziyu Jiang
- Suhang Zheng
- Minghui Shan
- Xiaoxiao Xu
- Lin Qu
affiliations:
- Alibaba Group
arxiv_id: '2609.23377'
url: https://arxiv.org/abs/2609.23377
pdf_url: https://arxiv.org/pdf/2609.23377
published: '2026-09-19'
collected: '2026-09-22'
category: Training
direction: 类别感知迭代专家训练与策略集成
tags:
- Category-Aware RL
- Multi-Teacher Distillation
- Iterative Expert Training
- Policy Integration
- Software Engineering Agents
one_liner: 解决软件工程 Agent 多类别任务在不均衡 RL 下的跷跷板问题，通过类别专家迭代训练与多教师蒸馏融合为单一策略
practical_value: '- **类别不平衡下的 RL 训练**：在电商/广告/搜索推荐场景中，不同 query 类型、商品类目、用户分群上的 Agent
  策略提升往往不均。可借鉴将任务池按业务维度划分，分别训练类别专家，再合并，避免统一 RL 导致部分类别退化。

  - **迭代刷新-修复-扩展（RRE）机制**：用当前策略重新评估实例掌握度，复用自身验证成功的轨迹做 Repair SFT，再按策略短板重新采样任务继续 RL。可迁移到推荐
  Agent 的长期训练中：周期性用线上策略回放成功 case 做 SFT，并动态调整训练样本分布，缓解遗忘和分布漂移。

  - **无需外部教师模型**：整个专家训练和集成不依赖 GPT-4 等外部模型生成轨迹或动作目标，全流程自举。对于企业内数据合规和成本敏感场景很有价值。

  - **多教师在线蒸馏（MOPD）**：通过标签路由将多个专家蒸馏到单一可部署学生模型，并用 ReLU 门控只保留每个教师相对参考策略的改进方向，可避免集成时负迁移。可借鉴用于多任务或多场景模型合并，尤其是线上只能部署单模型时。'
score: 7
source: huggingface-daily
depth: abstract
---

## 动机
软件工程任务类别异构（服务/数据层 bug、界面调整、基础设施等），在 pooled agentic RL 下不同类别提升不均，聚合指标掩盖类别间的跷跷板效应。

## 方法关键点
- 构建可执行任务池 + SWE Labeler 多轴标签系统，支持类别维度划分。
- 先做类别特定 RL 得到多个专家，但实例级进展仍不均。
- 提出 Refresh-Repair-Expand (RRE) 迭代：更新策略刷新实例掌握度；复用自身验证成功轨迹做 Repair SFT；按策略短板重新选任务继续 RL。
- 多专家融合采用 Label-routed multi-teacher on-policy distillation (MOPD)，将多个专家蒸馏为单一可部署学生模型；ReLU-gated reward extrapolation 只保留每个教师相对参考策略的改进方向。
- 全流程不依赖外部模型提供解轨迹或动作目标。

## 关键结果
- 最终 MOPD 策略在 Pro-618 上平均解决率 58.04%，在 SWE-bench Multilingual 上 59.00%。
- 相对基础模型分别提升 5.39 和 2.78 个百分点。
- 相比 Joint-RL 基线，各类别最小增益和专家增益恢复均有明显优势。
