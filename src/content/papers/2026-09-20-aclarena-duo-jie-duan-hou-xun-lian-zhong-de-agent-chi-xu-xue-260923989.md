---
title: 'ACLArena: Agent Continue Learning in Multi-stage Post-training'
title_zh: ACLArena：多阶段后训练中的 Agent 持续学习
authors:
- Haixin Wang
- Xiaoxuan Wang
- Junkai Zhang
- Han Zhang
- Renliang Sun
- Alexander K Taylor
- Yidan Shi
- Haoran Deng
- Chenguang Wang
- Jason Cong
affiliations:
- University of California, Los Angeles
- University of California, Santa Cruz
arxiv_id: '2609.23989'
url: https://arxiv.org/abs/2609.23989
pdf_url: https://arxiv.org/pdf/2609.23989
published: '2026-09-20'
collected: '2026-09-23'
category: Agent
direction: Agent 多阶段后训练与持续学习
tags:
- Agent Continual Learning
- Multi-stage Post-training
- On-policy Distillation
- LoRA Experts
- Model Merging
- SDFT
one_liner: 构建多阶段 Agent 后训练基准，诊断遗忘机制并融合 SDFT 与 LoRA-RL 专家路由，缓解跨阶段能力遗忘
practical_value: '- 做多阶段 agent 训练（如搜索问答、电商客服、工具调用）时，先 SFT 冷启动任务接口与行为格式，再用 RL/蒸馏精化；不要用
  SFT 恢复旧能力，其参数更新幅度是 RL 的 3-7 倍，容易覆盖相邻阶段能力。

  - 多教师 on-policy 蒸馏可采用 MOPD：对低熵 token 用 reverse KL 精确模仿，对高熵决策 token（选 query、工具调用）切换
  forward KL 并 top-q 截断，能避免 agentic 任务中熵坍塌和训练发散；多域 teacher 按 domain tag 路由，不要平均 logits。

  - 多领域电商/搜索 agent 可采用 MLE 架构：共享一个 SDFT 主干，每个领域（搜索、交易、客服）训练独立 LoRA adapter + RL，推理按环境上下文路由；参数隔离减少跨域遗忘，增量成本低、部署统一。

  - SDFT 轨迹蒸馏时必须 balanced-mix 而非按数据量随机混，防止高量任务淹没低资源领域；轨迹过滤需检查 final reward、工具调用合法性、协议合规并做近似去重。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
现代 agentic LLM 的多阶段后训练（CoT、工具使用、指令遵循）本质上是一个持续学习问题：训练新能力可能覆盖旧能力，工业界虽有多种整合尝试，但缺少可控基准与机制级理解。ACLArena 构建四阶段课程（Math→Search→E-commerce→IF）作为显微镜，系统分析遗忘与泛化。

## 方法关键点
- **诊断基线**：在 Qwen3-8B-Base 上顺序训练四个任务，通过 PCA 投影和 token 级预测一致性分析。发现不同任务产生部分对齐的参数位移；高熵 token（决策点）是遗忘集中发生处，低熵 token 几乎稳定。
- **三种整合范式**：MMOPD 在低熵 token 用 reverse KL、高熵 token 用 forward KL + top-q 截断；SDFT 用过滤后的 oracle 轨迹做 balanced-mix 自蒸馏；Model Merging 做权重平均。
- **MLE 方法**：先用 SDFT 得到共享能力基底，冻结主干后每个阶段训练独立 LoRA adapter 通过 RL 做轻量残差，推理按环境路由，参数隔离避免跨任务干扰。

## 关键实验与数字
- 顺序训练在 E-commerce 阶段造成严重遗忘：AIME26 从 25.83 跌至 6.04，NQ 从 45.2 跌至 14.6；最终 IF 阶段仅部分恢复（AIME26 10.21，NQ 33.5）。
- 事后整合只能恢复部分能力：MMOPD 将 NQ 恢复到 45.2、AIME26 到 21.25；SDFT 将 NQ 进一步提升到 48.3，但 IF-Eval 从 84.8 跌到 53.6；模型合并在 E-commerce/IF 上弱于顺序训练。
- MLE 在 in-domain 与 OOD 均更均衡：AIME26 21.04，NQ 49.7，τ3-Retail 32.9，IF-Eval 85.0，多跳搜索 38.6，GPQA 42.4，多类 OOD 最佳，接近独立专家并泛化更强。

## 一句话记忆
多阶段 agent 训练中共享单一模型强行整合异构能力会持续产生权衡；用 SDFT 共享基底 + 每任务 LoRA-RL 残差路由，是低成本且抗遗忘的实用架构。
